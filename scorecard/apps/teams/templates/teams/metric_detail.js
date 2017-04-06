var key = '{{metric.functional_group.abbreviation}}';
var hours,
    hourly_rate, hourly_rate_contractor,
    hourly_rate_auto;

var staff = $('#id_staffs'),
    operational_cost = $('#operational_cost'),
    license_cost = $('#id_license_cost');

switch (key) {
    case 'QE':
        hours = 40;
        hourly_rate = 45;
        costCal();
        autoCal();
        qualityCal();
        break;
    case 'TL':
        qualityCal();
        efficiencyCal();
        break;
    case 'RE':
        hours = 30;
        hourly_rate = 50;
        costCal();
        costReworkCal();
        qualityCal();
        efficiencyCal();
        break;
    case 'QA':
    case 'TE':
        bundleTestMetricCal();
}

// put TestMetric calculation together
function bundleTestMetricCal() {
    hours = '{{test_metric_config.hours_per_week}}';
    hourly_rate = '{{test_metric_config.costs_per_hour_staff}}';
    hourly_rate_contractor = '{{test_metric_config.costs_per_hour_contractor}}';
    hourly_rate_auto = '{{test_metric_config.costs_per_hour_staff}}';

    costCal();
    autoCal();
    qualityCal();
    efficiencyCal();
}


// Cost calculation include: Operational Cost and Total Cost
function costCal() {
    switch (key) {
        case 'QA':
        case 'TE':
            staff.on('input', function(){
                operational_cost.val(operationalCal(this.value, hours, hourly_rate)
                    + operationalCal($('#id_contractors').val(), hours, hourly_rate_contractor));
                $('#total_cost').val(parseFloat(license_cost.val()) + parseFloat(operational_cost.val()));
            });

            $('#id_contractors').on('input', function(){
                operational_cost.val(operationalCal(this.value, hours, hourly_rate_contractor)
                    + operationalCal(staff.val(), hours, hourly_rate));
                $('#total_cost').val(parseFloat(license_cost.val()) + parseFloat(operational_cost.val()));
            });

            license_cost.on('input', function(){
                $('#total_cost').val(parseFloat(this.value) + parseFloat(operational_cost.val()));
            });
            break;
        default:
            staff.on('input', function(){
                operational_cost.val(operationalCal(this.value, hours, hourly_rate));
                $('#total_cost').val(parseFloat(license_cost.val()) + parseFloat(operational_cost.val()));
            });

            license_cost.on('input', function(){
                $('#total_cost').val(parseFloat(this.value) + parseFloat(operational_cost.val()));
            });
        }
}

// Cost of Rework calculation for RE
function costReworkCal() {
    $('#id_rework_external_time').on('input', function(){
        $('#rework_external_cost').val(this.value * 50);
    });
}

// Cost of autoSavings calculation for QA/TE, External/Internal savings for QE
function autoCal() {
    switch (key) {
        case 'TE':
        case 'QA':
            $('#id_tc_auto_execution_time').on('input', function () {
                $('#auto_savings').val(autoSavingsCal($('#id_estimate_auto_time').val(), this.value, hourly_rate_auto));
            });
            $('#id_estimate_auto_time').on('input', function () {
                $('#auto_savings').val(autoSavingsCal(this.value, $('#id_tc_auto_execution_time').val(), hourly_rate_auto))
            });
            break;
        case 'QE':
            $('#id_other_savings').on('input', function(){
                qeInternalSavingsCal();
            });
            $('#id_ceeq_daily_summaries').on('input', function(){
                qeInternalSavingsCal();
            });
            $('#id_visilog_txl_parsed').on('input', function(){
                qeExternalSavingsCal();
            });
            $('#id_pheme_manual_tests').on('input', function(){
                qeExternalSavingsCal();
            });
            $('#id_pheme_auto_tests').on('input', function(){
                qeExternalSavingsCal();
            });
            break;
    }
}

// Cost of operational calculation
function operationalCal(staffs_or_contractors, hours, hourly_rate) {
    return staffs_or_contractors * hours * hourly_rate;
}

// Cost of automation calculation for QA, TE
function autoSavingsCal(estimate_time, tc_auto_time, hourly_rate_auto) {
    switch (key) {
        case 'TE':
        case 'QA':
            return (estimate_time - tc_auto_time) * hourly_rate_auto;
    }
}

// Calculation of average throughput for RE, 'QA, TE'
function qualityCal() {
    switch (key) {
        case 'QE':
            staff.on('input', function(){
                var avg_throughput = parseFloat($('#id_story_points_execution').val()) / parseFloat(this.value)
                $('#avg_throughput_qi').val(avg_throughput.toFixed(2));
            });
            $('#id_story_points_execution').on('input', function(){
                var avg_throughput = parseFloat(this.value) / parseFloat(staff.val())
                $('#avg_throughput_qi').val(avg_throughput.toFixed(2));
            });
            break;
        case 'RE':
            $('#id_active_projects').on('input', function(){
                $('#avg_throughput').val(parseFloat(this.value) + parseFloat($('#id_team_initiative').val()));
            });
            $('#id_team_initiative').on('input', function(){
                $('#avg_throughput').val(parseFloat(this.value) + parseFloat($('#id_active_projects').val()));
            });
            break;
        case 'TL':
            $('#id_builds_submitted').on('input', function(){
                tlBuildRejectedCal();
            });
            $('#id_builds_accepted').on('input', function(){
                tlBuildRejectedCal();
            });
            break;
        case 'QA':
        case 'TE':
            $('#id_staffs').on('input', function(){
                avgThroughputTestMetric();
            });
            $('#id_contractors').on('input', function() {
                avgThroughputTestMetric();
            });
            $('#id_testers').on('input', function(){
                grossAvailableTimeCal();
                efficiencyUtilizationCal();
            });
            $('#id_tc_manual_dev').on('input', function() {
                avgThroughputTestMetric();
                autoFootprintDevAge();
            });
            $('#id_tc_manual_execution').on('input', function() {
                avgThroughputTestMetric();
                autoFootprintExecutionAge();
            });
            $('#id_tc_auto_dev').on('input', function() {
                avgThroughputTestMetric();
                autoFootprintDevAge();
            });
            $('#id_tc_auto_execution').on('input', function() {
                avgThroughputTestMetric();
                autoFootprintExecutionAge();
            });
    }
}

// Calculation of average throughput for QA, TE
function avgThroughputTestMetric() {
    var hrs = parseFloat(staff.val()) + parseFloat($('#id_contractors').val()),
        dev = parseFloat($('#id_tc_manual_dev').val()) + parseFloat($('#id_tc_auto_dev').val()),
        execution = parseFloat($('#id_tc_manual_execution').val()) + parseFloat($('#id_tc_auto_execution').val());
    $('#avg_throughput').val(((dev + execution) / hrs).toFixed(2));
}

// Calculation of auto footprint dev age for QA, TE
function autoFootprintDevAge() {
    var manual = parseFloat($('#id_tc_manual_dev').val()),
        auto = parseFloat($('#id_tc_auto_dev').val());
    $('#auto_footprint_dev').val((auto / (manual + auto) * 100).toFixed(2) + '%');
}

// Calculation of auto footprint execution age for QA, TE
function autoFootprintExecutionAge(){
    var manual = parseFloat($('#id_tc_manual_execution').val()),
        auto = parseFloat($('#id_tc_auto_execution').val());
    $('#auto_footprint_execution').val((auto / (manual + auto) * 100).toFixed(2) + '%');
}

// Calculation of efficiency for RE, 'QA, TE'
function efficiencyCal() {
    switch (key) {
        case 'RE':
            staff.on('input', function(){
                $('#gross_available').val(this.value * 6 * 5);
                var efficiency = ($('#id_elicitation_analysis_time').val() / (this.value * 6 * 5) * 100).toFixed(2) ;
                $('#id_efficiency').val(efficiency + '%');
            });
            $('#id_elicitation_analysis_time').on('input', function(){
                var efficiency = (this.value / $('#gross_available').val() * 100).toFixed(2) ;
                $('#id_efficiency').val(efficiency + '%');
            });
            break;
        case 'TL':
            $('#id_administration_time').on('input', function(){
                efficiencyEfficiencyCal();
                efficiencyUtilizationCal();
            });
            $('#id_project_time').on('input', function(){
                efficiencyEfficiencyCal();
                efficiencyUtilizationCal();
            });
            $('#id_ticket_time').on('input', function(){
                efficiencyEfficiencyCal();
                efficiencyUtilizationCal();
            });
            $('#id_staffs').on('input', function(){
                efficiencyEfficiencyCal();
                efficiencyUtilizationCal();
            });
            $('#id_pto_holiday_time').on('input', function(){
                efficiencyUtilizationCal();
            });
            break;
        case 'QA':
        case 'TE':
            $('#id_ticket_prep, #id_ticket_execution').on('input', function(){
                activeTicketsCal();
            });
            $('#id_project_prep, #id_project_execution').on('input', function(){
                activeProjectsCal();
            });
            $('#id_tc_manual_dev_time, #id_tc_manual_execution_time, #id_tc_auto_dev_time, #id_tc_auto_execution_time').on('input', function(){
                autoAndExecTimeCal();
            });
            $('#id_initiative_time, #id_pto_holiday_time').on('input', function(){
                efficiencyUtilizationCal();
            });
            $('#id_standard_work_time').on('input', function(){
                productiveTimeCal();
            })
    }
}

function activeTicketsCal(){
    var tickets = parseFloat($('#id_ticket_prep').val()) + parseFloat($('#id_ticket_execution').val());
    $('#active_tickets').val(tickets);
}

function activeProjectsCal(){
    var projects = parseFloat($('#id_project_prep').val()) + parseFloat($('#id_project_execution').val());
    $('#active_projects').val(projects);
}

function autoAndExecTimeCal(){
    var time = parseFloat($('#id_tc_manual_dev_time').val())
        + parseFloat($('#id_tc_manual_execution_time').val())
        + parseFloat($('#id_tc_auto_dev_time').val())
        + parseFloat($('#id_tc_auto_execution_time').val());
    $('#auto_and_execution_time').val(time.toFixed(2));
    productiveTimeCal();
    efficiencyEfficiencyCal();
}

function grossAvailableTimeCal(){
    var gross = parseFloat($('#id_testers').val()) * 30;
    $('#gross_available_time').val(gross.toFixed(2));
    efficiencyEfficiencyCal();
}

function efficiencyEfficiencyCal(){
    switch (key) {
        case 'QA':
        case 'TE':
            var effi = parseFloat($('#auto_and_execution_time').val()) / parseFloat($('#gross_available_time').val()) * 100;
            $('#id_test_efficiency').val(effi.toFixed(2) + '%');
            break;
        case 'TL':
            var effi = 0;
            if ($('#id_staffs').val() != 0) {
                effi = (parseFloat($('#id_administration_time').val())
                    + parseFloat($('#id_project_time').val())
                    + parseFloat($('#id_ticket_time').val())) / ($('#id_staffs').val() * 30) * 100;
            }
            $('#id_efficiency').val(effi.toFixed(2) + '%');
    }
}

function productiveTimeCal(){
    var productive_time = parseFloat($('#auto_and_execution_time').val()) + parseFloat($('#id_standard_work_time').val());
    $('#productive_hours').val(productive_time.toFixed(2));
    efficiencyUtilizationCal();
}

$('#collect_data_button').click(function(){
    var key = $('#collect_data_key').val(),
        date = $('#collect_data_date').val();
    //console.log(key, date);
    $.getJSON("{% url 'teams:fetch_team_members_by_date'%}?key={0}&date={1}&subteam={{metric.subteam.id}}".format(key, date)).done(function(data){
        //console.log(data);
        $.ajaxSetup({cache: false});
        var contents_head = '<tr><th>Name</th><th>Updated</th></tr>',
            contents_body = '';
        $.each(data, function(index, value){
            contents_body += '<tr><td>' +value['staff'] + '</td><td>' + value['updated'] + '</td></tr>';
        });

        var contents = "<table id='tableData' class='table table-bordered'>"
            + "<thead>" + contents_head + "</thead>"
            + "<tbody>" +contents_body + "</tbody>"
            + "</table>";
        $('#collect-data-body').html(contents);
    });
    $('#collect-data-modal').modal('show');
});

function qeInternalSavingsCal(){
    var value = $('#id_ceeq_daily_summaries').val() * 20 + parseFloat($('#id_other_savings').val());
    $('#internal_savings').val(value);
}

function qeExternalSavingsCal(){
    var value = $('#id_visilog_txl_parsed').val() * .33
        + $('#id_pheme_manual_tests').val() * 1.79
        + $('#id_pheme_auto_tests').val() * 1.97;
    $('#external_savings').val(value.toFixed(2));
}

function efficiencyUtilizationCal(){
    var value = 0;
    switch (key){
        case 'QA':
        case 'TE':
            value = (parseFloat($('#productive_hours').val()) + parseFloat($('#id_initiative_time').val())) / ($('#id_testers').val() * 40 - parseFloat($('#id_pto_holiday_time').val())) * 100;
            $('#id_test_utilization').val(value.toFixed(2) + '%');
            break;
        case 'TL':
            value = (parseFloat($('#id_administration_time').val())
                + parseFloat($('#id_project_time').val())
                + parseFloat($('#id_ticket_time').val())) / ($('#id_staffs').val() * 40 - parseFloat($('#id_pto_holiday_time').val())) * 100;
            $('#id_utilization').val(value.toFixed(2) + '%');
            break;
    }
}

function tlBuildRejectedCal(){
    var value = parseFloat($('#id_builds_submitted').val()) - parseFloat($('#id_builds_accepted').val());
    $('#id_builds_rejected').val(value);
}