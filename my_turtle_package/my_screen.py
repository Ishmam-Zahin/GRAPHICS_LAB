import turtle

class MyScreen:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top
        self.screen = turtle.Screen()
        self.screen.setworldcoordinates(left, bottom, right, top)