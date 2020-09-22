import json

from web3 import Web3

# w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/e0ec62bcaf8c48f280127c0aa347ca24'))
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
# wallet_key = '7da5fec4819164669acf5b767dcfbc952ee3e58c0e5dc6b78ba0bedc55846650'
wallet_key = '9a800c9eee984cfb81a5eb850a82bd3b376746daa7020a9eed00c29161530acc'
def getChainReward(address):
    contract_address = "0x2556D96eFe5a902B0Bbb83659ef24687a70Eb766"
    checksum_address = w3.toChecksumAddress(contract_address)
    abi = """[
        {
            "inputs": [
                {
                    "internalType": "address[]",
                    "name": "_users",
                    "type": "address[]"
                },
                {
                    "internalType": "uint256[]",
                    "name": "_amounts",
                    "type": "uint256[]"
                }
            ],
            "name": "batchRecord",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "previousOwner",
                    "type": "address"
                },
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address"
                }
            ],
            "name": "OwnershipTransferred",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_user",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "record",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "_user",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "recordEvent",
            "type": "event"
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address"
                }
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_to",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "withdrawCZG",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "_to",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "withdrawEvent",
            "type": "event"
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "name": "userMapping",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]"""
    wallet_address = w3.toChecksumAddress(address)
    czg = w3.eth.contract(address=checksum_address, abi=abi)
    return czg.functions.userMapping(wallet_address).call()


def setChainReward(address, amount):
    contract_address = "0x2556D96eFe5a902B0Bbb83659ef24687a70Eb766"
    # w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/e0ec62bcaf8c48f280127c0aa347ca24'))
    # w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    checksum_address = w3.toChecksumAddress(contract_address)
    abi = """[
        {
            "inputs": [
                {
                    "internalType": "address[]",
                    "name": "_users",
                    "type": "address[]"
                },
                {
                    "internalType": "uint256[]",
                    "name": "_amounts",
                    "type": "uint256[]"
                }
            ],
            "name": "batchRecord",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "previousOwner",
                    "type": "address"
                },
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address"
                }
            ],
            "name": "OwnershipTransferred",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_user",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "record",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "_user",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "recordEvent",
            "type": "event"
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address"
                }
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_to",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "withdrawCZG",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "_to",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "withdrawEvent",
            "type": "event"
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "name": "userMapping",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]"""
    wallet_address = w3.toChecksumAddress("0xe58436F465ac6F32525fbFd75FE2e07181450155")
    # wallet_address = w3.toChecksumAddress(address)
    czg = w3.eth.contract(address=checksum_address, abi=abi)
    reward =  Web3.toWei(amount, 'ether')
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = czg.functions.record(wallet_address,reward).buildTransaction({
        'gas' : 2000000,
        'gasPrice' : w3.toWei('40','gwei'),
        'nonce' : nonce,
        'chainId' : 1337,
    })
    signed_txn = w3.eth.account.sign_transaction(txn_dict,private_key=wallet_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.getTransactionReceipt(txn_hash)
    return w3.toHex(tx_receipt.transactionHash)


def getMinerPool(addr):
    contract_address = "0xEc5aEbBD2F603b46b62A9d07166dAEcF5d64b22C"
    # w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/e0ec62bcaf8c48f280127c0aa347ca24'))
    # w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    checksum_address = w3.toChecksumAddress(contract_address)
    abi = """[
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "previousOwner",
                    "type": "address"
                },
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address"
                }
            ],
            "name": "OwnershipTransferred",
            "type": "event"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "_from",
                    "type": "address"
                },
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "_to",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "internalType": "uint256",
                    "name": "_value",
                    "type": "uint256"
                },
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "contractAddress",
                    "type": "address"
                }
            ],
            "name": "payUSDTEvent",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_from",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "buyFromUSDT",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address"
                }
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "name": "userMapping",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]"""
    wallet_address = w3.toChecksumAddress(addr)
    czg = w3.eth.contract(address=checksum_address, abi=abi)
    return czg.functions.userMapping(wallet_address).call()


def setChainRewards(addressList, amountList):
    contract_address = "0x2556D96eFe5a902B0Bbb83659ef24687a70Eb766"
    # w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/e0ec62bcaf8c48f280127c0aa347ca24'))
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    checksum_address = w3.toChecksumAddress(contract_address)
    abi = """[
        {
            "inputs": [
                {
                    "internalType": "address[]",
                    "name": "_users",
                    "type": "address[]"
                },
                {
                    "internalType": "uint256[]",
                    "name": "_amounts",
                    "type": "uint256[]"
                }
            ],
            "name": "batchRecord",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "previousOwner",
                    "type": "address"
                },
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address"
                }
            ],
            "name": "OwnershipTransferred",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_user",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "record",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "_user",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "recordEvent",
            "type": "event"
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address"
                }
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_to",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "withdrawCZG",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "_to",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "withdrawEvent",
            "type": "event"
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "name": "userMapping",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]"""
    wallet_address = w3.toChecksumAddress("0xe58436F465ac6F32525fbFd75FE2e07181450155")
    # wallet_address = w3.toChecksumAddress(address)
    czg = w3.eth.contract(address=checksum_address, abi=abi)
    # reward =  Web3.toWei(amount, 'ether')
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = czg.functions.batchRecord(addressList, amountList).buildTransaction({
        'gas' : 2000000,
        'gasPrice' : w3.toWei('40','gwei'),
        'nonce' : nonce,
        'chainId' : 1337,
    })
    # print(w3.eth.sign(wallet_address,text='dafdf'))
    signed_txn = w3.eth.account.sign_transaction(txn_dict,private_key=wallet_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    # tx_receipt = w3.eth.getTransactionReceipt(txn_hash)
    # print(w3.toHex(txn_hash))
    return w3.toHex(txn_hash)

def checkAddress(address, sign):
    w = w3.toChecksumAddress(address)
    nonce = w3.eth.getTransactionCount(w)
    s = w3.toHex(w3.keccak(text=str(address + str(nonce))))
    print(s)
    # s = w3.toHex(w3.eth.sign(w, h))
    return sign == s

# address = "0x0631fc9f6c0c4594D66eAaFa61EDDC6A1d4AB583"
# nonce = 2
# address + str(nonce) = 0x0631fc9f6c0c4594D66eAaFa61EDDC6A1d4AB5832
# toHex(keccak) 0x137a38d2f769a5dcdbf4941b5c48649fc0bd4769ef29bf68a808ae861d49e369
#print(checkAddress("0x0631fc9f6c0c4594D66eAaFa61EDDC6A1d4AB583",
#                    "0x137a38d2f769a5dcdbf4941b5c48649fc0bd4769ef29bf68a808ae861d49e369"))
