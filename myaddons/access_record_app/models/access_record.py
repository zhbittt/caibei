from odoo import fields, models


class Record(models.Model):

    _name = 'access.record'
    _description = '客户拜访记录'

    access_type = fields.Selection([
        ('interview', '面访'),
        ('telephone_interview', '电话访谈'),
    ], default='interview', string='类型')

    access_time = fields.Datetime(string='拜访时间')
    access_feedback = fields.Text(string='客户反馈')
    access_recommend = fields.Text(string='推荐内容')

    partner_id = fields.Many2one(
        'res.partner',
        delegate=True,
        ondelete='cascade',
        required=True,
        string='拜访对象',
    )

