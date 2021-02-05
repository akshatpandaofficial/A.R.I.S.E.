# This is a basic snake,water,gun game running on random choices by computer
# This is a problem in "Code with Harry" python programming series
# However code is not plagiarised.
import random
list_moves = ['snake','water','gun']
computer_move = random.choice(list_moves)
points_player = 0
points_computer = 0
while points_player!=5 and points_computer!=5:
    your_move = input('enter your move:')
    if computer_move == 'snake' and your_move == 'water':
        points_computer = points_computer + 1
        print(computer_move)
    elif computer_move == 'water' and your_move == 'snake':
        points_player == points_player + 1
        print(computer_move)
    elif computer_move == 'water' and your_move == 'gun':
        points_computer = points_computer + 1
        print(computer_move)
    elif computer_move == 'gun' and your_move == 'water':
        points_player = points_player + 1
        print(computer_move)
    elif computer_move == 'gun' and your_move == 'snake':
        points_computer = points_computer + 1
        print(computer_move)
    elif computer_move == 'snake' and your_move == 'gun':
        points_player = points_player + 1
        print(computer_move)
    elif computer_move == your_move:
        print(computer_move)
        pass
    else:
        print('Play Fair')
    print(points_player, points_computer)
if points_player == 5 and points_computer < 5:
    print('winner is player',points_player)
elif points_player < 5 and points_computer == 5:
    print('winner is computer',points_computer)
else:
    print('It is a  draw.')
