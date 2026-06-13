from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    markaz_total_quantity = fields.Float(
        string='إجمالي الكميات',
        compute='_compute_markaz_total_quantity',
        digits='Product Unit of Measure',
        store=True,
    )

    @api.depends('order_line.product_qty', 'order_line.display_type')
    def _compute_markaz_total_quantity(self):
        for order in self:
            order.markaz_total_quantity = sum(
                order.order_line.filtered(lambda line: not line.display_type).mapped('product_qty')
            )
