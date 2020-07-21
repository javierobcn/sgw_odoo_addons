# -*- coding: utf-8 -*-

# Created on 2020-07-19
# author: Javier https://www.sugestionweb.com
# email: javier@sugestionweb.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12


{
    'name': 'Chatter AEAT',
    'version': '1.1.1.01',
    'author': 'Sugestionweb.com',
    'category': 'Productivity',
    'website': 'https://www.sugestionweb.com',
    'license': 'AGPL-3',
    'sequence': 2,
    'summary': """    
    Customize the purchase orders tree to decorate the lines with diferent colors depending of the order status and invoiced status. 
    """,
    'description': """

    """,
    'images': ['static/description/banner.gif'],
    'depends': [
        'base',
        'mail',
        'l10n_es_aeat',
        'l10n_es_aeat_mod130',
        'l10n_es_aeat_mod303',
        'l10n_es_aeat_mod347'
        # 'digest',
        # when enterprise
        # 'web_mobile'
    ],
    'data': [
        'views/inherited_view.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': True,
}
