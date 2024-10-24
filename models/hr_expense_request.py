from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HRExpenseRequest(models.Model):
    _name = 'hr.expense.request'
    _description = 'HR Expense Request'

    name = fields.Char(string="Expense Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True, default=lambda self: self.env.user.employee_id)
    department_id = fields.Many2one(related='employee_id.department_id', string="Department", readonly=True)
    expense_type = fields.Selection([
        ('travel', 'Travel'),
        ('education', 'Education'),
        ('club_membership', 'Club Membership'),
        ('marriage', 'Marriage'),
        ('firstborn', 'Firstborn Child'),
        ('parking', 'Parking Allowance'),
        ('mobile', 'Mobile Phone Allowance'),
        ('airfare', 'Annual Airfare'),
    ], string="Expense Type", required=True)
    amount = fields.Float(string="Requested Amount")
    description = fields.Text(string="Description")
    attachment = fields.Binary(string="Attachment")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string="Status", default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hr.expense.request') or _('New')
        return super(HRExpenseRequest, self).create(vals)

    def action_submit(self):
        self.state = 'submitted'

    def action_approve(self):
        self.state = 'approved'

    def action_reject(self):
        self.state = 'rejected'

    def notify_approvers(self):
        self.activity_schedule(
            'mail.mail_activity_data_todo',
            user_id=self.employee_id.parent_id.user_id.id,
            summary="Approval required for expense request."
        )