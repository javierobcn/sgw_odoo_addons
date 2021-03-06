# ------------------------------------------------------------------------------
# # (c) 2020 Sugestionweb.com -  javier@sugestionweb.com
# # License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# ------------------------------------------------------------------------------

from odoo import api, models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    @api.multi
    def message_subscribe(
        self, partner_ids=None, channel_ids=None, subtype_ids=None, force=True
    ):
        ir_config = self.env["ir.config_parameter"]
        app_stop_subscribe = (
            False if ir_config.get_param("sgw_stop_subscribe") == "True" else False
        )
        if app_stop_subscribe:
            return
        else:
            return super(MailThread, self).message_subscribe(
                partner_ids, channel_ids, subtype_ids, force
            )

    @api.multi
    def message_auto_subscribe(self, updated_fields, values=None):
        ir_config = self.env["ir.config_parameter"]
        app_stop_subscribe = (
            False if ir_config.get_param("sgw_stop_subscribe") == "True" else False
        )
        if app_stop_subscribe:
            return
        else:
            return super(MailThread, self).message_auto_subscribe(
                updated_fields, values
            )

    @api.multi
    def _message_auto_subscribe_notify(self, partner_ids):
        ir_config = self.env["ir.config_parameter"]
        app_stop_subscribe = (
            False if ir_config.get_param("sgw_stop_subscribe") == "True" else False
        )
        if app_stop_subscribe:
            return
        else:
            return super(MailThread, self)._message_auto_subscribe_notify(partner_ids)
