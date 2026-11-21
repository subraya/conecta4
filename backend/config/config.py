

import os
from . import dev, test

def get_env_db_config():
    if os.environ.get("TESTING"):
        return test.DB_CONFIG
    return dev.DB_CONFIG

def get_env_gcp_config():
    if os.environ.get("TESTING"):
        return test.GCP_CONFIG
    return dev.GCP_CONFIG


PUMP_CONFIG = {
    "game_records": ["winner", "player1_type", "player2_type", "rules", "moves", "hash_id"]
}