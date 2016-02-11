# Choices of Column Fields
COMPLIMENTS = 'compliments'
COMPLAINTS = 'complaints'
ESCALATIONS = 'escalations'

# Innovation
BACKLOG_STORY = 'story_points_backlog'
STORY_POINTS_PREP = 'story_points_prep'
UNIT_TESTS_COVER = 'unit_tests_coverage'
DOCUMENT_COVER = 'documentation_coverage'
DEFECTS_IN_DEV = 'defects_in_dev'
REVISIONS = 'revisions'
ACTIVE_PROJECTS = 'active_projects'

SLAS_MET = 'slas_met'
DELAYS_INTRODUCED_TIME = 'delays_introduced_time'
SDIS_NOT_PREVENTED = 'sdis_not_prevented'
UAT_DEFECTS_NOT_PREVENTED = 'uat_defects_not_prevented'
RESOURCE_SWAP = 'resource_swap'
REWORK_INTRODUCED_TIME = 'rework_introduced_time'

AVERAGE_TEAM_SIZE = 'avg_team_size'
RESOURCE_SWAP_TIME = 'resource_swap_time'

LICENSE_COST = 'license_cost'
OTHER_SAVINGS = 'other_savings'

PHEME_MANUAL_TESTS = 'pheme_manual_tests'
PHEME_AUTO_TESTS = 'pheme_auto_tests'
VISILOG_TXL_PARSED = 'visilog_txl_parsed'
VISILOG_TXL_VIOLATION = 'visilog_txl_schema_violation'

# Test Lab
TICKETS_RECEIVED = 'tickets_received'
VIRTUAL_MACHINES = 'virtual_machines'
PHYSICAL_MACHINES = 'physical_machines'
POWER_UPS_A = 'power_consumption_ups_a'
POWER_UPS_B = 'power_consumption_upb_b'

# Requirements Engineering
BACKLOG = 'backlog'
TEAM_INITIATIVE = 'team_initiative'
REWORK_INTRO_TIME = 'rework_introduced_time'
SLAS_MISSED = 'slas_missed'
DELAYS_INTRO_TIME = 'delays_introduced_time'

# Quality Assurance and Test Engineering
TICKET_BACKLOG = 'ticket_backlog'
TICKET_PREP = 'ticket_prep'
TICKET_EXECUTION = 'ticket_execution'
TICKET_CLOSED = 'ticket_closed'
PROJECT_BACKLOG = 'project_backlog'
PROJECT_PREP = 'project_prep'
PROJECT_EXECUTION = 'project_execution'
PROJECT_CLOSED = 'project_closed'

AVERAGE_TIME_FRAME = 'avg_time_frame'

CHOICES_QI = (
    (COMPLIMENTS, 'Compliments'),
    (COMPLAINTS, 'Complaints'),
    (ESCALATIONS, 'Escalations'),
    (BACKLOG_STORY, 'Story Points Backlog'),
    (STORY_POINTS_PREP, 'Story Points Prep'),
    (UNIT_TESTS_COVER, 'Unit Tests Coverage'),
    (DOCUMENT_COVER, 'Documentation Coverage'),
    (DEFECTS_IN_DEV, 'Defects In Dev'),
    (REVISIONS, 'Revisions'),
    (ACTIVE_PROJECTS, 'Active Projects'),
    (SLAS_MET, 'SLAs Met'),
    (DELAYS_INTRODUCED_TIME, 'Delays Introduced Time'),
    (SDIS_NOT_PREVENTED, 'SDIs Not Prevented'),
    (UAT_DEFECTS_NOT_PREVENTED, 'Uat Defects Not Prevented'),
    (RESOURCE_SWAP, 'Resource Swap'),
    (REWORK_INTRODUCED_TIME, 'Rework Introduced Time'),
    (AVERAGE_TEAM_SIZE, 'Average Team Size'),
    (RESOURCE_SWAP_TIME, 'Resource Swap Time'),
    (LICENSE_COST, 'License Cost'),
    (OTHER_SAVINGS, 'Other Savings'),
    (PHEME_MANUAL_TESTS, 'Pheme Manual Tests'),
    (PHEME_AUTO_TESTS, 'Pheme Auto Tests'),
    (VISILOG_TXL_PARSED, 'Visilog TXL Parsed'),
    (VISILOG_TXL_VIOLATION, 'Visilog TXL Schema Violation')
)

CHOICES_TL = (
    (COMPLIMENTS, 'Compliments'),
    (COMPLAINTS, 'Complaints'),
    (ESCALATIONS, 'Escalations'),
    (TICKETS_RECEIVED, 'Tickets Received'),
    (VIRTUAL_MACHINES, 'Virtual Machines'),
    (PHYSICAL_MACHINES, 'Physical Machines'),
    (POWER_UPS_A, 'Power Consumption UPS A'),
    (POWER_UPS_B, 'Power Consumption UPS B'),
    (LICENSE_COST, 'License Cost')
)

CHOICES_RE = (
    (COMPLIMENTS, 'Compliments'),
    (COMPLAINTS, 'Complaints'),
    (ESCALATIONS, 'Escalations'),
    (BACKLOG, 'Backlog'),
    (ACTIVE_PROJECTS, 'Active Projects'),
    (TEAM_INITIATIVE, 'Team Initiative'),
    (REWORK_INTRO_TIME, 'Rework Introduced Time'),
    (SLAS_MET, 'SLAs Met'),
    (SLAS_MISSED, 'SLAs Missed'),
    (DELAYS_INTRO_TIME, 'Delays Introduced Time')
)

CHOICES_QA_TE = (
    (COMPLIMENTS, 'Compliments'),
    (COMPLAINTS, 'Complaints'),
    (ESCALATIONS, 'Escalations'),
    (TEAM_INITIATIVE, 'Team Initiative'),
    (TICKET_BACKLOG, 'Ticket Backlog'),
    (TICKET_PREP, 'Ticket Prep'),
    (TICKET_EXECUTION, 'Ticket Execution'),
    (TICKET_CLOSED, 'Ticket Closed'),
    (PROJECT_BACKLOG, 'Project Backlog'),
    (PROJECT_PREP, 'Project Prep'),
    (PROJECT_EXECUTION, 'Project Execution'),
    (PROJECT_CLOSED, 'Project Closed'),
    (SLAS_MET, 'SLAs Met'),
    (DELAYS_INTRO_TIME, 'Delays Introduced Time'),
    (SDIS_NOT_PREVENTED, 'SDIs Not Prevented'),
    (RESOURCE_SWAP, 'Resource Swap'),
    (REWORK_INTRO_TIME, 'Rework Introduced Time'),
    (AVERAGE_TEAM_SIZE, 'Average Team Size'),
    (AVERAGE_TIME_FRAME, 'Average Time Frame'),
    (LICENSE_COST, 'License Cost'),
    (OTHER_SAVINGS, 'Other Savings')
)
