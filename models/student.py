from odoo import models, fields, api


class Student(models.Model):
    _name = "student"
    _description = "student management"
    lastName = fields.Char(string='Last Name', required=True)
    firstName = fields.Char(string='First Name', required=True)
    birthDate = fields.Date(string='Birth Date', required=True)
    email = fields.Char(string='Email', required=True)
    cin = fields.Char(string='CIN', required=True)
    cne = fields.Char(string='CNE', required=True)
    phoneNumber = fields.Integer(string="Number Phone", required=True)
    paid = fields.Selection([('paid', 'Paid'), ('notPaid', 'Not Paid')], string='Paid', required=True)
