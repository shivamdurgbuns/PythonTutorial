import os,sys
import random
import re

def rps():
    res = True
    score={
        'comp': 0,
        'user': 0
    }
    choice = {
        'r': "Rock",
        'p': "Paper",
        's': "Scissors", 
    }
    os.system('cls')
    player = input('Enter player name:\t')
    print(f"Hello {player}, lets play Rock, Paper, Scissors.\n")
    print("Rules are simple, we both choose one of the three Rock, Paper, Scissors.\n\nRock beats Scissors.\
            \nScissors beats Paper.\nPaper beats Rock.\n")
    if player == "cupcake":
        cheatcode(score,choice,player)
    else:
        while res:
            try:
                u = input("\nChoose between Rock, Paper, Scissors by pressing\nR for Rock\nP for Paper\nS for Scissors.\t\t").lower()
                c = random.choice(('r','p','s'))
                print(f"\n{player} choose:\t{choice[u]}")
                print(f"Computer choose:\t{choice[c]}")
            except KeyError:
                print(f"\n{player} has selected wrong choice.")
                continue

            if u == 'r' and c == 's':
                print(f"\n{player} Wins.")
                score["user"] += 1
                res = aftergame(score,player)
                "continue" if res else "break"
            elif u == 's' and c == 'p':
                print(f"\n{player} Wins.")
                score["user"] += 1
                res = aftergame(score,player)
                "continue" if res else "break"
            elif u == "p" and c == "r":
                print(f"{player} Wins.")
                score["user"] += 1
                res = aftergame(score,player)
                "continue" if res else "break"
            elif u==c:
                print("It is a tie, both of you choose same.")
                res = aftergame(score,player)
                "continue" if res else "break"
            else:
                print("Computer Wins.")
                score["comp"] +=1
                res = aftergame(score,player)
                "continue" if res else "break"
            
    os.system('cls')
    print(f'\nThank you for playing {player}!')
    if score.get('user') > score.get('comp'):
        print(f'\nYou WIN!!!, Final Score is\n{player}: {score["user"]}\nComputer: {score["comp"]}\n')
        sys.exit()
    elif score.get('user') < score.get('comp'):
        print(f'\nYou LOSE!!!, Final Score is\n{player}: {score["user"]}\nComputer: {score["comp"]}\n')
        sys.exit()
    else:
        print(f'\nIts a Tie!!!, Final Score is\n{player}: {score.get("user")}\nComputer: {score.get("comp")}\n')
        sys.exit()

def aftergame(s,p):
    print(f'\nScore is\t{p} : {s["user"]}\t\tComputer: {s["comp"]}')
    cont = input(f'\n{p}, do you wanna keep playing?\t\t Press Yes or No\t')
    if re.search(r'[Yy][Ee][Ss]',cont):
        return True
    elif re.search(r'[Nn][Oo]',cont):
        return False
    else:
        print("\nYou have entered wrong option please type Yes or No")
        x = aftergame(s,p)
        return x

def cheatcode(s,c,p):
    res = True
    while res:
        try:
            u = input("\nChoose between Rock, Paper, Scissors by pressing\nR for Rock\nP for Paper\nS for Scissors.\t\t").lower()
            print(f"\n{p} choose:\t{c[u]}")
        except KeyError:
            print(f"\n{p} has selected wrong choice.")
            continue

        if u == "r":
            print("Computer choose: Scissors")
            s["user"] += 1
            res = aftergame(s,p)
            "continue" if res else "break"
        elif u == "p":
            print("Compute choose: Rock")
            s["user"] += 1
            res = aftergame(s,p)
            "continue" if res else "break"
        else:
            print("Computer choose: Paper")
            s["user"] += 1
            res = aftergame(s,p)
            "continue" if res else "break"

if __name__ == "__main__":
    rps()