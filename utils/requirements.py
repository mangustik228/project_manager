
import subprocess
from loguru import logger


class RequirementsManager:
    def __init__(self, venv):
        self.libs = []
        self.venv = venv

    def add(self, other: str):
        if not isinstance(other, str):
            raise TypeError('Либа должна передаваться строкой')
        self.libs.append(other)

    def install(self):
        if not self.venv:
            return
        logger.info(
            f'Библиотеки, которые будут устанавливаться: {self.libs}')
        command = ['venv/bin/pip', 'install'] + self.libs
        subprocess.run(command)
        output = subprocess.check_output(['venv/bin/pip', 'freeze'])
        with open('requirements.txt', 'w') as file:
            file.write(output.decode('utf-8'))
