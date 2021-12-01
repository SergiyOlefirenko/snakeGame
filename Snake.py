import turtle as t


STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for p in STARTING_POSITION:
            t1 = t.Turtle("square")
            t1.penup()
            t1.setposition(p)
            t1.color('white')
            self.body.append(t1)

    def get_snake_segments_positions(self):
        return [s.pos() for s in self.body]

    def move(self, distance=MOVE_DISTANCE):
        initial_positions = self.get_snake_segments_positions()
        for index, segment in enumerate(self.body[1:]):
            segment.setposition(initial_positions[index])
        self.head.forward(distance)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
