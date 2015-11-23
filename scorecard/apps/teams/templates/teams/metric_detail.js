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
        break;
    case 'QA':
        hours = 40;
        hourly_rate = 40;
        hourly_rate_contractor = 100;
        hourly_rate_auto = 40;
        costCal();
        autoCal();
        break;
    case 'TE':
        hours = 40;
        hourly_rate = 50;
        hourly_rate_auto = 50;
        costCal();
        autoCal();
}

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

function costReworkCal() {
    $('#id_rework_external_time').on('input', function(){
        $('#rework_external_cost').val(this.value * 50);
    });
}

function autoCal() {
    $('#id_tc_auto_execution_time').on('input', function(){
        $('#auto_savings').val(autoSavingsCal(this.value, hourly_rate_auto));
    })
}

function operationalCal(staffs, hours, hourly_rate) {
    return staffs * hours * hourly_rate;
}

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

function avgThroughputCal() {
    switch (key) {
        case 'RE':
            $('#id_active_projects').on('input', function(){
                $('#avg_throughput').val(parseFloat(this.value) + parseFloat($('#id_team_initiative').val()));
            });
            $('#id_team_initiative').on('input', function(){
                $('#avg_throughput').val(parseFloat(this.value) + parseFloat($('#id_active_projects').val()));
            });
    }
}

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