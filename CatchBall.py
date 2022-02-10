import pygame
from random import randint

pygame.init()

# initialize variables to keep track of the number of balls caught and the total number of balls dropped
score = 0
total = 0

# create a font to write the score in
font = pygame.font.SysFont('monospace', 50)

# create dictionaries for the settings of everything
display = {
    "width": 800,
    "height": 600
}

paddle = {
    "width": 200,
    "height": 20,
    "x": 300,
    "y": 580,
    "velocity": 25
}

ball = {
    "radius": 15,
    "y": 30,
    # random x-coordinate between 0 and the width of the display (800)
    "x": randint(0, display["width"]),
    "velocity": 15
}

# create a window and launch the game
# 800 width, 600 height
window = pygame.display.set_mode((display["width"], display["height"]))

pygame.display.set_caption("Catch Ball")

run = True
while run:
    pygame.time.delay(100)

    # fill the window with white
    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        # move the paddle to the left
        paddle["x"] -= paddle["velocity"]

    if keys[pygame.K_RIGHT]:
        # move the paddle to the right
        paddle["x"] += paddle["velocity"]

    # increase the y-coordinate of the ball (so it goes down)
    ball["y"] += ball["velocity"]

    # draw the ball on the screen
    pygame.draw.circle(window, (0, 0, 255), (ball["x"], ball["y"]), ball["radius"])

    # draw the paddle on the screen
    pygame.draw.rect(window, (255, 0, 0), (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

    # check if the ball hits the paddle
    if ball["y"] + ball["radius"] >= paddle["y"]:
        if ball["x"] > paddle["x"] and ball["x"] < paddle["x"] + paddle["width"]:
            # add 1 to the current score
            score += 1
        # add 1 to the total number of balls dropped on the screen
        total += 1

        # reset the ball's position at the top of the screen and at some random x-coordinate
        ball["y"] = 0
        ball["x"] = randint(0, display["width"])

    # write the score on a surface in black
    text_surface = font.render("Score: {0}/{1}".format(score, total), False, (0, 0, 0))
    # put the surface on the window at coordinates (10, 10) - top left of the screen
    window.blit(text_surface, (10, 10))

    # update the screen
    pygame.display.update()

pygame.quit()

