# **Лабораторна робота №5**
---
## Послідовність виконання лабораторної роботи:
#### 1. Для ознайомлeння з `docker-compose` звернулася до документації.
Щоб встановити `docker-compose` використав команди:
```text
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
#### 2. Ознайомилася з бібліотекою `Flask`, яку найчастіше використовують для створення простих веб-сайтів на Python.
#### 3. Моє завдання: за допомогою Docker автоматизувати розгортання веб сайту з усіма супутніми процесами. Зроблю я це двома методами: 
* за допомогою `Makefile`;
* за допомогою `docker-compose.yaml`.

#### 4. Першим розгляну метод з `Makefile`, але спочатку створю робочий проект.
#### 5. Створила папку `my_app` в якій буде знаходитись мій проект. Створила папку `tests` де будуть тести на перевірку працездатності мого проекту. Скопіювала файли `my_app/templates/index.html`, `my_app/app.py `, `my_app/requirements.txt`, `tests/conftest.py`, `tests/requirements.txt`, `tests/test_app.py` з репозиторію викладача у відповідні папки мого репозеторію. Ознайомилася із вмістом кожного з файлів. Звернула увагу на файл requirements.txt у папці проекту та тестах. Даний файл буде мітити залежності для мого проекту він містить назви бібліотек які імпортуються.
#### 6. Я спробувала чи проект є працездатним перейшовши у папку `my_app` та після ініціалізації середовища виконала команди записані нижче:
```text
sudo pipenv --python 3.8
sudo pipenv install -r requirements.txt
sudo pipenv run python app.py
```
1. Так само я ініціалузувала середовище для тестів у іншій вкладці шелу та запустила їх командою `sudo pipenv run pytest test_app.py --url http://localhost:5000` але спочатку треба перейти в папку `tests`:
    ```text
    oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab5/tests$ sudo pipenv run pytest test_app.py --url http://localhost:5000
================================ test session starts =================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/oleksandra/TPIS/Oleksandra_Yanovych_IK_31/lab5/tests
collected 4 items                                                                    

test_app.py ..FF                                                               [100%]

====================================== FAILURES ======================================
_____________________________________ test_logs ______________________________________

url = 'http://localhost:5000'

    def test_logs(url):
        response = requests.get(url + '/logs')
>       assert 'My Hostname is:' in response.text, 'Logs do not have Hostname'
E       AssertionError: Logs do not have Hostname
E       assert 'My Hostname is:' in '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n  "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n  ...en(\'logs/app.log\', \'r\') as log:\nFileNotFoundError: [Errno 2] No such file or directory: \'logs/app.log\'\n\n-->\n'
E        +  where '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n  "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n  ...en(\'logs/app.log\', \'r\') as log:\nFileNotFoundError: [Errno 2] No such file or directory: \'logs/app.log\'\n\n-->\n' = <Response [500]>.text

test_app.py:27: AssertionError
___________________________________ test_main_page ___________________________________

url = 'http://localhost:5000'

    def test_main_page(url):
        response = requests.get(url)
>       assert 'You are at main page.' in response.text, 'Main page without text'
E       AssertionError: Main page without text
E       assert 'You are at main page.' in '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n  "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n  ...)\nredis.exceptions.ConnectionError: Error -3 connecting to redis:6379. Temporary failure in name resolution.\n\n-->\n'
E        +  where '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n  "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n  ...)\nredis.exceptions.ConnectionError: Error -3 connecting to redis:6379. Temporary failure in name resolution.\n\n-->\n' = <Response [500]>.text

test_app.py:32: AssertionError
============================== short test summary info ===============================
FAILED test_app.py::test_logs - AssertionError: Logs do not have Hostname
FAILED test_app.py::test_main_page - AssertionError: Main page without text
============================ 2 failed, 2 passed in 0.89s =============================
oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab5/tests$ 
    ```
2. Звернула увагу, що в мене автоматично створюються файли `Pipfile` та `Pipfile.lock`, а також на хост машині буде створена папка `.venv`. Після зупинки проекту видалила їх.
3. Перевірила роботу сайту перейшовши головну сторінку. Сайт не працює бо відсутній `redis`.

#### 7. Видалила файли які постворювались після тестового запуску. Щоб моє середовище було чистим, все буде створюватись і виконуватись всередині Docker. Створила файли `Dockerfile.app`, `Dockerfile.tests` та `Makefile` який допоможе автоматизувати процес розгортання.
#### 8. Скопіювала вміст файлів `Dockerfile.app`, `Dockerfile.tests` та `Makefile` з репозиторію викладача та ознайомився із вмістом `Dockerfile` та `Makefile` та його директивами. 
Вміст файла `Dockerfile.app`:
```text
FROM python:3.8-slim
LABEL author="Oleksandra Yanovych"

# оновлюємо систему та встановлюємо потрібні пакети
RUN apt-get update \
    && apt-get upgrade -y\
    && apt-get install git -y\
    && pip install pipenv

WORKDIR /app

# Копіюємо файл із списком пакетів які нам потрібно інсталювати
COPY my_app/requirements.txt ./
RUN pipenv install -r requirements.txt

# Копіюємо наш додаток
COPY my_app/ ./

# Створюємо папку для логів
RUN mkdir logs

EXPOSE 5000

ENTRYPOINT pipenv run python app.py
```
Вміст файла `Dockerfile.tests`:
```text
FROM python:3.8-slim
LABEL author="Oleksandra Yanovych"

# оновлюємо систему та встановлюємо потрібні пакети
RUN apt-get update \
    && apt-get upgrade -y\
    && apt-get install git -y\
    && pip install pipenv

WORKDIR /tests

# Копіюємо файл із списком пакетів які нам потрібно інсталювати
COPY tests/requirements.txt ./
RUN pipenv install -r requirements.txt

# Копіюємо нашого проекту
COPY tests/ ./

ENTRYPOINT pipenv run pytest test_app.py --url http://app:5000
```
Вміст файла `Makefile`:
```text
STATES := app tests
REPO := oleksandrayanovych/lab4

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

run:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app:
	@docker run --rm -it --name test --net=appnet $(REPO):tests
	
docker-prune:
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force
```
Дерективи `app` та `tests`:
Створення імеджів для сайту та тесту відповідно.
Деректива `run`:
Запускає сторінку сайту.
Деректива `test-app`:
Запуск тесту сторінки.
Деректива `docker-prune`:
Очищення іміджів, контейнера і інших файлів без тегів.
#### 9. Для початку, використовуючи команду `sudo make app` створіть Docker імеджі для додатку та для тестів `sudo make tests`. Теги для цих імеджів є з моїм Docker Hub репозиторієм. Запустив додаток командою `sudo make run` та перейшовши в іншу вкладку шелу запустіть тести командою `sudo make test-app`.
Запуск сайту
```text
oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab5$ sudo make run
845ff6de24d78f02fdda307d1bffd879075d2f1c08609ffa53dc015d6ff8e7d1
Unable to find image 'redis:latest' locally
latest: Pulling from library/redis
e5ae68f74026: Pull complete 
37c4354629da: Pull complete 
b065b1b1fa0f: Pull complete 
6954d19bb2e5: Pull complete 
6333f8baaf7c: Pull complete 
f9772c8a44e7: Pull complete 
Digest: sha256:2f502d27c3e9b54295f1c591b3970340d02f8a5824402c8179dcd20d4076b796
Status: Downloaded newer image for redis:latest
e378c761e437630be910a6cbdc0d72e0b6266425a02f631ad0665f963386cd3d
f4298a08c975eb047b6640ec37fab6fa49e26ca5a8c551d9ac372bfef27a7c8b

```
Проходження тесту:
```text
oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab5$ sudo make test-app
============================= test session starts ==============================
platform linux -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /tests
collected 4 items                                                              

test_app.py ....                                                         [100%]

============================== 4 passed in 0.87s ===============================
```

#### 10. Зупинила проект натиснувши Ctrl+C та почистила всі ресурси `Docker` за допомогою `make`.
```text
oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab5$ sudo make docker-prune
f4298a08c975
e378c761e437
687e03b2c50c
87dad4c2fba5
Total reclaimed space: 0B
Deleted Volumes:
55e4c54e2321c9b58da223055fcc52a57585bbadb4f33d6ddf3d2ffa1f6d060e

Total reclaimed space: 0B
Deleted Networks:
appnet

Total reclaimed space: 0B

```

#### 11. Створила директиву `docker-push` в Makefile для завантаження створених імеджів у мій Docker Hub репозиторій.
Деректива `docker-push`:
```text
docker-push:
	@docker login \
	&& docker push $(REPO):app \
	&& docker push $(REPO):tests
```

#### 12. Видалила створені та закачані імеджі. Команда `docker images` виводить пусті рядки. Створила директиву в Makefile яка автоматизує процес видалення моїх імеджів.
Деректива `images-delete`:
```text
images-delete:
	@docker rmi $$(docker images -q)
```
Запуск:
```text
oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab5$ sudo docker images
REPOSITORY                TAG          IMAGE ID       CREATED          SIZE
oleksandrayanovych/lab4   tests        407b286c5bef   6 minutes ago    305MB
oleksandrayanovych/lab4   app          3256e6858468   10 minutes ago   302MB
redis                     latest       aea9b698d7d1   2 days ago       113MB
oleksandrayanovych/lab4   monitoring   0df47fd5a6a8   3 weeks ago      339MB
oleksandrayanovych/lab4   django       8b58c4667f83   3 weeks ago      339MB
python                    3.8-slim     214d62795dbb   5 weeks ago      122MB
docker/whalesay           latest       6b362a9f73eb   6 years ago      247MB
oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab5$ sudo make images-delete
Untagged: oleksandrayanovych/lab4:tests
Deleted: sha256:407b286c5befe09e857433cbd5b7f53400a8eb50283e5ded8caf6e03601c77c4
Deleted: sha256:ceee0171dc886f40808ecb6835fdf355f8558174217b76d781504358d552138e
Deleted: sha256:8c97f1c98178a2a3bb66f2bd0e96b5df3cdb942d62ed2463e2b723aea4cd295b
Deleted: sha256:1d3f667b018a57c869a221b30171614d06465cf0c27756f7bf66f61d294d3624
Deleted: sha256:0be5f8aa46c9b10f0f26b8815695fda782bcd9597d6b1771dc1ef9f7f5db83ec
Deleted: sha256:c33f0b98bb680578e2fc2e1eb6d0b9672c93c29672dba6c514c85941a410dbde
Deleted: sha256:911c178023d6367639a7ec7dfa0e9d2063e9ce7d28eb40f87e8efda207deaa58
Deleted: sha256:aee941a0274e99b76c0721a3e9c9b35320bcc22b3ef34b77c83b55401a142e29
Deleted: sha256:c75eda4c45bc6909e1198be9804f6cac9f54d2c5dee076ff73380cc134fb8b9a
Untagged: oleksandrayanovych/lab4:app
Deleted: sha256:3256e6858468d13975ee43be6e6da5982e22c58976f98ebb948a626f265c78cd
Deleted: sha256:bd4fce1f0096142748b1667c89ec9c80efbdc68a4d4a1fe4aa1b3930d6ea1279
Deleted: sha256:ccc43a900fd5dfd91c5e412c6ac879d3de074a7aa9e3e6c9081abe7ae79f6807
Deleted: sha256:5703d65f8e70d70458d449680ccd00becdb66f2f18e0d3e1ac6dfd25f3f58a15
Deleted: sha256:4afc6a3182f778eed504c905578aedb1817b85457fb049a2423a3c324850ebac
Deleted: sha256:23637eb33ff425e7806e1cc90010339e1a71570dd23288ee2e415def3ba87287
Deleted: sha256:03ccbde995f43474ea0474471616f6ca51de01dc1c7b1a542fffe29854d2a345
Deleted: sha256:93a3476e8a985d384fa161292a7b981d6df1d4d58c0143f2585743ab0b35797d
Deleted: sha256:dfdad1263fa4192f039b52aabad1f09af92d79cee1bde9a7639a6ffc901b28e4
Deleted: sha256:effc61ae83d1ccf85c980bdc78a7de3bc3770f6013a99e96671da343a07fad77
Deleted: sha256:fd62f579f826221a7c3e6ca308f3ad62358ab6da164892233f32d57078a2c43a
Deleted: sha256:78f152e194aa827b30daa36eeccade08c17697008b28f7271afb89aa95fa1243
Deleted: sha256:32f65e4a1994f8a5417df9c121e2fd8f367f1fc2a0b5471ec10dd979214187d0
Deleted: sha256:12f57a42801064a0fe44600511da5eaddfd0caab12454e9858d212ca1de00953
Deleted: sha256:80afe992a7cd092530950e4283eb9f331d97a82aacf93f907068796e2e92e37a
Untagged: redis:latest
Untagged: redis@sha256:2f502d27c3e9b54295f1c591b3970340d02f8a5824402c8179dcd20d4076b796
Deleted: sha256:aea9b698d7d1d2fb22fe74868e27e767334b2cc629a8c6f9db8cc1747ba299fd
Deleted: sha256:beb6c508926e807f60b6a3816068ee3e2cece7654abaff731e4a26bcfebe04d8
Deleted: sha256:a5b5ed3d7c997ffd7c58cd52569d8095a7a3729412746569cdbda0dfdd228d1f
Deleted: sha256:ee76d3703ec1ab8abc11858117233a3ac8c7c5e37682f21a0c298ad0dc09a9fe
Deleted: sha256:60abc26bc7704070b2977b748ac0fd4ca94b818ed4ba1ef59ca8803e95920161
Deleted: sha256:6a2f1dcfa7455f60a810bb7c4786d62029348f64c4fcff81c48f8625cf0d995a
Deleted: sha256:9321ff862abbe8e1532076e5fdc932371eff562334ac86984a836d77dfb717f5
Untagged: oleksandrayanovych/lab4:monitoring
Untagged: oleksandrayanovych/lab4@sha256:66cb2a2d2dd9e8acb4e475f8973f5c46b0bd7aebd1efa03658cfbb0ff363da25
Deleted: sha256:0df47fd5a6a8aa0fa00b4eee337f6ee56b6cf5500cf803b9f82b37ae5ab3dde4
Untagged: oleksandrayanovych/lab4:django
Untagged: oleksandrayanovych/lab4@sha256:d25945dd308943ba771168c2a1f250e1a9ec84875f4335a5d9a1a77a7c689bcb
Deleted: sha256:8b58c4667f83918d232b5c4fd4a01967c29c2ff7df76e9572f242027b2597717
Deleted: sha256:d13852d31da07425b785b5dca2125bee66adc944478280bdf5dd000cdd9e71e6
Deleted: sha256:ce83e735dd64f4cd2b259134cdefe5c1d52fc47dc1cea480e30618de620709d2
Deleted: sha256:efb2578f861f6eb0cba713d4c9b34363289ccba93409b1a419ef3978eb701a6f
Deleted: sha256:5b270dcda53a5237942b33f3f4efeca7bb9cce4aae317a395da961988c97e6bd
Deleted: sha256:42c5ad94c834af1c9bc15b69ff042456fd59278491f1f763219297507e99e541
Deleted: sha256:d369fcf2432c1509b74824dc83ee2fd9bfc34439613eac5e6e3fb66a3009989d
Deleted: sha256:59815e42ea4cd5b2bc3fcfdff45b0565089244e83d88ad8755f6d61a066c1b61
Deleted: sha256:edfc7de24e9d9f69df8278f09b4181d4fbb2883d4f428ba5360be27ba318d833
Deleted: sha256:4689445793b46e875a2ee81ad0fc05b01eb863f70d2de8d66c95dcc949385bbc
Deleted: sha256:99bf2d5ef1bd97a8970b7e80c06b6d52af6d5b82740a5050d336fee4a1444f19
Deleted: sha256:2f942ddb252f22f4dcc0b7fdd00efe9eda637b5ebb0b1ea11a4952e82c2a3934
Deleted: sha256:031d8965759e956d1146a061bed991189512c8d9981f10e342e32b8e0f69bf83
Deleted: sha256:bc3c46cc18ea86a60abc7e9df3296ee595d37152a17d881b440bb3fbaecd0206
Deleted: sha256:38c403c2d9b4b9c737aaccac9f28518accfd9ba2ec94204e5ed8d8fad7d0cf09
Deleted: sha256:f21a30124725f555d1d00101bcc30f3fd7c8425389da7cf05026873fe9e75188
Deleted: sha256:edd449c36a79cba1fd007c50c081af3107f097391464780a0137634bf9ce2dc4
Deleted: sha256:9f4376347e7155586d36fc45d36da2a6581839b05294e2db6a9db2e5af394ee4
Untagged: python:3.8-slim
Untagged: python@sha256:d31a1beb6ccddbf5b5c72904853f5c2c4d1f49bb8186b623db0b80f8c37b5899
Deleted: sha256:214d62795dbbd487ac169bb05c944ca76c11c7b5b5f0277509747824db906992
Deleted: sha256:2072f4f0804d38c63805f550eac93e494b408ad8982e27a464fecb7d5e5cda58
Deleted: sha256:a766fa6d3c77dd3b9ced55be33949a1e74b10a612020e1811e8b01cd914fe0db
Deleted: sha256:9dcdcbc891c78c6c76cf09888373a78f9aafc223bfc0325ddff8a83e3b7bbe0a
Deleted: sha256:e3b8dc3b414c4a2cedba49b7442af204935d902b3338dbebdd1267c36fcc219d
Deleted: sha256:e8b689711f21f9301c40bf2131ce1a1905c3aa09def1de5ec43cf0adf652576e
Untagged: docker/whalesay:latest
Untagged: docker/whalesay@sha256:178598e51a26abbc958b8a2e48825c90bc22e641de3d31e18aaf55f3258ba93b
Deleted: sha256:6b362a9f73eb8c33b48c95f4fcce1b6637fc25646728cf7fb0679b2da273c3f4
Deleted: sha256:34dd66b3cb4467517d0c5c7dbe320b84539fbb58bc21702d2f749a5c932b3a38
Deleted: sha256:52f57e48814ed1bb08a651ef7f91f191db3680212a96b7f318bff0904fed2e65
Deleted: sha256:72915b616c0db6345e52a2c536de38e29208d945889eecef01d0fef0ed207ce8
Deleted: sha256:4ee0c1e90444c9b56880381aff6455f149c92c9a29c3774919632ded4f728d6b
Deleted: sha256:86ac1c0970bf5ea1bf482edb0ba83dbc88fefb1ac431d3020f134691d749d9a6
Deleted: sha256:5c4ac45a28f91f851b66af332a452cba25bd74a811f7e3884ed8723570ad6bc8
Deleted: sha256:088f9eb16f16713e449903f7edb4016084de8234d73a45b1882cf29b1f753a5a
Deleted: sha256:799115b9fdd1511e8af8a8a3c8b450d81aa842bbf3c9f88e9126d264b232c598
Deleted: sha256:3549adbf614379d5c33ef0c5c6486a0d3f577ba3341f573be91b4ba1d8c60ce4
Deleted: sha256:1154ba695078d29ea6c4e1adb55c463959cd77509adf09710e2315827d66271a
 
```

#### 13. Перейшла до іншого варіанту з використанням `docker-compose.yaml`. Для цього створила даний файл у кореновій папці проекту та заповнила вмістом з прикладу. Проект який я буду розгортити за цим варіантом трохи відрізняється від першого тим що у нього зявляється дві мережі: приватна і публічна.
Файл `docker-compose.yaml`:
```text
version: '3.8'
services:
  hits:
    build:
      context: .
      dockerfile: Dockerfile.app
    image: oleksandrayanovych/lab4:compose-app
    container_name: app
    depends_on:
      - redis
    networks:
      - public
      - secret
    ports:
      - 80:5000
    volumes:
      - hits-logs:/hits/logs
  tests:
    build:
      context: .
      dockerfile: Dockerfile.tests
    image: oleksandrayanovychlab4:compose-tests
    container_name: tests
    depends_on:
      - hits
    networks:
      - public
  redis:
    image: redis:alpine
    container_name: redis
    volumes:
      - redis-data:/data
    networks:
      - secret
volumes:
  redis-data:
    driver: local
  hits-logs:
    driver: local

networks:
  secret:
    driver: bridge
  public:
    driver: bridge
```

#### 14. Перевірила чи `Docker-compose` встановлений та працює у моїй системі, а далі просто запускаю `docker-compose`:
```text
docker-compose --version
sudo docker-compose -p lab5 up
```
```text
oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab5$ docker-compose --version
docker-compose version 1.29.2, build 5becea4c
```

#### 15. Перевірила чи працює веб-сайт. Дана сторінка відображається за адресою `http://172.19.0.2:5000/`
#### 16. Перевірила чи компоуз створив докер імеджі. Всі теги коректні і назва репозиторія вказана коректно:
```text
oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/lab5$ sudo docker images
REPOSITORY                TAG             IMAGE ID       CREATED          SIZE
oleksandrayanovychlab4    compose-tests   9f9b6c76f9dd   59 seconds ago   301MB
oleksandrayanovych/lab4   compose-app     f64dc16dd05f   2 minutes ago    299MB
python                    3.8-slim        1e46b5746c7c   2 days ago       122MB
redis                     alpine          3900abf41552   5 days ago       32.4MB

```

#### 17. Зупинила проект натиснувши `Ctrl+C` і почистітила ресурси створені компоуз командою `docker-compose down`.

#### 18. Завантажила створені імеджі до Docker Hub репозиторію за допомого команди `sudo docker-compose push`.

#### 19. Що на Вашу думку краще використовувати `Makefile` чи `docker-compose.yaml`? - На мою думку `Makefile` при використанні більш інтуїтивно зрозумілий, адже можна в ньому побачити які команди запускаються, але і в одночас треба знати які команди використовувати. На рахунок `docker-compose.yaml` він менш зрозумілий і там не показано команди які потрібно запустити а лише вказано що потрібно запусти, підклучити чи збілдити і користувача не хвилює як воно це робить. Як для мене мені обидва методи добрі.

#### 20. (Завдання) Оскільки Ви навчились створювати docker-compose.yaml у цій лабораторній то потрібно:
- Cтворила `docker-compose.yaml` для лабораторної №4. Компоуз повинен створити два імеджі для `Django` сайту та моніторингу, а також їх успішно запустити.
Файлик `docker-compose.yaml`:
```text
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: oleksandrayanovych/lab4:compose-jango
    container_name: django
    networks:
      - public
    ports:
      - 8000:8000
  monitoring:
    build:
      context: .
      dockerfile: Dockerfile.site
    image: oleksandrayanovych/lab4:compose-monitoring
    container_name: monitoring
    network_mode: host

networks:
  public:
    driver: bridge
```
#### 21. Після успішного виконання роботи я відредагувала свій `README.md` у цьому репозиторію та створила pull request.
