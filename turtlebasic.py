import turtle

# Clipping window boundaries
x_min, x_max = -100, 300
y_min, y_max = -50, 200

# Region codes
LEFT, RIGHT, BOTTOM, TOP = 1, 2, 4, 8

def draw_line(t, x1, y1, x2, y2, color):
    t.pencolor(color)
    t.pensize(2)
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
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

def region_code(x, y):
    code = 0
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

def cohen_sutherland(x1, y1, x2, y2):
    accept = False

    while True:
        code1 = region_code(x1, y1)
        code2 = region_code(x2, y2)
        if (code1 | code2) == 0:    # completely inside
            accept = True
            break
        elif (code1 & code2) != 0:  # completely outside
            break
        else:
            code = code1 if code1 != 0 else code2
            if code & TOP:
                y = y_max
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            elif code & BOTTOM:
                y = y_min
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            elif code & LEFT:
                x = x_min
                y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
            elif code & RIGHT:
                x = x_max
                y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
            
            if code == code1:
                x1, y1 = x, y
            else:
                x2, y2 = x, y
    if accept:
        return (x1, y1, x2, y2)
    else:
        return None

WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("Cohen-Sutherland Line Clipping")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)



lines = []

with open("lines.txt", "r") as file:
    next(file)  # Skip the header line

    for line in file:
        x1, y1, x2, y2 = map(float, line.split())
        lines.append((x1, y1, x2, y2))


draw_axes(t, WIDTH, HEIGHT)

# Draw the clipping rectangle
t.pencolor("black")
t.penup()
t.goto(x_min, y_min)
t.pendown()
t.goto(x_max, y_min)
t.goto(x_max, y_max)
t.goto(x_min, y_max)
t.goto(x_min, y_min)
t.penup()


for x1, y1, x2, y2 in lines:
    draw_line(t, x1, y1, x2, y2, 'lightgray')
    clipped_line = cohen_sutherland(x1, y1, x2, y2)
    if clipped_line:
        draw_line(t, clipped_line[0], clipped_line[1], clipped_line[2], clipped_line[3], 'black')

turtle.done()