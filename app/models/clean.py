from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class Clean(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "clean"

    id = db.Column(db.BigInteger, autoincrement=True)
    stage_id = db.Column(db.Integer, primary_key=True, nullable=False)
    total_clean_rate = db.Column(db.Float)
    total_clean_rate2 = db.Column(db.Float)
