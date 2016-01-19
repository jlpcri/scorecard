/**
 * Created by sliu on 1/14/16.
 */
$('#date-range').on('apply.daterangepicker', function(event, picker){
    var start = picker.startDate.format('YYYY-MM-DD'),
        end = picker.endDate.format('YYYY-MM-DD');
    window.location.href = "{% url 'datas:datas'%}?start=" + start + "&end=" + end;
});