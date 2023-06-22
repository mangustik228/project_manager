import os
import subprocess
from loguru import logger
from utils.base_manager import BaseManager
from utils.functions import check_atribute
from exceptions.exc import ProjectIsExist
from utils.creators import create_readme


class Manager(BaseManager):
    @check_atribute('name')
    def create_new_project(self):
        if not self.namespace.get("name"):
            logger.debug(f'Не созданы README.md и main.py')
            return
        name = self.namespace.get("name")
        if os.path.exists(name):
            raise ProjectIsExist(f"Проект с именем \"{name}\" уже существуют")
        os.makedirs(f"{name}/app/utils")
        self.requirements.add('loguru')
        os.chdir(name)
        self.copy_file('app/main.py')
        create_readme(name)
        logger.info(f'Создан проект {name}.')

    @check_atribute('git')
    def create_repo_git(self):
        self.copy_file('.gitignore')
        subprocess.run(["git", "init"])
        logger.info(f'Создан .gitignore и инициализирован репозиторий')

    @check_atribute('env')
    def create_env_file(self):
        self.copy_file('.env')
        logger.info(f'Создан фаил .env ')

    @check_atribute('config')
    def create_config_template(self):
        self.requirements.add('pydantic')
        self.requirements.add('python-dotenv')
        self.copy_file('config.ini')
        self.copy_folder('app/config')
        logger.info(f'Создана папка config и скопирован фаил config.ini')

    @check_atribute("venv")
    def create_venv(self):
        subprocess.run(['python3', '-m', 'venv', 'venv'])
        logger.info(f'Создано виртуальное окружение')

    @check_atribute('args')
    def create_args_parser(self):
        self.copy_file('app/arg_parser.py', 'app/config/arg_parser.py')

    @check_atribute("test")
    def create_test_folder(self):
        self.copy_file('pytest.ini')
        self.copy_folder('tests')
        self.requirements.add('pytest')
        logger.info(f'Созданы заготовки под тесты')

    @check_atribute('name')
    def finish(self):
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', 'Initilization'])
        subprocess.run(['code', '.'])
