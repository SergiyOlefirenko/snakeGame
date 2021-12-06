import turtle as t
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard


def main():
    snake = Snake()
    food = Food()
    score = Scoreboard()

    # initalize screen 
    screen = t.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snace game')
    screen.tracer(0)
    screen.listen()
    screen.onkey(key="Left", fun=snake.go_left)
    screen.onkey(key="Right", fun=snake.go_right)
    screen.onkey(key="Up", fun=snake.go_up)
    screen.onkey(key="Down", fun=snake.go_down)

    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 10:
            food.refresh()
            snake.extend()
            score.increase_score()
        
        snake_x = abs(snake.head.xcor())
        snake_y = abs(snake.head.ycor())
        if snake_x > 280 or snake_y > 280:
            is_game_on = False
            score.game_over()

        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                score.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
