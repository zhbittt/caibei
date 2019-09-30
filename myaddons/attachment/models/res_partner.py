from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    attachment_ids = fields.One2many('ir.attachment', 'partner_id')

