# from hobbit_core.db import db
from app.exts import db
from app.models.nodes import Nodes
from app.models.pending_miner import PendMiner
from app.services.nodes import NodesService


class PendingMinerService:
    model = PendMiner

    @classmethod
    def list(cls):
        return cls.model.query

    @classmethod
    def addMiner(cls, miner, addr, hashCode, createdTime):
        local = db.session.query(cls.model).filter(PendMiner.miner_address == addr).all()
        if len(local) > 0:
            return 0

        pending = PendMiner(miner_address=addr,
                            hash=hashCode,
                            mid=miner.id,
                            created_time=createdTime,
                            status="0"
                            )
        node = Nodes(miner_address=addr,
                     miner_level='',
                     miner_price='',
                     miner_ability=0.00,
                     miner_quantum=0.00,
                     miner_wind=0.00,
                     created_time=createdTime,
                     parent_id=0,
                     left_id=0,
                     right_id=0,
                     node_type=0,
                     double_track=0,
                     gravitation=0,
                     node_track=0
                     )
        db.session.add(node)
        db.session.add(pending)
        db.session.commit()
        return pending.id

    @classmethod
    def listByStatus(cls):
        return db.session.query(cls.model).filter(PendMiner.status == "0").all()

    @classmethod
    def upPending(cls,pending, addInPool):
        node = NodesService.updateMiner(pending.mid, pending.miner_address, pending.created_time, addInPool)
        if node.miner_ability == 0:
            pending.status = '2'
            db.session.add(pending)
            db.session.commit()
            return
        db.session.add(pending)
        db.session.add(node)
        db.session.commit()