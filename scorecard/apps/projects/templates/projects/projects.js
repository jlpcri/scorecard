/**
 * Created by sliu on 1/11/16.
 */

// Use jquery date picker for ProjectPhase/Tickets Estimate/Actual Start/End
$('.input-date').datepicker();

$('.newProject form').on('submit', function(event){
    var name = $('.newProject form #id_name').val();
    if (name == ''){
        showErrMsg('#newProjectErrMessage', 'Name is Empty');
        return false;
    }
});

$('.editProject').on('show.bs.modal', function(e){
    var project_id = $(e.relatedTarget).data('project-id'),
        project_name = $(e.relatedTarget).data('project-name'),
        project_revenue = $(e.relatedTarget).data('project-revenue');

    $(e.currentTarget).find('input[name="editProjectId"]').val(project_id);
    $(e.currentTarget).find('input[name="editProjectName"]').val(project_name);
    $(e.currentTarget).find('select[name="editProjectRevenue"]').val(project_revenue);

    $('.editProject .modal-title').html('Project Edit - ' + project_name);
});

$('.editProject form').on('submit', function(event){
    var name = $('#editProjectName').val();
    if (name == ''){
        showErrMsg('#editProjectErrMessage', 'Name is Empty');
        return false;
    }
});

$('.newPhase form').on('submit', function(event){
    var project = $('.newPhase form #id_project').val(),
        fg = $('.newPhase form #id_functional_group').val(),
        lead = $('.newPhase form #id_lead').val(),
        name = $('.newPhase form #id_name').val();
    if (project == '') {
        showErrMsg('#newPhaseErrMessage', 'Project is not selected');
        return false;
    }
    if (fg == '') {
        showErrMsg('#newPhaseErrMessage', 'Functional Group is not selected');
        return false;
    }
    if (lead == '') {
        showErrMsg('#newPhaseErrMessage', 'Lead is not selected');
        return false;
    }
    if (name == '') {
        showErrMsg('#newPhaseErrMessage', 'Name is empty');
        return false;
    }
});

$('.newTicket form').on('submit', function(event){
    var fg = $('.newTicket form #id_functional_group').val(),
        lead = $('.newTicket form #id_lead').val(),
        key = $('.newTicket form #id_key').val();
    if (fg == '') {
        showErrMsg('#newTicketErrMessage', 'Functional Group is not selected');
        return false;
    }
    if (lead == '') {
        showErrMsg('#newTicketErrMessage', 'Lead is not selected');
        return false;
    }
    if (key == '') {
        showErrMsg('#newTicketErrMessage', 'Key is empty');
        return false;
    }
});

$('.editTicket').on('show.bs.modal', function(e){
    var ticket_id = $(e.relatedTarget).data('ticket-id'),
        ticket_key = $(e.relatedTarget).data('ticket-key'),
        ticket_fg = $(e.relatedTarget).data('ticket-fg'),
        ticket_lead = $(e.relatedTarget).data('ticket-lead'),
        ticket_estimate_start = $(e.relatedTarget).data('ticket-estimate-start'),
        ticket_estimate_end = $(e.relatedTarget).data('ticket-estimate-end'),
        ticket_actual_start = $(e.relatedTarget).data('ticket-actual-start'),
        ticket_actual_end = $(e.relatedTarget).data('ticket-actual-end');

    $(e.currentTarget).find('input[name="editTicketId"]').val(ticket_id);
    $(e.currentTarget).find('input[name="editTicketKey"]').val(ticket_key);
    $('#editTicketFunctionalGroup').val(ticket_fg);
    $('#editTicketLead').val(ticket_lead);
    $('#editTicketEstimateStart').val(ticket_estimate_start);
    $('#editTicketEstimateEnd').val(ticket_estimate_end);
    $('#editTicketActualStart').val(ticket_actual_start);
    $('#editTicketActualEnd').val(ticket_actual_end);

    $('.editTicket .modal-title').html('Ticket Edit - ' + ticket_key);
});

$('.editTicket form').on('submit', function(event){
    var key = $('#editTicketKey').val();
    var estimate_start = $('#editTicketEstimateStart').val(),
        estimate_end = $('#editTicketEstimateEnd').val(),
        actual_start = $('#editTicketActualStart').val(),
        actual_end = $('#editTicketActualEnd').val();

    if (key == ''){
        showErrMsg('#editTicketErrMessage', 'Key is Empty');
        return false;
    } else if (estimate_start && !(moment(estimate_start, 'MM/DD/YYYY', true).isValid())){
        showErrMsg('#editTicketErrMessage', 'Estimate Start format should be MM/DD/YYYY ');
        return false;
    } else if (estimate_end && !(moment(estimate_end, 'MM/DD/YYYY', true).isValid())){
        showErrMsg('#editTicketErrMessage', 'Estimate End format should be MM/DD/YYYY ');
        return false;
    } else if (actual_start && !(moment(actual_start, 'MM/DD/YYYY', true).isValid())){
        showErrMsg('#editTicketErrMessage', 'Actual Start format should be MM/DD/YYYY ');
        return false;
    } else if (actual_end && !(moment(actual_end, 'MM/DD/YYYY', true).isValid())){
        showErrMsg('#editTicketErrMessage', 'Actual End format should be MM/DD/YYYY ');
        return false;
    }
});

$('.editPhase').on('show.bs.modal', function(e) {
    var phase_id = $(e.relatedTarget).data('phase-id'),
        phase_project = $(e.relatedTarget).data('phase-project'),
        phase_fg = $(e.relatedTarget).data('phase-fg'),
        phase_lead = $(e.relatedTarget).data('phase-lead'),
        phase_name = $(e.relatedTarget).data('phase-name'),
        phase_key = $(e.relatedTarget).data('phase-key'),
        phase_estimate_start = $(e.relatedTarget).data('phase-estimate-start'),
        phase_estimate_end = $(e.relatedTarget).data('phase-estimate-end'),
        phase_actual_start = $(e.relatedTarget).data('phase-actual-start'),
        phase_actual_end = $(e.relatedTarget).data('phase-actual-end');

    $('#editPhaseProject').val(phase_project);
    $('#editPhaseFunctionalGroup').val(phase_fg);
    $('#editPhaseLead').val(phase_lead);
    $(e.currentTarget).find('input[name="editPhaseId"]').val(phase_id);
    $(e.currentTarget).find('input[name="editPhaseName"]').val(phase_name);
    $(e.currentTarget).find('input[name="editPhaseKey"]').val(phase_key);
    $('#editPhaseEstimateStart').val(phase_estimate_start);
    $('#editPhaseEstimateEnd').val(phase_estimate_end);
    $('#editPhaseActualStart').val(phase_actual_start);
    $('#editPhaseActualEnd').val(phase_actual_end);

    $('.editPhase .modal-title').html('Project Phase Edit - ' + phase_name);
});

$('.editPhase form').on('submit', function(event){
    var name = $('#editPhaseName').val(),
        estimate_start_string = $('#editPhaseEstimateStart').val(),
        estimate_end_string = $('#editPhaseEstimateEnd').val(),
        actual_start_string = $('#editPhaseActualStart').val(),
        actual_end_string = $('#editPhaseActualEnd').val(),
        estimate_start = new Date(estimate_start_string),
        estimate_end = new Date(estimate_end_string),
        actual_start = new Date(actual_start_string),
        actual_end = new Date(actual_end_string);

    if (name == ''){
        showErrMsg('#editPhaseErrMessage', 'Name is Empty');
        return false;
    } else if (estimate_start_string && !(moment(estimate_start_string, 'MM/DD/YYYY', true).isValid())){
        showErrMsg('#editPhaseErrMessage', 'Estimate Start format should be MM/DD/YYYY ');
        return false;
    } else if (estimate_end_string && !(moment(estimate_end_string, 'MM/DD/YYYY', true).isValid())){
        showErrMsg('#editPhaseErrMessage', 'Estimate End format should be MM/DD/YYYY ');
        return false;
    } else if (actual_start_string && !(moment(actual_start_string, 'MM/DD/YYYY', true).isValid())){
        showErrMsg('#editPhaseErrMessage', 'Actual Start format should be MM/DD/YYYY ');
        return false;
    } else if (actual_end_string && !(moment(actual_end_string, 'MM/DD/YYYY', true).isValid())){
        showErrMsg('#editPhaseErrMessage', 'Actual End format should be MM/DD/YYYY ');
        return false;
    } else if (estimate_start > estimate_end) {
        showErrMsg('#editPhaseErrMessage', 'Estimate End cannot be earlier than Estimate Start');
        return false;
    } else if (actual_start > actual_end) {
        showErrMsg('#editPhaseErrMessage', 'Actual End cannot be earlier than Actual Start');
        return false;
    }
});

function showErrMsg(location, msg) {
    $(location).css({
        'font-size': 15,
        'color': 'blue'
    });
    $(location).html('Error: ' + msg);
}