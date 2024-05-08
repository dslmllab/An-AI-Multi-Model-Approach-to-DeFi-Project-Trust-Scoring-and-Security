import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def get_api_keys(keyid):

    match keyid:
        case "ether":
            api_key = config['etherscan']['ether_api_key']
            return api_key
        case "bscan":
            api_key = config['bscscan']['bscscan_api_key']
            return api_key
        case "ftscan":
            api_key = config['ftsscan']['ftscan_api_key']
            return api_key
        case "searchapi":
            search_api_key = config['google']['search_api_key']
            return search_api_key
        case "searchengine":
            engine_id =  config['google']['search_engine_id']
            return engine_id
        case "openaikey":
            openaikey = config['openai']
            return openaikey



