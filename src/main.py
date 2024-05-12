print('Приветствую! Добро пожаловать в универсальный калькулятор и конвертер! Здесь вы можете выполнять арифметические операции, рассчитывать доходность вклада, конвертировать меры и веса, а также переводить числа из различных систем счисления в десятичную. Удобство и функциональность в одном месте!')
print('Выбери операцию:')
print('┏ 1. Сложение')
print('┣ 2. Вычитание')
print('┣ 3. Умножение')
print('┣ 4. Деление')
print('┣ 5. Возведение в степень')
print('┣ 6. Конвертер мер и весов')
print('┣ 7. Доходность вклада')
print('┗ 8. Перевод из различных систем счисления в десятичную')
choice = int(input())           #выбор пользователя


if choice == 1:         #Сложение
    print('Сейчас порешаем :)')
    num1 = int(input('Первое слагаемое = '))
    num2 = int(input('Второое слагаемое = '))
    print('Ответ:', num1 + num2)


elif choice == 2:       #Вычитание
    print('Сейчас порешаем :)')
    num1 = int(input('Уменьшаемое = '))
    num2 = int(input('Вычитаемое = '))
    print('Ответ:', num1 - num2)


elif choice == 3:       #Умножение
    print('Сейчас порешаем :)')
    num1 = int(input('Первый множитель = '))
    num2 = int(input('Второй множитель = '))
    print('Ответ:', num1 * num2)


elif choice == 4:       #Деление
    print('Какое деление ты хочешь?')
    print('┏ 1. Обычное')
    print('┗ 2. Целочисленное деление')
    choice1 = int(input())
    if choice1 == 1:
        num1 = int(input('Делимое = '))
        num2 = int(input('Делитель = '))
        print('Ответ:', num1 / num2)
    else:
        num1 = int(input('Делимое = '))
        num2 = int(input('Делитель = '))
        print('Ответ:', num1 // num2)
        
        
    
elif choice == 5:       #Возведение в степень
    print('Сейчас порешаем :)')
    num1 = int(input('Основание = '))
    num2 = int(input('Степень = ' ))
    print('Ответ:', num1 ** num2)


elif choice == 6:       #Конвертер мер и весов
    print('Что будем конвертировать?')
    print('┏1. Вес')
    print('┗2. Растояние')
    choice5 = int(input())
if choice5 == 1:    #Вес
    print('Что ты хочешь конвертировать?')
    print('┏ 1. Миллиграммы --> граммы')
    print('┣ 2. Граммы --> килограммы')
    print('┣ 3. Килограммы --> тонны ')
    print('┣ 4. Граммы --> миллиграммы')
    print('┣ 5. Килограммы  --> граммы')
    print('┗ 6. Тонны  --> килограммы ')
    choice2 = int(input()) 
    if choice2 == 1:
        num1 = int(input('Миллиграммы = '))
        print('Ответ:', num1 / 1000)
    elif choice2 == 2:
        num1 = int(input('Граммы = '))
        print('Ответ:', num1 / 1000)
    elif choice2 == 3:
        num1 = int(input('Килограммы = '))
        print('Ответ:', num1 / 1000)
    elif choice2 == 4:
        num1 = int(input('Граммы = '))
        print('Ответ:', num1 * 1000)
    elif choice2 == 5:
        num1 = int(input('Килограммы = '))
        print('Ответ:', num1 * 1000)
    elif choice2 == 6:
        num1 = int(input('Тонны = '))
        print('Ответ:', num1 * 1000)
    
    
elif choice5 == 2:  #Растояние
    print('Что ты хочешь конвертировать?')
    print('┏ 1. Миллиметры --> сантиметры')
    print('┣ 2. Сантиметры --> метры')
    print('┣ 3. Метры --> километры')
    print('┣ 4. Сантиметры --> миллиметры')
    print('┣ 5. Метры --> сантиметры')
    print('┗ 6. Километры  --> метры')
    choice6 = int(input())
    if choice6 == 1:
        num1 = int(input('Миллиметры = '))
        print('Ответ:', num1 / 10)
    elif choice6 == 2:
        num1 = int(input('Сантиметры = '))
        print('Ответ:', num1 / 100)
    elif choice6 == 3:
        num1 = int(input('Метры = '))
        print('Ответ:', num1 / 1000)
    elif choice6 == 4:
        num1 = int(input('Сантиметры = '))
        print('Ответ:', num1 * 10)
    elif choice6 == 5:
        num1 = int(input('Метры = '))
        print('Ответ:', num1 * 100)
    elif choice6 == 6:
        num1 = int(input('Километры = '))
        print('Ответ:', num1 * 1000)

elif choice == 7:       #Доходность вклада
    print('Какой тип процента ты хочешь посчитать?')
    print('┏ 1. Простой')
    print('┗ 2. Сложный')
    choice3 = int(input())
    if choice3 == 1:
        initial = int(input('Начальная сумма = '))
        profitability = int(input('Доходность в %='))
        time =int(input('На сколько лет='))
        print('Ответ:', initial * (1 + (profitability / 100) * time))
    elif choice3 == 2:
        initial = int(input('Начальная сумма = '))
        profitability = int(input('Доходность в %='))
        time =int(input('На сколько лет = '))
        print('Ответ:', initial * ((1 + (profitability / 100)) ** time))
        


elif choice == 8:       #Перевод из различных систем счисления в десятичную
    print('Из какой системы будешь переводить:')
    print('┏ 1. Двоичной')
    print('┣ 2. Восьмеричной')
    print('┗ 3. Шестнадцатеричной')
    choice4 = int(input())
    if choice4 == 1:    #Перевод из 2 в 10
        _2_number = input('Число = ')
        decimal_number = int(_2_number, 2)
        print('Ответ:', decimal_number)
    elif choice4 == 2:  #Перевод из 8 в 10
        _8_number = input('Число = ')
        decimal_number = int(_8_number, 8)
        print('Ответ:', decimal_number)
    elif choice4 == 3:  #Перевод из 16 в 10
        _16_number  = input('Число = ')
        decimal_number = int(_16_number , 16)
        print('Ответ:', decimal_number)
        
        
        
elif choice == 25:
    multi_line_string = """
     _   _  ___  _____ ____ ____  ____  
    | | | |/ _ \| ____/ ___|___ \| ___|
    | |_| | | | |  _|| |  _  __) |___ \\
    |  _  | |_| | |__| |_| |/ __/ ___) |
    |_| |_|\___/|_____\____|_____|____/    
    """
    print(multi_line_string)

else:
    print('Ошибка. Введенное число вне диапазона 1-8') 
