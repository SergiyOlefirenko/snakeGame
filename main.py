import turtle as t
import time
from Playfield import Playfield
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard



def main():
    snake = Snake()
    food = Food()
    score = Scoreboard()
    screen = Playfield()

    # initialize screen 
    screen.playfield.onkey(key="Left", fun=snake.go_left)
    screen.playfield.onkey(key="Right", fun=snake.go_right)
    screen.playfield.onkey(key="Up", fun=snake.go_up)
    screen.playfield.onkey(key="Down", fun=snake.go_down)

    is_game_on = True
    while is_game_on:
        screen.playfield.update()
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

    screen.playfield.exitonclick()


if __name__ == "__main__":
    main()
