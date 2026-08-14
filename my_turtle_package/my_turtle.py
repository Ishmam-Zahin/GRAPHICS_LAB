import turtle

class MyTurtle(turtle.Turtle):
    def __init__(self, step_size = 1):
        super().__init__()
        self.step_size = step_size

    def forward(self, step):
        new_step = step * self.step_size
        super().forward(new_step)

    def goto(self, x, y):
        new_x = x * self.step_size
        new_y = y * self.step_size
        super().goto(new_x, new_y)