from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    record_ids = fields.One2many('res.record', 'partner_id')
