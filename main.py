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
    
    snake_x = abs(snake.head.xcor())
    snake_y = abs(snake.head.ycor())
    if snake_x > 280 or snake_y > 280:
        stop_game()
        score.game_over()
    
    print(f"Positions after step {snake.get_snake_segments_positions()}")

screen.exitonclick()
