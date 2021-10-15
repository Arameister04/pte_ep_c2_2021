import random

is_winner = False
while not is_winner:
    try:
        player = int(input("Válasszon kő - 1, papír - 2, olló - 3: "))
        bot = random.randint(1, 3)
        print(player, bot)
        if player == bot:
            print("Döntetlen")
        elif (player == 2 and bot == 1) or (player == 3 and bot == 2) or (player == 1 and bot == 3):
            print("Gratulálok nyertél!")
            is_winner = True
        elif (player == 1 and bot == 2) or (player == 2 and bot == 3) or (player == 3 and bot == 1):
            print("Sajnálom a gép nyert!")
            is_winner = True
        else:
            print("Nem megfelelő érték.")
    except:
        print("Nem megfelelő érték.")