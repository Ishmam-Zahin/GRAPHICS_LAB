from my_turtle_package.my_turtle import MyTurtle
from my_turtle_package.my_screen import MyScreen
from my_turtle_package.grid import Grid
import turtle

class Window:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def draw(self, t: MyTurtle):
        t.penup()
        t.goto(self.x_min, self.y_min)
        t.pendown()
        t.goto(self.x_max, self.y_min)
        t.goto(self.x_max, self.y_max)
        t.goto(self.x_min, self.y_max)
        t.goto(self.x_min, self.y_min)


class Point:
    def __init__(self, x, y, window: Window):
        self.x = x
        self.y = y
        self.bit = 0

        if x < window.x_min:
            self.bit |= 1
        if x > window.x_max:
            self.bit |= 2
        if y < window.y_min:
            self.bit |= 4
        if y > window.y_max:
            self.bit |= 8

    def draw(self, t: MyTurtle):
        t.penup()
        t.goto(self.x, self.y)
        t.dot(10, 'green')

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

        if p1.x == p2.x:
            self.slope = 0
        else:
            self.slope = (p2.y - p1.y) / (p2.x - p1.x)

    def draw(self, t: MyTurtle):
        t.penup()
        t.goto(self.p1.x, self.p1.y)
        t.pendown()
        t.goto(self.p2.x, self.p2.y)

    def calclulate_intersect_horizontal(self, p: Point, y, window: Window):
        if self.slope == 0:
            x = p.x
        else:
            x = p.x + (y - p.y) / self.slope
        p_new = Point(x, y, window)
        return p_new

    def calclulate_intersect_vertical(self, p: Point, x, window: Window):
            y = p.y + self.slope * (x - p.x)
            p_new = Point(x, y, window)
            return p_new

    def clip_point(self, p: Point, window: Window):
        if p.bit & 8:
            p_new = self.calclulate_intersect_horizontal(p, window.y_max, window)
            if p_new.bit == 0:
                p.x = p_new.x
                p.y = p_new.y
                p.bit = p_new.bit
        if p.bit & 4:
            p_new = self.calclulate_intersect_horizontal(p, window.y_min, window)
            if p_new.bit == 0:
                p.x = p_new.x
                p.y = p_new.y
                p.bit = p_new.bit
        if p.bit & 2:
            p_new = self.calclulate_intersect_vertical(p, window.x_max, window)
            if p_new.bit == 0:
                p.x = p_new.x
                p.y = p_new.y
                p.bit = p_new.bit
        if p.bit & 1:
            p_new = self.calclulate_intersect_vertical(p, window.x_min, window)
            if p_new.bit == 0:
                p.x = p_new.x
                p.y = p_new.y
                p.bit = p_new.bit

    def clip(self, t: MyTurtle, window: Window):
        if self.p1.bit & self.p2.bit:
            if not self.p1.bit | self.p2.bit:
                t.pencolor('green')
                self.draw(t)
            else:
                print('fucked')
                t.pencolor('red')
                self.draw(t)
        else:
            self.clip_point(self.p1, window)
            self.p1.draw(t)

            self.clip_point(self.p2, window)
            self.p2.draw(t)


def main():
    screen = MyScreen(-400, -400, 400, 400)
    t = MyTurtle(step_size = 10)
    t.pencolor('red')
    t.pensize(3)
    t.speed(1)
    grid = Grid(screen, t.step_size)
    grid.draw()

    window = Window(5, 35, 5, 25)
    window.draw(t)

    lines = []

    n = int(input('enter how many lines you want to draw: '))
    for i in range(n):
        x1, y1, x2, y2 = map(int, input(f'enter {i + 1}th line two points(x1, y1, x2, y2): ').split())
        p1 = Point(x1, y1, window)
        p2 = Point(x2, y2, window)
        line = Line(p1, p2)
        lines.append(line)

    for l in lines:
        t.pencolor('black')
        l.draw(t)
        l.clip(t, window)
        if not l.p1.bit | l.p2.bit:
            t.pencolor('green')
            l.draw(t)

    turtle.done()





if __name__ == '__main__':
    main()