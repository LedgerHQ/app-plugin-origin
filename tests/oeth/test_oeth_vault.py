from web3 import Web3
from tests.utils import run_test, load_contract

contract_oeth_vault = load_contract(
    "39254033945AA2E4809Cc2977E7087BEE48bd7Ab",
    "vault-core"
)

def test_oeth_vault_mint_weth(backend, navigator, test_name, wallet_addr):
    data = contract_oeth_vault.encode_abi("mint", [
        bytes.fromhex("C02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"),
        Web3.to_wei(1, "ether"),
        Web3.to_wei(1, "ether")
    ])

    run_test(contract_oeth_vault, data, backend, navigator, test_name, wallet_addr)

def test_oeth_vault_mint_reth(backend, navigator, test_name, wallet_addr):
    data = contract_oeth_vault.encode_abi("mint", [
        bytes.fromhex("ae78736cd615f374d3085123a210448e74fc6393"),
        Web3.to_wei(1, "ether"),
        Web3.to_wei(1, "ether")
    ])

    run_test(contract_oeth_vault, data, backend, navigator, test_name, wallet_addr)

def test_oeth_vault_mint_steth(backend, navigator, test_name, wallet_addr):
    data = contract_oeth_vault.encode_abi("mint", [
        bytes.fromhex("ae7ab96520de3a18e5e111b5eaab095312d7fe84"),
        Web3.to_wei(1, "ether"),
        Web3.to_wei(1, "ether")
    ])

    run_test(contract_oeth_vault, data, backend, navigator, test_name, wallet_addr)

def test_oeth_vault_mint_frxeth(backend, navigator, test_name, wallet_addr):
    data = contract_oeth_vault.encode_abi("mint", [
        bytes.fromhex("5e8422345238f34275888049021821e8e08caa1f"),
        Web3.to_wei(1, "ether"),
        Web3.to_wei(1, "ether")
    ])

    run_test(contract_oeth_vault, data, backend, navigator, test_name, wallet_addr)

def test_oeth_vault_redeem(backend, navigator, test_name, wallet_addr):
    data = contract_oeth_vault.encode_abi("redeem", [
        Web3.to_wei(1, "ether"),
        Web3.to_wei(0.88, "ether")
    ])

    run_test(contract_oeth_vault, data, backend, navigator, test_name, wallet_addr)
