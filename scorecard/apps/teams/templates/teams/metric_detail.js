var key = '{{metric.functional_group.key}}';
var hours,
    hourly_rate, hourly_rate_contractor,
    hourly_rate_auto;

switch (key) {
    case 'QI':
        hours = 40;
        hourly_rate = 45;
        costCalculation();
        break;
    case 'TL':
        //console.log('tl, nothing to do');
        break;
    case 'RE':
        hours = 30;
        hourly_rate = 50;
        costCalculation();
        costReworkCalculation();
        avgThroughputCalculation();
        break;
    case 'PQ':
        hours = 30;
        hourly_rate = 60;
        hourly_rate_auto = 40;
        costCalculation();
        autoCalculation();
        break;
    case 'QA':
        hours = 40;
        hourly_rate = 40;
        hourly_rate_contractor = 100;
        hourly_rate_auto = 40;
        costCalculation();
        autoCalculation();
        break;
    case 'TE':
        hours = 40;
        hourly_rate = 50;
        hourly_rate_auto = 50;
        costCalculation();
        autoCalculation();
}

function costCalculation() {
    switch (key) {
        case 'QA':
            $('#id_staffs').on('input', function(){
                $('#operational_cost').val(operationalCalculation(this.value, hours, hourly_rate)
                    + operationalCalculation($('#id_contractors').val(), hours, hourly_rate_contractor));
                $('#total_cost').val(parseFloat($('#id_license_cost').val()) + parseFloat($('#operational_cost').val()));
            });

            $('#id_contractors').on('input', function(){
                $('#operational_cost').val(operationalCalculation(this.value, hours, hourly_rate_contractor)
                    + operationalCalculation($('#id_staffs').val(), hours, hourly_rate));
                $('#total_cost').val(parseFloat($('#id_license_cost').val()) + parseFloat($('#operational_cost').val()));
            });

            $('#id_license_cost').on('input', function(){
                $('#total_cost').val(parseFloat(this.value) + parseFloat($('#operational_cost').val()));
            });
            break;
        default:
            $('#id_staffs').on('input', function(){
                $('#operational_cost').val(operationalCalculation(this.value, hours, hourly_rate));
                $('#total_cost').val(parseFloat($('#id_license_cost').val()) + parseFloat($('#operational_cost').val()));
            });

            $('#id_license_cost').on('input', function(){
                $('#total_cost').val(parseFloat(this.value) + parseFloat($('#operational_cost').val()));
            });
        }
}

function costReworkCalculation() {
    $('#id_rework_external_time').on('input', function(){
        $('#rework_external_cost').val(this.value * 50);
    });
}

function autoCalculation() {
    $('#id_tc_auto_execution_time').on('input', function(){
        $('#auto_savings').val(autoSavingsCalculation(this.value, hourly_rate_auto));
    })
}

function operationalCalculation(staffs, hours, hourly_rate) {
    return staffs * hours * hourly_rate;
}

function autoSavingsCalculation(tc_auto_time, hourly_rate_auto) {
    switch (key) {
        case 'TE':
            return (parseFloat(tc_auto_time) + 37) * hourly_rate_auto;
            break;
        case 'PQ':
        case 'QA':
            return tc_auto_time * hourly_rate_auto;
    }
}

function avgThroughputCalculation() {
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