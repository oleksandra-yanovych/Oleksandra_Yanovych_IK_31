# **Лабораторна робота №2**
---
## Послідовність виконання лабораторної роботи:
#### 1. Створюю папку ***Lab_2*** в якій ствоюю ***README.md***.
#### 2. За допомогою пакетного менеджера ***PIP*** інсталювала ***pipenv*** та створила ізольоване середовище для ***Python***. Використовуючи команди:
```text
sudo pip install pipenv
sudo pipenv --python 3.7
sudo pipenv shell
```
Ознайомилась з командаю `pipenv -h` і виконала її.
```text
(Lab2) oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/Lab2$ pipenv -h
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --completion                    Output completion (to be executed by the
                                  shell).

  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.

  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.

  --three / --two                 Use Python 3/2 when creating virtualenv.
  --clear                         Clears caches (pipenv, pip, and pip-tools).
                                  [env var: PIPENV_CLEAR]

  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check      Checks for PyUp Safety security vulnerabilities and against PEP
             508 markers provided in Pipfile.

  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.

  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  scripts    Lists scripts in current environment config.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Uninstalls a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
 
```
#### 3. Встановила бібліотеку ***requests*** в моєму середовищі. Ця бібліотека дозволяє створювати HTTP запити до заданих Web сторінок. А також встановила бібліотеку ***ntplib*** яка працює з часом.
Використав команди:
```text
pipenv install requests
pipenv install ntplib
```
#### 4. Створила ***app.py*** файл. Скопіювала код програми із репозиторію викладача до себе. Для кращого розуміння програми ознайомилась з ***Python tutorial***.
#### 5. Запускаю програму за допомогою команди `sudo python app.py`. 
Результат виконання:
```text
(Lab2) oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/Lab2$ python app.py
========================================
Результат без параметрів: 
No URL passed to function
========================================
Результат з правильною URL: 
Time is:  06:40:42 PM
Date is:  10-29-2021
success
```
#### 6. Встановила бібліотеку `pytest` за допомогою команди `pipenv install pytest`. Для кращого розуміння ознайомилася з документацією ***pytest***.
#### 7. Створила папку ***tests***, в якій створила файли ***tests.py*** і ***__init__.py***. Скопіювала код програми із репозиторію викладача до себе. Запускаю програму за допомогою команди `pytest tests/tests.py`. 
Виконанння програми:
```text
(Lab2) oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/Lab2/tests$ pytest tests.py
============================= test session starts =============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/oleksandra/TPIS/Oleksandra_Yanovych_IK_31/Lab2/tests
collected 5 items                                                             

tests.py .....                                                          [100%]

============================== 5 passed in 1.00s ==============================
```
#### 8. ❗ (Захист) У програмі дописала функцію яка буде перевіряти час доби AM/PM та відповідно друкувати: Доброго дня/ночі.
Код програми:
```python
def home_work(time = datetime.today().strftime("%H:%M %p")):
    msg = ""
    if "AM" in time:
    	msg = "Доброго дня!"
    elif "PM" in time:
    	msg = "Доброї ночі!"
    return msg
```
#### 9. ❗ (Захист) Написала тест що буде перевіряти правильність виконання моєї функції.
Код тесту:
```python
def test_home_work(self):
    self.assertEqual(home_work("07:03 PM"), "Доброї ночі!")
    self.assertEqual(home_work("07:30 AM"), "Доброго дня!")
```
Виконання тесту:
```text
(Lab2) oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/Lab2$ pytest tests/tests.py
============================= test session starts =============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/oleksandra/TPIS/Oleksandra_Yanovych_IK_31/Lab2
collected 5 items                                                             

tests/tests.py .....                                                    [100%]

============================== 5 passed in 1.06s ==============================

```
#### 10. Перенаправляю результат виконання тестів у файл ***results.txt*** за допомогою команди `pytest tests/tests.py > results.txt`, а також додаю результат виконання програми у кінець цього ж файл за допомогою команди `python app.py >> results.txt`.
#### 11. Зробила коміт із змінами до свого репозиторію.
#### 12. Заповнила ***Makefile*** необхідними командами (bash) для повної автоматизації процесу СІ мого проекту:
Вміст ***Makefile***:
```text
.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Installing pipenv and dependencies."
	@echo "--------------------------------------------"
	@echo " "
	sudo pip install pipenv
	sudo pipenv --python 3.8
	sudo pipenv install requests
	sudo pipenv install ntplib
	sudo pipenv install pytest

test:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Start tests."
	@echo "--------------------------------------------"
	@echo " "
	sudo pipenv run pytest tests/tests.py > results.txt

run:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Run Python app."
	@echo "--------------------------------------------"
	@echo " "
	sudo pipenv run python3 app.py >> results.txt

deploy:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Adding and Committing results.txt to git."
	@echo "--------------------------------------------"
	@echo " "
	git add results.txt
	git commit -m "Automatic commit by MakeFile"
	git push
```
#### 13. Закомітила зміни в Makefile до власного репозиторію.
#### 14. Склонувала ***git*** репозиторій на віртуальну машину Ubuntu. Перейшла у папку з  лабораторною роботою та запустила ***Makefile*** файл за допомогою команди `make all`.
Результатом виконання цієї команди є створено ізольоване середовище, виконано тести, запущено програму та закомічено файл у git репозеторій.
```text
oleksandra@oleksandra-VirtualBox:~/TPIS/Oleksandra_Yanovych_IK_31/Lab2$ make all
 
--------------------------------------------
Installing pipenv and dependencies.
--------------------------------------------
 
sudo pip install pipenv
[sudo] пароль до oleksandra: 
Requirement already satisfied: pipenv in /usr/local/lib/python3.8/dist-packages (2021.5.29)
Requirement already satisfied: certifi in /usr/lib/python3/dist-packages (from pipenv) (2019.11.28)
Requirement already satisfied: pip>=18.0 in /usr/lib/python3/dist-packages (from pipenv) (20.0.2)
Requirement already satisfied: virtualenv-clone>=0.2.5 in /usr/local/lib/python3.8/dist-packages (from pipenv) (0.5.7)
Requirement already satisfied: virtualenv in /usr/local/lib/python3.8/dist-packages (from pipenv) (20.9.0)
Requirement already satisfied: setuptools>=36.2.1 in /usr/lib/python3/dist-packages (from pipenv) (45.2.0)
Requirement already satisfied: distlib<1,>=0.3.1 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (0.3.3)
Requirement already satisfied: backports.entry-points-selectable>=1.0.4 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (1.1.0)
Requirement already satisfied: filelock<4,>=3.2 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (3.3.2)
Requirement already satisfied: six<2,>=1.9.0 in /usr/lib/python3/dist-packages (from virtualenv->pipenv) (1.14.0)
Requirement already satisfied: platformdirs<3,>=2 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (2.4.0)
sudo pipenv --python 3.8
Creating a virtualenv for this project...
Pipfile: /home/oleksandra/TPIS/Oleksandra_Yanovych_IK_31/Lab2/Pipfile
Using /usr/bin/python3.8 (3.8.10) to create virtualenv...
⠸ Creating virtual environment...created virtual environment CPython3.8.10.final.0-64 in 4819ms
  creator CPython3Posix(dest=/root/.local/share/virtualenvs/Lab2-0mIRC96O, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/root/.local/share/virtualenv)
    added seed packages: pip==21.3.1, setuptools==58.3.0, wheel==0.37.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment! 
Virtualenv location: /root/.local/share/virtualenvs/Lab2-0mIRC96O
sudo pipenv install requests
Installing requests...
Adding requests to Pipfile's [packages]...
✔ Installation Succeeded 
Installing dependencies from Pipfile.lock (18d437)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 9/9 — 00:00:34
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
sudo pipenv install ntplib
Installing ntplib...
Adding ntplib to Pipfile's [packages]...
✔ Installation Succeeded 
Installing dependencies from Pipfile.lock (18d437)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
sudo pipenv install pytest
Installing pytest...
Adding pytest to Pipfile's [packages]...
✔ Installation Succeeded 
Installing dependencies from Pipfile.lock (18d437)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
 
--------------------------------------------
Start tests.
--------------------------------------------
 
sudo pipenv run pytest tests/tests.py > results.txt
 
--------------------------------------------
Run Python app.
--------------------------------------------
 
sudo pipenv run python3 app.py >> results.txt
 
--------------------------------------------
Adding and Committing results.txt to git.
--------------------------------------------
 
git add results.txt
git commit -m "Automatic commit by MakeFile"
[master 0bd4a1b] Automatic commit by MakeFile
 1 file changed, 2 insertions(+), 2 deletions(-)
git push
Enumerating objects: 7, виконано.
Підрахунок об’єктів: 100% (7/7), виконано.
Стиснення об’єктів: 100% (4/4), виконано.
Запис об’єктів: 100% (4/4), 428 bytes | 428.00 KiB/s, виконано.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:oleksandra-yanovych/Oleksandra_Yanovych_IK_31.git
   b269bf2..0bd4a1b  master -> master
```

