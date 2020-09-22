from app.models.base_miner import BaseMiner


class BaseMinerService:
    model = BaseMiner

    @classmethod
    def list(cls):
        return cls.model.query


    @classmethod
    def getById(cls, id):
        return cls.model.query.filter(BaseMiner.id == id).one()
