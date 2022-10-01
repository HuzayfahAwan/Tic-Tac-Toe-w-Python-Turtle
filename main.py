# Tic-Tac-Toe Game #

# Importing the turtle module to draw on screen #

import turtle
window = turtle.Screen()
window.setup(width = 1.0, height = 1.0)
window.bgcolor("white")
window.title("Tic-Tac-Toe")

#**********SUB-PROGRAMS**********#

# This function will draw the game board on screen #

def drawBoard(turtle):
  turtle.penup()
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  turtle.backward(150)
  turtle.pendown()
  turtle.forward(300)
  turtle.penup()
  turtle.goto(0, 0)
  turtle.right(90)
  turtle.forward(30)
  turtle.left(90)
  turtle.backward(150)
  turtle.pendown()
  turtle.forward(300)
  turtle.penup()
  turtle.goto(0, 0)
  turtle.backward(50)
  turtle.left(90)
  turtle.pendown()
  turtle.forward(90)
  turtle.right(180)
  turtle.penup()
  turtle.forward(90)
  turtle.pendown()
  turtle.forward(90)
  turtle.penup()
  turtle.left(90)
  turtle.goto(0, 0)
  turtle.forward(50)
  turtle.left(90)
  turtle.pendown()
  turtle.forward(90)
  turtle.right(180)
  turtle.penup()
  turtle.forward(90)
  turtle.pendown()
  turtle.forward(90)

# This function will draw either X or O to the corresponding spot on the game board depending on what number the user enters from 0-8 #

def drawLetter(turtle, spot, p, pColor):
  if (spot == "0"):
    turtle.color(pColor)
    turtle.goto(-125, 30)
    turtle.write(p, font = ("Comic Sans MS", 45, "normal"))
    turtle.goto(0, 0)
  elif (spot == "1"):
    turtle.color(pColor)
    turtle.goto(-25, 30)
    turtle.write(p, font = ("Comic Sans MS", 45, "normal"))
    turtle.goto(0, 0)
  elif (spot == "2"):
    turtle.color(pColor)
    turtle.goto(75, 30)
    turtle.write(p, font = ("Comic Sans MS", 45, "normal"))
    turtle.goto(0, 0)
  elif (spot == "3"):
    turtle.color(pColor)
    turtle.goto(-125, -35)
    turtle.write(p, font = ("Comic Sans MS", 45, "normal"))
  elif (spot == "4"):
    turtle.color(pColor)
    turtle.goto(-25, -35)
    turtle.write(p, font = ("Comic Sans MS", 45, "normal"))
  elif (spot == "5"):
    turtle.color(pColor)
    turtle.goto(75, -35)
    turtle.write(p, font = ("Comic Sans MS", 45, "normal"))
  elif (spot == "6"):
    turtle.color(pColor)
    turtle.goto(-125, -95)
    turtle.write(p, font = ("Comic Sans MS", 45, "normal"))
  elif (spot == "7"):
    turtle.color(pColor)
    turtle.goto(-25, -95)
    turtle.write(p, font = ("Comic Sans MS", 45, "normal"))
  elif (spot == "8"):
    turtle.color(pColor)
    turtle.goto(75, -95)
    turtle.write(p, font = ("Comic Sans MS", 45, "normal"))

# This function will check whether there is a winner yet by checking to see if one of the players has achieved three spots in a row. #

def isGameOverTwoPlayer(turtle, x, o):
  if ("0" in x and "1" in x and "2" in x):
    turtle.goto(-125, 65)
    turtle.pendown()
    turtle.forward(255)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 1\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 1! YOU WIN")
    return True
  elif ("3" in x and "4" in x and "5" in x):
    turtle.goto(-125, 0)
    turtle.pendown()
    turtle.forward(255)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 1\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 1! YOU WIN")
    return True
  elif ("6" in x and "7" in x and "8" in x):
    turtle.goto(-125, -60)
    turtle.pendown()
    turtle.forward(255)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 1\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 1! YOU WIN")
    return True
  elif ("0" in x and "3" in x and "6" in x):
    turtle.goto(-105, 93)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(180)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 1\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 1! YOU WIN")
    return True
  elif ("1" in x and "4" in x and "7" in x):
    turtle.goto(-5, 93)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(180)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 1\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 1! YOU WIN")
    return True
  elif ("2" in x and "5" in x and "8" in x):
    turtle.goto(95, 93)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(180)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 1\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 1! YOU WIN")
    return True
  elif ("0" in x and "4" in x and "8" in x):
    turtle.goto(-140, 95)
    turtle.right(35)
    turtle.pendown()
    turtle.forward(320)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 1\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 1! YOU WIN")
    return True
  elif ("2" in x and "4" in x and "6" in x):
    turtle.goto(-140, -90)
    turtle.left(35)
    turtle.pendown()
    turtle.forward(315)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 1\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 1! YOU WIN")
    return True
  elif ("0" in o and "1" in o and "2" in o):
    turtle.goto(-125, 65)
    turtle.pendown()
    turtle.forward(255)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 2\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 2! YOU WIN")
    return True
  elif ("3" in o and "4" in o and "5" in o):
    turtle.goto(-125, 0)
    turtle.pendown()
    turtle.forward(255)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 2\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 2! YOU WIN")
    return True
  elif ("6" in o and "7" in o and "8" in o):
    turtle.goto(-125, -60)
    turtle.pendown()
    turtle.forward(255)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 2\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 2! YOU WIN")
    return True
  elif ("0" in o and "3" in o and "6" in o):
    turtle.goto(-105, 93)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(180)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 2\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 2! YOU WIN")
    return True
  elif ("1" in o and "4" in o and "7" in o):
    turtle.goto(-5, 93)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(180)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 2\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 2! YOU WIN")
    return True
  elif ("2" in o and "5" in o and "8" in o):
    turtle.goto(95, 93)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(180)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 1\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 1! YOU WIN")
    return True
  elif ("0" in o and "4" in o and "8" in o):
    turtle.goto(-140, 95)
    turtle.right(35)
    turtle.pendown()
    turtle.forward(320)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 2\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 2! YOU WIN")
    return True
  elif ("2" in o and "4" in o and "6" in o):
    turtle.goto(-140, -90)
    turtle.left(35)
    turtle.pendown()
    turtle.forward(315)
    turtle.penup()
    turtle.goto(-325, 0)
    turtle.write("Player 2\nWINS!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nCongratulations Player 2! YOU WIN")
    return True
  elif (len(o) == 4):
    turtle.goto(-325, 0)
    turtle.write("It's\na\nDRAW!", font = ("Verdana", 20, "bold"))
    turtle.goto(0, 0)
    print("\nNeither of you win or lose.")
    return True
  else:
    return False

# This function will execute the choosing of spots for both players and allow both players to choose what color their letters will be #

def chooseSpot():

# Possible Color Choices #
  print("")
  colors = ["Black", "Red", "Yellow", "Green", "Blue", "Orange", "Purple"]
  print(colors)

# Declaring Player 1 as X and allowing player 1 to choose the color of their X #
  
  player1 = "X"
  player1Color = str(input("\nPlayer 1 is going to be X. Please enter which color you would like the X to be from the list above: "))

# If the user decides to ignore the input instructions #

  while (colors.count(player1Color.capitalize()) == 0):
    print("\nPlease only input a color from the list above.\n")
    player1Color = str(input("Player 1 is going to be X. Please enter which color you would like the X to be from the list above: "))
    
# Declaring Player 2 as O and allowing player 2 to choose the color of their O #

  player2 = "O"
  player2Color = str(input("\nPlayer 2 is going to be O. Please enter which color you would like the O to be from the list above: "))

# If the user decides to ignore the input instructions, or if the player 2 chooses the same color as player 1 #

  while (colors.count(player2Color.capitalize()) == 0):
    print("\nPlease only input a color from the list above.\n")
    player2Color = str(input("Player 2 is going to be X. Please enter which color you would like the O to be from the list above: "))

  if (player2Color.capitalize() == player1Color.capitalize()):
    print("\nPlease input a different color from player 1 from the list above.\n")
    player2Color = str(input("Player 2 is going to be O. Please enter which color you would like the O to be from the list above: "))

# Intializing a turtle to be used for drawing the letters on the game board later on #

  DL = turtle.Turtle()
  DL.hideturtle()
  DL.penup()
  DL.speed(10)

# Intializing a turtle to be used for drawing a line through the winning letters on the game board later on #

  WL = turtle.Turtle()
  WL.hideturtle()
  WL.penup()
  WL.speed(10)

# These arrays will hold the number of each spot that's already taken on the game board to ensure that one of the players doesn't choose the same spot as the other. The individual Xspots and Ospots arrays will help in determining when there is a winner later on. Also, the fourth array just holds the numbers that are allowed to be input when choosing a spot range(0, 9). #

  taken_Xspots_num = []
  taken_Ospots_num = []
  taken_totalspots_num = []
  numbers_allowed = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
  
  while (isGameOverTwoPlayer(WL, taken_Xspots_num, taken_Ospots_num) != True):

# This 2D array will hold the spots of the game board. Players will choose spots for their shape/letter by typing in the corresponding number for whatever spot they pick. #
    
    possible_spots = [["0: top-left", "\t1: top-middle", "\t2: top-right"], ["3: middle-left", "4: middle-middle", "5: middle-right"], ["6: bottom-left", "7: bottom-middle", "8: bottom-right"]]
    print("")

#These two loops will print the contents of the 2D array above as a "spot-menu" for the user to choose from. #

    for row in range(len(possible_spots)):
      for col in range(len(possible_spots[row])):
        print(possible_spots[row][col], end="\t\t")
      print("")

    XSpot = input("\nPlayer 1, please choose a spot on the board by typing in the spot's corresponding NUMBER (0-8). ")
    while (XSpot not in numbers_allowed):
      XSpot = input("\nPlease ONLY choose a spot on the board by typing in the spot's corresponding NUMBER (type in a number from 0-8). ")
    while (taken_totalspots_num.count(XSpot) != 0):
      print("\nThat spot is already taken.")
      XSpot = input("\nPlease enter a different spot by typing in that spot's corresponding number on the board: ")
    else:
      taken_totalspots_num.append(XSpot)
      taken_Xspots_num.append(XSpot)
      drawLetter(DL, XSpot, player1, player1Color)

    if (isGameOverTwoPlayer(WL, taken_Xspots_num, taken_Ospots_num) == True):
      break
    
    OSpot = input("\nPlayer 2, please choose a spot on the board by typing in the spot's corresponding NUMBER (0-8). ")
    while (OSpot not in numbers_allowed):
      OSpot = input("\nPlease ONLY choose a spot on the board by typing in the spot's corresponding NUMBER (type in a number from 0-8). ")
    while (taken_totalspots_num.count(OSpot) != 0):
      print("\nThat spot is already taken.")
      OSpot = input("\nPlease enter a different spot by typing in that spot's corresponding number on the board: ")
    else:
      taken_totalspots_num.append(OSpot)
      taken_Ospots_num.append(OSpot)
      drawLetter(DL, OSpot, player2, player2Color)

      
#**********MAIN PROGRAM**********#

# Intializing the turtle that will draw the game board #

DB = turtle.Turtle()
DB.speed(10)
DB.hideturtle()

# Welcome Message and then asking the users if they're familiar with the rules of the game #

print("Welcome to Tic-Tac-Toe!\n")
rules = str(input("Would you like to be introduced to the rules? (yes or no) ")).lower()
while (rules != "yes" and rules != "y" and rules != "no" and rules != "n"):
  rules = input("\nWould you like to be introduced to the rules? (type yes or no) ").lower()
if (rules == "yes" or rules == "y"):
    print("\n1. Choose between versing the CPU or versing a friend.\n\n2. If you choose to verse a friend, then both of you will have to decide who Player 1 (X) is and who Player 2 (O) is. Player 1 gets to go first when choosing where to draw their shape/letter on the board, and Player 2 goes second.\n\n3. The game is won by getting three Xs or three Os in a row on the board.\n\n4. Have fun!")

# Calling these functions to draw the game board and begin the choosing of spots for both players #
  
drawBoard(DB)
chooseSpot()