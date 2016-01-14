/**
 * Created by sliu on 1/12/16.
 */


function setDate(start, end){
    $('#date-range span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
}

//setDate(moment().subtract(29, 'days'), moment());

function attachDateRangePicker() {
    $('#date-range').daterangepicker({
        ranges: {
            'Today': [moment(), moment()],
            'Last 30 Days': [moment().subtract(29, 'days'), moment()],
            'Last 60 Days': [moment().subtract(59, 'days'), moment()],
            'This Year': [moment().startOf('year'), moment().endOf('year')]
        }
    }, setDate(start, end));
}

$('#date-range').on('apply.daterangepicker', function(event, picker){
    var start = picker.startDate.format('YYYY-MM-DD'),
        end = picker.endDate.format('YYYY-MM-DD');
    window.location.href = "{% url 'teams:teams'%}?start=" + start + "&end=" + end;
});