from web3 import Web3
from tests.utils import run_test, load_contract

contract_oeth_zapper = load_contract(
    "9858e47bcbbe6fbac040519b02d7cd4b2c470c66",
    "zapper"
)

def test_oeth_zapper_deposit_eth(backend, navigator, test_name, wallet_addr):
    data = contract_oeth_zapper.encode_abi("deposit", [])

    run_test(
        contract_oeth_zapper, 
        data, 
        backend, 
        navigator, 
        test_name,
        wallet_addr,
        value=Web3.to_wei(1, "ether")
    )

def test_oeth_zapper_deposit_sfrxeth(backend, navigator, test_name, wallet_addr):
    data = contract_oeth_zapper.encode_abi("depositSFRXETH", [
        Web3.to_wei(1, "ether"),
        Web3.to_wei(0.991, "ether")
    ])

    run_test(contract_oeth_zapper, data, backend, navigator, test_name, wallet_addr)
