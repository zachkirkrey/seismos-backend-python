from sqlalchemy.orm import backref
from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class Well(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "well"

    id = db.Column(db.Integer, primary_key=True)
    well_uuid = db.Column(db.String(36), nullable=False)
    pad_id = db.Column(db.Integer, nullable=False)
    well_name = db.Column(db.Text)
    well_api = db.Column(db.Text)
    formation_id = db.Column(db.Integer)
    num_stages = db.Column(db.Integer)
    total_planned_stage = db.Column(db.Integer)
    total_perfs = db.Column(db.Integer)
    total_clusters = db.Column(db.Integer)
    frac_system = db.Column(db.Text)
    fluid_system = db.Column(db.Text)
    well_start_time = db.Column(db.DateTime)
    well_end_time = db.Column(db.DateTime)
    bottom_hole_latitude = db.Column(db.Float)
    bottom_hole_longitude = db.Column(db.Float)
    surface_longitude = db.Column(db.Float)
    surface_latitude = db.Column(db.Float)
    lateral_length = db.Column(db.Float)
    lateral_length_unit = db.Column(db.Text)
    measured_depth = db.Column(db.Float)
    vertical_depth = db.Column(db.Float)
    vertical_depth_unit = db.Column(db.Text)
    surface_latitude = db.Column(db.Text)
    surface_longitude = db.Column(db.Text)
    bottom_hole_latitude = db.Column(db.Text)
    bottom_hole_longitude = db.Column(db.Text)
    estimated_surface_vol = db.Column(db.Float)
    estimated_bbls = db.Column(db.Float)
    estimated_gallons = db.Column(db.Float)
    casing_od = db.Column(db.Float)
    casing_wt = db.Column(db.Float)
    casing_id = db.Column(db.Float)
    casing_depth_md = db.Column(db.Float)
    casing_tol = db.Column(db.Float)
    liner1_od = db.Column(db.Float)
    liner1_wt = db.Column(db.Float)
    liner1_id = db.Column(db.Text)
    liner1_depth_md = db.Column(db.Float)
    liner1_tol = db.Column(db.Float)
    liner2_od = db.Column(db.Float)
    liner2_wt = db.Column(db.Float)
    liner2_id = db.Column(db.Text)
    liner2_depth_md = db.Column(db.Float)
    liner2_tol = db.Column(db.Float)
    measured_depth_unit = db.Column(db.Text)

    daily_logs = db.relationship(
        "DailyLog",
        foreign_keys=[id],
        primaryjoin="Well.id == DailyLog.well_id",
        uselist=True
    )

    default_value = db.relationship(
        "DefaultVal",
        foreign_keys=[id],
        primaryjoin="Well.id == DefaultVal.well_id",
    )

    default_advance_val = db.relationship(
        "DefaultAdvanceVal",
        foreign_keys=[id],
        primaryjoin="Well.id == DefaultAdvanceVal.well_id",
    )

    default_param_val = db.relationship(
        "DefaultParamVal",
        foreign_keys=[id],
        primaryjoin="Well.id == DefaultParamVal.well_id",
    )

    tracking_sheet = db.relationship(
        "TrackingSheet",
        foreign_keys=[id],
        primaryjoin="Well.id == TrackingSheet.well_id",
        uselist=True,
        backref=backref('well', uselist=False),
        lazy=True,
    )

    def get_logs(self):
        logs = []
        for log in self.daily_logs:
            logs.append({
                "date": int(log.date.timestamp() * 1000),
                "description": log.description,
            })

        return logs
