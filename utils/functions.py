from loguru import logger
from utils.base_manager import BaseManager
from functools import wraps


def check_atribute(name: str):
    def inner_function(func: callable):
        @wraps(func)
        def inner_function_2(*args, **kwargs):
            manager: BaseManager = args[0]
            # Используется исключающее ИЛИ
            if manager.namespace.get(name) != \
                    manager.namespace.get('full'):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error(e)
                    exit()
        return inner_function_2
    return inner_function
