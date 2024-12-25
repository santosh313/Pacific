// Copyright (c) 2024, santoshsutar3130@gmail.com and contributors
// For license information, please see license.txt

frappe.query_reports["Collection of Fee"] = {
	"filters": [

		{
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            // "default": frappe.datetime.add_days(frappe.datetime.nowdate(), -30)
        },
		{
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            // "default": frappe.datetime.nowdate()
        },
		{
			"fieldname": "student",
			"fieldtype": "Link",
			"options": "Student",
			"label": "Student",
			"width": 150
		},
		{
			"fieldname": "student_name",
			"fieldtype": "Link",
			"label": "Student Name",
			"options":"Student",
			"width": 200
		},
		{
			"fieldname": "first_name",
			"fieldtype": "Data",
			"label": "First Name",
			"width": 150
		},
		{
			"fieldname": "last_name",
			"fieldtype": "Data",
			"label": "Last Name",
			"width": 150
		},
		{
			"fieldname": "custom_student_batch_program_name",
			"fieldtype": "Link",
			"label": "Student Batch Program Group",
			"optons": "Student Batch Group",
			"width": 150
		},
		{
			"fieldname": "custom_program_type",
			"fieldtype": "Link",
			"label": "Program Type",
			"options": "Program Group",
			"width": 150
		},
		{
			"fieldname": "custom_programs",
			"fieldtype": "Link",
			"label": "Programs",
			"options": "Program",
			"width": 150
		},
		{
			"fieldname": "source_of_admission",
			"fieldtype": "Select",
			"label": "Source of Admission",
			"options": ["","Self", "Channel Partner", "Referral"],
			"default": "",
			"width": 150
		},
		{
			"fieldname": "fees_opted_option",
			"fieldtype": "Select",
			"label": "Fees Opted Option",
			"options" :["","Semester Wise","Year Wise","Program Wise","Program with loan"],
			"width": 150
		},
		{
			"fieldname": "payment_type",
			"fieldtype": "Select",
			"label": "Payment Type",
			"options": ["","Direct","Loan"],
			"width": 150
		},
		{
			"fieldname": "custom_admission_status",
			"fieldtype": "Select",
			"label": "Admission Status",
			"options" : [ "","Active","Inactive","Withdrawal"],
			"width": 150,
			"default": "",
		},
		

	],
	};

