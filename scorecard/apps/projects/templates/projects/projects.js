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
        ticket_lead = $(e.relatedTarget).data('ticket-lead');

    $(e.currentTarget).find('input[name="editTicketId"]').val(ticket_id);
    $(e.currentTarget).find('input[name="editTicketKey"]').val(ticket_key);
    $('#editTicketFunctionalGroup').val(ticket_fg);
    $('#editTicketLead').val(ticket_lead);
});