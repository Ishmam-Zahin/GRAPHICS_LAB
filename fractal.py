import turtle
from my_turtle_package.my_turtle import MyTurtle
from my_turtle_package.my_screen import MyScreen
from my_turtle_package.grid import Grid
import math


class KochCurve:
    def __init__(self, order):
        self.order = order

    def _rotate_point(self, origin, point, angle_deg):
        angle = math.radians(angle_deg)
        ox, oy = origin
        px, py = point

        dx = px - ox
        dy = py - oy

        new_dx = dx * math.cos(angle) - dy * math.sin(angle)
        new_dy = dx * math.sin(angle) + dy * math.cos(angle)

        return (ox + new_dx, oy + new_dy)

    def _koch(self, t: MyTurtle, p1, p2, order):
        if order == 0:
            t.penup()
            t.goto(p1[0], p1[1])
            t.pendown()
            t.goto(p2[0], p2[1])
            return

        x1, y1 = p1
        x2, y2 = p2

        # points that split the segment into three equal parts
        a = (x1 + (x2 - x1) / 3, y1 + (y2 - y1) / 3)
        b = (x1 + 2 * (x2 - x1) / 3, y1 + 2 * (y2 - y1) / 3)

        # peak point, rotate 'b' around 'a' by 60 degrees
        peak = self._rotate_point(a, b, 60)

        self._koch(t, p1, a, order - 1)
        self._koch(t, a, peak, order - 1)
        self._koch(t, peak, b, order - 1)
        self._koch(t, b, p2, order - 1)

    def draw(self, t: MyTurtle, start, end):
        self._koch(t, start, end, self.order)
        t.hideturtle()


def main():
    screen = MyScreen(-400, -400, 400, 400)
    t = MyTurtle(step_size = 10)
    grid = Grid(screen, t.step_size)
    grid.draw()

    t.pensize(3)
    t.speed(1)
    t.pencolor('red')


    # order = int(input('enter the order of the Koch curve: '))
    order = 1
    koch = KochCurve(order)
    koch.draw(t, start=(-30, 0), end=(30, 0))




    turtle.done()




if __name__ == '__main__':
    main()