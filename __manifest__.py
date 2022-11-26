# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Student Management',
    'version' : '1.0.0',
    'summary': 'Student Management Platform',
    'sequence': 10,
    'author': 'Ismail Abdelouahab',
    'company': 'IA-Enterprise',
    'description': """
Student Platform
====================
An Odoo open source platform for managing students subscriptions
""",
    'category': 'Scholar services/Students',
    'website': 'https://www.odoo.com/app/Student_management',
    'images' : [''],
    'depends' : ['base'],
    'data': [
        'views/student.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
