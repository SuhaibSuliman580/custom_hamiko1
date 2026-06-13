from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    markaz_thickness = fields.Float(string='السماكة')
    markaz_width = fields.Float(string='العرض')
