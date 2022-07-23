import random

user_wins = 0
computer_wins = 0
options = ['r', 'p', 's']
#           0    1    2
# r for rock p for paper s for scissor

while True:
    user_input = input('Type r for rock, p for paper, s for scissor to start the battle!  or type "q" to quit. ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print('computer picked', computer_pick + '.')

    if user_input == 'r' and computer_pick == 's':
        print('Point for you! ')
        user_wins += 1

    elif user_input == 'p' and computer_pick == 'r':
        print('Point for you! ')
        user_wins += 1

    elif user_input == 's' and computer_pick == 'p':
        print('Point for you! ')
        user_wins += 1
    



    if computer_pick == 'r' and user_input == 's':
        print('Point for the computer! ')
        computer_wins += 1

    elif computer_pick == 'p' and user_input == 'r':
        print('Point for the computer! ')
        computer_wins += 1

    elif computer_pick == 's' and user_input == 'p':
        print('Point for the computer! ')
        computer_wins += 1

    if computer_pick == user_input:
        print('Its a tie!')

print('You got', user_wins, 'points.')
print('computer got', computer_wins, 'points.')

if computer_wins > user_wins:
    print('The computer won :(')
elif computer_wins < user_wins:
    print('You won!')