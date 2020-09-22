from hobbit_core.db import transaction, db

from app.models.base_miner import BaseMiner
from app.models.nodes import Nodes


class NodesService:
    model = Nodes

    @classmethod
    def list(cls):
        return cls.model.query


    @classmethod
    def updateMiner(cls, mid, addr,created_time,addInPool):
        miner = db.session.query(cls.model).filter(Nodes.miner_address == addr).first()
        base = db.session.query(BaseMiner).filter(BaseMiner.id == mid).first()
        if base.price == addInPool:
            miner.miner_level = base.miner_level
            miner.miner_price = base.miner_price
            miner.miner_ability = base.miner_ability
            miner.miner_quantum = base.miner_quantum
            miner.miner_wind = base.miner_wind
            miner.created_time = created_time
        return miner

    @classmethod
    def bindParentMiner(cls, addr, parentAddr):
        parentMiner = db.session.query(cls.model).filter(Nodes.miner_address == parentAddr).first()
        if parentMiner is None or parentMiner.miner_ability == 0:
            return 0
        localMiner = db.session.query(cls.model).filter(Nodes.miner_address == addr).first()
        if localMiner.parent_id != 0:
            return 1
        if localMiner is None:
            localMiner = Nodes(miner_address=addr,
                               miner_level='',
                               miner_price='',
                               miner_ability=0.00,
                               miner_quantum=0.00,
                               miner_wind=0.00,
                               parent_id=0,
                               left_id=0,
                               right_id=0,
                               node_type=0,
                               double_track=0,
                               gravitation=0,
                               node_track=0
                               )
            db.session.add(localMiner)
            db.session.commit()

        if parentMiner.left_id == 0:
            localMiner.parent_id = parentMiner.id
            localMiner.node_type = 1
            parentMiner.left_id = localMiner.id
        elif parentMiner.right_id == 0:
            localMiner.parent_id = parentMiner.id
            localMiner.node_type = 2
            parentMiner.right_id = localMiner.id
        else:
            minerList = cls.list()
            parentId = parentMiner.left_id
            for mine in minerList:
                if mine.id == parentId:
                    if mine.left_id == 0:
                        localMiner.parent_id = mine.id
                        localMiner.node_type = 1
                        mine.left_id = localMiner.id
                        parentMiner = mine
                        break
                    else:
                        parentId = mine.left_id
        db.session.add(localMiner)
        db.session.add(parentMiner)
        db.session.commit()
        return localMiner.parent_id
