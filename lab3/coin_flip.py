from random import randint

def coin_flips():
    return [randint(0,1) for i in range(1000000)]

def same_bet(bet):
    coins = coin_flips()
    wins = [i for i in coins if i == bet]
    return len(wins)

def changing_bet():
    bet = 0
    coins = coin_flips()
    wins = 0
    for i in range(len(coins)):
        if coins[i] == bet:
            wins += 1
        bet = (bet + 1) % 2
    return wins

def stats_collect():
    same_bet_result = same_bet(randint(0, 1))
    changing_bet_result = changing_bet()
    if same_bet_result > changing_bet_result:
        return "Same bet has greater chance"
    elif same_bet_result < changing_bet_result:
        return "Changing bet has greater result"