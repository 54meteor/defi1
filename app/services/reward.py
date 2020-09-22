from hobbit_core.db import db

from app.models.reward import Reward


class RewardService:
    model = Reward

    @classmethod
    def addrlist(cls, addr):
        return cls.model.query.filter(Reward.miner_address == addr).all()


    @classmethod
    def rewardList(cls):
        return cls.model.query.filter(Reward.hash_code == "").all()


    @classmethod
    def updateReward(cls, reward):
        db.session.add(reward)
        db.session.commit()