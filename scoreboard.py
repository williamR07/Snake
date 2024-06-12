from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'score = {self.score}', align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.clear()
        self.write(f'You scored: {self.score}', align=ALIGNMENT, font=FONT)
        self.goto(0, 0)
        self.write('GAME OVER :(', align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
