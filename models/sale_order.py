from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    route_id = fields.Many2one('stock.route', string='Punto de venta',domain="[('company_id', '=', company_id),('sale_selectable', '=', True)]",)
    
    @api.onchange('route_id')
    def _onchange_route_id(self):
        """Cuando cambia la ruta en la orden, se actualiza en todas las líneas."""
        for order in self:
            if order.route_id:
                order.order_line.write({'route_id': order.route_id.id})