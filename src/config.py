import tomllib
import os
from typing import Optional

DEBUG = os.getenv("DEBUG", "0") in ("1", "true", "True")

class Config:
    """
    get config from ENV or default locations
    1. $RAG_CONFIG
    2. ~/.config/rag-openheidelberg/config.toml
    3. $DAGSTER_HOME/configs/rag-openheidelberg/config.toml
    4. /etc/rag-openheidelberg/config.toml
    5. /usr/local/etc/rag-openheidelberg/config.toml
    6. raise FileNotFoundError
    params:
        configfile: str|None = None, if None, search for config file
    """

    def __init__(self, configfile: Optional[str] = None) -> None:
        if not configfile:
            configfile = self.find_configfile()
        with open(configfile, "rb") as f:
            self.config = tomllib.load(f)

    def get(self, key: Optional[str]) -> dict:
        if not key:
            return self.config
        return self.config.get(key, {})
    
    def find_configfile(self) -> str:
        for config_path in [
            os.getenv("RAG_CONFIG", ""),
            os.path.expanduser("~/.config/rag-openheidelberg/config.toml"),
            os.getenv("DAGSTER_HOME", "") + "configs/rag-openheidelberg/config.toml",
            "/etc/rag-openheidelberg/config.toml",
            "/usr/local/etc/rag-openheidelberg/config.toml"]:
            if DEBUG:
                print(f"Checking for config file at: {config_path}")
            if os.path.exists(config_path):
                if DEBUG:
                    print(f"Found config file at: {config_path}")
                return config_path
        raise FileNotFoundError("No config file found")
