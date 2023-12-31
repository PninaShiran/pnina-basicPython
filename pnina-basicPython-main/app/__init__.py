from flask_restx import Api
from flask import Blueprint

from .main.controller.student_controller import api as students_ns
from .main.controller.student_grade_controller import api as students_grades_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='STUDENTS APP',
          version='1.0',
          description='flask restplus web service for students and grades'
          )

api.add_namespace(students_ns, path='/student')
api.add_namespace(students_grades_ns, path='/student')