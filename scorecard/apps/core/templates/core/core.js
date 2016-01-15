/**
 * Created by sliu on 1/8/16.
 * Used for Sub-Tab selection for Teams
 */

// String format custom method
String.prototype.format = function () {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

var active_tab = String(""),
    key = '{{key}}';

if (!key){
    key = '{{user.humanresource.functional_group.key}}';
}

$('#subnav-tabs').find('a[data-toggle="tab"]').on('show.bs.tab', function(e){
    active_tab = e.target.hash;
});


$(document).ready(function(){
    switch (key) {
        case 'PQ':
            $('#subnav-tabs').find('a[href="#product_quality"]').tab('show');
            break;
        case 'QA':
            $('#subnav-tabs').find('a[href="#quality_assurance"]').tab('show');
            break;
        case 'QI':
            $('#subnav-tabs').find('a[href="#quality_innovation"]').tab('show');
            break;
        case 'RE':
            $('#subnav-tabs').find('a[href="#requirements_engineering"]').tab('show');
            break;
        case 'TE':
            $('#subnav-tabs').find('a[href="#test_engineering"]').tab('show');
            break;
        case 'TL':
            $('#subnav-tabs').find('a[href="#test_lab"]').tab('show');
            break;
        default:
            $('#subnav-tabs').find('a[href="#product_quality"]').tab('show');
    }
});

$('.input-date').datepicker();

