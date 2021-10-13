import math
# Initial state.
state=[
['-','-','-'],
['-','-','-'],
['-','-','-'],
]

# Mapping of options player can select (e.g. selecting 3 will place an 'X' or 'O' on the top-right tile).
selection=[
[1,2,3],
[4,5,6],
[7,8,9],
]

# Print the board layout.
def printState(list):
    for x in range(0,3):
        print('| ' + str(list[x][0]) +' '+ str(list[x][1]) +' '+ str(list[x][2]) + ' |')

# Show the mapping to players.
print('Here is the mapping for the tiles you can select (e.g. inputting \'3\' will place an \'X\' or \'O\' on the top-right tile):')
printState(selection)
print()

# Flag whether the game is finished.
gameDone=False
# We will use this variable to iterate through the current active player (1 or 2) and the turn count.
init=0
# List of available tiles.
availableList = [1,2,3,4,5,6,7,8,9]


while gameDone == False:
    x_or_o = ''
    # Determine whether the current player is 'X' (player 1) or 'O' (player 2).
    if (init % 2 + 1) == 1:
        x_or_o = 'X'
    else:
        x_or_o = 'O'

    print('Turn ' +str(init+1))
    print('Go player '+str(init%2+1)+ ' (player ' +x_or_o+'). Here is the current board layout:')
    printState(state)
    selectedTile=0

    # Ask player to pick a tile until they select one that is not out of bounds (outside of 1-9) and not already selected.
    while selectedTile not in availableList:
        selectedTile=int(input(f'Pick a tile among {availableList}: '))
        print()
        if selectedTile not in availableList:
            print('That tile is already taken or out of bounds!')
        else:
            availableList.remove(selectedTile)
            break

    first=math.ceil(selectedTile/3)-1
    sec=selectedTile%3-1
    state[first][sec]=x_or_o

    # After each turn, determine whether the game is done (a player won or no all 9 tiles exhausted without a victor).
    for x in range (0,3):
        # Check for column win.
        if (state[0][x] == state[1][x] == state[2][x]) and all(elem in ('X','O') for elem in (state[0][x], state[1][x], state[2][x])):
            gameDone = True
            print('Congratulations, player '+str(init%2+1) +' (player ' +x_or_o+') wins!')
            printState(state)
        # Check for row win.
        elif (state[x][0] == state[x][1] == state[x][2]) and all(elem in ('X','O') for elem in (state[x][0], state[x][1], state[x][2])):
            gameDone = True
            print('Congratulations, player '+str(init%2+1) +' (player ' +x_or_o+') wins!')
            printState(state)
    # Check for diagonal win (top-left to bottom-right).
    if (state[0][0] == state[1][1] == state[2][2]) and all(elem in ('X','O') for elem in (state[0][0], state[1][1], state[2][2])):
        gameDone = True
        print('Congratulations, player ' + str(init % 2 + 1) +' (player ' +x_or_o+') wins!')
        printState(state)
    # Check for diagonal win (bottom-left to top-right).
    elif (state[2][0] == state[1][1] == state[0][2]) and all(elem in ('X','O') for elem in (state[2][0], state[1][1], state[0][2])):
        gameDone = True
        print('Congratulations, player ' + str(init % 2 + 1) +' (player ' +x_or_o+') wins!')
        printState(state)

    # If no more available tiles, the game ends in a draw.
    if not availableList:
        print("Game ended in a draw!")
        gameDone = True
        exit()

    init+=1