from hobbit_core.db import BaseModel, Column, reference_col  # NOQA F401
from sqlalchemy.orm import relationship  # NOQA F401

from app.exts import db
from app.models.base import EntityBase


class Nodes(db.Model, EntityBase):
    __tablename__ = 'miners'
    id = db.Column(db.Integer, primary_key=True)
    miner_address = db.Column(db.String)
    parent_id = db.Column(db.Integer)
    left_id = db.Column(db.Integer)
    right_id = db.Column(db.Integer)
    node_type = db.Column(db.String)
    miner_level = db.Column(db.String)
    miner_price = db.Column(db.DECIMAL)
    miner_ability = db.Column(db.DECIMAL)
    miner_quantum = db.Column(db.DECIMAL)
    miner_wind = db.Column(db.DECIMAL)
    created_time = db.Column(db.Integer)
    double_track = db.Column(db.DECIMAL)
    gravitation = db.Column(db.DECIMAL)
    node_track = db.Column(db.DECIMAL)
