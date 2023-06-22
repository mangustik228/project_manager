import argparse
import os
import shutil

from loguru import logger
from config.config import get_settings
from utils.requirements import RequirementsManager


class BaseManager:
    def __init__(self, namespace, base_path: str):
        self.namespace = namespace
        venv = self._namespace.get('venv') or self._namespace.get('full')
        self.requirements = RequirementsManager(venv)
        self.settings = get_settings(base_path)

    @property
    def namespace(self):
        return self._namespace

    @namespace.setter
    def namespace(self, other: argparse.Namespace):
        self._namespace = {}
        for key, value in other._get_kwargs():
            self._namespace[key] = value

    def copy_file(self, output_path: str, input_path: str = None):
        if input_path is None:
            input_path = output_path
        if os.path.exists(input_path):
            logger.warning(
                f'"{input_path}" фаил уже существует, он не был перезаписан')
            return
        shutil.copy(f'{self.settings.base_path}/{output_path}', input_path)

    def copy_folder(self, output_path: str, input_path: str = None):
        if input_path is None:
            input_path = output_path
        if os.path.exists(input_path):
            logger.warning(
                f'"{input_path}" папка уже существует, она не был перезаписан')
            return
        shutil.copytree(
            f'{self.settings.base_path}/{output_path}', input_path)
