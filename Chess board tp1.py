# Updated Animation Starter Code

from tkinter import *
import copy

####################################
# init
####################################


def init(data):
    
    data.originalBoard = [
    ["W-Rook", "W-Knight", "W-Bishop", "W-Queen", "W-King", "W-Bishop", "W-Knight", "W-Rook"], 
    ["W-Pawn", "W-Pawn", "W-Pawn", "W-Pawn", "W-Pawn", "W-Pawn", "W-Pawn", "W-Pawn"], 
    [None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None], 
    ["B-Pawn", "B-Pawn", "B-Pawn", "B-Pawn", "B-Pawn", "B-Pawn", "B-Pawn", "B-Pawn"], 
    ["B-Rook", "B-Knight", "B-Bishop", "B-Queen", "B-King", "B-Bishop", "B-Knight", "B-Rook"]
    ]
    data.margin = data.width/10

    data.board = copy.deepcopy(data.originalBoard)
    #label all data values.
    #create a new board that will be changed for final animation
    data.newBoard= copy.deepcopy(data.board)
    cellWidth = (data.width-(data.margin*2))//len(data.board[0])
    cellHeight = (data.height-(data.margin*2))//len(data.board)
    data.cellSize = min(cellWidth, cellHeight)
    data.selection = 0
    data.selectedRow = 0
    data.selectedCol = 0
    data.insertNum = 0
    data.range = [str(i) for i in range(1, len(data.board)+1)]
    data.finishGame = 0
    data.mode = "startState"
    data.isPaused = False
    data.background = PhotoImage(file="rsz_scoreback.gif")
    data.allSelected = []
    data.moveColor = 0







####################################
# mode dispatcher
####################################

#3 different modes and screens. hence, three different types of each function

#leads to the mouse pressed for specific state
def mousePressed(event, data):
    if (data.mode == "startState"):      startStateMousePressed(event, data)
    elif (data.mode == "choosePlayers"): choosePlayersMousePressed(event, data)
    elif (data.mode == "gameState"):     gameStateMousePressed(event, data)
    elif (data.mode == "gameOverState"): gameOverStateMousePressed(event, data)

#leads to the key pressed for specific state
def keyPressed(event, data):
    if (data.mode == "startState"):         startStateKeyPressed(event, data)
    elif (data.mode == "choosePlayers"):    choosePlayersKeyPressed(event, data)    
    elif (data.mode == "gameState"):        gameStateKeyPressed(event, data)
    elif (data.mode == "gameOverState"):    gameOverStateKeyPressed(event, data)

#leads to the timer fired for specific state
def timerFired(data):
    if (data.mode == "startState"):         startStateTimerFired(data)
    elif (data.mode == "choosePlayers"):    choosePlayersTimerFired(data)    
    elif (data.mode == "gameState"):        gameStateTimerFired(data)
    elif (data.mode == "gameOverState"):    gameOverStateTimerFired(data)

#leads to the redraw for specific state
def redrawAll(canvas, data):
    if (data.mode == "startState"):         startStateRedrawAll(canvas, data)
    elif (data.mode == "choosePlayers"):    choosePlayersRedrawAll(canvas, data)    
    elif (data.mode == "gameState"):        gameStateRedrawAll(canvas, data)
    elif (data.mode == "gameOverState"):    gameOverStateRedrawAll(canvas, data)



####################################
# startState mode
####################################

#the start star mode displays the starting screen where 
def startStateMousePressed(event, data):
    if (data.width/2-data.margin) <= event.x <= (data.width/2+data.margin) and\
        (data.height-data.margin*3) <= event.y <= (data.height - data.margin*2):
        data.mode = "choosePlayers"
        
        
def startStateKeyPressed(event, data):
   # data.mode = "gameState"
    pass
    
def startStateTimerFired(data):
    pass
    
#function draws writing for the start screen. including instructions on how
#to start game.
def startStateRedrawAll(canvas, data):
    canvas.create_image(0, 0,
                    anchor=NW,image=data.background)
    canvas.create_text(data.width/2, data.height/2-data.margin*3,
                       text="Welcome to", font="GameofThrones 26 bold")
    canvas.create_line(data.width/2-data.width/4, data.height/2-data.margin*2.7,
     data.width/2+data.width/4, data.height/2-data.margin*2.7, width = 5) 
     
    canvas.create_line(data.width/2-data.width/4, data.height/2-data.margin*2.6,
     data.width/2+data.width/4, data.height/2-data.margin*2.6, width = 5)                  
                 
    
    canvas.create_text(data.width/2, data.height/2-data.margin*1.5,
                       text="Game  Of  Thrones" + "\n" + \
                       "                 Chess", 
                       font="GameofThrones 50 bold")
                       
    canvas.create_oval(data.width/2-data.margin, data.height-data.margin*3, 
    data.width/2+data.margin, data.height - data.margin*2, fill = "black")
    
    canvas.create_text(data.width/2, data.height-data.margin*2.5,
                       text="Play", font="GameofThrones 30 bold", 
                       fill = "white")


####################################
# choosePlayers mode
####################################

#the start star mode displays the starting screen where 
def choosePlayersMousePressed(event, data):
    pass

def choosePlayersKeyPressed(event, data):
   # data.mode = "gameState"
    if (event.char == "p"):
        data.mode = "gameState"

def choosePlayersTimerFired(data):
    pass
    
#function draws writing for the start screen. including instructions on how
#to start game.
def choosePlayersRedrawAll(canvas, data):
    canvas.create_image(0, 0,
                    anchor=NW,image=data.background)
    canvas.create_text(data.width/2, data.height/2-data.margin,
                       text="     Single or" + "\n" + " Multiplayer?", 
                                font="GameofThrones 72 bold")
                                
    canvas.create_text(data.width/2, data.height-data.margin*2,
                       text="Press 'p' to play!", font="GameofThrones 20")


####################################
# gameState mode
####################################

# class ChessPiece(object):
#     def __init__(self, team, type):
#         self.team = team
#         self.type = type
#         self.moveRow = 0
#         self.moveCol = 0
#     
#     def postition(self):
#         return (self.moveRow, self.moveCol)
#         
#         
#         
# class Pawn(ChessPiece):
#     def move(self):
#         if self.team == "Black":
#             self.moveRow -= 1
#         if self.team == "White":
#             self.moveRow += 1
#             
# class Pawn(ChessPiece):
#     def move(self):
#         if self.team == "Black":
#             self.moveRow -= 1
#         if self.team == "White":
#             self.moveRow += 1



def isLegalMovePawn(data, type, row, col, newRow, newCol):
    differenceRow = (newRow - row)
    differenceCol = (newCol - col)
    newPlace = data.board[newRow][newCol] 

    
    if type[0] == "W" and data.moveColor%2 == 0:
        if (newPlace == None or newPlace[0] == "B") and (differenceRow == 1 or differenceRow == 2) and differenceCol== 0 :
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
        elif (newPlace == None or newPlace[0] == "B") and (differenceRow == differenceCol) :
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
            
    if type[0] == "B" and data.moveColor%2 != 0:
        if (newPlace == None or newPlace[0] == "W") and (differenceRow == -1 or differenceRow == -2) and differenceCol== 0:
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
        elif (newPlace == None or newPlace[0] == "W") and (differenceRow == differenceCol) :
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1

def isLegalMoveRook(data, type, row, col, newRow, newCol):
    differenceRow = (newRow - row)
    differenceCol = (newCol - col)
    newPlace = data.board[newRow][newCol] 

    
    if type[0] == "W" and data.moveColor%2 == 0:
        if (newPlace == None or newPlace[0] == "B"):
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
            
    if type[0] == "B" and data.moveColor%2 != 0:
        if (newPlace == None or newPlace[0] == "W"):
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
            
def isLegalMoveKnight(data, type, row, col, newRow, newCol):
    differenceRow = abs(newRow - row)
    differenceCol = abs(newCol - col)
    newPlace = data.board[newRow][newCol]
    
    if type[0] == "W" and data.moveColor%2 == 0:
        if (newPlace == None or newPlace[0] == "B") and (differenceRow == 2 and differenceCol == 1) :
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
            
        if (newPlace == None or newPlace[0] == "B") and (differenceRow == 1 and differenceCol == 2) :
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
            
    if type[0] == "B" and data.moveColor%2 != 0:
        if (newPlace == None or newPlace[0] == "W") and (differenceRow == 2 and differenceCol == 1):
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
            
        if (newPlace == None or newPlace[0] == "W") and (differenceRow == 1 and differenceCol == 2):
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1

def isLegalMoveBishop(data, type, row, col, newRow, newCol):
    differenceRow = abs(newRow - row)
    differenceCol = abs(newCol- col)
    newPlace = data.board[newRow][newCol]
    
    if type[0] == "W" and data.moveColor%2 == 0:
         
        if (newPlace == None or newPlace[0] == "B") and (differenceRow == differenceCol) :
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
            
    if type[0] == "B" and data.moveColor%2 != 0:
        if (newPlace == None or newPlace[0] == "W") and (differenceRow == differenceCol):
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1

def isLegalMoveQueen(data, type, row, col, newRow, newCol):
    difference = (newRow - row)
    newPlace = data.board[newRow][newCol]
    
    if type[0] == "W" and data.moveColor%2 == 0:
        if (newPlace == None or newPlace[0] == "B"):
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
            
    if type[0] == "B" and data.moveColor%2 != 0:
        if (newPlace == None or newPlace[0] == "W"):
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
            
            
def isLegalMoveKing(data, type, row, col, newRow, newCol):
    difference = (newRow - row)
    
    if type[0] == "W" and data.moveColor%2 == 0:
        if data.board[newRow][newCol] == None and (difference == 1 or difference == 2) :
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1
            
    if type[0] == "B" and data.moveColor%2 != 0:
        if data.board[newRow][newCol] == None and (difference == -1 or difference == -2):
            data.board[newRow][newCol] = type
            data.board[row][col] = None
            data.moveColor += 1


def isLegalMove(data, type, row, col, newRow, newCol):
    if type[2:] == "Pawn":
        if isLegalMovePawn(data, type, row, col, newRow, newCol) == False:
            return False
            
    elif type[2:] == "Rook":
        if isLegalMoveRook(data, type, row, col, newRow, newCol) == False:
            return False
            
    elif type[2:] == "Knight":
        if isLegalMoveKnight(data, type, row, col, newRow, newCol) == False:
            return False
            
    elif type[2:] == "Bishop":
        if isLegalMoveBishop(data, type, row, col, newRow, newCol) == False:
            return False
            
    elif type[2:] == "Queen":
        if isLegalMoveQueen(data, type, row, col, newRow, newCol) == False:
            return False
    
    elif type[2:] == "King":
        if isLegalMoveKing(data, type, row, col, newRow, newCol) == False:
            return False
    
    return True






def make2dList(rows, cols, item):
    a = []
    for row in range(rows):
        a += [[item] * cols]
    return a

    return board

def gameStateMousePressed(event, data):
    #if game is finished, dont take anymore pressed mouses.
    if data.finishGame == 1:
        pass
    else:
        if (data.width-data.margin*2) <= event.x <= (data.width-data.margin) and \
        (data.margin/8) <= event.y <= (data.margin-30):
            data.mode = "gameOverState"
            data.board =  data.originalBoard
   
        if (data.margin) <= event.x<= (data.width/2-data.margin*3) and \
        (data.margin/8) <= event.y <= (data.margin-30):
            data.mode = "startState"
            data.board =  data.originalBoard

        #row and column currently selected by user.
        data.selectedRow = (event.y -(data.margin)) // data.cellSize
        data.selectedCol = (event.x -(data.margin))// data.cellSize
        data.selection = (data.selectedRow, data.selectedCol)
        data.allSelected.append(data.selection)
        if len(data.allSelected) %2 == 0:
            print(data.allSelected)
            makeMove(data, event)

        
        

    
    
    

def gameStateKeyPressed(event, data):
    #if game is finished, dont take anymore pressed keys.
    if data.finishGame == 1:
        pass
    #move rows and columns for shifting keys up, down, left, right
    elif event.keysym == "Up":
        data.selectedRow -= 1
    elif event.keysym == "Down":
        data.selectedRow += 1
    elif event.keysym == "Left":
        data.selectedCol -= 1
    elif event.keysym == "Right":
        data.selectedCol += 1
    elif event.keysym == "p":
        data.mode = "gameOverState"
    #insert input by user.
    elif event.char in data.range:
        data.insertNum = event.char
    #selected keys by user
    data.selection = \
    (data.selectedRow%(len(data.board)), data.selectedCol%(len(data.board)))
    
def drawBoard(canvas, data):
    #drawbottomBoard(canvas, data)

    for row in range(len(data.board)):
        for col in range(len(data.board[row])):
            txt = data.board[row][col]
            
            
            left = col*data.cellSize
            top = row*data.cellSize
            #if square/cell is selected, change color of cell.
            if (row, col) == data.selection:
                color = "salmon"
            
            else:
                if row%2 == 0 and col%2 != 0:
                    color = "light blue"
                if row%2 == 0 and col%2 == 0:
                    color = "midnightblue"

                if row%2 != 0 and col%2 != 0:
                    color = "midnightblue"
                if row%2 != 0 and col%2 == 0:
                    color = "light blue"
                    
            canvas.create_rectangle(data.margin + left, data.margin + top, 
                                    data.margin + left + data.cellSize, 
                                    data.margin + top + data.cellSize,
                                    fill=color, width = 1, outline = "white")
            
            if txt != None:
                if txt[0] == "W":
                    canvas.create_text( 
                                    data.margin + left + data.cellSize/2, 
                                    data.margin + top + data.cellSize/2,
                                    text=txt, fill = "white")
                if txt[0] == "B":
                    canvas.create_text(
                                    data.margin + left + data.cellSize/2, 
                                    data.margin + top + data.cellSize/2,
                                    text=txt, fill = "Black")
                                    
                                    
                                    
    for row in range(len(data.board)):
        top = row*data.cellSize
        canvas.create_text(data.margin-10, top + data.margin*(1.5),
        text = len(data.board) - row) 
    
    for row in range(len(data.board)):
        left = row*data.cellSize
        canvas.create_text(left + data.margin*1.5, data.height - data.margin+10,
        text = chr(65+row)) 

def makeMove(data, event):
    original = data.allSelected[-2]
    currRow = int(original[0])
    currCol = int(original[1])

    move = data.allSelected[-1]
    newRow = int(move[0])
    newCol = int(move[1])
    txt = data.board[currRow][currCol]
    print(newRow, newCol)
    print(txt)
    if isLegalMove(data, txt, currRow, currCol, newRow, newCol):
        print("hey")


def drawbottomBoard(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    
    canvas.create_rectangle(data.margin- data.margin/4, 
    data.margin- data.margin/4, data.width - data.margin/4*3, 
    data.height-data.margin/4*3, fill = "white")


def gameStateTimerFired(data):
    pass

def drawHelpButton(canvas, data):
    canvas.create_rectangle(data.margin, data.margin/8, 
        data.width/2-data.margin*3, data.margin-30, fill = "mediumpurple4")
        
    canvas.create_text(data.margin, data.margin/4, anchor = NW,
    text = "   Help", font="GameofThrones 20", fill = "white")
    
def drawQuitButton(canvas, data):
    canvas.create_rectangle(data.width - data.margin, data.margin/8, 
        data.width-data.margin*2, data.margin-30, fill = "mediumpurple4")
        
    canvas.create_text(data.width - data.margin*2, data.margin/4, anchor = NW,
    text = "  Quit", font="GameofThrones 20", fill = "white")

def drawPlayer(canvas, data):
    if data.moveColor %2 == 0:
        canvas.create_rectangle(data.width/2 - data.margin*2, data.margin/8, 
            data.width/2 + data.margin*2, data.margin-30, fill = "mediumpurple4")
            
        canvas.create_text(data.width/2, data.margin/2.5,
        text = "White   Player's   Turn", font="GameofThrones 20", fill = "white")
    
    if data.moveColor %2 != 0:
        canvas.create_rectangle(data.width/2 - data.margin*2, data.margin/8, 
            data.width/2+data.margin*2, data.margin-30, fill = "mediumpurple4")
            
        canvas.create_text(data.width/2, data.margin/2.5,
        text = "Black   Player's   Turn", font="GameofThrones 20", fill = "white")
        

def gameStateRedrawAll(canvas, data):
    drawbottomBoard(canvas, data)
    drawBoard(canvas, data)
    drawHelpButton(canvas, data)
    drawQuitButton(canvas, data)
    drawPlayer(canvas, data)
    


####################################
# gameOverState mode
####################################

#gameOver state does not allow any user input or actions other than restarting
#the game

def gameOverStateMousePressed(event, data):
    pass

#if s is pressed, game restarts by setting mode to starting screen.
def gameOverStateKeyPressed(event, data):
    if event.char == "s":
        data.mode = "startState"

def gameOverStateTimerFired(data):
    pass

#this function draws the text on the the gameover screen displaying, the score
#that was received when playing and instructions on how to re-start the game.
def gameOverStateRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width/2, data.height/2-data.margin*2,
                       text="Game is Over!", font="Arial 26 bold", 
                       fill = "white")
    #canvas.create_text(data.width/2, data.height/2-data.margin/2,
     #                  text="Final Score is : " + str(data.score), 
      #                 font="Arial 20", fill = "white")
    canvas.create_text(data.width/2, data.height/2+data.margin*2,
                       text="Press 's' to restart game!", 
                       font="Arial 20", fill = "white")


    

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 800)
