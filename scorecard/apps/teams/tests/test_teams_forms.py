from datetime import datetime
import random
from django.test import TestCase

from scorecard.apps.teams.forms import InnovationForm, RequirementForm, LabForm, TestForm


class InnovationFormTest(TestCase):
    # def test_innovation_form_valid_with_valid_params(self):
    #     data = {
    #         'staffs': random.randint(1, 100),
    #         'contractors': random.randint(1, 100),
    #         'openings': random.randint(1, 100),
    #         'compliments': random.randint(1, 100),
    #         'complaints': random.randint(1, 100),
    #         'escalations': random.randint(1, 100),
    #         'slas_met': random.randint(1, 100),
    #         'delays_introduced_time': random.randint(1, 100),
    #         'sdis_not_prevented': random.randint(1, 100),
    #         'resource_swap': random.randint(1, 100),
    #         'rework_introduced_time': random.randint(1, 100),
    #         'avg_team_size': random.randint(1, 100),
    #         'overtime_weekday': random.randint(1, 100),
    #         'overtime_weekend': random.randint(1, 100),
    #         'rework_time': random.randint(1, 100),
    #         'resource_swap_time': random.randint(1, 100),
    #         'license_cost': random.randint(1, 100),
    #         'other_savings': random.randint(1, 100),
    #         'story_points_backlog': random.randint(1, 100),
    #         'story_points_prep': random.randint(1, 100),
    #         'story_points_execution': random.randint(1, 100),
    #         'unit_tests_dev': random.randint(1, 100),
    #         'unit_tests_coverage': random.randint(1, 100),
    #         'documentation_coverage': random.randint(1, 100),
    #         'defects_in_dev': random.randint(1, 100),
    #         'elicitation_analysis_time': random.randint(1, 100),
    #         'revisions': random.randint(1, 100),
    #         'active_projects': random.randint(1, 100),
    #         'uat_defects_not_prevented': random.randint(1, 100),
    #         'pheme_manual_tests': random.randint(1, 100),
    #         'pheme_auto_tests': random.randint(1, 100),
    #         'visilog_txl_parsed': random.randint(1, 100),
    #         'visilog_txl_schema_violation': random.randint(1, 100),
    #
    #         'table_row': [random.randint(1, 10)],
    #         'quality_graph': {'title': 'UAT Defects',
    #                           'data': [{'date': datetime.now().strftime("%b %-d")}],
    #                           'value': random.randint(1, 10)},
    #         'efficiency_graph': {'title': 'Average Throughput',
    #                              'data': [{'date': datetime.now().strftime("%b %-d")}],
    #                              'value': random.randint(1, 10)},
    #         'throughput_graph': {'title': 'Defects Found',
    #                              'data': [{'date': datetime.now().strftime("%b %-d")}],
    #                              'value': random.randint(1, 10)},
    #         'progress_graph': {'title': 'Test Case Automation',
    #                            'data': [{'date': datetime.now().strftime("%b %-d")}],
    #                            'value': random.randint(1, 10)},
    #     }
    #     form = InnovationForm(data=data)
    #     self.assertTrue(form.is_valid())

    def test_innovation_form_invalid_with_blank_data(self):
        form = InnovationForm({})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'staffs': ['This field is required.'],
            'contractors': ['This field is required.'],
            'openings': ['This field is required.'],
            'compliments': ['This field is required.'],
            'complaints': ['This field is required.'],
            'escalations': ['This field is required.'],
            'slas_met': ['This field is required.'],
            'delays_introduced_time': ['This field is required.'],
            'sdis_not_prevented': ['This field is required.'],
            'resource_swap': ['This field is required.'],
            'rework_introduced_time': ['This field is required.'],
            'avg_team_size': ['This field is required.'],
            'overtime_weekday': ['This field is required.'],
            'overtime_weekend': ['This field is required.'],
            'rework_time': ['This field is required.'],
            'resource_swap_time': ['This field is required.'],
            'license_cost': ['This field is required.'],
            'other_savings': ['This field is required.'],
            'story_points_backlog': ['This field is required.'],
            'story_points_prep': ['This field is required.'],
            'story_points_execution': ['This field is required.'],
            'unit_tests_dev': ['This field is required.'],
            'unit_tests_coverage': ['This field is required.'],
            'documentation_coverage': ['This field is required.'],
            'defects_in_dev': ['This field is required.'],
            'elicitation_analysis_time': ['This field is required.'],
            'revisions': ['This field is required.'],
            'active_projects': ['This field is required.'],
            'uat_defects_not_prevented': ['This field is required.'],
            'pheme_manual_tests': ['This field is required.'],
            'pheme_auto_tests': ['This field is required.'],
            'visilog_txl_parsed': ['This field is required.'],
            'visilog_txl_schema_violation': ['This field is required.']
        })


class RequirementFormTest(TestCase):
    def test_requirement_form_valid_with_valid_params(self):
        data = {
            'staffs': random.randint(1, 100),
            'openings': random.randint(1, 100),
            'contractors': random.randint(1, 100),
            'compliments': random.randint(1, 100),
            'complaints': random.randint(1, 100),
            'backlog': random.randint(1, 100),
            'team_initiative': random.randint(1, 100),
            'active_projects': random.randint(1, 100),
            'elicitation_analysis_time': random.randint(1, 100),
            'revisions': random.randint(1, 100),
            'rework_introduced_time': random.randint(1, 100),
            'slas_met': random.randint(1, 100),
            'slas_missed': random.randint(1, 100),
            'delays_introduced_time': random.randint(1, 100),
            'escalations': random.randint(1, 100),
            'overtime_weekday': random.randint(1, 100),
            'overtime_weekend': random.randint(1, 100),
            'rework_external_time': random.randint(1, 100),
            'travel_cost': random.randint(1, 100)
        }
        form = RequirementForm(data=data)
        self.assertTrue(form.is_valid)

    def test_requirement_form_invalid_with_blank(self):
        form = RequirementForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'staffs': ['This field is required.'],
            'openings': ['This field is required.'],
            'contractors': ['This field is required.'],
            'compliments': ['This field is required.'],
            'complaints': ['This field is required.'],
            'backlog': ['This field is required.'],
            'team_initiative': ['This field is required.'],
            'active_projects': ['This field is required.'],
            'elicitation_analysis_time': ['This field is required.'],
            'revisions': ['This field is required.'],
            'rework_introduced_time': ['This field is required.'],
            'slas_met': ['This field is required.'],
            'slas_missed': ['This field is required.'],
            'delays_introduced_time': ['This field is required.'],
            'escalations': ['This field is required.'],
            'overtime_weekday': ['This field is required.'],
            'overtime_weekend': ['This field is required.'],
            'rework_external_time': ['This field is required.'],
            'travel_cost': ['This field is required.'],
        })


class LabFormTest(TestCase):
    def test_lab_form_valid_with_valid_params(self):
        data = {
            'staffs': random.randint(1, 100),
            'openings': random.randint(1, 100),
            'contractors': random.randint(1, 100),
            'compliments': random.randint(1, 100),
            'complaints': random.randint(1, 100),
            'tickets_received': random.randint(1, 100),
            'tickets_closed': random.randint(1, 100),
            'virtual_machines': random.randint(1, 100),
            'physical_machines': random.randint(1, 100),
            'power_consumption_ups_a': random.randint(1, 100),
            'power_consumption_ups_b': random.randint(1, 100),
            'license_cost': random.randint(1, 100)
        }
        form = LabForm(data=data)
        self.assertTrue(form.is_valid())

    def test_lab_form_invalid_with_blank(self):
        form = LabForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'staffs': ['This field is required.'],
            'openings': ['This field is required.'],
            'contractors': ['This field is required.'],
            'compliments': ['This field is required.'],
            'complaints': ['This field is required.'],
            'tickets_received': ['This field is required.'],
            'tickets_closed': ['This field is required.'],
            'virtual_machines': ['This field is required.'],
            'physical_machines': ['This field is required.'],
            'power_consumption_ups_a': ['This field is required.'],
            'power_consumption_ups_b': ['This field is required.'],
            'license_cost': ['This field is required.']
        })


class TestFormTest(TestCase):
    # def test_test_form_valid_with_valid_params(self):
    #     data = {
    #         'staffs': random.randint(1, 100),
    #         'contractors': random.randint(1, 100),
    #         'openings': random.randint(1, 100),
    #         'compliments': random.randint(1, 100),
    #         'complaints': random.randint(1, 100),
    #         'escalations': random.randint(1, 100),
    #         'slas_met': random.randint(1, 100),
    #         'delays_introduced_time': random.randint(1, 100),
    #         'sdis_not_prevented': random.randint(1, 100),
    #         'resource_swap': random.randint(1, 100),
    #         'rework_introduced_time': random.randint(1, 100),
    #         'avg_team_size': random.randint(1, 100),
    #         'overtime_weekday': random.randint(1, 100),
    #         'overtime_weekend': random.randint(1, 100),
    #         'rework_time': random.randint(1, 100),
    #         'resource_swap_time': random.randint(1, 100),
    #         'license_cost': random.randint(1, 100),
    #         'other_savings': random.randint(1, 100),
    #         'team_initiative': random.randint(1, 100),
    #         'ticket_backlog': random.randint(1, 100),
    #         'ticket_prep': random.randint(1, 100),
    #         'ticket_execution': random.randint(1, 100),
    #         'ticket_closed': random.randint(1, 100),
    #         'project_backlog': random.randint(1, 100),
    #         'project_prep': random.randint(1, 100),
    #         'project_execution': random.randint(1, 100),
    #         'project_closed': random.randint(1, 100),
    #         'tc_manual_dev': random.randint(1, 100),
    #         'tc_manual_dev_time': random.randint(1, 100),
    #         'tc_manual_execution': random.randint(1, 100),
    #         'tc_manual_execution_time': random.randint(1, 100),
    #         'tc_auto_dev': random.randint(1, 100),
    #         'tc_auto_dev_time': random.randint(1, 100),
    #         'tc_auto_execution': random.randint(1, 100),
    #         'tc_auto_execution_time': random.randint(1, 100),
    #         'defect_caught': random.randint(1, 100),
    #         'uat_defects_not_prevented': random.randint(1, 100),
    #         'standards_violated': random.randint(1, 100),
    #         'avg_time_frame': random.randint(1, 100),
    #
    #         'table_row': [random.randint(1, 10)],
    #         'quality_graph': {'title': 'UAT Defects',
    #                           'data': [{'date': datetime.now().strftime("%b %-d")}],
    #                           'value': random.randint(1, 10)},
    #         'efficiency_graph': {'title': 'Average Throughput',
    #                              'data': [{'date': datetime.now().strftime("%b %-d")}],
    #                              'value': random.randint(1, 10)},
    #         'throughput_graph': {'title': 'Defects Found',
    #                              'data': [{'date': datetime.now().strftime("%b %-d")}],
    #                              'value': random.randint(1, 10)},
    #         'progress_graph': {'title': 'Test Case Automation',
    #                            'data': [{'date': datetime.now().strftime("%b %-d")}],
    #                            'value': random.randint(1, 10)},
    #     }
    #     form = TestForm(data=data)
    #     self.assertTrue(form.is_valid())

    def test_test_form_invalid_with_blank(self):
        form = TestForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'staffs': ['This field is required.'],
            'contractors': ['This field is required.'],
            'openings': ['This field is required.'],
            'compliments': ['This field is required.'],
            'complaints': ['This field is required.'],
            'escalations': ['This field is required.'],
            'slas_met': ['This field is required.'],
            'delays_introduced_time': ['This field is required.'],
            'sdis_not_prevented': ['This field is required.'],
            'resource_swap': ['This field is required.'],
            'rework_introduced_time': ['This field is required.'],
            'avg_team_size': ['This field is required.'],
            'overtime_weekday': ['This field is required.'],
            'overtime_weekend': ['This field is required.'],
            'rework_time': ['This field is required.'],
            'resource_swap_time': ['This field is required.'],
            'license_cost': ['This field is required.'],
            'other_savings': ['This field is required.'],
            'team_initiative': ['This field is required.'],
            'ticket_backlog': ['This field is required.'],
            'ticket_prep': ['This field is required.'],
            'ticket_execution': ['This field is required.'],
            'ticket_closed': ['This field is required.'],
            'project_backlog': ['This field is required.'],
            'project_prep': ['This field is required.'],
            'project_execution': ['This field is required.'],
            'project_closed': ['This field is required.'],
            'tc_manual_dev': ['This field is required.'],
            'tc_manual_dev_time': ['This field is required.'],
            'tc_manual_execution': ['This field is required.'],
            'tc_manual_execution_time': ['This field is required.'],
            'tc_auto_dev': ['This field is required.'],
            'tc_auto_dev_time': ['This field is required.'],
            'tc_auto_execution': ['This field is required.'],
            'tc_auto_execution_time': ['This field is required.'],
            'defect_caught': ['This field is required.'],
            'uat_defects_not_prevented': ['This field is required.'],
            'standards_violated': ['This field is required.'],
            'avg_time_frame': ['This field is required.']
        })
