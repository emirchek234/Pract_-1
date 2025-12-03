import random
import os

stats_dir = "game_stats"



def save_statistics(stats_dir, winner, size, moves_count):
    stats_file = os.path.join(stats_dir, "statistics.txt")
    
    with open(stats_file, "a", encoding="utf-8") as f:
        result = "Ничья" if winner == "Ничья" else f"Победитель: {winner}"
        f.write(f"Результат игры: {result} | Размер доски: {size}x{size} | Всего ходов: {moves_count}\n")


def print_board(board):
    size = len(board)
    print("  " + " ".join(str(i + 1) for i in range(size)))
    for i in range(size):
        print(i + 1, " ".join(board[i]))


def check_win(board, player):
    size = len(board)

    # строки
    for row in board:
        if all(cell == player for cell in row):
            return True

    # столбцы
    for col in range(size):
        if all(board[row][col] == player for row in range(size)):
            return True

    # главная диагональ
    if all(board[i][i] == player for i in range(size)):
        return True

    # побочная диагональ
    if all(board[i][size - i - 1] == player for i in range(size)):
        return True

    return False


def board_full(board):
    return all(cell != "." for row in board for cell in row)



def play_game():
    moves_count = 0

    # Ввод размера поля
    while True:
        try:
            size = int(input("Выберете размер доски (3-9): "))
            if 3 <= size <= 9:
                break
            else:
                print("Неправильный размер, попробуйте еще раз: ")
        except ValueError:
            print("Нужно вводить число!")

    # Создаем пустое поле
    board = [["."] * size for _ in range(size)]

    players = ["X", "O"]
    current_player = random.choice(players)
    print(f"\nСлучайный первый игрок: {current_player}\n")


    while True:
        print_board(board)
        print(f"\n{current_player}'очередь")

        # Ввод хода
        try:
            row, col = map(int, input("Введите строку и столбец (например, 1 2): ").split())
            row -= 1
            col -= 1

            if not (0 <= row < size and 0 <= col < size):
                print("\nНеверная позиция, попробуйте еще раз!")
                continue

            if board[row][col] != ".":
                print("\nСотовый уже занят, попробуйте еще раз!")
                continue
        except:
            print("\nНеверный ввод, повторите попытку!")
            continue

        # Совершаем ход
        board[row][col] = current_player
        moves_count += 1

        # Проверка выигрыша
        if check_win(board, current_player):
            print_board(board)
            print(f"\n{current_player} выйграл!\n")
            save_statistics(stats_dir, current_player, size, moves_count)
            break

        # Проверка ничьей
        if board_full(board):
            print_board(board)
            print("\nЭто ничья\n")
            save_statistics(stats_dir, current_player, size, moves_count)
            break

        # Переход хода
        current_player = "O" if current_player == "X" else "X"




while True:
    play_game()

    again = input("Сыграть еще раз? (д/н): ").strip().lower()
    if again != "y":
        break

    