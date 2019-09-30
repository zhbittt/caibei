from odoo import fields, models


class Attachment(models.Model):

    _inherit = 'ir.attachment'

    partner_id = fields.Many2one('res.partner', string='关联对象')
