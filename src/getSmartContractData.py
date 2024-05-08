
import requests
import configparser
import getApiKeys

config = configparser.ConfigParser()
config.read('config.ini')



ETHERSCAN_API_KEY = getApiKeys.get_api_keys('ether')
ETHERSCAN_API_ENDPOINT = "https://api.etherscan.io/api"

BACSCAN_API_KEY = getApiKeys.get_api_keys('bscan')

BACSCAN_API_ENDPOINT = "https://api.bscscan.com/api"

ftSCAN_API_KEY = getApiKeys.get_api_keys('ftscan')

ftSCAN_API_ENDPOINT = "https://api.bscscan.com/api"


def get_contract_details(contract_address):
    params = {
        "module": "contract",
        "action": "getabi",
        "address": contract_address,
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(ETHERSCAN_API_ENDPOINT, params=params)
    abi_data = response.json()

    params = {
        "module": "account",
        #"action": "tokentx",
        "action": "txlist",
        "address": contract_address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(ETHERSCAN_API_ENDPOINT, params=params)
    tx_data = response.json()

    if abi_data["status"] == "1" and tx_data["status"] == "1":
        contract_abi = abi_data["result"]

        contract_transactions = tx_data["result"]

        return contract_abi, contract_transactions
    else:
        return None, None


import requests
import configparser
import getApiKeys

config = configparser.ConfigParser()
config.read('config.ini')



ETHERSCAN_API_KEY = get_api_keys.get_api_keys('ether')
ETHERSCAN_API_ENDPOINT = "https://api.etherscan.io/api"

BACSCAN_API_KEY = get_api_keys.get_api_keys('bscan')

BACSCAN_API_ENDPOINT = "https://api.bscscan.com/api"

ftSCAN_API_KEY = get_api_keys.get_api_keys('ftscan')

ftSCAN_API_ENDPOINT = "https://api.bscscan.com/api"


def get_contract_details(contract_address):
    params = {
        "module": "contract",
        "action": "getabi",
        "address": contract_address,
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(ETHERSCAN_API_ENDPOINT, params=params)
    abi_data = response.json()

    params = {
        "module": "account",
        #"action": "tokentx",
        "action": "txlist",
        "address": contract_address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(ETHERSCAN_API_ENDPOINT, params=params)
    tx_data = response.json()

    if abi_data["status"] == "1" and tx_data["status"] == "1":
        contract_abi = abi_data["result"]

        contract_transactions = tx_data["result"]

        return contract_abi, contract_transactions
    else:
        return None, None

