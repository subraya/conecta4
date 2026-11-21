
from config.config import get_env_gcp_config


class Storage:
    def __init__(self, gcp_config = None):
        if not gcp_config:
            gcp_config = get_env_gcp_config()
        self.project_id = gcp_config["project_id"]