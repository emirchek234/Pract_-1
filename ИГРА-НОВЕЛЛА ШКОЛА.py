# Словарь для описания уровней и характеристик
game_data = {
    "player": {
        "name": "",
        "health": 100
    }
}

# Список для инвентаря
inventory = ['телефон']

# Множество для отслеживания выполненных действий
completed_actions = set()

# Функция для красивого вывода текста
def print_slow(text):
    import time
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

# Функция для отображения инвентаря
def show_inventory():
    print_slow(f"📦 Ваш инвентарь: {', '.join(inventory)}")

# Функция для отображения здоровья
def show_health():
    print_slow(f"❤️ Здоровье: {game_data['player']['health']}%")

# Функция первого уровня
def level_1():
    print_slow("\n" + "="*50)
    print_slow("УРОВЕНЬ 1: ПОИСК КЛЮЧА ОТ КЛАССА")
    print_slow("="*50)
    
    print_slow("Вы просыпаетесь в школьном классе после последнего урока.")
    print_slow("Школа уже пустая, все ушли домой, а вы заснули за партой.")
    print_slow("Дверь класса закрыта на ключ! Нужно найти способ выбраться.")
    
    # Словарь с описанием предметов
    items_description = {
        "учебник": "Старый потрёпанный учебник по математике",
        "ручка": "Синяя шариковая ручка, почти закончилась",
        "дневник": "Ваш дневник с двойкой по физике.",
        "ключ": "Блестящий металлический ключ от классной двери!",
        "яблоко": "Сочное зелёное яблоко", 
        "телефон": "Ваш телефон, к сожалению, разряжен"
    }
    
    print_slow("\nОсматриваете класс. На столе видны различные предметы:")
    
    searched_locations = set()  # Множество проверенных мест
    
    while "ключ" not in inventory:
        print_slow("\nКуда посмотрите?")
        print_slow("1 - учительский стол")
        print_slow("2 - ваша парта") 
        print_slow("3 - шкаф с пособиями")
        print_slow("4 - окно")
        print_slow("инвентарь - посмотреть инвентарь")
        print_slow("здоровье - посмотреть здоровье")
        
        choice = input("\nВаш выбор: ").lower().strip()
        
        if choice == "инвентарь":
            show_inventory()
            continue
        elif choice == "здоровье":
            show_health()
            continue
        
        if choice == "1" and "учительский стол" not in searched_locations:
            print_slow("\nВы подходите к учительскому столу.")
            print_slow("На столе лежат: учебник, ручка и дневник.")
            print_slow("Какой предмет возьмёте? (напишите название предмета)")
            
            item_choice = input().lower().strip()
            
            if item_choice in ["учебник", "ручка", "дневник"]:
                if item_choice not in inventory and item_choice == 'ручка':
                    inventory.append(item_choice)
                    print_slow(f"Вы взяли {item_choice}. {items_description[item_choice]}")
                elif item_choice not in inventory and item_choice == 'дневник':
                    print_slow(f"Вы взяли {item_choice}. {items_description[item_choice]}")
                    game_data['player']['health'] -= 15
                    print(f'вы решили не брать {item_choice} и получили душевный урон! Здоровье -15%')
                    show_health()
                elif item_choice not in inventory and item_choice == 'Учебник':
                    inventory.append(item_choice)
                    print_slow(f"Вы взяли {item_choice}. {items_description[item_choice]}")
                    game_data['player']['health'] -= 10
                    print(f'открыв {item_choice}, вы вспомнили про несделанное домашнее задание! Здоровье - 10%')
                    show_health()
                else:
                    print_slow(f"У вас уже есть {item_choice}!")
            else:
                print_slow("Такого предмета здесь нет.")
                continue
            
            searched_locations.add("учительский стол")
            
        elif choice == "2" and "ваша парта" not in searched_locations:
            print_slow("\nВы проверяете свою парту. Под партой что-то нацарапано...")
            print_slow("В пенале находите ручку, а в рюкзаке - яблоко.")
            print_slow("Какой предмет возьмёте? (напишите название предмета)")
            
            for item in ["ручка", "яблоко", 'надпись']:
                print_slow(f"- {item}")
            
            item_choice = input().lower().strip()
            
            if item_choice in ["ручка", "яблоко"]:
                if item_choice not in inventory:
                    inventory.append(item_choice)
                    print_slow(f"Вы взяли {item_choice}. {items_description[item_choice]}")
                else:
                    print_slow(f"У вас уже есть {item_choice}!")
            elif item_choice == 'надпись':
                print('под партой нацарапана цифра "6"')
                continue
            else:
                print_slow("Такого предмета здесь нет.")
                continue
            
            searched_locations.add("ваша парта")
            
        elif choice == "3" and "шкаф" not in searched_locations:
            print_slow("\nВы открываете шкаф с учебными пособиями.")
            print_slow("Среди старых карт и глобусов замечателе блестящий ключ!")
            print_slow("Вы берёте КЛЮЧ от классной двери!")

            
            inventory.append("ключ")
            searched_locations.add("шкаф")
            completed_actions.add("нашел ключ")
            
        elif choice == "4":
            print_slow("\nВы подходите к окну - оно находится на третьем этаже.")
            print_slow("Прыгать опасно для жизни! Лучше поискать другой выход.")
            game_data['player']['health'] -= 10
            print_slow("От одной мысли о прыжке вам стало плохо. Здоровье -10%")
            show_health()
            
        elif choice in ["1", "2", "3"]:
            location_name = {
                "1": "учительский стол", 
                "2": "ваша парта", 
                "3": "шкаф"
            }[choice]
            
            if location_name in searched_locations:
                print_slow(f"\nВы уже проверяли {location_name}. Здесь больше ничего полезного.")
        else:
            print_slow("Неверный выбор. Попробуйте ещё раз.")
    
    print_slow("\n🎉 УРА! Вы нашли ключ от классной двери!")
    print_slow("Вы открываете дверь и выходите в школьный коридор.")
    completed_actions.add("прошел уровень 1")
    return True

# Функция второго уровня  
def level_2():
    print_slow("\n" + "="*50)
    print_slow("УРОВЕНЬ 2: ОБХОД ДЕЖУРНОГО УЧИТЕЛЯ")
    print_slow("="*50)
    
    print_slow("Вы вышли в школьный коридор. До выхода на свободу остаётся совсем немного!")
    print_slow("Но вот незадача - у выхода дежурует учительница Мария Ивановна.")
    print_slow("Нужно как-то отвлечь её или обойти!")
    
    # Словарь с состояниями учительницы
    teacher_state = {
        "position": "у выхода",
        "distracted": False,
        "items_taken": []
    }
    
    corridor_actions = 0
    
    while teacher_state["position"] == "у выхода":
        print_slow("\nВаши действия:")
        print_slow("1 - попробовать пройти мимо")
        print_slow("2 - отвлечь учительницу")
        print_slow("3 - осмотреть коридор")
        print_slow("4 - использовать предмет из инвентаря")
        print_slow("инвентарь - посмотреть инвентарь")
        print_slow("здоровье - посмотреть здоровье")
        
        choice = input("\nВаш выбор: ").lower().strip()
        
        if choice == "инвентарь":
            show_inventory()
            continue
        elif choice == "здоровье":
            show_health()
            continue
        
        if choice == "1":
            print_slow("\nВы пытаетесь пройти мимо Марии Ивановны...")
            print_slow('Мария Ивановна: "Куда это ты собрался, у нас вечером кружок по физике!"')
            print_slow("Вас возвращают обратно в коридор.")
            corridor_actions += 1
            game_data['player']['health'] -= 15
            show_health()
            
        elif choice == "2":
            print_slow("\nВы пытаетесь отвлечь учительницу:")
            print_slow('Вы: "Мария Ивановна, в кабинете химии что-то разлилось!"')
            
            if corridor_actions >= 2:
                print_slow("Мария Ивановна бежит проверять кабинет химии!")
                teacher_state["position"] = "кабинет химии"
                completed_actions.add("отвлек учительницу")
            else:
                print_slow('Мария Ивановна: "не поверю твоми шуткам!"')
            corridor_actions += 1

        elif choice == "3":
            print_slow("\nВы осматриваете коридор и находите:")
            
            if "записка" not in inventory and "записка" not in teacher_state["items_taken"]:
                print_slow("- странная записка на полу")
                take_note = input("Поднять записку? (да/нет): ").lower().strip()
                
                if take_note == "да":
                    inventory.append("записка")
                    teacher_state["items_taken"].append("записка")
                    corridor_actions += 1
                    print_slow("Вы подняли оборванную записку. На ней написано: 'Пароль: 248#'")
            else:
                print_slow("В коридоре больше ничего интересного.")

        elif choice == "4":
            if not inventory:
                print_slow("У вас нет предметов для использования!")
                continue
                
            print_slow("\nКакой предмет использовать?")
            show_inventory()
            
            item = input().lower().strip()
            
            if item not in inventory:
                print_slow("У вас нет такого предмета!")
            elif item == "яблоко":
                print_slow("Вы катите яблоко по полу в противоположную сторону.")
                print_slow("Мария Ивановна пошла посмотреть, что это за шум!")
                teacher_state["position"] = "исследует шум"
                inventory.remove("яблоко")
                completed_actions.add("использовал яблоко")
            elif item == "записка":
                print_slow("На записке написан пароль: 248#")
                print_slow("Возможно, он пригодится для чего-то...")
            else:
                print_slow(f"{item.capitalize()} не помогает в этой ситуации. -10% Здоровья")
                game_data['player']['health'] -= 10
                show_health()
            corridor_actions += 1
        else:
            print_slow("Неверный выбор. Попробуйте ещё раз.")

        if corridor_actions > 7:
            print_slow("\nВы слишком долго возитесь! Охранник заметил вас и вернул в класс.")
            print_slow("ИГРА ОКОНЧЕНА")
            return False
    
    print_slow("\nПока Мария Ивановна отвлечена, вы проскальзываете к выходу!")
    
    # Финальная загадка
    print_slow("\nДверь выхода закрыта кодовым замком!")
    print_slow("На замке 4 цифры. У вас есть 3 попытки!")
    
    attempts = 3
    while attempts > 0:
        try:
            code = int(input("Введите 4-значный код: "))
            
            if code == 2486:
                print_slow("🔓 ЩЁЛК! Замок открылся!")
                completed_actions.add("угадал код")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print_slow(f"❌ Неверно! Осталось попыток: {attempts}")
                else:
                    print_slow("❌ Вы исчерпали все попытки! Охранник нашёл вас.")
                    print_slow("ИГРА ОКОНЧЕНА")
                    return False
        except ValueError:
            print_slow("Пожалуйста, введите число!")
    
    print_slow("\n🎉 ПОЗДРАВЛЯЕМ! ВЫ ВЫБРАЛИСЬ ИЗ ШКОЛЫ!")
    print_slow("Вы чувствуете свежий вечерний воздух - вы СВОБОДНЫ!")
    completed_actions.add("прошел уровень 2")
    completed_actions.add("побег удался")
    return True

# Основная функция игры
def main():
    print("🎒" * 20)
    print("ТЕКСТОВАЯ ИГРА: ПОБЕГ ИЗ ШКОЛЫ")
    print("🎒" * 20)
    
    # Получаем имя игрока
    game_data["player"]["name"] = input("Как вас зовут? ").strip()
    if not game_data["player"]["name"]:
        game_data["player"]["name"] = "Ученик"
    
    print_slow(f"\nПриветствую, {game_data['player']['name']}!")
    print_slow("Ваша цель - выбраться из школы после уроков.")
    print_slow("Будьте внимательны и используйте предметы с умом!")
    
    input("\nНажмите Enter чтобы начать...")
    
    # Прохождение уровней
    if level_1():
        if level_2():
            # Финальная статистика
            print_slow("\n" + "⭐" * 50)
            print_slow("ВЫ УСПЕШНО ЗАВЕРШИЛИ ИГРУ!")
            print_slow("⭐" * 50)
            print_slow(f"Игрок: {game_data['player']['name']}")
            print_slow(f"Финальное здоровье: {game_data['player']['health']}%")
            print_slow(f"Предметов собрано: {len(inventory)}")
            print_slow(f"Выполнено действий: {completed_actions}")
            show_inventory()
            
            if game_data['player']['health'] > 80:
                print_slow("\n🏆 ОТЛИЧНЫЙ РЕЗУЛЬТАТ! Вы почти не пострадали!")
            elif game_data['player']['health'] > 50:
                print_slow("\n👍 ХОРОШИЙ РЕЗУЛЬТАТ! Немного потрёпанный, но живой!")
            else:
                print_slow("\n😅 НЕУДАЧНЕНЬКО! Но главное, что выбрался!")
    
    print_slow("\nСпасибо за игру!")

# Запуск игры
main()