
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

//$("select").change(function(){
//    $("select option:selected").each(function(){
//        console.log($(this).text())
//    })
//})