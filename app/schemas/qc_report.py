from marshmallow import Schema, fields


class SyncCloudRequestScehma(Schema):
    project_uuid = fields.UUID(required=True)
    well_uuid = fields.UUID(required=True)
