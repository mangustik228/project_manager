from loguru import logger
from utils.base_manager import BaseManager


def check_atribute(name: str):
    def inner_function(func: callable):
        def inner_function_2(*args, **kwargs):
            manager: BaseManager = args[0]
            if manager.namespace.get(name) or \
                    manager.namespace.get('full'):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error(e)
                    exit()
        return inner_function_2
    return inner_function
