from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    create_po = fields.Boolean(string='create_po')
