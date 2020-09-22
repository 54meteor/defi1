from hobbit_core.db import BaseModel, Column, reference_col  # NOQA F401
from sqlalchemy.orm import relationship  # NOQA F401

from app.exts import db
from app.models.base import EntityBase


class Chain(db.Model, EntityBase):
    __tablename__ = 'zero_pools'
    id = db.Column(db.Integer, primary_key=True)
    pool_size = db.Column(db.String)
    per_reward = db.Column(db.String)
    life_cycle = db.Column(db.String)
    per_time = db.Column(db.String)
