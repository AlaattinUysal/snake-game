import random
import turtle
from turtle import Turtle,Screen
FONT =("Bodoni",14,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        x = 0
        y=turtle.Screen().window_height()/2 - 30
        self.goto(x,y)
        self.color("white")
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}",move= False,align="center",font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",move= False,align="center",font= FONT)



    def increase_score(self):
        self.score += 1
        self.write_score()

