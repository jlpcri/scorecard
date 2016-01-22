/**
 * Created by sliu on 1/12/16.
 */
$('#date-range').on('apply.daterangepicker', function(event, picker){
    var start = picker.startDate.format('YYYY-MM-DD'),
        end = picker.endDate.format('YYYY-MM-DD');
    window.location.href = "{% url 'teams:teams'%}?start=" + start + "&end=" + end;
});