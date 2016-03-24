from datetime import datetime, timedelta
from django.conf import settings
from django.db.models import Sum, Avg
from pytz import timezone
from scorecard.apps.automations.models import Automation

from scorecard.apps.personals.models import TestStats, RequirementStats, LabStats
from scorecard.apps.personals.models import InnovationStats
from scorecard.apps.users.models import FunctionalGroup, Subteam
from models import TestMetricsConfiguration, InnovationMetrics, TestMetrics, RequirementMetrics, LabMetrics
from scorecard.apps.automations.utils import CHOICES_QE, CHOICES_RE, CHOICES_TL, CHOICES_QA_TE


def context_teams(request):
    start_end = get_start_end_from_request(request)
    start = start_end['start']
    end = start_end['end']

    groups = []
    for group in FunctionalGroup.objects.all():
        group_dict = {'group': group,
                      'weeks': group.metrics_set.filter(subteam=None).order_by('-created'),
                      'subteams': [{'team': team, 'weeks': team.metrics_set.filter(created__range=(start, end)).order_by('-created')}
                                   for team in Subteam.objects.filter(parent=group)]}
        if request.user.is_superuser:
            metrics_set = group.metrics_set.filter(created__range=(start, end), subteam=None).order_by('-created')

            group_dict['subteams'].append({
                'team': {'name': 'Team'},
                'weeks': metrics_set
            })

        groups.append(group_dict)

    # for functional_group in functional_groups:
    #     if functional_group.key == 'QA':
    #         qas = functional_group.testmetrics_set.filter(created__range=(start, end)).order_by('-created')
    #         qas_ytd = get_ytd_data(qas, functional_group.key)
    #     elif functional_group.key == 'QI':
    #         qis = functional_group.innovationmetrics_set.filter(created__range=(start, end)).order_by('-created')
    #         qis_ytd = get_ytd_data(qis, functional_group.key)
    #     elif functional_group.key == 'RE':
    #         res = functional_group.requirementmetrics_set.filter(created__range=(start, end)).order_by('-created')
    #         res_ytd = get_ytd_data(res, functional_group.key)
    #     elif functional_group.key == 'TE':
    #         tes = functional_group.testmetrics_set.filter(created__range=(start, end)).order_by('-created')
    #         tes_ytd = get_ytd_data(tes, functional_group.key)
    #     elif functional_group.key == 'TL':
    #         tls = functional_group.labmetrics_set.filter(created__range=(start, end)).order_by('-created')
    #         tls_ytd = get_ytd_data(tls, functional_group.key)

    context = {
        'groups': groups,
        'start': start,
        'end': end
    }

    return context


def get_start_end_from_request(request):
    try:
        end = datetime.strptime(request.GET.get('end'), '%Y-%m-%d') + timedelta(seconds=24 * 60 * 60 -1)
    except (TypeError, ValueError):
        end = datetime.now()

    try:
        start = datetime.strptime(request.GET.get('start'), '%Y-%m-%d')
    except (TypeError, ValueError):
        start = end - timedelta(days=60)

    start = timezone(settings.TIME_ZONE).localize(start)
    end = timezone(settings.TIME_ZONE).localize(end)

    return {
        'start': start,
        'end': end
    }


def fetch_team_members_per_team_per_date(key, date, subteam):
    year = date[:4]
    month = date[6:7]
    day = date[8:10]
    team_personals = []

    if key in ['QA', 'TE']:
        team_personals = TestStats.objects.filter(human_resource__functional_group__abbreviation=key,
                                                  human_resource__subteam__id=subteam,
                                                  created__year=year,
                                                  created__month=month,
                                                  created__day=day)
    elif key in ['QI', 'QE']:
        team_personals = InnovationStats.objects.filter(human_resource__functional_group__abbreviation=key,
                                                        human_resource__subteam__id=subteam,
                                                        created__year=year,
                                                        created__month=month,
                                                        created__day=day)
    elif key == 'RE':
        team_personals = RequirementStats.objects.filter(human_resource__functional_group__abbreviation=key,
                                                         human_resource__subteam__id=subteam,
                                                         created__year=year,
                                                         created__month=month,
                                                         created__day=day)
    elif key == 'TL':
        team_personals = LabStats.objects.filter(human_resource__functional_group__abbreviation=key,
                                                 human_resource__subteam__id=subteam,
                                                 created__year=year,
                                                 created__month=month,
                                                 created__day=day)

    return team_personals


def fetch_collect_data_per_team_per_date(key, date, subteam):
    form_data = calculate_data = automation_data = {}
    team_personals = fetch_team_members_per_team_per_date(key, date, subteam)

    # QA, TE
    overtime_weekday = overtime_weekend = rework_time = 0
    tc_manual_dev = tc_manual_dev_time = tc_manual_execution = tc_manual_execution_time = 0
    tc_auto_dev = tc_auto_dev_time = tc_auto_execution = tc_auto_execution_time = 0
    defect_caught = uat_defects_not_prevented = standards_violated = resource_swap_time = 0

    # QI
    story_points_execution = unit_tests_dev = elicitation_analysis_time = 0

    # RE
    revisions = rework_external_time = travel_cost = 0

    # TL
    tickets_closed = 0

    if key in ['QA', 'TE']:
        try:
            test_metric_config = TestMetricsConfiguration.objects.get(functional_group__abbreviation=key)
            hours = test_metric_config.hours_per_week
            costs_staff = test_metric_config.costs_per_hour_staff
        except TestMetricsConfiguration.DoesNotExist:
            hours, costs_staff = 0, 0

        for person in team_personals:
            overtime_weekday += person.overtime_weekday
            overtime_weekend += person.overtime_weekend
            rework_time += person.rework_time

            tc_manual_dev += person.tc_manual_dev
            tc_manual_dev_time += person.tc_manual_dev_time
            tc_manual_execution += person.tc_manual_execution
            tc_manual_execution_time += person.tc_manual_execution_time

            tc_auto_dev += person.tc_auto_dev
            tc_auto_dev_time += person.tc_auto_dev_time
            tc_auto_execution += person.tc_auto_execution
            tc_auto_execution_time += person.tc_auto_execution_time

            defect_caught += person.defect_caught
            uat_defects_not_prevented += person.uat_defects_not_prevented
            standards_violated += person.standards_violated
            resource_swap_time += person.resource_swap_time

        form_data = {
            'overtime_weekday': overtime_weekday,
            'overtime_weekend': overtime_weekend,
            'rework_time': rework_time,
            'tc_manual_dev': tc_manual_dev,
            'tc_manual_dev_time': tc_manual_dev_time,
            'tc_manual_execution': tc_manual_execution,
            'tc_manual_execution_time': tc_manual_execution_time,
            'tc_auto_dev': tc_auto_dev,
            'tc_auto_dev_time': tc_auto_dev_time,
            'tc_auto_execution': tc_auto_execution,
            'tc_auto_execution_time': tc_auto_execution_time,
            'defect_caught': defect_caught,
            'uat_defects_not_prevented': uat_defects_not_prevented,
            'standards_violated': standards_violated,
            'resource_swap_time': resource_swap_time
        }

        if (tc_manual_dev + tc_auto_dev) > 0:
            auto_footprint_dev_age = float(tc_auto_dev) / (tc_manual_dev + tc_auto_dev)
        else:
            auto_footprint_dev_age = 0
        if (tc_manual_execution + tc_auto_execution) > 0:
            auto_footprint_execution_age = float(tc_auto_execution) / (tc_manual_execution + tc_auto_execution)
        else:
            auto_footprint_execution_age = 0
        auto_and_execution_time = tc_manual_dev_time + tc_manual_execution_time + tc_auto_dev_time + tc_auto_execution_time
        gross_available_time = len(team_personals) * 30
        if len(team_personals) > 0:
            avg_throughput = (tc_manual_dev + tc_auto_dev + tc_manual_execution + tc_auto_execution) / float(len(team_personals))
            efficiency = auto_and_execution_time / gross_available_time
        else:
            avg_throughput = 0
            efficiency = 0

        calculate_data = {
            'auto_footprint_dev_age': auto_footprint_dev_age,
            'auto_footprint_execution_age': auto_footprint_execution_age,
            'avg_throughput': avg_throughput,
            'auto_and_execution_time': auto_and_execution_time,
            'gross_available_time': gross_available_time,
            'efficiency':  efficiency,
            'operational_cost': len(team_personals) * hours * costs_staff,
            'total_cost': len(team_personals) * hours * costs_staff,
            'auto_savings': tc_auto_execution_time * costs_staff
        }

        automation_data = get_automation_data(key, CHOICES_QA_TE, date)

    elif key in ['QI', 'QE']:
        for person in team_personals:
            overtime_weekday += person.overtime_weekday
            overtime_weekend += person.overtime_weekend
            rework_time += person.rework_time
            story_points_execution += person.story_points_execution
            unit_tests_dev += person.unit_tests_dev
            elicitation_analysis_time += person.elicitation_analysis_time

        form_data = {
            'overtime_weekday': overtime_weekday,
            'overtime_weekend': overtime_weekend,
            'rework_time': rework_time,
            'story_points_execution': story_points_execution,
            'unit_tests_dev': unit_tests_dev,
            'elicitation_analysis_time': elicitation_analysis_time
        }
        calculate_data = {
            'avg_throughput': float(story_points_execution) / len(team_personals) if len(team_personals) > 0 else 0,
            'operational_cost': len(team_personals) * 40 * 45,
            'total_cost': len(team_personals) * 40 * 45
        }
        automation_data = get_automation_data(key, CHOICES_QE, date)

    elif key == 'RE':
        for person in team_personals:
            overtime_weekday += person.overtime_weekday
            overtime_weekend += person.overtime_weekend
            rework_time += person.rework_time
            elicitation_analysis_time += person.elicitation_analysis_time
            revisions += person.revisions
            rework_external_time += person.rework_external_time
            travel_cost += person.travel_cost

        form_data = {
            'overtime_weekday': overtime_weekday,
            'overtime_weekend': overtime_weekend,
            'rework_time': rework_time,
            'elicitation_analysis_time': elicitation_analysis_time,
            'revisions': revisions,
            'rework_external_time':  rework_external_time,
            'travel_cost': travel_cost
        }
        calculate_data = {
            'gross_available_time': len(team_personals) * 6 * 5,
            'efficiency': elicitation_analysis_time / (len(team_personals) * 6 * 5) if len(team_personals) > 0 else 0,
            'operational_cost': len(team_personals) * 30 * 50,
            'rework_external_cost': rework_external_time * 50
        }
        automation_data = get_automation_data(key, CHOICES_RE, date)

    elif key == 'TL':
        for person in team_personals:
            overtime_weekday += person.overtime_weekday
            overtime_weekend += person.overtime_weekend
            rework_time += person.rework_time
            tickets_closed += person.tickets_closed

        form_data = {
            'overtime_weekday': overtime_weekday,
            'overtime_weekend': overtime_weekend,
            'rework_time': rework_time,
            'tickets_closed': tickets_closed
        }
        automation_data = get_automation_data(key, CHOICES_TL, date)

    form_data['staffs'] = len(team_personals)

    return {
        'form_data': form_data,
        'calculate_data': calculate_data,
        'automation_data': automation_data
    }


def get_ytd_data(group, key):
    count = len(group)
    data = {}
    total_costs, total_active_projects, total_active_tickets, total_avg_throughput = 0, 0, 0, 0

    if key in ['QA', 'TE']:
        for item in group:
            total_active_projects += item.active_projects
            total_active_tickets += item.active_tickets
            total_avg_throughput += item.avg_throughput
            total_costs += item.total_operational_cost

        data = {
            'staffs': {
                'total': group.aggregate(Sum('staffs'))['staffs__sum'],
                'avg': group.aggregate(Avg('staffs'))['staffs__avg']
            },
            'active_projects': {
                'total': total_active_projects,
                'avg': total_active_projects / count if count > 0 else 0
            },
            'active_tickets': {
                'total': total_active_tickets,
                'avg': total_active_tickets / count if count > 0 else 0
            },
            'avg_throughput': {
                'total': total_avg_throughput,
                'avg': total_avg_throughput / count if count > 0 else 0
            },
            'total_operational_cost': {
                'total': total_costs,
                'avg': total_costs / count if count > 0 else 0
            }
        }

    elif key in ['QI', 'QE']:
        for item in group:
            total_costs += item.total_operational_cost

        data = {
            'staffs': {
                'total': group.aggregate(Sum('staffs'))['staffs__sum'],
                'avg': group.aggregate(Avg('staffs'))['staffs__avg']
            },
            'story_points_backlog': {
                'total': group.aggregate(Sum('story_points_backlog'))['story_points_backlog__sum'],
                'avg': group.aggregate(Avg('story_points_backlog'))['story_points_backlog__avg']
            },
            'avg_team_size': {
                'total': group.aggregate(Sum('avg_team_size'))['avg_team_size__sum'],
                'avg': group.aggregate(Avg('avg_team_size'))['avg_team_size__avg']
            },
            'total_operational_cost': {
                'total': total_costs,
                'avg': total_costs / count if count > 0 else 0
            },
        }
    elif key == 'RE':
        for item in group:
            total_active_projects += item.active_projects
            total_avg_throughput += item.avg_throughput
            total_costs += item.total_operational_cost

        data = {
            'staffs': {
                'total': group.aggregate(Sum('staffs'))['staffs__sum'],
                'avg': group.aggregate(Avg('staffs'))['staffs__avg']
            },
            'active_projects': {
                'total': total_active_projects,
                'avg': total_active_projects / count if count > 0 else 0
            },
            'elicitation_analysis_time': {
                'total': group.aggregate(Sum('elicitation_analysis_time'))['elicitation_analysis_time__sum'],
                'avg': group.aggregate(Avg('elicitation_analysis_time'))['elicitation_analysis_time__avg']
            },
            'avg_throughput': {
                'total': total_avg_throughput,
                'avg': total_avg_throughput / count if count > 0 else 0
            },
            'total_operational_cost': {
                'total': total_costs,
                'avg': total_costs / count if count > 0 else 0
            }
        }
    elif key == 'TL':
        data = {
            'staffs': {
                'total': group.aggregate(Sum('staffs'))['staffs__sum'],
                'avg': group.aggregate(Avg('staffs'))['staffs__avg']
            },
            'tickets_received': {
                'total': group.aggregate(Sum('tickets_received'))['tickets_received__sum'],
                'avg': group.aggregate(Avg('tickets_received'))['tickets_received__avg']
            },
            'tickets_closed': {
                'total': group.aggregate(Sum('tickets_closed'))['tickets_closed__sum'],
                'avg': group.aggregate(Avg('tickets_closed'))['tickets_closed__avg']
            },
            'virtual_machines': {
                'total': group.aggregate(Sum('virtual_machines'))['virtual_machines__sum'],
                'avg': group.aggregate(Avg('virtual_machines'))['virtual_machines__avg']
            },
            'license_cost': {
                'total': group.aggregate(Sum('license_cost'))['license_cost__sum'],
                'avg': group.aggregate(Avg('license_cost'))['license_cost__avg']
            }
        }

    return data


def get_automation_data(key, choices, date=None):
    data = {}
    for item in choices:
        try:
            automation = Automation.objects.get(functional_group__abbreviation=key,
                                                column_field=item[0])

            if automation.script_file:
                try:
                    exec(automation.script_file.read())
                except IOError:
                    continue

                try:
                    result = run_script(date)
                except Exception:
                    result = 0

                data[item[0]] = result
        except Automation.DoesNotExist:
            continue

    return data


def aggregate_subteam_to_team(subteam):
    # print subteam.created.date(), subteam.subteam
    year = subteam.created.date().year
    month = subteam.created.date().month
    day = subteam.created.date().day

    if subteam.functional_group.abbreviation == 'QE':
        try:
            team = InnovationMetrics.objects.get(functional_group__abbreviation=subteam.functional_group.abbreviation,
                                                 subteam__isnull=True,
                                                 created__year=year,
                                                 created__month=month,
                                                 created__day=day)
            subteams = InnovationMetrics.objects.filter(functional_group__abbreviation=subteam.functional_group.abbreviation,
                                                        subteam__isnull=False,
                                                        created__year=year,
                                                        created__month=month,
                                                        created__day=day)
            exclusion_list = ['id', 'created', 'confirmed', 'updated', 'functional_group', 'subteam',
                              'avg_throughput', 'operational_cost', 'total_operational_cost']
            aggregate_save_to_team(team, subteams, exclusion_list)

        except InnovationMetrics.DoesNotExist:
            pass

    elif subteam.functional_group.abbreviation == 'RE':
        try:
            team = RequirementMetrics.objects.get(functional_group__abbreviation=subteam.functional_group.abbreviation,
                                                  subteam__isnull=True,
                                                  created__year=year,
                                                  created__month=month,
                                                  created__day=day)
            subteams = RequirementMetrics.objects.filter(functional_group__abbreviation=subteam.functional_group.abbreviation,
                                                         subteam__isnull=False,
                                                         created__year=year,
                                                         created__month=month,
                                                         created__day=day)
            exclusion_list = ['id', 'created', 'confirmed', 'updated', 'functional_group', 'subteam',
                              'avg_throughput', 'gross_available_time', 'efficiency',
                              'operational_cost', 'total_operational_cost']
            aggregate_save_to_team(team, subteams, exclusion_list)

        except RequirementMetrics.DoesNotExist:
            pass

    elif subteam.functional_group.abbreviation == 'TL':
        try:
            team = LabMetrics.objects.get(functional_group__abbreviation=subteam.functional_group.abbreviation,
                                          subteam__isnull=True,
                                          created__year=year,
                                          created__month=month,
                                          created__day=day)
            subteams = LabMetrics.objects.filter(functional_group__abbreviation=subteam.functional_group.abbreviation,
                                                 subteam__isnull=False,
                                                 created__year=year,
                                                 created__month=month,
                                                 created__day=day)
            exclusion_list = ['id', 'created', 'confirmed', 'updated', 'functional_group', 'subteam']
            aggregate_save_to_team(team, subteams, exclusion_list)

        except LabMetrics.DoesNotExist:
            pass

    elif subteam.functional_group.abbreviation in ['QA', 'TE']:
        try:
            team = TestMetrics.objects.get(functional_group__abbreviation=subteam.functional_group.abbreviation,
                                           subteam__isnull=True,
                                           created__year=year,
                                           created__month=month,
                                           created__day=day)

            subteams = TestMetrics.objects.filter(functional_group__abbreviation=subteam.functional_group.abbreviation,
                                                  subteam__isnull=False,
                                                  created__year=year,
                                                  created__month=month,
                                                  created__day=day)
            exclusion_list = ['id', 'created', 'confirmed', 'updated', 'functional_group', 'subteam',
                              'auto_footprint_dev_age', 'auto_footprint_execution_age', 'avg_throughput',
                              'active_tickets', 'active_projects', 'auto_and_execution_time',
                              'gross_available_time', 'efficiency',
                              'operational_cost', 'total_operational_cost', 'auto_savings']
            # team_fields = team._meta.get_fields()
            # aggregate_fields = [field for field in team_fields if field.name not in exclusion_list]
            #
            # for field in aggregate_fields:
            #     team.__dict__[field.get_attname()] = subteams.aggregate(Sum(field.get_attname())).values()[0]
            # team.save()
            aggregate_save_to_team(team, subteams, exclusion_list)

        except TestMetrics.DoesNotExist:
            pass


def aggregate_save_to_team(team, subteams, exclusion_list):
    team_fields = team._meta.get_fields()
    aggregate_fields = [field for field in team_fields if field.name not in exclusion_list]

    for field in aggregate_fields:
        team.__dict__[field.get_attname()] = subteams.aggregate(Sum(field.get_attname())).values()[0]
    if not team.updated:
        team.updated = True
    team.save()
