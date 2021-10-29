print("Перша константа", False)
print("Друга константа", True)
print("Третя константа", None)

print("--------------------------------------")

# 2.2 Результат роботи вбудованих функцій за допомогою команд:
print("Число 7 в двійковій системі числення дорівнює: ", bin(7))
print("7 в 4 степені дорівнює: ", pow(7,4))
print("Мінімальне число з чисел 8,3,1,6,17 :",min(8,3,1,6,1))
print("--------------------------------------")

# 2.3 Результат роботи циклу і розгалужень за допомогою команд:
x= [3 for i in range(17)]
print("Виведення 17 трійок з масиву: ",x)

b=7
print("Змінна B дорівнює 7" if b == 7 else "Змінна B не дорівнює 7")
print("--------------------------------------")


# 2.4 Результат роботи конструкції `try`->`except`->`finally` за допомогою команд:
y=[7,3,5]
print("Що буде якщо вивести сьомий елемент масиву y[]?: ")
try:
    print(y[7])
except Exception as e:
    print(e)
finally:
    print("То ось що буде!")
print("--------------------------------------")


# 2.5 Результат роботи контекст-менеджера `with` за допомогою команд:
i=1
with open("README.md", "r") as file:
    print("Вміст файлу README.md")
    for line in file:
        print("Рядок " + str(i) + ": " + line)
        i=i+1
print("--------------------------------------")


# 2.6 Результат роботи з `lambdas` за допомогою команд:
new_lambda = lambda first_str, second_str: f"Об`єднання першого і другого рядка: {first_str + second_str}"
print("Розташування функції в памяті: ", new_lambda)
print("Виклик лямбди: ", new_lambda("str1", "_str2"))