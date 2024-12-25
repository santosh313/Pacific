# Copyright (c) 2024, santoshsutar3130@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    return columns, data

def get_data(filters):
    query = """
        SELECT 
            s.name AS student_id,
            s.first_name AS first_name,
            s.last_name AS last_name,
            s.custom_student_batch_group_name AS batch_group_name,
            s.custom_program_group AS program_group,
            s.custom_programs AS programs,
            s.custom_source_of_admission AS source_of_admission,
            s.custom_fees_option_opted AS fees_option_opted,
            s.custom_payment_type AS payment_type,
            s.custom_Admission_status AS admission_status,
            f.grand_total AS grand_total,
            f.outstanding_amount AS outstanding_amount,
            (f.grand_total - f.outstanding_amount) AS paid_amount,
            pe.posting_date AS payment_date,
            pe.party_name AS party_name
        FROM 
            `tabStudent` s
        LEFT JOIN 
            `tabFees` f ON s.name = f.student
        LEFT JOIN 
            `tabPayment Entry` pe ON pe.party = s.name
        WHERE 
            f.docstatus = 1
    """
    
    # Adding dynamic filters
    if filters:
        if filters.get("from_date") and filters.get("to_date"):
            query += " AND pe.posting_date BETWEEN %(from_date)s AND %(to_date)s"
        elif filters.get("from_date"):
            query += " AND pe.posting_date >= %(from_date)s"
        elif filters.get("to_date"):
            query += " AND pe.posting_date <= %(to_date)s"
        
        if filters.get("custom_admission_status"):
            query += " AND s.custom_Admission_status = %(custom_admission_status)s"

        if filters.get("source_of_admission"):
            query += " AND s.custom_source_of_admission = %(source_of_admission)s"

        if filters.get("fees_opted_option"):
            query += " AND s.custom_fees_option_opted = %(fees_opted_option)s"

        if filters.get("payment_type"):
            query += " AND s.custom_payment_type = %(payment_type)s"

        if filters.get("programs"):
            query += " AND s.custom_programs = %(programs)s"

        if filters.get("program_group"):
            query += " AND s.custom_program_group = %(program_group)s"

    query += " GROUP BY s.name"  # Grouping by Student ID instead of Fees ID
    
    # Execute the query
    data = frappe.db.sql(query, filters or {}, as_dict=True)

    # Format the fetched data for display
    formatted_data = []
    for row in data:
        formatted_data.append([
            row.get("student_id"),
            row.get("first_name"),
            row.get("last_name"),
            row.get("batch_group_name"),
            row.get("program_group"),
            row.get("programs"),
            row.get("source_of_admission"),
            row.get("fees_option_opted"),
            row.get("payment_type"),
            row.get("admission_status"),
            row.get("grand_total") or 0,
            row.get("outstanding_amount") or 0,
            row.get("paid_amount") or 0,
            row.get("payment_date") or "N/A",
            row.get("party_name") or "N/A"
        ])

    return formatted_data

def get_columns():
    return [
        {"label": "Student ID", "fieldtype": "Data", "width": 120},
        {"label": "First Name", "fieldtype": "Data", "width": 150},
        {"label": "Last Name", "fieldtype": "Data", "width": 150},
        {"label": "Batch Group Name", "fieldtype": "Data", "width": 150},
        {"label": "Program Group", "fieldtype": "Data", "width": 150},
        {"label": "Programs", "fieldtype": "Data", "width": 150},
        {"label": "Source of Admission", "fieldtype": "Data", "width": 150},
        {"label": "Fees Option Opted", "fieldtype": "Data", "width": 150},
        {"label": "Payment Type", "fieldtype": "Data", "width": 150},
        {"label": "Admission Status", "fieldtype": "Data", "width": 150},
        {"label": "Grand Total", "fieldtype": "Currency", "width": 120},
        {"label": "Outstanding Amount", "fieldtype": "Currency", "width": 120},
        {"label": "Paid Amount", "fieldtype": "Currency", "width": 120},
        {"label": "Payment Date", "fieldtype": "Date", "width": 120},
        {"label": "Party Name", "fieldtype": "Data", "width": 150},
    ]
