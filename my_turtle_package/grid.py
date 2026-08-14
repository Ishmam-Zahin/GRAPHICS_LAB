import turtle
from my_turtle_package.my_screen import MyScreen

class Grid:
    def __init__(self, screen: MyScreen, step_size):
        self.screen = screen
        self.step_size = step_size

    def draw(self):
        t = turtle.Turtle()
        t.speed(0)
        t.pencolor('gray')
        for x in range(self.screen.left, self.screen.right + 1, self.step_size):
            t.penup()
            t.goto(x, self.screen.top)
            t.pendown()
            t.goto(x, self.screen.bottom)

        for x in range(self.screen.bottom, self.screen.top + 1, self.step_size):
            t.penup()
            t.goto(self.screen.left, x)
            t.pendown()
            t.goto(self.screen.right, x)

        t.pencolor('blue')
        t.pensize(2)

        t.penup()
        t.goto(self.screen.left, 0)
        t.pendown()
        t.goto(self.screen.right, 0)

        t.penup()
        t.goto(0, self.screen.top)
        t.pendown()
        t.goto(0, self.screen.bottom)

        t.hideturtle()