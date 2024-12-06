from odoo import fields,models
class Quiz(models.Model):
    _inherit="ustadam.quiz"
    image=fields.Image("Quiz Image",required=True)