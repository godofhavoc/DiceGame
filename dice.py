import sys
from random import shuffle, randint
from tabulate import tabulate

def game_dice(N, M):
    players = [i for i in range(N)]
    shuffle(players)

    score = [0 for _ in range(N)]
    prev_roll = [0 for _ in range(N)]
    rank_stack = []
    i = 0

    while len(rank_stack) < N:
        if prev_roll[i] == '*':
            print('Player-{} have rolled 1 twice so your chance is forfeit\n'.format(i + 1))
        if not (i in rank_stack or prev_roll[i] == '*'):
            inp = None
            while inp != 'r':
                print("\nPlayer-{} its your turn(press 'r' to roll the dice,'q' to quit)".format(i + 1))
                inp = input()

                if inp == 'q':
                    print('Quitting...')
                    return

            roll_value = randint(1, 6)
            prev_roll[i] = roll_value

            if score[i] + roll_value <= M:
                score[i] += roll_value
            print('\nYou have rolled the value {}, and your total score is now {}\n'.format(roll_value, score[i]))

            if score[i] == M:
                rank_stack.append(i)
                print('Congrats player-{} has won and received rank-{}\n'.format(i + 1, len(rank_stack)))
            elif roll_value == 6:
                print(
                    'Player-{} have rolled 6, so you have one extra chance to roll\n'.format(i + 1))
                continue
            elif prev_roll[i] == roll_value == 1:
                prev_roll[i] = '*'
            
            print('\n>>>>>> Winners Rank Table <<<<<<<\n')
            table = [['Player-{}'.format(j + 1), i + 1] for i, j in enumerate(rank_stack)]
            print(tabulate(table, headers=['Player', 'Rank']))

        if prev_roll[i] == '*' and i not in rank_stack:
            prev_roll[i] = 0
        if i < N - 1:
            i += 1
        else:
            i = 0

if __name__ == '__main__':
    try:
        game_dice(int(sys.argv[1]), int(sys.argv[2]))
    except IndexError:
        print("Please provide two integer arguments...")
    except ValueError:
        print('Please input proper integers as arguments...')
