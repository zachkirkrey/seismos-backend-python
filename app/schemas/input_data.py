from marshmallow import Schema, fields, validate


class InputFileSchema(Schema):
    file = fields.Raw(
        required=True,
        metadata=dict(description='File to upload'),
        type="file",
        name="filename",
    )


class InputDataRequestSchema(Schema):
    project_id = fields.Int()
    well_id = fields.Int()


class FileResponseSchema(Schema):
    file = fields.Str()


class DataInputDataInputSchema(Schema):
    hydrophone = fields.Nested(FileResponseSchema)
    pumping_data = fields.Nested(FileResponseSchema)
    pressure = fields.Nested(FileResponseSchema)
    survey = fields.Nested(FileResponseSchema)
    gamma_ray = fields.Nested(FileResponseSchema)
    mud_log = fields.Nested(FileResponseSchema)


class DataInputDataSchema(Schema):
    data_input = fields.Nested(DataInputDataInputSchema)


class DataInputResponseSchema(Schema):
    status = fields.Int()
    message = fields.Str()
    data = fields.Nested(DataInputDataSchema)


class DataInputFileUploadSchema(Schema):
    file = fields.Raw(type="file")


class DataInputAreaPathSchema(Schema):
    data_area = fields.Str(validate=validate.OneOf([
        "hydrophone",
        "pressure",
        "pumping_data",
        "survey",
        "gamma_ray",
        "mud_log",
    ]))
