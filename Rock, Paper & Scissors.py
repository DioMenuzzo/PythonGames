import random
main = 0

while main == 0:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None
    play = 0

    #Player choice:
    while player not in choices:
        player = input('\nrock, paper or scissors? ').lower()

    #Tie condition
    if player == computer:
        print('Computer: ',computer)
        print('Player: ',player)
        print('Tie!\n')

    #Player as Rock.
    elif player == 'rock':
        #R = Rock X C = Paper (LOSE):
        if computer == 'paper':
            print('Computer: ',computer)
            print('Player: ',player)
            print('You lose!\n')

        #P = Rock X C = Scissors (WIN):
        elif computer == 'scissors':
            print('Computer: ',computer)
            print('Player: ',player)
            print('You win!\n')

    #Player as Paper.
    elif player == 'paper':
        #P = Paper X C = Scissors (LOSE):
        if computer == 'scissors':
            print('Computer: ',computer)
            print('Player: ',player)
            print('You lose!\n')

        #P = Paper X C = Rock (WIN):
        elif computer == 'rock':
            print('Computer: ',computer)
            print('Player: ',player)
            print('You win!\n')

    #Player as Scissors.
    elif player == 'scissors':
        #P = Scissors X C = Rock (LOSE):
        if computer == 'rock':
            print('Computer: ',computer)
            print('Player: ',player)
            print('You lose!\n')

        #P = Scissors X C = Paper (WIN):
        elif computer == 'paper':
            print('Computer: ',computer)
            print('Player: ',player)
            print('You win!\n')
    
    #Play again:
    while play == 0:
        play_again = input('Play again?\n(y) - yes\n(n) - no: ').lower()

        #Play Again = YES
        if play_again == 'y':
            print('Jan-Ken-Pon!\n')
            break
        
        #Play again = NO
        elif play_again == 'n':
            main = 1
            print('Bye, Bye!')
            break
        
        #Error
        elif play_again != 'y' and 'n':
            print('Invalid Command...')