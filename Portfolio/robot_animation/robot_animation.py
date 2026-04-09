"""
The following program creates animation with pygame.  A robot
rounds the 4 corners of a window until the user ends the program
by closing the window
"""


import pygame

# Initialize pygame modules
pygame.init()
# Set the dimensions of the display window
window = pygame.display.set_mode((640, 480))

# Load the robot image, located in the same folder as the program
robot = pygame.image.load("robot.png")

# Initialize position and state variables
x = 0
y = 0
direction = 0 # 0: right, 1: down, 2: left, 3: up
velocity = 1
clock = pygame.time.Clock()

while True:
    # Loop for event handling, where user ends program by closing window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Drawing/animation 
    window.fill((0, 0, 0))          # Background is a black window
    window.blit(robot, (x, y))      # Draw robot at the coordinates
    pygame.display.flip()           # Update display 
    
    # Logic for animation, keeping state of robot traveling the perimeter
    if direction == 0:
        # The robot moves right until it hits the right-most boundary
        x += velocity
        if x + robot.get_width() >= 640:
            direction += 1

    elif direction == 1:
        # The robot travels down until it hits the bottom-most boundary
        y += velocity
        if y + robot.get_height() >= 480:
            direction += 1

    elif direction == 2:
        # The robot travels left until it hits the left-most boundary (x = 0)
        x -= velocity
        if x <= 0:
            direction += 1

    elif direction == 3:
        # The robot travels up until it hits the top-most boundary (y = 0)
        y -= velocity
        if y <= 0:
            direction = 0   # Reset the state so that robot moves right again
    
    # Set the frame rate at 60 frames per second
    clock.tick(60)