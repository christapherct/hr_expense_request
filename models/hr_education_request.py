from odoo import models, fields, api, _


class HREducationRequest(models.Model):
    _name = 'hr.education.request'
    _description = 'Education Request'

    name = fields.Char(string="Educational Request Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True,)
    department_id = fields.Many2one(related='employee_id.department_id', string="Department", readonly=True)
    academic_year = fields.Char(string="Academic Year")
    installment_num = fields.Float(string="Installment Number")
    child_id = fields.Many2one('child.education.master', string="Child Name")
    child_visa = fields.Char(related="child_id.visa_num", string="Child Visa ID")
    invoice_attachment = fields.Binary(string="Invoice Attachment")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string="Status", default='draft')

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('hr.education.request') or _('New')

    def action_submit(self):
        self.state = 'submitted'


