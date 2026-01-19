# FirstDjangoProject
 Проект для курса "Технологии создания интернет приложений" СПБГУПТД"

# Памятка

1) Установить Python PyCharm Git 

2) Создаем проект New Project

Прописываем location, велком скрипт не нужен, выбираем custom environment с type: "Virtualenv", проверяем что base python версия совпадает с той, которая ищется в командной строке через "python -v"
3) Команды в терминале

pip install django 

pip freeze > requirements.txt  

django-admin.exe startproject urlsite

4) Создаем конфигурациию Edit Configuration

Выбираем Питон, прописываем name, указываем версию питона, скрипт указываем manage.py, с параметром runserver, рабочая директория - имя_проекта\urlsite

5) Запускаем сервер, проверяем работоспосбность
