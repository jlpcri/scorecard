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
            'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            'Last 7 Days': [moment().subtract(6, 'days'), moment()],
            'Last 30 Days': [moment().subtract(29, 'days'), moment()],
            'This Month': [moment().startOf('month'), moment().endOf('month')],
            'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        }
    }, setDate(start, end));
}

$('#date-range').on('apply.daterangepicker', function(event, picker){
    var start = picker.startDate.format('YYYY-MM-DD'),
        end = picker.endDate.format('YYYY-MM-DD');
    window.location.href = "{% url 'teams:teams'%}?start=" + start + "&end=" + end;
});