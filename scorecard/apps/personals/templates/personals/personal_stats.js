/**
 * Created by sliu on 3/31/16.
 */
$('#collect-data-button').click(function(){
    $.ajaxSetup({
        beforeSend: function(){
            $('#collect-data-progress').show();
        },
        complete: function(){
            $('#collect-data-progress').hide();
        },
        success: function(){}
    });
    var id = '{{personal_stat.id}}',
        key = '{{ personal_stat.human_resource.functional_group.abbreviation }}';
    $.getJSON("{% url 'personals:collect_data' %}?stats_id={0}&key={1}".format(id, key)).done(function(data){
        //console.log(data);
        $.each(data, function(k, v){
            $("input[name='{0}']".format(k)).val(v).addClass('gentle');
        })
    });
});