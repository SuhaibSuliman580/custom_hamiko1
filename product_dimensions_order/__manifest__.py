{
    'name': 'Product Dimensions on Orders',
    'version': '17.0.1.0.4',
    'summary': 'Add thickness and width fields to products, sale orders, and purchase orders',
    'category': 'Sales/Purchase',
    'author': 'Custom',
    'license': 'LGPL-3',
    'depends': [
        'product',
        'sale_management',
        'purchase',
    ],
    'data': [
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
