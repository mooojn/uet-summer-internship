from odoo import models, fields, api

class CourseInherited(models.Model):
    _inherit = "ustadam.course"
    _description = "will hold user info"


    def action_register_course(self):
        user = self.env.user
        self.user_ids |= user  
        return True
    def action_register_course_inherited(self):
        current_user = self.env.user
        courses = self.env['ustadam.course'].search([('user_ids', '=', current_user.id)])

        action = {
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban,form',
            'res_model': 'ustadam.course',
            'domain': [('id', 'in', courses.ids)],
            'context': self.env.context,
        }
        return action
    def action_view_content(self):
        action = self.env.ref('sincsol__lms__course.view_content').read()[0]
        action['context'] = {
            'default_course_id': self.id,  # Example context if needed
            # Add more context as needed
        }
        return action