# Created on 2019-07-15
# author: Javier https://www.sugestionweb.com
# email: javier@sugestionweb.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Decorate invoices supplier Tree",
    "version": "12.0.0.1.0",
    "author": "Sugestionweb.com",
    "category": "Productivity",
    "website": "https://www.sugestionweb.com",
    "license": "AGPL-3",
    "sequence": 2,
    "summary": """
    Customizes the list of vendor bills with different colors depending on
whether the bill is open, paid or canceled.
    """,
    "images": ["static/description/icon.png"],
    "depends": ["base", "purchase"],
    "data": ["views/inherited_view.xml"],
    "qweb": ["static/src/xml/*.xml"],
    "demo": [],
    "test": [],
    "css": [],
    "js": [],
    "installable": True,
    "application": False,
    "auto_install": False,
}
