{
    'name': 'HR Expense Request',
    'version': '17.0',
    'category': 'Human Resources',
    'sequence': -100,
    'summary': 'Module for managing employee expense requests like travel, education, and allowances.',
    'description': """
        This module enables employees to submit expense requests for travel, educational allowances, and other benefits.
        The requests flow through an approval system and integrate with payroll for reimbursements.
        """,
    'author': 'Christapher Thomas',
    'depends': [
        'base', 'hr', 'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_expense_request_view.xml',
        'views/hr_travel_request_view.xml',
        'views/hr_education_request_view.xml',
        'views/child_education_master_view.xml'
    ],

    'installable': True,
    'application': False,
}
