from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator

from app.schemas import (
    SuccessSchema,
    ErrorSchema,
    OCReportSchema,
)


class OCReport(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: OCReportSchema},
    )
    def get(self):
        """ Get OC raport data"""
        return {"report": "OC report data"}

    @jwt_required()
    @swagger_decorator(
        json_schema=OCReportSchema,
        response_schema={200: SuccessSchema, 401: ErrorSchema},
    )
    def post(self):
        """ Approve OC report """
        return {"msg": "Report approve"}


class OCReportExport(Resource):
    @jwt_required()
    @swagger_decorator(
        json_schema=OCReportSchema,
        response_schema={200: SuccessSchema, 401: ErrorSchema},
    )
    def post(self):
        """ Export OC """
        return {"msg": "OC export"}
