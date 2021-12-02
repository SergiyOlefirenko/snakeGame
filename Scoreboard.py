from turtle import Turtle


ALIGN = 'center'
FONT = ("Arial", 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.update_scoreboard()

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", True, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=ALIGN, font=FONT)
