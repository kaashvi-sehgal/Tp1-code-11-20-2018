# Updated Animation Starter Code

from tkinter import *
import copy

####################################
# init
####################################


def init(data):
    data.margin = data.width/10

    data.board = make2dList(8, 8, 0)
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






####################################
# mode dispatcher
####################################

#3 different modes and screens. hence, three different types of each function

#leads to the mouse pressed for specific state
def mousePressed(event, data):
    if (data.mode == "startState"): 
        startStateMousePressed(event, data)
    elif (data.mode == "choosePlayers"):
        choosePlayersMousePressed(event, data)

    elif (data.mode == "gameState"):   
        gameStateMousePressed(event, data)
    elif (data.mode == "gameOverState"):       
        gameOverStateMousePressed(event, data)

#leads to the key pressed for specific state
def keyPressed(event, data):
    if (data.mode == "startState"): 
        startStateKeyPressed(event, data)
    elif (data.mode == "choosePlayers"):
        choosePlayersKeyPressed(event, data)    
    elif (data.mode == "gameState"):   
        gameStateKeyPressed(event, data)
    elif (data.mode == "gameOverState"):       
        gameOverStateKeyPressed(event, data)

#leads to the timer fired for specific state
def timerFired(data):
    if (data.mode == "startState"): 
        startStateTimerFired(data)
    elif (data.mode == "choosePlayers"):
        choosePlayersTimerFired(data)    

    elif (data.mode == "gameState"):   
        gameStateTimerFired(data)
    elif (data.mode == "gameOverState"):       
        gameOverStateTimerFired(data)

#leads to the redraw for specific state
def redrawAll(canvas, data):
    if (data.mode == "startState"): 
        startStateRedrawAll(canvas, data)
    elif (data.mode == "choosePlayers"):
        choosePlayersRedrawAll(canvas, data)    
    elif (data.mode == "gameState"):   
        gameStateRedrawAll(canvas, data)
    elif (data.mode == "gameOverState"):       
        gameOverStateRedrawAll(canvas, data)



####################################
# startState mode
####################################

#the start star mode displays the starting screen where 
def startStateMousePressed(event, data):
    pass

def startStateKeyPressed(event, data):
   # data.mode = "gameState"
    if (event.char == "p"):
        data.mode = "choosePlayers"

def startStateTimerFired(data):
    pass
    
#function draws writing for the start screen. including instructions on how
#to start game.
def startStateRedrawAll(canvas, data):

    canvas.create_text(data.width/2, data.height/2-data.margin*1.5,
                       text="Welcome to", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2-data.margin,
                       text="Game Of Thrones Chess!", font="Arial 48 bold")
    canvas.create_text(data.width/2, data.height-data.margin*2,
                       text="Press any key to choose" + "\n" + " the number of players!", font="Arial 20")


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

    canvas.create_text(data.width/2, data.height/2-data.margin,
                       text="     Choose " + "\n" + "your player!", 
                                font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height-data.margin*2,
                       text="Press 'p' to play!", font="Arial 20")


####################################
# gameState mode
####################################




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
        #row and column currently selected by user.
        data.selectedRow = (event.y -(data.margin)) // data.cellSize
        data.selectedCol = (event.x -(data.margin))// data.cellSize
        data.selection = (data.selectedRow, data.selectedCol)
    

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
    #if original board had an empty space, only then can backspace
    elif event.keysym == "BackSpace" and \
        data.board[data.selectedRow][data.selectedCol] == 0:
        data.newBoard[data.selectedRow][data.selectedCol] = 0
    #replace what was inputed with an empty string when backspacing.
        data.insertNum = " "
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
            left = col*data.cellSize
            top = row*data.cellSize
            #if square/cell is selected, change color of cell.
            if (row, col) == data.selection:
                color = "midnightblue"
            else:
                color = "light blue"
            canvas.create_rectangle(data.margin + left, data.margin + top, 
                                    data.margin + left + data.cellSize, data.margin + top + data.cellSize,
                                    fill=color, width = 1, outline = "white")
    for row in range(len(data.board)):
        top = row*data.cellSize
        canvas.create_text(data.margin-10, top + data.margin*(2),text = len(data.board) - row) 
    
    for row in range(len(data.board)):
        left = row*data.cellSize
        canvas.create_text(left + data.margin*(2), data.height - data.margin-10,text = len(data.board) - row) 


        

def drawbottomBoard(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    
    canvas.create_rectangle(data.margin- data.margin/4, 
    data.margin- data.margin/4, data.width - data.margin/4*3, 
    data.height-data.margin/4*3, fill = "white")


def gameStateTimerFired(data):
    pass



def gameStateRedrawAll(canvas, data):
    drawbottomBoard(canvas, data)
    drawBoard(canvas, data)


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
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "red")
    canvas.create_text(data.width/2, data.height/2-data.textMargin*2,
                       text="Game is Over!", font="Arial 26 bold", 
                       fill = "white")
    canvas.create_text(data.width/2, data.height/2-data.textMargin/2,
                       text="Final Score is : " + str(data.score), 
                       font="Arial 20", fill = "white")
    canvas.create_text(data.width/2, data.height/2+data.textMargin*2,
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