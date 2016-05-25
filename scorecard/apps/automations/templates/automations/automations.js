/**
 * Created by sliu on 2/15/16.
 */

$(document).ready(function(){
    var role = $('#user_role').val();
    if (role == 'normal') {
        $('a[href="#personal"]').click();
    }
});

$('.newAutomationTeam form').submit(function(event){
    var file = $('.newAutomationTeam form #id_script_file')[0].files[0];
    if (file){
        if (!file.name.match('.py')){
            showErrMsg('#newAutomationTeamErrMessage', 'UploadFile is not .py');
            return false;
        }
    }
});

$('.newAutomationPersonal form').submit(function(event){
    var file = $('.newAutomationPersonal form #id_script_file')[0].files[0];
    if (file){
        if (!file.name.match('.py')){
            showErrMsg('#newAutomationPersonalErrMessage', 'UploadFile is not .py');
            return false;
        }
    }
});

$('.batchAutomationPersonal form').submit(function(event){
    var file = $('.batchAutomationPersonal form #id_script_file')[0].files[0];
    console.log(file);
    if (typeof file == 'undefined'){
        showErrMsg('#batchAutomationPersonalErrMessage', 'No upload file selected.');
        return false;
    } else if (!file.name.match('.py')){
        showErrMsg('#batchAutomationPersonalErrMessage', 'UploadFile is not .py');
        return false;
    }
});