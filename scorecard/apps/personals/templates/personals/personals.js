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

$(".dropdown-menu li a").click(function(){
    //console.log($(this).text());
    $.getJSON("{% url 'personals:fetch_personals_by_date' %}?date={0}".format($(this).text())).done(function(data){
        //console.log(data);

        var pq_content = '',
            qa_content = '',
            te_content = '',
            qi_content = '',
            re_content = '',
            tl_content = '';

        $.each(data['pq_personals'], function(index, person){
            pq_content += '<tr>'
                + '<td><a href=\"personal_stats\/{0}\/?key=PQ\">'.format(person['id']) + person['staff'] +'</a></td>'
                + '<td>' + person['tc_manual_dev'] + '</td>'
                + '<td>' + person['tc_manual_exec'] + '</td>'
                + '<td>' + person['tc_auto_dev'] + '</td>'
                + '<td>' + person['tc_auto_exec'] + '</td>'
                + '</tr>'
        });

        $.each(data['qa_personals'], function(index, person){
            qa_content += '<tr>'
                + '<td><a href=\"personal_stats\/{0}\/?key=QA\">'.format(person['id']) + person['staff'] +'</a></td>'
                + '<td>' + person['tc_manual_dev'] + '</td>'
                + '<td>' + person['tc_manual_exec'] + '</td>'
                + '<td>' + person['tc_auto_dev'] + '</td>'
                + '<td>' + person['tc_auto_exec'] + '</td>'
                + '</tr>'
        });

        $.each(data['te_personals'], function(index, person){
            te_content += '<tr>'
                + '<td><a href=\"personal_stats\/{0}\/?key=TE\">'.format(person['id']) + person['staff'] +'</a></td>'
                + '<td>' + person['tc_manual_dev'] + '</td>'
                + '<td>' + person['tc_manual_exec'] + '</td>'
                + '<td>' + person['tc_auto_dev'] + '</td>'
                + '<td>' + person['tc_auto_exec'] + '</td>'
                + '</tr>'
        });

        $.each(data['qi_personals'], function(index, person){
            qi_content += '<tr>'
                + '<td><a href=\"personal_stats\/{0}\/?key=QI\">'.format(person['id']) + person['staff'] +'</a></td>'
                + '<td>' + person['story_points'] + '</td>'
                + '<td>' + person['unit_tests_dev'] + '</td>'
                + '<td>' + person['analysis_time'] + '</td>'
                + '</tr>'
        });

        $.each(data['re_personals'], function(index, person){
            re_content += '<tr>'
                + '<td><a href=\"personal_stats\/{0}\/?key=RE\">'.format(person['id']) + person['staff'] +'</a></td>'
                + '<td>' + person['analysis_time'] + '</td>'
                + '<td>' + person['revisions'] + '</td>'
                + '<td>' + person['rework_internal'] + '</td>'
                + '<td>' + person['rework_external'] + '</td>'
                + '<td>' + person['travel_cost'] + '</td>'
                + '</tr>'
        });

        $.each(data['tl_personals'], function(index, person){
            tl_content += '<tr>'
                + '<td><a href=\"personal_stats\/{0}\/?key=TL\">'.format(person['id']) + person['staff'] +'</a></td>'
                + '<td>' + person['tickets_closed'] + '</td>'
                + '<td>' + person['rework_time'] + '</td>'
                + '<td>' + person['overtime_weekday'] + '</td>'
                + '</tr>'
        });

        $(".tab-content .date-title").html('<h4>'+data['date'] + '</h4>');
        $("#pq-content .table-responsive .table tbody").html(pq_content);
        $("#qa-content .table-responsive .table tbody").html(qa_content);
        $("#te-content .table-responsive .table tbody").html(te_content);
        $("#qi-content .table-responsive .table tbody").html(qi_content);
        $("#re-content .table-responsive .table tbody").html(re_content);
        $("#tl-content .table-responsive .table tbody").html(tl_content);
    })
});