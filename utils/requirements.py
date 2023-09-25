import subprocess
from loguru import logger
from tqdm import tqdm


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
        command = ['venv/bin/pip', 'install'] + self.libs
        logger.info(f'Будет установлено {len(self.libs)} библиотек: ')
        for lib in self.libs:
            with tqdm(total=1, desc=f'installing {lib:20}', position=0, unit_divisor=5) as pbar:
                command = ["venv/bin/pip", "install", lib]
                status = subprocess.run(command, stdout=subprocess.PIPE)
                if status.returncode:
                    logger.error(f'Problem with install {lib}')
                pbar.update(1)

        output = subprocess.check_output(['venv/bin/pip', 'freeze'])
        with open('requirements.txt', 'w') as file:
            file.write(output.decode('utf-8'))
