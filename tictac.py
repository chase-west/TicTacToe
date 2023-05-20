
currentPlayer = "X"
winner = None
gameRunning = True

#create board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

def printBoard(board):
    print(board[0] + " | " + board[1] + " | "  + board[2] + " | ")
    print("-----------")
    print(board[3] + " | " + board[4] + " | "  + board[5] + " | ")
    print("-----------")
    print(board[6] + " | " + board[7] + " | "  + board[8] + " | ")

#player input
#hello world
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Invalid")

#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRows(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board and winner != None:
        printBoard(board)
        print("Tie!")
        gameRunning = False


def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRows(board):
        print(f"The winner is {winner}")
        gameRunning = False
        


#Switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkTie(board)
    checkWin()
    switchPlayer()
    if winner != None:
        printBoard(board)
        break