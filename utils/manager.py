import os
import subprocess
from loguru import logger
from utils.base_manager import BaseManager
from utils.functions import check_atribute
from exceptions.exc import ProjectIsExist
from utils.creators import create_readme
from PyInquirer import prompt


class Manager(BaseManager):
    def create_new_project(self):
        if not self.name:
            logger.info(f'Не созданы README.md и main.py')
            return
        if os.path.exists(self.name):
            raise ProjectIsExist(
                f"Проект с именем \"{self.name}\" уже существуют")
        else:
            os.makedirs(self.name)
            os.chdir(self.name)

    def ask_about_name(self):
        if self.name is not None:
            return

        questions = [
            {
                'type': 'list',
                'name': 'choice',
                'message': 'Не указано имя проекта:',
                'choices': [
                    'Так и задумано',
                    'Отменить',
                    'Ввести имя проекта',
                ],
            }
        ]
        answer = prompt(questions).get("choice")
        if answer is None:
            logger.info(f'strange error')
            exit()
        if answer == "Так и задумано":
            logger.info('Создаю файлы в текущей папке')
            return
        if answer == "Отменить":
            logger.warning('Программа отменена')
            exit()
        if answer == "Ввести имя проекта":
            self.name = input()

    def create_template(self):
        if os.path.exists('app'):
            logger.error(f'folder app is exist')
            return
        os.makedirs("app")
        if self.namespace.get("fastapi"):
            logger.info(f"Создаю fastapi приложение {self.name}")
            self.requirements.add("fastapi")
            self.requirements.add("SQLAlchemy")
            self.requirements.add("alembic")
            self.copy_file('app/main_fastapi.py', 'app/main.py')
            self.copy_folder("app/utils")
            self.copy_folder("app/routers")
            self.copy_folder("app/db")
            os.makedirs("app/services")
        else:
            self.copy_file('app/main_sample.py')
            logger.info(f'Создан проект {self.name}.')
        if self.namespace.get("logs"):
            self.requirements.add('loguru')
        create_readme(self.name)
        self.copy_folder('.vscode')

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
        self.requirements.add('pydantic-settings')
        os.makedirs('app/config')
        self.copy_file("app/config/__init__.py")
        self.copy_file("config.ini")
        if self.namespace.get("fastapi"):
            self.copy_file("app/config/config_fastapi.py",
                           "app/config/config.py")
        elif self.namespace.get("telebot"):
            self.copy_file("app/confgi/config_telebot.py",
                           "app/config/congig.py")
        else:
            self.copy_file("app/config/config_sample.py",
                           "app/config/config.py")
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
        self.requirements.add('pytest-mock')
        logger.info(f'Созданы заготовки под тесты')

    @check_atribute('logs')
    def create_logs(self):
        os.mkdir('logs')
        if self.namespace.get("telebot"):
            self.requirements.add("telebot")
            self.copy_file('app/config/logs_telebot.py', 'app/config/logs.py')
        else:
            self.copy_file("app/config/logs.py")
        logger.info(f'Добавлен файл app/config/logs.py')

    @check_atribute('name')
    def finish(self):
        if self.namespace.get("git"):
            subprocess.run(['git', 'add', '.'])
            logger.warning("You must start command `git commit`")
        subprocess.run(['code', '.'])
