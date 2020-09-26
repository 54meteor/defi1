import os

from web3 import Web3

from app.contracts.ContractHandler import getMinerPool, setChainReward, setChainRewards
from app.run import scheduler


def chain_search():
    print("chain_search")
    with scheduler.app.app_context():
        from app.services.pending_miner import PendingMinerService
        pendList = PendingMinerService.listByStatus()
        for pending in pendList:
            addInPool = getMinerPool(pending.miner_address)
            if addInPool > 0:
                print(addInPool)
                print(pending.miner_address)
                pending.status = '1'
                PendingMinerService.upPending(pending, str(addInPool))

def set_reward():
    with scheduler.app.app_context():
        from app.services.reward import RewardService
        rewardList = RewardService.rewardList()
        userList = []
        amountList = []
        if len(rewardList) > 0:
            for reward in rewardList:
                userList.append(Web3.toChecksumAddress(reward.miner_address))
                amountList.append(Web3.toWei(reward.reward, 'ether'))
            hash_code = setChainRewards(userList, amountList)
            for reward in rewardList:
                reward.hash_code = hash_code
                RewardService.updateReward(reward)


def reward():
    os.system('/defi/treecode')



