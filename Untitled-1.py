while True:
    try:
        print("\n=== ПРОСТОЙ КАЛЬКУЛЯТОР ===")
        print("1. Арифметические операции")
        print("2. Операторы сравнения") 
        print("3. Логические операции")
        print("4. Побитовые операции")
        print("5. Операторы принадлежности")
        print("6. Операторы тождественности")
        print("0. Выход")

        choice = input("\nВыберите тип операции (0-6): ")
        
        if choice == "0":
            print("Выход из программы")
            break
            
        elif choice == "1":
            # Арифметические операции
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            
            print(f"{a} + {b} = {a + b}")
            print(f"{a} - {b} = {a - b}")
            print(f"{a} * {b} = {a * b}")
            if b != 0:
                print(f"{a} / {b} = {a / b}")
                print(f"{a} // {b} = {a // b}")
                print(f"{a} % {b} = {a % b}")
            else:
                print("Деление на ноль невозможно!")
            print(f"{a} ** {b} = {a ** b}")
            
        elif choice == "2":
            # Операторы сравнения
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            
            print(f"{a} == {b} = {a == b}")
            print(f"{a} != {b} = {a != b}")
            print(f"{a} > {b} = {a > b}")
            print(f"{a} < {b} = {a < b}")
            print(f"{a} >= {b} = {a >= b}")
            print(f"{a} <= {b} = {a <= b}")
            
        elif choice == "3":
            # Логические операции
            a = input("Введите первое значение (True/False): ").lower() == "true"
            b = input("Введите второе значение (True/False): ").lower() == "true"
            
            print(f"{a} and {b} = {a and b}")
            print(f"{a} or {b} = {a or b}")
            print(f"not {a} = {not a}")
            print(f"not {b} = {not b}")
            
        elif choice == "4":
            # Побитовые операции
            a = int(input("Введите первое целое число: "))
            b = int(input("Введите второе целое число: "))
            
            print(f"{a} & {b} = {a & b}")
            print(f"{a} | {b} = {a | b}")
            print(f"{a} ^ {b} = {a ^ b}")
            print(f"~{a} = {~a}")
            print(f"{a} << {b} = {a << b}")
            print(f"{a} >> {b} = {a >> b}")
            
        elif choice == "5":
            # Операторы принадлежности
            items = input("Введите элементы списка через запятую: ").split(',')
            item = input("Введите элемент для проверки: ")
            
            print(f"Список: {items}")
            print(f"'{item}' in список = {item in items}")
            print(f"'{item}' not in список = {item not in items}")
            
        elif choice == "6":
            # Операторы тождественности
            a = input("Введите первое значение: ")
            b = input("Введите второе значение: ")
            
            # Для чисел преобразуем в соответствующий тип
            try:
                a_num = float(a) if '.' in a else int(a)
                b_num = float(b) if '.' in b else int(b)
                a, b = a_num, b_num
            except:
                pass
                
            print(f"{a} is {b} = {a is b}")
            print(f"{a} is not {b} = {a is not b}")
            
        else:
            print("Неверный выбор! Попробуйте снова.")
            
    except ValueError:
        print("Ошибка: введите корректные данные!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")