from hobbit_core.db import BaseModel, Column, reference_col  # NOQA F401
from sqlalchemy.orm import relationship  # NOQA F401

from app.exts import db
from app.models.base import EntityBase


class PendMiner(db.Model, EntityBase):
    __tablename__ = 'pending_miners'
    id = db.Column(db.Integer, primary_key=True)
    miner_address = db.Column(db.String)
    mid = db.Column(db.Integer)
    status = db.Column(db.String)
    created_time = db.Column(db.Integer)
    hash = db.Column(db.String)
