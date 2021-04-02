def welcome():
    print("*** *** *** *** *** ***")
    print("    Приветствую Вас    ")
    print("        в игре         ")
    print("   крестики и нолики   ")
    print("*** *** *** *** *** ***")
    print("   формат ввода: х у   ")
    print("   х - номер строки    ")
    print("   у - номер столбца   ")
    print("*** *** *** *** *** ***")

def show():
    print()
    print("    | 0 | 1 | 2 |    ")
    print(". . . . . . . . . . .")

    for i, row in enumerate(field_game):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print(". . . . . . . . . . .")
    print()

def ask():
    while True:
        cords = input("          Ваш ход: ").split()

        if len(cords) != 2:
            print(" Пожалуйста, введите 2 координаты! ")
            continue
        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Пожалуйста, введите числа ")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! Повторите попытку ")
            continue
        if field_game[x][y] != " ":
            print(" Клетка занята! Укажите другую ")
            continue
        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field_game[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print(" Выиграл x!")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Выиграл 0!")
            return True
    return False

welcome()
field_game = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field_game[x][y] = "x"
    else:
        field_game[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break