from flask import jsonify, Blueprint
from flask_restful import (Resource, Api, reqparse,
                           inputs, fields, marshal,
                           marshal_with, url_for, abort)

import models

form_fields = {
    'id': fields.Integer,
    'libraryName': fields.String,
    'libraryLocation': fields.String,
    'managerName': fields.String,
    'managerEmail': fields.String,
    'managerPhonenumber': fields.String,
    'capacityOfAudiences': fields.Integer,
    'facilities': fields.String,
    'requirementsForSpeaker': fields.String,
    'personalInfoAgreement': fields.Boolean,
    'noVolunteerAgreement': fields.Boolean,
    'otherFacilities': fields.String,
    'createdAt': fields.datetime,
}


def form_or_404(form_id):
    try:
        form = models.Form.get(models.Form.id == form_id)
    except models.Form.DoesNotExist:
        abort(404)
    else:
        return form


class FormList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No course title provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='No course URL provided',
            location=['form', 'json'],
            type=inputs.url
        )
        # Standard setup
        super().__init__()

    def get(self):
        courses = [marshal(form, form_fields)
                   for form in models.Form.select()]
        return jsonify({'courses': courses})

    def post(self):
        args = self.reqparse.parse_args()
        models.Form.create(**args)
        return jsonify({'courses': [{'title': 'Python Basics'}]})


class Form(Resource):
    # @marshal_with(course_fields) == marshal(add_reviews(course_or_404(id)), course_fields)
    @marshal_with(form_fields)
    def get(self, id):
        return form_or_404(id)

    def put(self, id):
        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})


forms_api = Blueprint('resources.forms', __name__)
api = Api(forms_api)
api.add_resource(
    FormList,
    '/forms',
    endpoint='forms'
)

api.add_resource(
    Form,
    '/forms/<int:id>',
    endpoint='form'
)
