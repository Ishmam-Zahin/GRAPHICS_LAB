from my_turtle_package.my_turtle import MyTurtle
from my_turtle_package.my_screen import MyScreen
from my_turtle_package.grid import Grid
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def _draw_point(self, p: Point, t: MyTurtle):
        t.penup()
        t.goto(p.x, p.y)
        t.dot(10, 'blue')

    def _connect_points(self, points: list[Point], t: MyTurtle):
        t.penup()
        for i, p in enumerate(points):
            t.goto(p.x, p.y)
            if i == 0:
                t.pendown()

    def draw_with_bresenham(self, t: MyTurtle):
        self._draw_point(self.p1, t)
        self._draw_point(self.p2, t)
        points = [self.p1]
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        tmp_x = self.p1.x
        tmp_y = self.p1.y

        if abs(dy) <= abs(dx):
            p = 2 * dy - dx
            while tmp_x < self.p2.x:
                if p < 0:
                    tmp_x += 1
                    tmp_y = tmp_y
                    p += 2 * dy
                else:
                    tmp_x += 1
                    tmp_y += 1
                    p += 2 * dy - 2 * dx
                tmp_p = Point(tmp_x, tmp_y)
                self._draw_point(tmp_p, t)
                points.append(tmp_p)
        else:
            p = 2 * dx - dy
            while tmp_y < self.p2.y:
                if p < 0:
                    tmp_x = tmp_x
                    tmp_y += 1
                    p += 2 * dx
                else:
                    tmp_x += 1
                    tmp_y += 1
                    p += 2 * dx - 2 * dy
                tmp_p = Point(tmp_x, tmp_y)
                self._draw_point(tmp_p, t)
                points.append(tmp_p)
        points.append(self.p2)
        self._connect_points(points, t)

    def draw_with_dda(self, t: MyTurtle):
        self._draw_point(self.p1, t)
        self._draw_point(self.p2, t)
        points = [self.p1]

        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y

        steps = max(abs(dx), abs(dy))

        x_inc = dx / steps
        y_inc = dy / steps

        tmp_x = self.p1.x
        tmp_y = self.p1.y

        for _ in range(steps):
            tmp_x += x_inc
            tmp_y += y_inc
            tmp_p = Point(round(tmp_x), round(tmp_y))
            self._draw_point(tmp_p, t)
            points.append(tmp_p)

        points.append(self.p2)
        self._connect_points(points, t)


def main():
    screen = MyScreen(-400, -400, 400, 400)
    t = MyTurtle(step_size = 10)
    grid = Grid(screen, t.step_size)
    grid.draw()

    t.pensize(3)
    t.pencolor('red')
    t.speed(1)

    x1, y1 = map(int, input('enter the first co-ordinates(x, y): ').split())
    x2, y2 = map(int, input('enter the last co-ordinates(x, y): ').split())

    line = Line(x1, y1, x2, y2)

    option = input('enter line draw method b/d(bresenham/dda): ')
    if option == 'b':
        line.draw_with_bresenham(t)
    elif option == 'd':
        line.draw_with_dda(t)

    turtle.done()




if __name__ == '__main__':
    main()