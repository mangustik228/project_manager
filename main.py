from loguru import logger
from config.arg_parser import get_namespace
from utils.manager import Manager
from utils.Interactive_questions import InteractiveQuestions

CONFIG_FILE = "/home/bacek/scripts/project_manager/config.ini"


def main():
    namespace = get_namespace(CONFIG_FILE)
    namespace = InteractiveQuestions.check_flag(namespace)
    manager = Manager(namespace, CONFIG_FILE)
    manager.ask_about_name()
    manager.create_new_project()
    manager.create_template()
    manager.create_env_file()
    manager.create_repo_git()
    manager.create_entrypoint()
    manager.create_config_template()
    manager.create_test_folder()
    manager.create_terminal()
    manager.create_args_parser()
    manager.create_logs()
    manager.create_venv()
    manager.requirements.install()
    manager.finish()
    logger.success(f'Проект создан. поздравляю')


if __name__ == '__main__':
    main()
