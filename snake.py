from turtle import Turtle,Screen
screen=Screen()
positions= [(0, 0), (-20, 0), (-30, 0)]
class Snake:
    def __init__(self,name):
        self.name=name
        self.snake_body=[]
        self.make_snake()
    def make_snake(self):
        for i in positions:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape('square')
            new_segment.speed(6)
            new_segment.goto(i)
            new_segment.color('white')
            self.snake_body.append(new_segment)
    def right(self):
        if self.snake_body[0].heading()!=270:
            self.snake_body[0].setheading(90)
    def forward(self):
        if self.snake_body[0].heading() != 180:
           self.snake_body[0].setheading(0)
    def left(self):
        if self.snake_body[0].heading() != 0:
           self.snake_body[0].setheading(180)
    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)
    def signal(self):
        screen.onkeypress(self.right,'w')
        screen.onkeypress(self.left,'a')
        screen.onkeypress(self.forward,'d')
        screen.onkeypress(self.down,'s')
    def move(self):

        for i in range(len(self.snake_body) - 1, 0, -1):
            x_cor = self.snake_body[i - 1].xcor()
            y_cor = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x_cor, y_cor)
        self.snake_body[0].forward(20)
       # self.snake_body[0].left(90)
    def add_sgmnts(self):
        new_sgmnt=Turtle()
        new_sgmnt.penup()
        new_sgmnt.shape('square')
        new_sgmnt.color('white')
        new_sgmnt.speed(6)
        self.snake_body.append(new_sgmnt)
