from hobbit_core.db import BaseModel, Column, reference_col  # NOQA F401
from sqlalchemy.orm import relationship  # NOQA F401

from app.exts import db
from app.models.base import EntityBase


class BaseMiner(db.Model, EntityBase):
    __tablename__ = 'base_miners'
    id = db.Column(db.Integer, primary_key=True)
    miner_level = db.Column(db.String)
    miner_price = db.Column(db.DECIMAL)
    miner_ability = db.Column(db.DECIMAL)
    miner_quantum = db.Column(db.DECIMAL)
    miner_wind = db.Column(db.DECIMAL)
    price = db.Column(db.String)
