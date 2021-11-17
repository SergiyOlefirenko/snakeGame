import turtle as t


class Snake:
    def __init__(self, start_position=[(0,0), (-20, 0), (-40, 0)]):
        body = []
        for p in start_position:
            t1 = t.Turtle("square")
            t1.penup()
            t1.setposition(p)
            t1.color('white')
            body.append(t1)
        self.body = body
    
    def get_snake_segments_positions(self):
        return [s.pos() for s in self.body]

    def move(self, distance=20):
        initial_positions = self.get_snake_segments_positions()

        for index, segment in enumerate(self.body[1:]):
            segment.setposition(initial_positions[index])

        s1 = self.body[0]
        if int(s1.heading()) == 0:
            s1.setposition(x=s1.xcor() + distance, y=s1.ycor())
        elif int(s1.heading()) == 90:
            s1.setposition(x=s1.xcor(), y=s1.ycor() + distance)
        elif int(s1.heading()) == 180:
            s1.setposition(x=s1.xcor() - distance, y=s1.ycor())
        elif int(s1.heading()) == 270:
            s1.setposition(x=s1.xcor(), y=s1.ycor() - distance)

    def turn_left(self):
        self.body[0].setheading(self.body[0].heading() + 90)
    
    def turn_right(self):
        self.body[0].setheading(self.body[0].heading() - 90)
