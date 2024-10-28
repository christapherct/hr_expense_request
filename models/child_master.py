from odoo import models, fields, api, _


class ChildEducationMaster(models.Model):
    _name = 'child.education.master'
    _description = 'Child Education Master'

    name = fields.Char(string="Child Name")
    visa_num = fields.Char(string="Visa ID")