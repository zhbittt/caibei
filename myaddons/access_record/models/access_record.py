from odoo import fields, models,api


class Record(models.Model):

    _name = 'res.record'
    _description = '客户拜访记录'

    access_type = fields.Selection([
        ('interview', '面访'),
        ('telephone_interview', '电话访谈'),
    ], default='interview', string='类型')

    access_time = fields.Datetime(string='拜访时间')
    access_feedback = fields.Text(string='客户反馈')
    access_recommend = fields.Text(string='推荐内容')

    def _get_default_parent_id(self):
        default_parent_id = self.env.context.get('default_parent_id')
        return default_parent_id if default_parent_id else None

    partner_id = fields.Many2one(
        'res.partner',
        delegate=True,
        ondelete='cascade',
        string='关联对象',
        default=_get_default_parent_id,
    )

    access_user = fields.Many2one('res.partner', domain="[('parent_id', '=', partner_id)]", string='拜访对象')
    access_user_name = fields.Char(related='access_user.name', string='拜访对象姓名')
