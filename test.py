import turtle
import datetime
import sys

class Board:
    def __init__(self):
        self.width, self.height = 360, 360
        self.s = turtle.Screen()
        self.s.bgcolor("black")
        self.t = turtle.Turtle()
        self.t.color("lightgreen")
        self.t.width("2")
        self.t.speed(0)

    def draw_board(self):
        self.t.penup()
        self.t.goto(-380, 320)
        self.t.pendown()
        self.t.forward(753)
        self.t.right(90)
        self.t.forward(630)
        self.t.right(90)
        self.t.forward(753)
        self.t.right(90)
        self.t.forward(630)
        self.t.penup()
        self.t.right(180)
        self.t.forward(210)
        self.t.pendown()
        self.t.left(90)
        self.t.forward(753)
        self.t.right(90)
        self.t.forward(210)
        self.t.right(90)
        self.t.forward(753)
        self.t.penup()
        self.t.left(90)
        self.t.forward(210)
        self.t.left(90)
        self.t.forward(251)
        self.t.pendown()
        self.t.left(90)
        self.t.forward(630)
        self.t.right(90)
        self.t.forward(251)
        self.t.right(90)
        self.t.forward(630)

    def Box(self):
        # BOX1
        self.t.penup()
        self.t.goto(-251, 210)
        self.t.pendown()
        self.t.circle(1)
        # BOX2
        self.t.penup()
        self.t.goto(0, 210)
        self.t.pendown()
        self.t.circle(1)
        # BOX3
        self.t.penup()
        self.t.goto(251, 210)
        self.t.pendown()
        self.t.circle(1)
        # BOX4
        self.t.penup()
        self.t.goto(-251, 0)
        self.t.pendown()
        self.t.circle(1)
        # BOX5
        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()
        self.t.circle(1)
        # BOX6
        self.t.penup()
        self.t.goto(251, 0)
        self.t.pendown()
        self.t.circle(1)
        # BOX7
        self.t.penup()
        self.t.goto(-251, -210)
        self.t.pendown()
        self.t.circle(1)
        # BOX8
        self.t.penup()
        self.t.goto(0, -210)
        self.t.pendown()
        self.t.circle(1)
        # BOX9
        self.t.penup()
        self.t.goto(251, -210)
        self.t.pendown()
        self.t.circle(1)

class Draw_x:
    def __init__(self):
        self.width, self.height = 360, 360
        self.t = turtle.Turtle()
        self.t.color("Cyan")
        self.t.width("2")
        self.t.speed(0)

    # Drawing x method
    def draw(self, pos):
        self.t.penup()
        self.t.goto(pos[0] - 25, pos[1] - 25)
        self.t.setheading(45)
        self.t.pendown()
        self.t.forward(70)
        self.t.right(180)
        self.t.forward(35)
        self.t.right(90)
        self.t.forward(35)
        self.t.right(180)
        self.t.forward(70)

class Draw_o:
    def __init__(self):
        self.width, self.height = 360, 360
        self.t = turtle.Turtle()
        self.t.color("pink")
        self.t.width("2")
        self.t.speed(0)

    # Drawing o method
    def draw(self, pos):
        self.t.penup()
        self.t.goto(pos[0], pos[1] - 25)
        self.t.pendown()
        self.t.circle(25)

class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.drawx = Draw_x()
        self.drawo = Draw_o()

    def draw_line(self, x1, y1, x2, y2):
        t = turtle.Turtle()
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.color("white")
        t.width(3)
        t.goto(x2, y2)

    def check_winner(self):
        # Checks the rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                self.draw_line(-251, 210 - i//3 * 210, 251, 210 - i//3 * 210)
                return True

        # Checks the columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                self.draw_line(-251 + i * 251, 320, -251 + i * 251, -320)
                return True

        # Checks diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            self.draw_line(-251, 210, 251, -210)
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            self.draw_line(251, 210, -251, -210)
            return True

        return False

    def turn(self):
        # Ask the player for a box number
        move = int(turtle.textinput(f"{self.current_player}, select a box, 1-9:", "Enter box number: ")) - 1

        # Checks if the box is empty
        if self.board[move] != ' ':
            print("This box is already filled")
            return False

        # Pins the box with the current player
        if self.current_player == self.player1:
            self.board[move] = 'X'
            self.drawx.draw((-251 + (move % 3) * 251, 210 - (move // 3) * 210))
        else:
            self.board[move] = 'O'
            self.drawo.draw((-251 + (move % 3) * 251, 210 - (move // 3) * 210))

        # Print the current board
        print(" ".join(self.board))

        # Checks if there is a winner after a move
        if self.check_winner():
            print(f"{self.current_player} wins")
            return True

        # Check for a tie
        if all(box != ' ' for box in self.board):
            print("It's a tie")
            return True

        # Player turns
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
        return False
        



game = Game()
game.player1 = input("Player 1, choose X or O: ").upper()
game.player2 = 'X' if game.player1 == 'O' else 'O'
game.current_player = game.player1

    


# Draw board
board = Board()
board.draw_board()
board.Box()

# Game starts
while not game.turn():
    pass
