"""
The following program utilizes the pygame module to design and display an analog
clock that has moving hour, minute, and second hands.  The window title displays
the current system time.  
"""

import pygame, math
from datetime import datetime

# Configure and set up the pygame window, including the frame rate with pygame.time.Clock()
pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

# Configurations for the center of the analog clock, along with radii for spoke and outer edge of clock
center = (window_width/2, window_height/2)
hub_radius = 10
face_radius = 0.40 * window_height

# color palette, standard RGB, used in analog clock display
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

def get_hand_tip(center, length, angle_degrees):
    """
    The code has been refactored to utilize a helper function to convert polar coordinates
    into Cartesian coordinates.  The function subtracts 90 degrees to align with pygame
    configurations, such that -90 degrees, or 270 degrees, aligns with the 12 o'clock position
    """
    radians = math.radians(angle_degrees - 90)
    x = center[0] + length * math.cos(radians)
    y = center[1] + length * math.sin(radians)
    return (x, y)

# Main loop, with event handling allowing user to quit program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # Get the current system time
    time_now = datetime.now()
    seconds = time_now.second
    minutes = time_now.minute
    hours = time_now.hour

    # Format the pygame window title to display the current system time in digital format
    pygame.display.set_caption(str(f"{hours:02}:{minutes:02}:{seconds:02}"))

    # Calculate angles for the second, minute, and hour hands
    sec_angle = seconds * 6 # The second hand moves 6 degrees each second
    min_angle = minutes * 6 # The minute hand moves 6 degrees each minute
    # The hour hand moves a total of 30 degrees each hour, or half a degree each minute
    hour_angle = (hours % 12) * 30 + (minutes * 0.5) 

    # Drawing the pygame window and analog clock
    window.fill(black)

    # Clock face circles, including center hub and outer clock face
    pygame.draw.circle(window, red, center, face_radius, 4) # Optional thickness of outer clock face
    pygame.draw.circle(window, red, center, hub_radius) # Center hub is a filled-in circle

    # Draw the second, minute, and hour hands using the helper function, get_hand_tip, with varying thickness of hands
    pygame.draw.line(window, blue, center, get_hand_tip(center, 0.38 * window_height, sec_angle), 2)
    pygame.draw.line(window, blue, center, get_hand_tip(center, 0.35 * window_height, min_angle), 4)
    pygame.draw.line(window, blue, center, get_hand_tip(center, 0.25 * window_height, hour_angle), 6)

    pygame.display.flip()
    clock.tick(60)