import json
import os

def load_config():
    """Load configuration from a JSON file"""
    #config_path = './config/testsetting.json'  # Path to JSON file
    config_path = os.path.join("config","testsetting.json")
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print(f"[ERROR]: Config file {config_path} not found.")
        return {}