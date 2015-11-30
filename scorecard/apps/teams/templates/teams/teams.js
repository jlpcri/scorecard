/**
 * Created by sliu on 11/17/15.
 */
var active_tab = String("");

$('#subnav-tabs').find('a[data-toggle="tab"]').on('show.bs.tab', function(e){
    active_tab = e.target.hash;
});


$(document).ready(function(){
    $('#subnav-tabs').find('a[href="#product_quality"]').tab('show');
});

