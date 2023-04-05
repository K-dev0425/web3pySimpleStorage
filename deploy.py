from solcx import compile_standard, install_solc
import json
from web3 import Web3

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile Our Standard

install_solc("0.8.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    }
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connection to ganache
w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:7545"))
chain_id = 5777
my_address = "0x1851c1a57b2A69ec695f8943169b29b9537101E9"
private_key = "0xd61abb0342a5ee594ef07c3421e4b90fe955b3c7bb42d6c6d432678da83d55a8"

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode) 
# get transaction count
nonce = w3.eth.get_transaction_count(my_address)
# submit the transaction that deploys the contract
transaction = SimpleStorage.constructor().build_transaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)
