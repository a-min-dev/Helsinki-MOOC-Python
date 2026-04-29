import pygame
import random

def is_collected(player_rect, asteroid_rect):
    # Check if the robot player has caught an asteroid rock
    return player_rect.colliderect(asteroid_rect)

def player_in_bounds(current_x, object_width, screen_width):
    # Keep the robot player within the game's window boundaries
    return max(0, min(current_x, screen_width - object_width))

def spawn_asteroid(spawn_rate):
    # Determine if a new asteroid rock should appear in the game window
    return random.randint(1, spawn_rate) == 1

def increase_difficulty(current_speed, increment):
    # Increase the gameplay speed after the player reaches a level up milestone
    return current_speed + increment