from functools import lru_cache
from loguru import logger
from pydantic import BaseSettings
from configparser import ConfigParser


class _Settings(BaseSettings):
    base_path: str


@lru_cache
def get_settings(config_path) -> _Settings:
    config_ini = ConfigParser()
    config_ini.read(config_path)
    base_path = config_ini.get('default', 'base_path')
    return _Settings(base_path=base_path)
