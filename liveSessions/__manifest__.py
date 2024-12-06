# -*- coding: utf-8 -*-
{
    'name': "uteach_live_sessions",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Sheri & Moon",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/group.xml',
        'views/live-session-view.xml',
        'views/live_web.xml',
        'views/modal_form_coach.xml',
        'views/live_session_info_template.xml',
        'views/live_session_coach_menu.xml',
        'views/registration_success_template.xml',
        'views/menu-items.xml',
    ],
    'assets': {
        'web.assets_frontend': [
        'live_sessions/static/src/js/modal.js'  
        ]   
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

