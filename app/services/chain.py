from app.models.chain import Chain


class ChainService:
    model = Chain

    @classmethod
    def list(cls):
        return cls.model.query.one()


