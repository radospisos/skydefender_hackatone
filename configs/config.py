import json

def get_config(config_path):
    with open('configs/' + config_path, 'r', encoding='utf-8') as f:
         config = json.load(f)
    return config
