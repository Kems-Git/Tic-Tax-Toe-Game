import pygame

# Create the spaces that will hold the player's values
board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

# To ensure consistent pieces on board
Xpos, Opos = ['X', 'O']

# Player 1 and 2's mark
u1 = u2 = ""


def printBoard():
    global board
    print(board[1], "|", board[2], "|", board[3])
    print("__|___|___")
    print(board[4], "|", board[5], "|", board[6])
    print("__|___|___")
    print(board[7], "|", board[8], "|", board[9])
    print("  |   |   ")


# Sets the players with their marks
def playerChoice():
    global u1, u2
    u1 = input("User1: Who would you like to be? X or O?")

    if u1.upper() == Xpos:
        u1 = Xpos
        u2 = Opos
    elif u1.upper() == Opos:
        u1 = Opos
        u2 = Xpos
    else:
        print("Invalid choice. Please pick again")
        playerChoice()


# Place the user's mark on chosen space
def position(user):
    global board
    pos = input("Place your marker(1-9): ")
    # Stops overwriting other user spaces or choosing the same space twice
    if int(pos) not in range(1, 9):
        print("Value is not in 1-9. Please pick again")
        position(user)
    elif board[int(pos)] == Xpos:
        print("This space is unavailable. Please pick again")
        position(user)
    elif board[int(pos)] == Opos:
        print("This space is unavailable. Please pick again")
        position(user)
    else:
        board[int(pos)] = user
    printBoard()


# Checks every possible win outcome per user
def evaluate(user, b):
    space_count = 0
    # Checks for available spaces on board
    for keys in b:
        if b[keys] == " ":
            space_count =+1
    if ((b[1] == b[2] == b[3] == user) or b[4] == b[5] == b[6] == user) or (b[7] == b[8] == b[9] == user) or (
            b[1] == b[4] == b[7] == user) or (b[2] == b[5] == b[8] == user) or (b[3] == b[6] == b[9] == user) or (
            b[1] == b[5] == b[9] == user) or (b[3] == b[5] == b[7] == user):
        txt = "{} wins!!!".format(user)
        print(txt)
        return False
    #If no more spaces, end game as a draw
    elif space_count == 0:
        print("No more available spaces. It is a draw")
        return False
    return True


# Connects all the functions together to create the game
def playGame():
    play = True
    playerChoice()
    while play:
        print("User 1: place your marker ")
        position(u1)
        play = evaluate(u1, board)
        if play:
            print("User 2: place your marker ")
            position(u2)
            play = evaluate(u2, board)


playGame()
