import random
from decouple import config
def start_game():
    massiv = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,30]
    luck = random.choice(massiv)
    num = int(input("Введите число от 1 до 30: "))
    if 1>num>30:
        num = int(input("Пожалуйста введите от 1 до 30:\n "))
    bid = int(input("Сделайте ставку: "))
    MY_MONEY = config("MY_MONEY", cast=int)

    if num == luck:
        MY_MONEY += bid * 2
    else:
        MY_MONEY -= bid

    print("Хотите ли вы сыграть еще?\n Если да то отправьте + \n Если нет то отправьте - ")
    a = input(": ")
    if a == "+":
        start_game()
    if a == "-":
        print(f"У вас осталось {MY_MONEY} денег")
    else:
        a = input("Повторяем ДА это + \nНЕТ это -\n ")