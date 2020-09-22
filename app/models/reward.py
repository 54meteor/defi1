from hobbit_core.db import BaseModel, Column, reference_col  # NOQA F401
from sqlalchemy.orm import relationship  # NOQA F401

from app.exts import db
from app.models.base import EntityBase


class Reward(db.Model, EntityBase):
    __tablename__ = 'reward_records'
    id = db.Column(db.Integer, primary_key=True)
    miner_address = db.Column(db.String)
    reward = db.Column(db.String)
    hash_code = db.Column(db.String)
