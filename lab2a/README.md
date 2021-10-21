# **Лабораторна робота №2А**
---
## Послідовність виконання лабораторної роботи:
#### 1. Переглянула офіційну документацію для ***Python***.
#### 2. Створюю файл ***lab2.1.py*** для виконання базових прикладів.
1. Виводжу вбудованні константи за допомогою команд:

    ```python
    print("Перша константа: ", True)
    print("Друга константа: ", False)
    print("Третя константа: ", None)
    ```
1. Виводжу результат роботи вбудованих функцій за допомогою команд:
   ```python
   print("Число 7 в двійковій системі числення дорівнює: ", bin(7))
   print("7 в 4 степені дорівнює: ", pow(7,4))
   print("Мінімальне число з чисел 8,3,1,6,17 :",min(8,3,1,6,1))
    ```
1. Виводжу результат роботи циклу і розгалужень за допомогою команд:
    ```python
    x= [3 for i in range(17)]
    print("Виведення 17 трійок з масиву: ",x)

    b=7
    print("Змінна B дорівнює 7" if b == 7 else "Змінна B не дорівнює 7")
    ```
1. Виводжу результат роботи конструкції `try`->`except`->`finally` при помилці за допомогою команд:
    ```python
    y=[7,3,5]
    print("Що буде якщо вивести сьомий елемент масиву y[]?: ")
   try:
        print(y[7])
   except Exception as e:
        print(e)
   finally:
        print("То ось що буде!")
    ```
1. Виводжу результат роботи контекст-менеджера `with` за допомогою команд:
    ```python
    i=1
    with open("README.md", "r") as file:
        print("Вміст файлу README.md")
        for line in file:
            print("Рядок " + str(i) + ": " + line)
            i=i+1
    ```
1. Виводжу результат роботи з `lambdas` за допомогою команд:
    ```python
    new_lambda = lambda first_str, second_str: f"Об`єднання першого і другого рядка: {first_str + second_str}"
    print("Розташування функції в памяті: ", new_lambda)
    print("Виклик лямбди: ", new_lambda("str1", "_str2"))
    ```
#### 3. Створюю у власному репозиторії такі файли:
   ```text
   lab2a/
   ├── modules/
   │   └── common.py
   ├── __init__.py
   └── __main__.py
   ```
1. Перейшовши у папку з даними файлами запустив виконання програми цією командою:

    ```sh
    python3 .
    ```
    Виконання команди:
    ```text
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ python3 .
    We are in the __main__
    2021-10-21 21:23:11.192655
    linux
    test
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ 
    ```
1. Після запуску команди `python3 .` програма в першому рядку виводить назву файла який виконувався, в другому рядку виводиться час і дата виконання даної програми, в третьому рядку виводиться ос на якій було запущено програму і в четвертому рядку виведено текст "test".

    a. Після запуску команди: `python3 . -h` в консоль виводиться інформація про додаткові параметри та їх використання. Результат виконання команди:
    ```text
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ python3 . -h
    usage: . [-h] [-o OPT] [-l]

    Приклад передачі аргументів у Python програму.

    optional arguments:
      -h, --help            show this help message and exit
      -o OPT, --optional OPT
                            Цей параметр є вибірковим.
      -l, --logs            Якщо виконати команду з цим параметром будуть
                            виводитись логи.
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ 
    ```
    
    b. Після запуску команди: `python3 . -o "Цей текст також має вивестись"` в консоль виводиться інформація така сама як і в пункті 2. тільки додається текст про те що з консолї було передано аргумент і саме повідомлення яке ми передаємо. Результат виконання команди:
    ```text
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ python3 . -o "Цей текст також має вивестись"
    We are in the __main__
    2021-10-21 21:25:16.047023
    linux
    З консолі було передано аргумент
    ========== >> Цей текст також має вивестись << ==========
    test
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ 
    ```
    c. Детально ознайомилась з аргументами.
    d. Ознайомилась з логуванням і запустила команду `python3 . --logs`.
    Результат виконання команди:
    ```text
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ python3 . --logs
    2021-10-21 21:27:23,713 root INFO: Тут буде просто інформативне повідомлення
    2021-10-21 21:27:23,713 root WARNING: Це Warning повідомлення
    2021-10-21 21:27:23,713 root ERROR: Це повідомлення про помилку
    test
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ 
    ```
1. Створила власну функцію у файлі `common.py` яка буде виводить всі парні числа від 0 до 100,  якщо у функцію передати значення True і непарні якщо значення False. Виклик цієї функцію виконую з `__main__` .
Код власної функції:
    ```python
    def num_filtr(fl):
        numbers=range(0,101)
        if fl=="True":
    	    msg = "Парні елементи -> " 
        elif fl=="False":
    	    msg = "Непарні елементи -> "
    	    
        for num in numbers:
        	if (fl == "True") & (num%2 == 0):
        	    msg += str(num) + ", "
        	elif (fl == "False") & (num%2 != 0):
        	    msg += str(num) + ", "
        return msg
    ```
    Результат виконання з параметром `-o True`:
    ```text
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ python3 . -o True
    We are in the __main__
    2021-10-21 21:34:16.245742
    linux
    Парні елементи -> 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 
    З консолі було передано аргумент
     ========== >> True << ==========
    test
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ 
    ```
    Результат виконання з параметром `-o False`:
    ```text
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ python3 . -o False
    We are in the __main__
    2021-10-21 21:37:04.987689
    linux
    Непарні елементи -> 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 
    З консолі було передано аргумент
     ========== >> False << ==========
    test
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ 
    ```
1. Створила функцію яка може виконуватись з помилкою. У випадку її виникнення виводить `ERROR` повідомлення за допомогою логування використовуючи бібліотеку `logging`. Якщо функція виконалася без помилки то виводить `INFO` повідомлення.
Код власної функції:
    ```python
    def array():
        x=[1,2,3,4,5,6,7]
        print("Масив: ", x)
        print("Введіть номер елемента масиву, який хочете вивести: ")
        index = int(input())
        try:
        	print(f"X[{index}] = {x[index]}")
        except IndexError:
            logging.error("Такого елементу в масиві немає")
        else:
        	logging.info("Ви ввели коректні дані")
    ```
    Результат виконання з помилкою:
    ```text
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ python3 .
    We are in the __main__
    2021-10-21 21:54:37.679342
    linux
    Масив: [1, 2, 3, 4, 5, 6, 7]
    Введіть номер елемента масиву, який хочете вивести: 
    11
    2021-10-21 21:55:17,876 root ERROR: Такого елементу в масиві немає
    test
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ 
    ```
    Результат виконання без помилки:
    ```text
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ python3 .
    We are in the __main__
    2021-10-21 21:59:12.014345
    linux
    Масив: [1, 2, 3, 4, 5, 6, 7]
    Введіть номер елемента масиву, який хочете вивести: 
    3
    X[3] = 4
    2021-10-21 22:00:01,322 root INFO: Ви ввели коректні дані
    test
    oleksandra@oleksandra-VirtualBox:~/Oleksandra_Yanovych_IK_31/Lab2a$ 
    ```
