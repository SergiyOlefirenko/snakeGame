import turtle as t
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard


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
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="space", fun=stop_game)
screen.onkey(key="Left", fun=snake.go_left)
screen.onkey(key="Right", fun=snake.go_right)
screen.onkey(key="Up", fun=snake.go_up)
screen.onkey(key="Down", fun=snake.go_down)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        score.increase_score()
    
    print(f"Positions after step {snake.get_snake_segments_positions()}")

screen.exitonclick()
