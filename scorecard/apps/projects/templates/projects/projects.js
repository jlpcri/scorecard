/**
 * Created by sliu on 1/11/16.
 */
$('#editProject').on('show.bs.modal', function(e){
    var project_id = $(e.relatedTarget).data('project-id'),
        project_name = $(e.relatedTarget).data('project-name');
    $(e.currentTarget).find('input[name="editProjectId"]').val(project_id);
    $(e.currentTarget).find('input[name="editProjectName"]').val(project_name);
});

$('#editTicket').on('show.bs.modal', function(e){
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
});

$('#editPhase').on('show.bs.modal', function(e) {
    var phase_id = $(e.relatedTarget).data('phase-id'),
        phase_project = $(e.relatedTarget).data('phase-project'),
        phase_fg = $(e.relatedTarget).data('phase-fg'),
        phase_lead = $(e.relatedTarget).data('phase-lead'),
        phase_name = $(e.relatedTarget).data('phase-name'),
        phase_key = $(e.relatedTarget).data('phase-key');

    $('#editPhaseProject').val(phase_project);
    $('#editPhaseFunctionalGroup').val(phase_fg);
    $('#editPhaseLead').val(phase_lead);
    $(e.currentTarget).find('input[name="editPhaseId"]').val(phase_id);
    $(e.currentTarget).find('input[name="editPhaseName"]').val(phase_name);
    $(e.currentTarget).find('input[name="editPhaseKey"]').val(phase_key);

});