from openpyxl.styles import colors
from openpyxl.styles import Fill, Color, PatternFill, Font

HEAD_QI = [
    'Week Ending',
    'Quality Innovation',
    'Staff',
    'Opening Positions',
    'Contractors',
    'Throughput',
    'Backlog Story Points',
    'Story Points Prep',
    'Story Points Execution',
    'Unit Tests Dev',
    'Unit Testing Coverage',
    'Documentation',
    'Defects due to Dev',
    'Quality',
    'SLAS met',
    'Delays Introduced',
    'UAT defects not prevented',
    'SDIs not prevented',
    'Resource swap',
    'Escalations',
    'Rework introduced',
    'Efficiency',
    'Average team size',
    'Overtime Weekday',
    'Overtime Weekend',
    'Average Throughput',
    'Rework Hours',
    'Resource swap hours',
    'Costs',
    'Coding Operational Costs',
    'Licensing Costs',
    'Total Operational Costs',
    'Usage',
    'Pheme manual tests',
    'Pheme automatic tests',
    'Visilog TXL parsed',
    'Visilog TXL schema violation found',
    'Other savings'
]

HEAD_RE = [
    'Week Ending',
    'Staff',
    'Opening Positions',
    'Contractors',
    'Throughput',
    'Backlog',
    'Active Projects',
    'Team Initiatives',
    'Elicitation and Analysis',
    'Quality',
    'Revisions',
    'Rework introduced',
    'Avg Throughput',
    'SLAs met',
    'Delays introduced',
    'Escalations',
    'Efficiency',
    'Gross Available Hours',
    'Efficiency',
    'Overtime Weekend',
    'Overtime Weekday',
    'Rework From External',
    'Costs',
    'Cost of Rework',
    'Resource Swap Hours',
    'Travel Costs',
    'Overall Operating Costs'
]

HEAD_TL = [
    'Week Ending',
    'Test Lab',
    'Staff',
    'Opening Positions',
    'Contractors',
    'Throughput',
    'Tickets Received',
    'Tickets Closed',
    'Virtual Machines',
    'Physical Machines',
    'Costs',
    'Power Consumption UPS A',
    'Power Consumption UPS B',
    'Licensing Costs'
]

HEAD_PQ_QA_TE = []

blackFill = PatternFill(
    fill_type='solid',
    start_color='FF000000',
    end_color='FFFFFFFF')
cornFlowerBlueFill = PatternFill(
    start_color='6495ED',
    end_color='6495ED',
    fill_type='solid')
oliveDrabFill = PatternFill(
    start_color='6B8E23',
    end_color='6B8E23',
    fill_type='solid')
rebeccaPurpleFill = PatternFill(
    start_color='663399',
    end_color='663399',
    fill_type='solid')
saddleBrownFill = PatternFill(
    start_color='8B4513',
    end_color='8B4513',
    fill_type='solid')
darkGreenFill = PatternFill(
    start_color='006400',
    end_color='006400',
    fill_type='solid')


def write_to_excel(metric, ws):
    if metric.functional_group.key == 'QI':
        for col in range(1, len(HEAD_QI) + 1):
            cell = ws.cell(row=1, column=col)
            cell.value = HEAD_QI[col-1]

        row = 4
        # column 2
        ws.cell(row=1, column=2).font = Font(color=colors.WHITE)
        for r_index in range(1, row + 1):
            ws.cell(row=r_index, column=2).fill = blackFill

        ws.cell(row=row, column=3).value = metric.staffs
        ws.cell(row=row, column=4).value = metric.openings
        ws.cell(row=row, column=5).value = metric.contractors

        # column 6
        ws.cell(row=1, column=6).font = Font(color=colors.WHITE)
        for r_index in range(1, row + 1):
            ws.cell(row=r_index, column=6).fill = cornFlowerBlueFill

        ws.cell(row=row, column=7).value = metric.story_points_backlog
        ws.cell(row=row, column=8).value = metric.story_points_prep
        ws.cell(row=row, column=9).value = metric.story_points_execution
        ws.cell(row=row, column=10).value = metric.unit_tests_dev
        ws.cell(row=row, column=11).value = metric.unit_tests_coverage
        ws.cell(row=row, column=12).value = metric.documentation_coverage
        ws.cell(row=row, column=13).value = metric.defects_in_dev

        # column 14
        ws.cell(row=1, column=14).font = Font(color=colors.WHITE)
        for r_index in range(1, row + 1):
            ws.cell(row=r_index, column=14).fill = rebeccaPurpleFill

        ws.cell(row=row, column=15).value = metric.slas_met
        ws.cell(row=row, column=16).value = metric.delays_introduced_time
        ws.cell(row=row, column=17).value = metric.uat_defects_not_prevented
        ws.cell(row=row, column=18).value = metric.sdis_not_prevented
        ws.cell(row=row, column=19).value = metric.resource_swap
        ws.cell(row=row, column=20).value = metric.escalations
        ws.cell(row=row, column=21).value = metric.rework_introduced_time

        # column 22
        ws.cell(row=1, column=22).font = Font(color=colors.WHITE)
        for r_index in range(1, row + 1):
            ws.cell(row=r_index, column=22).fill = saddleBrownFill

        ws.cell(row=row, column=23).value = metric.avg_team_size
        ws.cell(row=row, column=24).value = metric.overtime_weekday
        ws.cell(row=row, column=25).value = metric.overtime_weekend
        ws.cell(row=row, column=26).value = metric.avg_throughput
        ws.cell(row=row, column=27).value = metric.rework_time
        ws.cell(row=row, column=28).value = metric.resource_swap_time

        # column 29
        ws.cell(row=1, column=29).font = Font(color=colors.WHITE)
        for r_index in range(1, row + 1):
            ws.cell(row=r_index, column=29).fill = oliveDrabFill

        ws.cell(row=row, column=30).value = metric.operational_cost
        ws.cell(row=row, column=31).value = metric.license_cost
        ws.cell(row=row, column=32).value = metric.total_operational_cost

        # column 33
        ws.cell(row=1, column=33).font = Font(color=colors.WHITE)
        for r_index in range(1, row + 1):
            ws.cell(row=r_index, column=33).fill = darkGreenFill

        ws.cell(row=row, column=34).value = metric.pheme_manual_tests
        ws.cell(row=row, column=35).value = metric.pheme_auto_tests
        ws.cell(row=row, column=36).value = metric.visilog_txl_parsed
        ws.cell(row=row, column=37).value = metric.visilog_txl_schema_violation
        ws.cell(row=row, column=38).value = metric.other_savings

    elif metric.functional_group.key == 'TL':
        for col in range(1, len(HEAD_TL) + 1):
            cell = ws.cell(row=1, column=col)
            cell.value = HEAD_TL[col-1]
        row = 4
        # ws.cell(row=row, column=1).value = ''

        # column 2
        ws.cell(row=1, column=2).font = Font(color=colors.WHITE)
        for r_index in range(1, row + 1):
            ws.cell(row=r_index, column=2).fill = blackFill

        ws.cell(row=row, column=3).value = metric.staffs
        ws.cell(row=row, column=4).value = metric.openings
        ws.cell(row=row, column=5).value = metric.contractors

        # column 6
        ws.cell(row=1, column=6).font = Font(color=colors.WHITE)
        for r_index in range(1, row + 1):
            ws.cell(row=r_index, column=6).fill = cornFlowerBlueFill

        ws.cell(row=row, column=7).value = metric.tickets_received
        ws.cell(row=row, column=8).value = metric.tickets_closed
        ws.cell(row=row, column=9).value = metric.virtual_machines
        ws.cell(row=row, column=10).value = metric.physical_machines

        # column 11
        ws.cell(row=1, column=11).font = Font(color=colors.WHITE)
        for r_index in range(1, row + 1):
            ws.cell(row=r_index, column=11).fill = oliveDrabFill

        ws.cell(row=row, column=12).value = metric.power_consumption_ups_a
        ws.cell(row=row, column=13).value = metric.power_consumption_ups_b
        ws.cell(row=row, column=14).value = metric.license_cost





