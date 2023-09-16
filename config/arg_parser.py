import argparse
from configparser import ConfigParser


def _get_version(config_path) -> str:
    _config_ini = ConfigParser()
    _config_ini.read(config_path)
    return _config_ini.get('default', 'version')


def get_namespace(config_path: str):
    version = _get_version(config_path)
    parser = argparse.ArgumentParser(
        prog='Project manager',  # Название программы
        description='Предназначено для создания проектов и добавления стандартных файлов в существующие проекты. Если стоит флаг -f то с остальными ключами происходит инверсия',
        epilog='Vasiliy mangust 2023'
    )

    # параметр nargs:
    # "+" - 1 и более аргументов
    # "?" - 0 или 1 аргумент
    # Если не указывать: то 1

    # параметр action
    # по умолчанию "store" - будет брать значение за флагом
    # при "store_const" будет брать из аргумента const
    # при "store_true"|"store_false" тоже самое что и store_const, только не надо указывать const & default

    parser.add_argument('name', nargs='?', default=False,
                        help='Название нового проекта')

    parser.add_argument('-g', '--git', action="store_true",
                        help='Инициализировать репозиторий и создать .gitignore и первый коммит')

    parser.add_argument('-l', '--logs', action="store_true",
                        help="Создать заготовку для логгирования")

    parser.add_argument('-c', '--config', action="store_true",
                        help='Добавить config/config.py, а также config.ini')

    parser.add_argument('-v', '--venv', action="store_true",
                        help='Добавить виртуальное окружение в проекте')

    parser.add_argument('-a', '--args', action="store_true",
                        help='Добавить парсер аргументов при запуске')

    parser.add_argument('-e', '--env', action="store_true",
                        help='Добавить файл .env с стандартными секретами')

    parser.add_argument('-t', '--test', action="store_true",
                        help='Добавить файл pytest.ini')

    parser.add_argument('-f', '--full', action="store_true",
                        help='Создать все что только можно')

    parser.add_argument('--version', action="version",
                        help='Вывести номер версии', version=f'%(prog)s {version}')

    namespace = parser.parse_args()
    return namespace
