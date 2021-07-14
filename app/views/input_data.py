from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator
import flasgger
import marshmallow
from app.schemas import InputFileSchema


class InputData(Resource):
    @jwt_required()
    @flasgger.swag_from(
        {
            "tags": ["Input data"],
            "requestBody": {
                "required": True,
                "content": {
                    "multipart/form-data": {
                        "schema": flasgger.marshmallow_apispec.schema2jsonschema(
                            marshmallow.Schema.from_dict(
                                {
                                    **InputFileSchema().fields,
                                    "attachments": marshmallow.fields.List(
                                        marshmallow.fields.Raw(
                                            metadata=dict(
                                                type="file",
                                                description="files to attach",
                                            )
                                        )
                                    ),
                                }
                            )
                        ),
                        "encoding": {
                            "watchers": {"style": "form", "explode": True},
                            "attachments": {"style": "form", "explode": True},
                        },
                    }
                },
            },
            "responses": {
                204: {"msg": "File is uploaded"},
            },
        }
    )
    def post(self):
        """ Upload file into server """
        f = request.files["file"]
        f.save(f"static/{f.filename}")
        return {"msg": "OK"}

    @jwt_required()
    @swagger_decorator(response_schema={200: InputFileSchema}, tag="Input data")
    def get(self):
        """Get file wich has been uploaded earler"""
        return {"filename": "some file"}
