from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5,0.5)
        self.color('red')
        self.speed('fastest')
    def move(self):

        x_cor=random.choice(range(-380,380))
        y_cor=random.choice(range(-380,380))
        self.goto(x_cor,y_cor)