var key = '{{metric.functional_group.key}}';
var hours,
    hourly_rate, hourly_rate_contractor,
    hourly_rate_auto;

var staff = $('#id_staffs'),
    operational_cost = $('#operational_cost'),
    license_cost = $('#id_license_cost');

switch (key) {
    case 'QI':
        hours = 40;
        hourly_rate = 45;
        costCal();
        break;
    case 'TL':
        //console.log('tl, nothing to do');
        break;
    case 'RE':
        hours = 30;
        hourly_rate = 50;
        costCal();
        costReworkCal();
        avgThroughputCal();
        efficiencyCal();
        break;
    case 'PQ':
        hours = 30;
        hourly_rate = 60;
        hourly_rate_auto = 40;
        costCal();
        autoCal();
        avgThroughputCal();
        break;
    case 'QA':
        hours = 40;
        hourly_rate = 40;
        hourly_rate_contractor = 100;
        hourly_rate_auto = 40;
        costCal();
        autoCal();
        avgThroughputCal();
        break;
    case 'TE':
        hours = 40;
        hourly_rate = 50;
        hourly_rate_auto = 50;
        costCal();
        autoCal();
        avgThroughputCal();
}

// Cost calculation include: Operational Cost and Total Cost
function costCal() {
    switch (key) {
        case 'QA':
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

// Cost of automation calculation for PQ, QA, TE
function autoCal() {
    $('#id_tc_auto_execution_time').on('input', function(){
        $('#auto_savings').val(autoSavingsCal(this.value, hourly_rate_auto));
    })
}

// Cost of operational calculation
function operationalCal(staffs, hours, hourly_rate) {
    return staffs * hours * hourly_rate;
}

// Cost of automation calculation for PQ, QA, TE
function autoSavingsCal(tc_auto_time, hourly_rate_auto) {
    switch (key) {
        case 'TE':
            return (parseFloat(tc_auto_time) + 37) * hourly_rate_auto;
            break;
        case 'PQ':
        case 'QA':
            return tc_auto_time * hourly_rate_auto;
    }
}

// Calculation of average throughput for RE, 'PQ, QA, TE'
function avgThroughputCal() {
    switch (key) {
        case 'RE':
            $('#id_active_projects').on('input', function(){
                $('#avg_throughput').val(parseFloat(this.value) + parseFloat($('#id_team_initiative').val()));
            });
            $('#id_team_initiative').on('input', function(){
                $('#avg_throughput').val(parseFloat(this.value) + parseFloat($('#id_active_projects').val()));
            });
            break;
        case 'PQ':
        case 'QA':
        case 'TE':
            $('#id_staffs').on('input', function(){
                avgThroughputTestMetric();
            });
            $('#id_contractors').on('input', function() {
                avgThroughputTestMetric();
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

// Calculation of average throughput for PQ, QA, TE
function avgThroughputTestMetric() {
    var hrs = parseFloat(staff.val()) + parseFloat($('#id_contractors').val()),
        dev = parseFloat($('#id_tc_manual_dev').val()) + parseFloat($('#id_tc_auto_dev').val()),
        execution = parseFloat($('#id_tc_manual_execution').val()) + parseFloat($('#id_tc_auto_execution').val());
    $('#avg_throughput').val(((dev + execution) / hrs).toFixed(2));
}

// Calculation of auto footprint dev age for PQ, QA, TE
function autoFootprintDevAge() {
    var manual = parseFloat($('#id_tc_manual_dev').val()),
        auto = parseFloat($('#id_tc_auto_dev').val());
    $('#auto_footprint_dev').val((auto / (manual + auto) * 100).toFixed(2) + '%');
}

// Calculation of auto footprint execution age for PQ, QA, TE
function autoFootprintExecutionAge(){
    var manual = parseFloat($('#id_tc_manual_execution').val()),
        auto = parseFloat($('#id_tc_auto_execution').val());
    $('#auto_footprint_execution').val((auto / (manual + auto) * 100).toFixed(2) + '%');
}

// Calculation of efficiency for RE, 'PQ, QA, TE'
function efficiencyCal() {
    switch (key) {
        case 'RE':
            staff.on('input', function(){
                $('#gross_available').val(this.value * 6 * 5);
            });
            $('#id_elicitation_analysis_time').on('input', function(){
                var efficiency = (this.value / $('#gross_available').val() * 100).toFixed(2) ;
                $('#id_efficiency').val(efficiency + '%');
            });
    }

}