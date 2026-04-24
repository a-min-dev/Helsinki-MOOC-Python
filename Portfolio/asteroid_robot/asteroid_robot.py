"""
The following program utilizes the pygame module to design a game where a player controls
the horizontal movements of a robot character to collect falling asteroids before the asteroids
reach the ground.  

Once a character achieves a certain number of points, the asteroids will begin to fall faster, which
increases the difficulty of the game.

The game ends once the robot character misses catching a falling asteroid and the asteroid reaches 
the ground or when the player manually closes the game window
"""

import pygame
import random

# Initialize the game window and the caption to be displayed
pygame.init()
window_width, window_height = 640, 480
window = pygame.display.set_mode((window_width, window_height)) 
pygame.display.set_caption(str(f"Asteroid City:  Robot Saves the Day"))
clock = pygame.time.Clock() # Control the frames per second of the game

# Load the images of the robot and the rock, placed in the same directory as the main file
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

# Determine the dimensions of the robot and the asteroid to handle collisions in the game
robot_width = robot.get_width()
robot_height = robot.get_height()

rock_width = rock.get_width()
rock_height = rock.get_height()

# At the start of the game, the robot is positioned in the center of the window
robot_x = window_width // 2
robot_y = window_height - robot_height - 10

# List to handle multiple asteroid objects
asteroids = []

# Variables for gameplay, including the score counter and speed of the falling asteroid
score_counter = 0
rock_speed = 2
level_up_threshold = 10
game_running = True

game_font = pygame.font.SysFont("Arial", 24)

# Main loop of gameplay
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # User input for movement of the robot
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        robot_x -= 4
    if keys[pygame.K_RIGHT]:
        robot_x += 4

    # Boundary limits to prevent the robot from moving off the screen
    robot_x = max(0, min(robot_x, window_width - robot_width))

    # Create a Rect for player's robot to handle collision detection with the falling asteroids
    robot_rect = pygame.Rect(robot_x, robot_y, robot_width, robot_height)

    # On the average of once every 150 frames, a falling asteroid spawns at a random horizontal coordinate
    if random.randint(1, 150) == 1:
        new_x = random.randint(0, window_width - rock_width)
        asteroids.append(pygame.Rect(new_x, -rock_height, rock_width, rock_height))

    # Using list slicing, iterate over a shallow copy of the list of asteroids
    for rock_rect in asteroids[:]:
        rock_rect.y += rock_speed # The asteroid falls down the screen

        # THe case where the player's robot catches a falling asteroid 
        if robot_rect.colliderect(rock_rect):
            score_counter += 1 # Increase the player's score
            asteroids.remove(rock_rect) # Remove the asteroid from the list

            # Once a player reaches a particular threshold, the game difficulty increases
            if score_counter >= level_up_threshold:
                rock_speed += 0.5
                level_up_threshold += 10

        # In the case the player fails to catch an asteroid, the asteroid hits the ground;  game is over
        elif rock_rect.y > window_height:
            game_running = False

    # Set the gameplay window to a black screen
    window.fill((0, 0, 0))

    # Draw the player's robot
    window.blit(robot, (robot_x, robot_y))

    # Draw the asteroids in the list
    for rock_rect in asteroids:
        window.blit(rock, (rock_rect.x, rock_rect.y))

    # Draw the score counter in the upper right corner of the window
    text = game_font.render(f"Points: {score_counter}", True, (255, 0, 0))
    window.blit(text, (window_width - 130, 10))

    # Update the display and keep the frame rate at 60 fps
    pygame.display.flip()
    clock.tick(60)

# Game over:  final results are displayed in the terminal
print(f"GAME OVER!  Your Final Score: {score_counter}")
pygame.time.wait(3000)
pygame.quit()