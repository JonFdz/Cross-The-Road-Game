import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Jumping Turtle")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars
    car_manager.create_cars()
    car_manager.move()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect player reach finish
    if player.player_at_finish_line():
        car_manager.new_level()
        player.restart_pos()
        scoreboard.increase_level()

screen.exitonclick()
