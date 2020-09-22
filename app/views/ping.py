from decimal import Decimal

from flask import Blueprint, jsonify, request, json

from hobbit_core.pagination import PageParams, pagination  # NOQA
from app import models  # NOQA
from app import schemas  # NOQA
from app.contracts import ContractHandler
from app.contracts.ContractHandler import checkAddress
from app.services.base_miner import BaseMinerService
from app.services.chain import ChainService
from app.services.nodes import NodesService
from app.services.pending_miner import PendingMinerService
from app.services.reward import RewardService
from app.utils import decimalutil
bp = Blueprint('ping', __name__)


@bp.route('/getinfo/<addr>', methods=['GET'])
def ping(addr):
    miner = {"miner_address": addr}
    nodes = NodesService.list()
    miner['node'] = getInfo(addr, nodes)
    miner['reward'] = getReward(addr)
    miner['chain'] = getChain()
    miner['base_miner'] = getMinerList()
    return jsonify(miner)


def getMinerList():
    rs = BaseMinerService.list()
    minerList = []
    for r in rs:
        r.miner_quantum = decimalutil.decimal2str(r.miner_quantum, '0.00')
        r.miner_ability = decimalutil.decimal2str(r.miner_ability, '0.00')
        r.miner_wind = decimalutil.decimal2str(r.miner_wind, '0.00')
        minerList.append(r.to_json())
    return minerList


def getChain():
    chainInfo = ChainService.list()
    day = Decimal(60 * 60 * 24 / 3) * Decimal(chainInfo.per_reward)
    days = 365 - int(chainInfo.life_cycle)
    chain = {'per_reward': chainInfo.per_reward,
             'day_output': decimalutil.decimal2str(day, '0.00'),
             'total_output': decimalutil.decimal2str(days * day, '0.00')}
    return chain


def getReward(addr):
    ability = {'totalReward': Decimal(0)}
    reward = RewardService.addrlist(addr)
    for r in reward:
        if r.miner_address == addr:
            ability['totalReward'] += Decimal(r.reward)
    ability['totalReward'] = decimalutil.decimal2str(ability['totalReward'], '0.00000000')
    ability['availableReward'] = str(ContractHandler.getChainReward(addr))
    return ability


def getInfo(addr, nodes):
    ability = {'total_ability': Decimal(0)}
    rs = []
    for node in nodes:
        ability['total_ability'] += node.node_track
        node.node_track = decimalutil.decimal2str(node.node_track, '0.00')
        node.double_track = decimalutil.decimal2str(node.double_track, '0.00')
        node.miner_quantum = decimalutil.decimal2str(node.miner_quantum, '0.00')
        node.gravitation = decimalutil.decimal2str(node.gravitation, '0.00')
        node.miner_ability = decimalutil.decimal2str(node.miner_ability, '0.00')
        rs.append(node.to_json())
        if node.miner_address == addr:
            ability['miner_ability'] = node.miner_ability
            ability['double_track'] = node.double_track
            ability['gravitation'] = node.gravitation
            ability['node_track'] = node.node_track
    ability['total_ability'] = decimalutil.decimal2str(ability['total_ability'], '0.00')
    return ability


# @bp.route('/pool/', methods=['GET'])
# def test():
#     return ContractHandler.getMinerPool()


@bp.route('/bind/', methods=['POST'])
def bindParent():
    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    parentAddr = json_data.get("pAddr")
    localAddr = json_data.get("lAddr")
    sign = json_data.get("sign")
    if not checkAddress(localAddr,sign):
        return jsonify({'msg': 'Sign invalid', 'code': '200'})
    rs = NodesService.bindParentMiner(localAddr, parentAddr)
    if rs == 0:
        return jsonify({'msg': 'parent not miner', 'code': '400'})
    elif rs == 1:
        return jsonify({'msg': 'Already has parent', 'code': '400'})
    return jsonify({'parent_id': rs, 'msg': 'Bind Success', 'code': '200'})


@bp.route('/createMiner/', methods=['POST'])
def createMiner():
    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    mid = json_data.get("mid")
    addr = json_data.get("address")
    hashCode = json_data.get("hash")
    createTime = json_data.get("create_time")
    sign = json_data.get("sign")
    if not checkAddress(addr,sign):
        return jsonify({'msg': 'Sign invalid', 'code': '200'})
    miner = BaseMinerService.getById(mid)
    mid = PendingMinerService.addMiner(miner, addr, hashCode, createTime)
    if mid == 0:
        return jsonify({'addr': mid, 'msg': 'miner exist', 'code': '400'})
    return jsonify({'mid': mid, 'msg': 'pending', 'code': '200'})
