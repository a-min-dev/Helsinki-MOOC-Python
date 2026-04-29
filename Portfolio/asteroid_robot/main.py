"""
The following program utilizes the pygame module to design a game where a player controls
the horizontal movements of a robot character to collect falling asteroids before the asteroids
reach the ground.  

Once a character achieves a certain number of points, the asteroids will begin to fall faster, which
increases the difficulty of the game.

The game ends once the robot character misses catching a falling asteroid and the asteroid reaches 
the ground or when the player manually closes the game window.

The original program code has been refactored to include a config.py file
"""

import pygame
import random
import config

# Initialize the game window and the caption to be displayed
pygame.init()
window_width, window_height = config.WIDTH, config.HEIGHT
window = pygame.display.set_mode((config.WIDTH, config.HEIGHT)) 
pygame.display.set_caption(config.CAPTION)
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
robot_x = (config.WIDTH // 2) - (robot_width // 2)
robot_y = config.HEIGHT - robot_height - config.PLAYER_BOTTOM_SCREEN_PADDING

# List to handle multiple asteroid objects
asteroids = []

# Variables for gameplay, including the score counter and speed of the falling asteroid
score_counter = 0
rock_speed = config.INITIAL_ROCK_SPEED
level_up_threshold = config.LEVEL_UP_STEP
game_running = True

game_font = pygame.font.SysFont(config.FONT_NAME, config.FONT_SIZE)

# Main loop of gameplay
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # User input for movement of the robot
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        robot_x -= config.PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        robot_x += config.PLAYER_SPEED

    # Boundary limits to prevent the robot from moving off the screen
    robot_x = max(0, min(robot_x, config.WIDTH - robot_width))

    # Create a Rect for player's robot to handle collision detection with the falling asteroids
    robot_rect = pygame.Rect(robot_x, robot_y, robot_width, robot_height)

    # On the average of once every 150 frames, a falling asteroid spawns at a random horizontal coordinate
    if random.randint(1, config.SPAWN_RATE) == 1:
        new_x = random.randint(0, config.WIDTH - rock_width)
        asteroids.append(pygame.Rect(new_x, -rock_height, rock_width, rock_height))

    # Using list slicing, iterate over a shallow copy of the list of asteroids
    for rock_rect in asteroids[:]:
        rock_rect.y += rock_speed

        # THe case where the player's robot catches a falling asteroid 
        if robot_rect.colliderect(rock_rect):
            score_counter += 1 # Increase the player's score
            asteroids.remove(rock_rect) # Remove the asteroid from the list

            # Once a player reaches a particular threshold, the game difficulty increases
            if score_counter >= config.LEVEL_UP_STEP:
                rock_speed += config.SPEED_INCREMENT
                level_up_threshold += config.LEVEL_UP_STEP

        # In the case the player fails to catch an asteroid, the asteroid hits the ground;  game is over
        elif rock_rect.y > config.HEIGHT:
            game_running = False

    # Set the gameplay window to a black screen
    window.fill(config.COLOR_BLACK)

    # Draw the player's robot
    window.blit(robot, (robot_x, robot_y))

    # Draw the asteroids in the list
    for rock_rect in asteroids:
        window.blit(rock, (rock_rect.x, rock_rect.y))

    # Draw the score counter in the upper right corner of the window
    text = game_font.render(f"Points: {score_counter}", True, config.COLOR_RED)
    window.blit(text, (config.WIDTH - text.get_width() - config.SCOREBOARD_X_PADDING, config.SCOREBOARD_Y_OFFSET))

    # Update the display and keep the frame rate at 60 fps
    pygame.display.flip()
    clock.tick(config.FPS)

# Game over:  final results are displayed in the terminal
print(f"GAME OVER!  Your Final Score: {score_counter}")
pygame.time.wait(config.GAME_OVER_WAIT)
pygame.quit()