from loguru import logger
from PyInquirer import prompt, style_from_dict, Token

CUSTOM_STYLE = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',
    Token.Answer: '#5F819D bold',
})


QUESTIONS = [
    {
        'type': 'list',
        'name': 'name',
        'message': 'Выберите один из вариантов:',
        'choices': [
            'Создать в текущей директории',
            'Ввести название проекта',
        ],
    },
    {
        'type': 'input',
        'name': 'name',
        'message': 'Введите ваше имя:',
        'when': lambda answers: answers['name'] == 'Ввести название проекта',
    },
    {
        'type': 'list',
        'name': 'fastapi',
        'message': 'Какого типа приложения создать?',
        'choices': [
            'fastapi',
            'Простое',
        ],
    },
    {
        'type': 'list',
        'name': 'git',
        'message': 'Создать репозиторий git?',
        'choices': ['ДА', 'НЕТ'],
    },
    {
        'type': 'list',
        'name': 'telebot',
        'message': 'Будет ли использоваться телебот?',
        'choices': ['ДА', 'НЕТ'],
    },
    {
        'type': 'list',
        'name': 'logs',
        'message': 'Создать заготовку для логгирования?',
        'choices': ['ДА', 'НЕТ'],
    },
    {
        'type': 'list',
        'name': 'config',
        'message': 'Добавить config/config.py, а также config.ini?',
        'choices': ['ДА', 'НЕТ'],
    },
    {
        'type': 'list',
        'name': 'venv',
        'message': 'Добавить виртуальное окружение в проекте?',
        'choices': ['ДА', 'НЕТ'],
    },
    {
        'type': 'list',
        'name': 'args',
        'message': 'Добавить парсер аргументов при запуске?',
        'choices': ['ДА', 'НЕТ'],
    },
    {
        'type': 'list',
        'name': 'env',
        'message': 'Добавить файл .env с стандартными секретами?',
        'choices': ['ДА', 'НЕТ'],
    },
    {
        'type': 'list',
        'name': 'test',
        'message': 'Установить pytest?',
        'choices': ['ДА', 'НЕТ'],
    },
    {
        'type': 'list',
        'name': 'run',
        'message': 'Установить базовый скрипт run.sh',
        'choices': ['ДА', 'НЕТ'],
    },
    {
        'type': 'list',
        'name': 'terminal',
        'message': 'Создать базовый файл terminal.ipynb',
        'choices': ['ДА', 'НЕТ'],
    },
]


class InteractiveQuestions:
    @classmethod
    def check_flag(cls, namespace):
        if namespace.interactive:
            return cls()
        else:
            return namespace

    def __init__(self) -> None:
        self.answers = prompt(QUESTIONS, style=CUSTOM_STYLE)
        if not self.answers:
            exit()

    def _get_kwargs(self):
        self.prepare_answer()
        return self.answers.items()

    def prepare_answer(self):
        for key, value in self.answers.items():
            logger.info(key, value)
            if key == "name" and value == "Создать в текущей директории":
                self.answers["name"] = False
            if key == "fastapi" and value == "Простое":
                self.answers['fastapi'] = False
            if value == "НЕТ":
                self.answers[key] = False
            if value == "ДА":
                self.answers[key] = True
            if value == "fastapi":
                self.answers["fastapi"] = True
        self.answers["full"] = False
