
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

def get_contract_info(contract_address):
    params1 = {
        "module": "contract",
        "action": "getsourcecode",
        "address": contract_address,
        "apikey": ETHERSCAN_API_KEY
    }
    params2 = {
        "module": "contract",
        "action": "getsourcecode",
        "address": contract_address,
        "apikey": BACSCAN_API_KEY
    }
    params3 = {
        "module": "contract",
        "action": "getsourcecode",
        "address": contract_address,
        "apikey": ftSCAN_API_KEY
    }


    response = requests.get(ETHERSCAN_API_ENDPOINT, params=params1)

    data = response.json()

    if data["status"] == "1" :
        source_code = data["result"][0]["SourceCode"]
        contract_name = data["result"][0]["ContractName"]
        compiler_version = data["result"][0]["CompilerVersion"]
        return source_code, contract_name, compiler_version
    else:
        response = requests.get(BACSCAN_API_ENDPOINT, params=params2)
        data = response.json()
        print(data)
        if data["status"] == "1":
            source_code = data["result"][0]["SourceCode"]
            contract_name = data["result"][0]["ContractName"]
            compiler_version = data["result"][0]["CompilerVersion"]
            return source_code, contract_name, compiler_version
        else:
            response = requests.get(ftSCAN_API_KEY, params=params3)
            data = response.json()

            if data["status"] == "1":
                source_code = data["result"][0]["SourceCode"]
                contract_name = data["result"][0]["ContractName"]
                compiler_version = data["result"][0]["CompilerVersion"]
                return source_code, contract_name, compiler_version

            else:
                return None, None, None
