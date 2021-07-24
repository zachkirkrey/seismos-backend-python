from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class LocationInfo(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "location_info"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    county_name_id = db.Column(db.Integer, nullable=False)
    basin_name_id = db.Column(db.Integer, nullable=False)
    state_id = db.Column(db.Integer, nullable=False)
    job_info_id = db.Column(db.Integer)

    country_name = db.relationship(
        "CountryName",
        foreign_keys=[county_name_id],
        primaryjoin="LocationInfo.county_name_id == CountryName.id"
    )

    basin_name = db.relationship(
        "BasinName",
        foreign_keys=[basin_name_id],
        primaryjoin="LocationInfo.basin_name_id == BasinName.id"
    )

    state = db.relationship(
        "State",
        foreign_keys=[state_id],
        primaryjoin="LocationInfo.state_id == State.id"
    )


class CountryName(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "county_name"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    county_name = db.Column(db.Text)


class BasinName(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "basin_name"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    basin_name = db.Column(db.Text, nullable=False)


class State(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "state"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    value = db.Column(db.Text, nullable=False)
