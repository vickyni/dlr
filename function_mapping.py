from collections import namedtuple

function_mapping = {
	'Select Report Level':'sel_rpt_lvl',
	'Select Country/Company':'sel_cty_comp',
	'Weekending Date Range Start date':'wk_date_start',
	'Weekending Date Range End date':'wk_date_end',
	'Select Report Format':'sel_rpt_format',
	'Select Report Criteria':'sel_rpt_crit',
	'Account / Employee':'sel_acc_emp',
	'Enter Account ID':'enter_acc',
	'Enter Department':'enter_dep',
	'Enter Serial number ':'enter_sn',
	'Enter workitem':'enter_workitem'
}


Request = namedtuple('Request','report_level country_or_company start_date end_date \
          report_format report_criteria report_output_level \
          account_id department serial_number workitem' )