from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    markaz_thickness = fields.Float(string='السماكة', readonly=False, copy=False)
    markaz_width = fields.Float(string='العرض', readonly=False, copy=False)

    @api.onchange('product_id')
    def _onchange_product_id_markaz_dimensions(self):
        for line in self:
            product_tmpl = line.product_id.product_tmpl_id
            line.markaz_thickness = product_tmpl.markaz_thickness
            line.markaz_width = product_tmpl.markaz_width

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            product_id = vals.get('product_id')
            if product_id:
                product = self.env['product.product'].browse(product_id)
                vals.setdefault('markaz_thickness', product.product_tmpl_id.markaz_thickness)
                vals.setdefault('markaz_width', product.product_tmpl_id.markaz_width)
        return super().create(vals_list)

    def write(self, vals):
        if 'product_id' in vals:
            vals = dict(vals)
            product = self.env['product.product'].browse(vals['product_id'])
            vals.setdefault('markaz_thickness', product.product_tmpl_id.markaz_thickness if product else 0.0)
            vals.setdefault('markaz_width', product.product_tmpl_id.markaz_width if product else 0.0)
        return super().write(vals)
