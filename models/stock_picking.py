# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)
class Picking(models.Model):
    _inherit = 'stock.picking'
    
    @api.model_create_multi
    def create(self, vals_list):
        pickings = super().create(vals_list)
        if 'picking_type_id' in vals_list:
            for picking in self:
                sequence = picking.picking_type_id.sequence_id
                #_logger.info(f"Revirtiendo secuencia para {picking.name}")
                sequence.sudo().write({'number_next': sequence.number_next_actual - 1})
        return pickings
    
    def write(self, vals):
        res = super(Picking, self).write(vals)
        # Restaurar la secuencia original solo si `picking_type_id` fue cambiado
        if 'picking_type_id' in vals:
            for picking in self:
                sequence = picking.picking_type_id.sequence_id
                #_logger.info(f"Revirtiendo secuencia para {picking.name}")
                sequence.sudo().write({'number_next': sequence.number_next_actual - 1})
        return res
    
    def button_validate(self):
        self.name = self.picking_type_id.sequence_id.next_by_id()

        res = super(Picking, self).button_validate()
        
        return res