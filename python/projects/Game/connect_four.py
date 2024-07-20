matrix = [[' ' for j in range(1, 8)] for i in range(6)]
player, winner = 1, False


def connect4Board(matrix):
    for row in range(12):
        if row % 2 == 0:
            actRow = int(row / 2)
            for col in range(13):
                if col % 2 == 0:
                    actCol = int(col / 2)
                    if col != 12:
                        print(matrix[actRow][actCol], end='')
                    else:
                        print(matrix[actRow][actCol])
                else:
                    print("|", end='')
        else:
            print("-------------")


def checkWin(matrix, coordinates, player):
    connect4Board(matrix)
    # Diagonal 1
    start = coordinates
    while start[0] > 0 and start[1] > 0:
        start = (start[0] - 1, start[1] - 1)

    diag1 = []
    index = start
    while index[0] < len(matrix) and index[1] < len(matrix[0]):
        diag1.append(matrix[index[0]][index[1]])
        index = (index[0] + 1, index[1] + 1)

    # Diagonal 2
    start = coordinates
    while start[0] < len(matrix) - 1 and start[1] > 0:
        start = (start[0] + 1, start[1] - 1)

    diag2 = []
    index = start
    while index[0] >= 0 and index[1] < len(matrix[0]):
        diag2.append(matrix[index[0]][index[1]])
        index = (index[0] - 1, index[1] + 1)

    # Row and column 
    cordiRow, cordiCol = coordinates
    col = [col[cordiCol] for col in matrix]
    row = matrix[cordiRow]

    # Flattining all 4 list to find match
    rowlist = str("".join(map(str, row)))
    collist = str("".join(map(str, col)))
    diaglist1 = str("".join(map(str, diag1)))
    diaglist2 = str("".join(map(str, diag2)))

    match = u'\u274C' * 4 if player == 1 else u'\u2B24' * 4
    searchin = [rowlist, collist, diaglist1, diaglist2]

    for item in searchin:
        if (match in item):
            print(f'match found player {player} is the winner')
            globals()['winner'] = True


def move():
    move1 = list(range(1, 8))
    move = 'move'
    while move not in move1:
        move = input("Enter column 1-7: ")
        if move.isnumeric() == True:
            move = int(move)
    return move


def gamePlayerInfo():  # Not using this
    print('Welcome to connect 4 \n this is 2 player game.')
    p1 = input('Player1 Name: ')
    p2 = input('Player2  Name: ')
    print(p1, p2)


def playerPlay(player):
    while winner != True:
        print(f"Player {player} play: ")
        moveCol = move()
        if player == 1:
            for moveRow in range(5, -1, -1):
                if matrix[moveRow][moveCol - 1] == ' ':
                    matrix[moveRow][moveCol - 1] = u'\u274C'
                    coordinates = (moveRow, moveCol - 1)
                    checkWin(matrix, coordinates, player)
                    player = 2
                    break
        else:
            for moveRow in range(5, -1, -1):
                if matrix[moveRow][moveCol - 1] == ' ':
                    matrix[moveRow][moveCol - 1] = u'\u2B24'
                    coordinates = (moveRow, moveCol - 1)
                    checkWin(matrix, coordinates, player)
                    player = 1
                    break
        cb = [i[0] for i in matrix]
        flat_matrix = sum(matrix, [])

        if ' ' not in flat_matrix:
            print('All Block filled, Game over....')
            break
        elif winner == True:
            break


print('\nWelcome to CONNECT FOUR GAME \n')
connect4Board(matrix)
playerPlay(player)
