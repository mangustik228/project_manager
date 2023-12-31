
from datetime import datetime
import os

from loguru import logger


def create_readme(file_name):
    if os.path.exists("README.md"):
        logger.warning('README.md doesn\'t created. It was exists')
    with open('README.md', 'w', encoding='utf-8') as file:
        empty = "\n"
        file.write(f'''### {file_name}{empty * 25}
---

created: {datetime.now().strftime('%Y-%m-%d %H:%M')}
author: Vasiliy_mangust228
email: <a href="mailto:bacek.mangust@gmail.com">bacek.mangust@gmail.com</a>
tg: https://t.me/mangusik228
''')
