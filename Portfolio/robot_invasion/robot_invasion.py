"""
The program creates animation with the pygame and random modules to simulate a robot invasion,
where robots seem to fall from the sky, or top of the screen, in random positions and with a
random speed.  Once the robot reaches the ground, the robot will start to move to the right or to
the left and then disappear off from the screen.
"""


import pygame, random

# Initialize Pygame conditions:  screen size 
pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
 
# Load the image of the robot, located in the same folder as the python file 
robot_image = pygame.image.load("robot.png")
robot_width = robot_image.get_width()
robot_height = robot_image.get_height()

# Use of a list to keep track of the robots
robots = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Spawn and add a new robot (approximately two per second) with randomness
    if random.randint(1, 30) == 1:
        new_robot = {
            "x": random.randint(0, screen_width - robot_width),
            # The robot will start above the screen
            "y": -robot_height,
            "falling": True,
            # Randomly choose a horizontal direction for the robot once it reaches the ground
            "speed_x": random.choice([-2, 2]),
            # Randomly choose a vertical speed for the falling robot
            "speed_y": random.randint(2, 5)
        }
        robots.append(new_robot)

    # Create a dark background for the screen
    screen.fill((0, 0, 0))

    # Iterate backwards through list of robots to later remove robots from the list
    for i in range(len(robots) - 1, -1, -1):
        r = robots[i]

        # Case for robots falling from the top of the screen
        if r["falling"]:
            r["y"] += r["speed_y"]
            # Check to see if robot has hit the ground, or bottom of the screen
            if r["y"] + robot_height >= screen_height:
                # Pin the robot to the ground, or bottom of the screen
                r["y"] = screen_height - robot_height
                # Switch the "falling" state of the robot
                r["falling"] = False
        # If the robot is not falling, it is moving horizontally on the ground/bottom of the screen
        else:
            r["x"] += r["speed_x"]

        # Details for animating the robot onto the screen
        screen.blit(robot_image, (r["x"], r["y"]))

        # Robots that have moved off the right/left edges of the screen are removed from the list
        if r["x"] < -robot_width or r["x"] > screen_width:
            robots.pop(i)

    pygame.display.flip()
    clock.tick(60)