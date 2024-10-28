from odoo import models, fields, api, _


class HRTravelRequest(models.Model):
    _name = 'hr.travel.request'
    _inherit = 'hr.expense.request'
    _description = 'Travel Request'

    name = fields.Char(string="Travel Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True,)
    department_id = fields.Many2one(related='employee_id.department_id', string="Department", readonly=True)
    from_date = fields.Date(string="From Date", required=True)
    to_date = fields.Date(string="To Date", required=True)
    accommodation_required = fields.Boolean(string="Accommodation Required")
    accommodation_amount = fields.Float(string="Accommodation Amount")
    travel_type = fields.Selection([
        ('domestic', 'Domestic'),
        ('international', 'International'),
    ], string="Type of Travel", required=True)
    kit_allowance_needed = fields.Boolean(string="Kit Allowance Needed", default=False)
    request_type = fields.Selection([
        ('reimbursement', 'Reimbursement'),
        ('prepaid', 'Prepaid'),
    ], string="Request Type", required=True)
    airfare_attachment = fields.Binary(string="Airfare Attachment")
    airfare_amount = fields.Float(string="Airfare Amount")
    accommodation_attachment = fields.Binary(string="Accommodation Attachment")
    other_attachment = fields.Binary(string="Other Attachment")
    other_amount = fields.Float(string="Other Amount")
    amount = fields.Float(string="Amount")
    meeting_attachment = fields.Binary(string="Meeting Attachment")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string="Status", default='draft')
    expense_request_id = fields.Many2one('hr.expense.request', string="Expense Request")
    expense_type = fields.Selection(related="expense_request_id.expense_type")
    # expense_type = fields.Many2one('hr.expense.type', string="Expense Type", required=True,
    #                                default=lambda self: self.env['hr.expense.type'].search([('name', '=', 'Travel')],
    #                                                                                        limit=1).id)

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('hr.travel.request') or _('New')
    #     if 'expense_type' not in vals:
    #         # You can set a default value for expense_type based on your requirement
    #         vals['expense_type'] = self.env['hr.expense.type'].search([('name', '=', 'Travel')], limit=1).id
    #     return super(HRTravelRequest, self).create(vals)

    def action_submit(self):
        self.state = 'submitted'


