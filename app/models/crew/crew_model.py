from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class Crew(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "crew"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    shift = db.Column(db.Text, nullable=False)
    role = db.Column(
        db.Enum("admin", "manager", "engineer"), nullable=False, default="N"
    )
    manager_id = db.Column(db.Integer)
