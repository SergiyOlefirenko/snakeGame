import turtle as t


WIDTH = 600
HEIGHT = 600

class Playfield(t.Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.playfield = t.Screen()
        self.initialize_screen()
        self.draw_playfield_limits()
    
    def initialize_screen(self):
        self.playfield.setup(width=WIDTH, height=HEIGHT)
        self.playfield.bgcolor('black')
        self.playfield.title('Snace game')
        self.playfield.tracer(0)
        self.playfield.listen()
    
    def draw_playfield_limits(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(WIDTH/2-20, HEIGHT/2-20)
        self.pendown()
        self.goto(-(WIDTH/2-20), HEIGHT/2-20)
        self.goto(-(WIDTH/2-20), -(HEIGHT/2-20))
        self.goto(WIDTH/2-20, -(HEIGHT/2-20))
        self.goto(WIDTH/2-20, HEIGHT/2-20)
