from configparser import ConfigParser
from typing import NamedTuple
import sys
import argparse


def _get_version() -> str:
    _config_ini = ConfigParser()
    _config_ini.read('config.ini')
    return _config_ini.get('default', 'version')


class _Args(NamedTuple):
    fp: str
    debug: bool


def get_namespace() -> _Args:
    parser = argparse.ArgumentParser(
        prog='',  # Название программы
        description='',  # Описание
        epilog='Vasiliy mangust 2023'
    )

    version = _get_version()

    # параметр nargs:
    # "+" - 1 и более аргументов
    # "?" - 0 или 1 аргумент
    # Если не указывать: то 1

    parser.add_argument('name', nargs='?', default=False,
                        help='Название нового проекта')

    parser.add_argument('-d', '--debug', action="store_true",
                        help='Инициализировать репозиторий и создать .gitignore')

    parser.add_argument('--version', action="version",
                        help='Вывести номер версии', version=f'%(prog)s {version}')

    namespace = parser.parse_args(sys.argv[1:])
    return namespace
