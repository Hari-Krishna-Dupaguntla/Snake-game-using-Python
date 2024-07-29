from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("score.txt",mode="r") as file:
            self.Highscore=int(file.read())
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.Highscore}", False, "center", ("Arial", 24, "normal"))
    def reset_score(self):
        if self.score>self.Highscore:
            self.Highscore = self.score
            with open("score.txt",mode='w') as file:
                file.write(str(self.Highscore))
        self.score=0
        self.update_score()
    # def game_is_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",False, "center", ("Arial", 24, "normal"))
    def increase_score(self):
        self.score+=1
        # self.clear()
        self.update_score()
