# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "PoS Order Margin",
    "summary": "Margin on PoS Order",
    "version": "15.0.1.0.0",
    "category": "Point Of Sale",
    "author": "GRAP, Odoo Community Association (OCA)",
    "maintainers": ["legalsylvain"],
    "website": "https://github.com/OCA/pos",
    "license": "AGPL-3",
    "depends": [
        "point_of_sale",
    ],
    "data": [
        "views/view_pos_config.xml",
        "views/view_pos_order.xml",
    ],
    "qweb": [
        "static/src/xml/pos_margin.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_margin/static/src/css/pos_margin.css",
            "pos_margin/static/src/js/models.js",
            "pos_margin/static/src/js/OrderWidget.js",
            "pos_margin/static/src/js/OrderSummaryMargin.js",
        ],
    },
    "installable": True,
}
