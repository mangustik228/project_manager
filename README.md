# Project_manager

## Использования: 

1. Для удобного пользования, правильнее добавить в alias
    ```bash 
    # ~/.bash_aliases
    alias project_manager="path/to/interpretator /path/to/main.py"
    # bash
    . ~/.bashrc # Применяем изменения (ну можно ребутнуться...)
    ```

1. Чтоб создать проект: 

    ```bash 
    project_manager [project_name] [flags]
    ```

1. Забыл флаг: 
   ```bash 
   project_manager [-h --help]
   ```


## Инструкция для добавления: 
1. Добавление нового флага происходит в файле `config/arg_parser.py`

2. В `utils.manager` создаем функцию с декоратором `@check_atribute(...)`в который передаем название флага

3. В `main.py` вызываем соответствующий метод у `manager`



---

created: 2023-06-20 14:49  
author: Vasiliy_mangust228  
email: <a href="mailto:bacek.mangust@gmail.com">bacek.mangust@gmail.com</a>  
tg: https://t.me/mangusik228  