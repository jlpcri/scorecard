/**
 * Created by sliu on 2/15/16.
 */
$('#automation-new-modal form').submit(function(event){
    var file = $('#id_script_file')[0].files[0];
    if (file){
        if (!file.name.match('.py')){
            $('#newAutomationErrMessage').html('UploadFile is not .py');
            return false;
        }
    }
});