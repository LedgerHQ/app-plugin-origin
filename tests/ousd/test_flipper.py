from web3 import Web3
from tests.utils import run_test, load_contract

contract_ousd_flipper = load_contract(
    "cecaD69d7D4Ed6D52eFcFA028aF8732F27e08F70",
    "flipper"
)

def test_ousd_flipper_flip_with_usdc(backend, navigator, test_name, wallet_addr):
    data = contract_ousd_flipper.encode_abi("buyOusdWithUsdc", [
        Web3.to_wei(10000, "ether")
    ])

    run_test(
        contract_ousd_flipper, 
        data, 
        backend, 
        navigator, 
        test_name, 
        wallet_addr
    )

def test_ousd_flipper_flip_to_usdc(backend, navigator, test_name, wallet_addr):
    data = contract_ousd_flipper.encode_abi("sellOusdForUsdc", [
        Web3.to_wei(10000, "ether")
    ])

    run_test(
        contract_ousd_flipper, 
        data, 
        backend, 
        navigator, 
        test_name, 
        wallet_addr
    )

def test_ousd_flipper_flip_with_usdt(backend, navigator, test_name, wallet_addr):
    data = contract_ousd_flipper.encode_abi("buyOusdWithUsdt", [
        Web3.to_wei(10000, "ether"),
    ])

    run_test(
        contract_ousd_flipper, 
        data, 
        backend, 
        navigator, 
        test_name, 
        wallet_addr
    )

def test_ousd_flipper_flip_to_usdt(backend, navigator, test_name, wallet_addr):
    data = contract_ousd_flipper.encode_abi("sellOusdForUsdt", [
        Web3.to_wei(10000, "ether")
    ])

    run_test(
        contract_ousd_flipper, 
        data, 
        backend, 
        navigator, 
        test_name, 
        wallet_addr
    )

def test_ousd_flipper_flip_with_dai(backend, navigator, test_name, wallet_addr):
    data = contract_ousd_flipper.encode_abi("buyOusdWithDai", [
        Web3.to_wei(10000, "ether")
    ])

    run_test(
        contract_ousd_flipper, 
        data, 
        backend, 
        navigator, 
        test_name, 
        wallet_addr
    )

def test_ousd_flipper_flip_to_dai(backend, navigator, test_name, wallet_addr):
    data = contract_ousd_flipper.encode_abi("sellOusdForDai", [
        Web3.to_wei(10000, "ether")
    ])

    run_test(
        contract_ousd_flipper, 
        data, 
        backend, 
        navigator, 
        test_name, 
        wallet_addr
    )
