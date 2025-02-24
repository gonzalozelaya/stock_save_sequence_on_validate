from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def create(self, vals):
        _logger.info(f"Creating order line: {str(vals)}")
        """Hereda la ruta de la orden de venta al crear una nueva línea."""
        if 'order_id' in vals:
            if vals['route_id'] == False:
                order = self.env['sale.order'].browse(vals['order_id'])
                _logger.info(f"Order data:{str(order)}")
                if order.route_id:
                    vals['route_id'] = order.route_id.id  # Asigna la ruta de la orden a la línea
        return super(SaleOrderLine, self).create(vals)
