from turtle import Turtle
class Score_board:
    def __init__(self,name):
        self.name=name
        self.score=0
        self.score_manager=Turtle()
    def up_score(self):
        self.score+=1
    def score_update(self):
        self.score_manager.clear()
        self.score_manager.penup()
        self.score_manager.color('white')
        self.score_manager.goto(0, 270)
        self.score_manager.write(f' Score:{self.score}',align='center',font=('Arial',14,'normal'))
        self.score_manager.hideturtle()
