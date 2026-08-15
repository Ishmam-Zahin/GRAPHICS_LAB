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

    def draw(self, t: MyTurtle):
        t.penup()
        t.setheading(0)
        t.goto(*self.p1)
        t.pendown()
        t.goto(*self.p2)
        t.goto(*self.p3)
        t.goto(*self.p4)
        t.goto(*self.p1)

    def translate_point(self, p, dx, dy):
        return (p[0] + dx, p[1] + dy)

    def translate(self, t: MyTurtle, dx, dy):
        self.p1 = self.translate_point(self.p1, dx, dy)
        self.p2 = self.translate_point(self.p2, dx, dy)
        self.p3 = self.translate_point(self.p3, dx, dy)
        self.p4 = self.translate_point(self.p4, dx, dy)

        self.draw(t)

    def get_centroid(self):
        return ((self.p1[0] + self.p2[0] + self.p3[0] + self.p4[0]) / 4), ((self.p1[1] + self.p2[1] + self.p3[1] + self.p4[1]) / 4)

    def rotate_point(self, rad, p):
        return ((p[0] * math.cos(rad) - p[1] * math.sin(rad)), (p[0] * math.sin(rad) + p[1] * math.cos(rad)))

    def rotate(self, t: MyTurtle, angle, pivot = None):
        rad = math.radians(angle)
        if pivot is None:
            px, py = self.get_centroid()
        else:
            px = pivot[0]
            py = pivot[1]
            t.pencolor('black')
            t.penup()
            t.goto(px, py)
            t.dot(10, 'black')

        t_tmp = MyTurtle(t.step_size)
        t_tmp.speed(1)
        t_tmp.pensize(2)

        t_tmp.pencolor('blue')
        self.translate(t_tmp, -px, -py)

        self.p1 = self.rotate_point(rad, self.p1)
        self.p2 = self.rotate_point(rad, self.p2)
        self.p3 = self.rotate_point(rad, self.p3)
        self.p4 = self.rotate_point(rad, self.p4)

        t_tmp.clear()
        self.draw(t_tmp)

        t_tmp.clear()
        t_tmp.hideturtle()

        t.pencolor('blue')
        self.translate(t, px, py)

    def scale_point(self, p, sx, sy):
        return (p[0] * sx), (p[1] * sy)

    def scale(self, t: MyTurtle, sx, sy, fixed_point = None):
        if fixed_point is None:
            fx, fy = self.get_centroid()
        else:
            fx = fixed_point[0]
            fy = fixed_point[1]
            t.pencolor('black')
            t.penup()
            t.goto(fx, fy)
            t.dot(10, 'black')

        t_tmp = MyTurtle(t.step_size)
        t_tmp.speed(1)
        t_tmp.pensize(2)

        t_tmp.pencolor('blue')
        self.translate(t_tmp, -fx, -fy)

        self.p1 = self.scale_point(self.p1, sx, sy)
        self.p2 = self.scale_point(self.p2, sx, sy)
        self.p3 = self.scale_point(self.p3, sx, sy)
        self.p4 = self.scale_point(self.p4, sx, sy)

        t_tmp.clear()
        self.draw(t_tmp)

        t_tmp.clear()
        t_tmp.hideturtle()

        t.pencolor('blue')
        self.translate(t, fx, fy)

        


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

    option = input('enter t/r/s(translation/rotation/scaling): ')

    if option == 's':
        sx = int(input('enter scaling factor x: '))
        sy = int(input('enter scaling factor y: '))
        fx = int(input('enter fixed point x(999 for center): '))
        if fx != 999:
            fy = int(input('enter fixed point y: '))
    
        if fx == 999:
            rec.scale(t, sx, sy)
        else:
            rec.scale(t, sx, sy, (fx, fy))
    elif option == 'r':
        angle = int(input('enter rotation angle in degree: '))
        px = int(input('enter pivot point x(999 for center): '))
        if px != 999:
            py = int(input('enter pivot point y: '))
    
        if px == 999:
            rec.rotate(t, angle)
        else:
            rec.scale(t, angle, (px, py))
    elif option == 't':
        dx = int(input('enter dx: '))
        dy = int(input('enter dy: '))
        rec.translate(t, dx, dy)


    turtle.done()



if __name__ == '__main__':
    main()