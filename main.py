import turtle as t
import time
from Snake import Snake


def stop_game():
    global is_game_on
    is_game_on = False

# initalize screen 
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snace game')
screen.tracer(0)


snake = Snake()

is_game_on = True
while is_game_on:
    screen.listen()
    screen.onkey(key="space", fun=stop_game)
    screen.onkey(key="a", fun=snake.turn_left)
    screen.onkey(key="d", fun=snake.turn_right)
    snake.move()
    screen.update()
    time.sleep(0.1)
    print(f"Positions after step {snake.get_snake_segments_positions()}")

screen.exitonclick()