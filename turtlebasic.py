import turtle
import math

def to_radian(degree):
    return (degree * math.pi) / 180

def draw_polygon(t, poly, color):
    t.pensize(2)
    t.pencolor(color)
    t.penup()
    t.goto(poly[0][0], poly[0][1])
    t.pendown()
    for i in range(len(poly)):
        next_vertex = poly[(i + 1) % len(poly)]
        t.goto(next_vertex[0], next_vertex[1])
    t.penup()

def draw_axes(t, width, height):
    t.pencolor("black")
    t.pensize(1)

    t.penup()
    t.goto(-width / 2, 0)
    t.pendown()
    t.goto(width / 2, 0)
    t.write("X", align="center", font=("Arial", 12, "normal"))

    t.penup()
    t.goto(0, -height / 2)
    t.pendown()
    t.goto(0, height / 2)
    t.write("Y", align="center", font=("Arial", 12, "normal"))
    
    t.penup()

def mark_pivot_point(t, pivot_point, color):
    t.penup()
    t.goto(pivot_point[0], pivot_point[1])
    t.dot(10, color)

screen = turtle.Screen()
screen.title("2D Polygon Rotation")
screen.setup(width=800, height=600)
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.hideturtle()
t.speed(0.6)
t.pensize(2)

original_coordinates = [
    (150, 150),
    (250, 200),
    (200, 250)
]
angle = 45
rx, ry = (50, 50)

draw_axes(t, 800, 600)
mark_pivot_point(t, (rx, ry), "black")

rotated_coordinates = []

for point in original_coordinates:
    x, y = point

    x_shifted = x - rx
    y_shifted = y - ry

    rad_angle = to_radian(angle)
    cos_angle = math.cos(rad_angle)
    sin_angle = math.sin(rad_angle)
    
    x_rotated = x_shifted * cos_angle - y_shifted * sin_angle
    y_rotated = x_shifted * sin_angle + y_shifted * cos_angle

    final_x = x_rotated + rx
    final_y = y_rotated + ry
    
    rotated_coordinates.append((final_x, final_y))

draw_polygon(t, original_coordinates, "orange")
draw_polygon(t, rotated_coordinates, "black")

screen.mainloop()