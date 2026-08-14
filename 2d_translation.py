import turtle
import math
from my_turtle_package.my_turtle import MyTurtle
from my_turtle_package.my_screen import MyScreen
from my_turtle_package.grid import Grid

class Rectangle:
    def __init__(self, top_left_x, top_left_y, width, height):
        self.p1 = (top_left_x, top_left_y)
        self.p2 = (top_left_x + width, top_left_y)
        self.p3 = (top_left_x + width, top_left_y - height)
        self.p4 = (top_left_x, top_left_y - height)
        self.height = height
        self.width = width

    def draw(self, turtle: MyTurtle):
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(*self.p1)
        turtle.pendown()
        turtle.goto(*self.p2)
        turtle.goto(*self.p3)
        turtle.goto(*self.p4)
        turtle.goto(*self.p1)

    def translate(self, turtle: MyTurtle, dx, dy):
        self.p1 = (self.p1[0] + dx, self.p1[1] + dy)
        self.p2 = (self.p2[0] + dx, self.p2[1] + dy)
        self.p3 = (self.p3[0] + dx, self.p3[1] + dy)
        self.p4 = (self.p4[0] + dx, self.p4[1] + dy)

        self.draw(turtle)

    def rotate_point(self, rad, p):
        return ((p[0] * math.cos(rad) - p[1] * math.sin(rad)), (p[0] * math.sin(rad) + p[1] * math.cos(rad)))

    def rotate(self, turtle: MyTurtle, angle, pivot = None):
        rad = math.radians(angle)
        if pivot is None:
            px = (self.p1[0] + self.p2[0] + self.p3[0] + self.p4[0]) / 4
            py = (self.p1[1] + self.p2[1] + self.p3[1] + self.p4[1]) / 4
        else:
            px = pivot[0]
            py = pivot[1]
            turtle.pencolor('black')
            turtle.penup()
            turtle.goto(px, py)
            turtle.dot(10, 'black')
        turtle_tmp = MyTurtle(turtle.step_size)
        turtle_tmp.speed(1)
        turtle_tmp.pensize(2)

        turtle_tmp.pencolor('blue')
        self.translate(turtle_tmp, -px, -py)

        self.p1 = self.rotate_point(rad, self.p1)
        self.p2 = self.rotate_point(rad, self.p2)
        self.p3 = self.rotate_point(rad, self.p3)
        self.p4 = self.rotate_point(rad, self.p4)

        turtle_tmp.clear()
        self.draw(turtle_tmp)

        turtle_tmp.clear()
        turtle_tmp.hideturtle()

        turtle.pencolor('blue')
        self.translate(turtle, px, py)


def main():
    screen = MyScreen(-400, -400, 400, 400)
    t = MyTurtle(step_size=10)
    t.pencolor('red')
    t.pensize(3)
    t.speed(1)
    grid = Grid(screen, t.step_size)
    grid.draw()

    top_left_x = int(input('enter the rectangle top left x: '))
    top_left_y = int(input('enter the rectangle top left y: '))
    height = int(input('enter rectangle height: '))
    width = int(input('enter rectangle width: '))

    rec = Rectangle(top_left_x, top_left_y, width, height)
    rec.draw(t)

    angle = int(input('enter rotation angle in degree: '))
    pivot_x = int(input('enter pivot x(enter 999 for no pivot): '))
    if(pivot_x != 999):
        pivot_y = int(input('enter pivot y: '))
    if(pivot_x == 999):
        rec.rotate(t, angle)
    else:
        rec.rotate(t, angle, (pivot_x, pivot_y))



    turtle.done()



if __name__ == '__main__':
    main()