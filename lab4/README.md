# **Лабораторна робота №4**
---
## Послідовність виконання лабораторної роботи:
#### 1. Для ознайомлення з `Docker` звернулась до документації.
#### 2. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запустітила перевірку версії командою 
`sudo docker -v > my_work.log`, 
####виведення допомоги командою 
`sudo docker --help >> my_work.log` 
####та тестовий імедж командою 
`sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log`
####Вивід цих команд перенаправила у файл 
`my_work.log` 
####та закомітила його до репозиторію.
#### 3. `Docker` працює з Імеджами та Контейнерами. Імедж це свого роду операційна система з попередньо інстальованим ПЗ. Контейнер це запущений Імедж. Ідея роботи `Docker` дещо схожа на віртуальні машини. Спочатку створив імедж з якого буде запускатись контейнер.
#### 4. Для знайомства з `Docker` створила імедж із `Django` сайтом зробленим у попередній роботі.
1. ##### Оскільки мій проект на `Python` то і базовий імедж також потрібно вибрати відповідний. Використовую команду `docker pull python:3.8-slim` щоб завантажити базовий імедж з репозиторію. Переглядаю створеного вміст імеджа командою `docker inspect python:3.8-slim`
    ##### Перевіряю чи добре встановився даний імедж командою:
    
    ```text
    oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab4$ docker images
REPOSITORY        TAG       IMAGE ID       CREATED       SIZE
docker/whalesay   latest    6b362a9f73eb   6 years ago   247MB 
    ```
2. ##### Створила файл з іменем `Dockerfile` та скопіювала туди вміс такого ж файлу з репозиторію викладача.
    ###### Вміст файлу `Dockerfile`:
    ```text
    FROM python:3.8-slim
    
    LABEL author="Bohdan"
    LABEL version=1.0
    
    # оновлюємо систему
    RUN apt-get update && apt-get upgrade -y
    
    # Встановлюємо потрібні пакети
    RUN apt-get install git -y && pip install pipenv
    
    # Створюємо робочу папку
    WORKDIR /lab
    
    # Завантажуємо файли з Git
    RUN git clone https://github.com/BobasB/devops_course.git
    
    # Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
    WORKDIR /app
    RUN cp -r /lab/devops_course/lab3/* .
    
    # Інсталюємо всі залежності
    RUN pipenv install
    
    # Відкриваємо порт 8000 на зовні
    EXPOSE 8000
    
    # Це команда яка виконається при створенні контейнера
    ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```
3. ##### Ознайомилася із коментарями та зрозуміла структуру написання `Dockerfile`.
4. ##### Змінений`Dockerfile` файл:
    ```text
    FROM python:3.8-slim

    LABEL author="Oleksandra"
    LABEL version=1.0

    # оновлюємо систему
    RUN apt-get update && apt-get upgrade -y

    # Встановлюємо потрібні пакети
    RUN apt-get install git -y && pip install pipenv

    # Створюємо робочу папку
    WORKDIR /lab

    # Завантажуємо файли з Git
    RUN git clone https://github.com/oleksandra-yanovych/Oleksandra_Yanovych_IK_31.git

    # Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
    WORKDIR /app
    RUN cp -r /lab/Oleksandra_Yanovych_IK_31/lab3/* .

    # Інсталюємо всі залежності
    RUN pipenv install

    # Відкриваємо порт 8000 на зовні
    EXPOSE 8000

    # Це команда яка виконається при створенні контейнера
    ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```
#### 5. Створила власний репозиторій на [Docker Hub](https://cloud.docker.com/repository/registry-1.docker.io/oleksandrayanovych/lab4). Для цього залогінився у власний аккаунт на Docker Hub після чого перейшов у вкладку Repositories і далі натиснув кнопку Create new repository.
#### 6. Виконала білд (build) Docker імеджа та завантажила його до репозиторію. Для цього вказала правильну назву репозиторію та TAG. 
    ```bash
    sudo docker build -f Dockerfile -t oleksandrayanovych/lab4:django .
    docker images
    oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab4$ docker login
    Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
    Username: oleksandrayanovych
    Password: 
    WARNING! Your password will be stored unencrypted in /home/oleksandra/.docker/config.json.
    Configure a credential helper to remove this warning. See
    https://docs.docker.com/engine/reference/commandline/login/#credentials-store

    Login Succeeded

    docker push oleksandrayanovych/lab4:django
    ```
    -  [посилання на імедж](https://hub.docker.com/layers/177239812/oleksandrayanovych/lab4/django/images/sha256-d25945dd308943ba771168c2a1f250e1a9ec84875f4335a5d9a1a77a7c689bcb?context=repo)

#### 7. Для запуску веб-сайту виконала команду:
    ```bash
    docker run -it --name=django --rm -p 8000:8000 oleksandrayanovych/lab4:django
    ``` 
    - перейшла на адресу `http://127.0.0.1:8000` та переконалась що веб-сайт працює;
#### 8. Оскільки веб-сайт готовий і працює, потрібно створити ще один контейнер із програмою моніторингу нашого веб-сайту (Завдання на роботу):
    - створюю ще один Dockerfile в якому помістила програму моніторингу `Dockerfile.site`
    - виконала білд даного імеджа та дала йому тег `monitoring`; [Docker](https://hub.docker.com/layers/177240528/oleksandrayanovych/lab4/monitoring/images/sha256-66cb2a2d2dd9e8acb4e475f8973f5c46b0bd7aebd1efa03658cfbb0ff363da25?context=repo)
    - запустила два контейнери одночасно (_у різних вкладках_) та переконалась, що програма моніторингу успішно доступається до сторінок веб-сайту:
    ```bash
    docker run -it --name=django --rm -p 8000:8000 oleksandrayanovych/lab4:django
    
    docker run -it --name=monitoring --rm --net=host -v $(pwd)/server.log:/app/server.log oleksandrayanovych/lab4:monitoring
    ``` 
    - закомітила Dockerfile та результати роботи програми моніторингу запущеної з Docker контейнера 
#### 9. Після успішного виконання роботи відредагувала мій персональний _README.md_ у цьому репозиторію та створила pull request.
