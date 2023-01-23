import random


def input_numbers_of_pencils():
    while True:
        try:
            user_input = int(input("How many pencils would you like to use:\n"))
        except ValueError:
            print("The number of pencils should be numeric")
        else:
            if user_input > 0:
                break
            else:
                print("The number of pencils should be positive")
    return user_input


def input_name_of_player():
    name_players = ["John", "Jack"]
    print("Who will be the first (John, Jack):")
    while True:
        user_input = input()
        if user_input in name_players:
            break
        else:
            print("Choose between 'John' and 'Jack'")
    return user_input


def print_board(x):
    print("|" * x)


def input_player_move(x):
    possible_values = [1, 2, 3]
    print("John's turn!")
    while True:
        try:
            user_input = int(input())
        except ValueError:
            print("Possible values: '1', '2' or '3'")
        else:
            if user_input in possible_values:
                if user_input <= x:
                    break
                else:
                    print("Too many pencils were taken")
            else:
                print("Possible values: '1', '2' or '3'")
    return user_input


def input_bot_move(x):
    print("Jack's turn!")
    if x % 4 == 0:
        input_bot = 3
    # 3 7 11 15 19
    elif (x - 1) % 2 == 0 and (x - 1) % 4 != 0:
        input_bot = 2
    elif x % 2 == 0:
        input_bot = 1
    elif x == 1:
        input_bot = 1
    else:
        input_bot = random.randint(1, 3)
    print(input_bot)
    return input_bot


def print_player_win(name):
    if name == "John":
        print("Jack won!")
    else:
        print("John won!")


def main():

    numbers_of_pencils = input_numbers_of_pencils()
    player = input_name_of_player()
    while True:
        print_board(numbers_of_pencils)
        if player == "John":
            move = input_player_move(numbers_of_pencils)
        else:
            move = input_bot_move(numbers_of_pencils)
        numbers_of_pencils -= move
        if numbers_of_pencils == 0:
            print_player_win(player)
            break
        else:
            if player == "John":
                player = "Jack"
            else:
                player = "John"

main()
