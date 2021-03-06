"""

Pygame-based program that counts down to a set time.
Pygame loop inspired by: http://programarcadegames.com/index.php?chapter=introduction_to_graphics

Author: jjantonsen

Date: Sep 28 2017

"""

# Imports
import pygame
import time
import datetime

pygame.init()

# Set pygame variables
BLACK = (0,0,0)
WHITE = (255,255,255)
screen_w = 1824 # screen width in pixels
screen_h = 984 # screen height in pixels
size = (int(screen_w),int(screen_h))
screen = pygame.display.set_mode(size)
pygame.display.set_caption("COUNTDOWN")

# Initialize time variable (change the variable 'then' to your desired goal)
then = datetime.datetime(2017,10,6,19,30,0) # year, month, day, h, m, s

# Display 
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get(): # Quit if key is pressed
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            done = True
            
    # Calculate current time difference, generate string
    now = datetime.datetime.now()
    diff = then-now
    days = diff.days
    hours, seconds = divmod(diff.seconds,3600)
    minutes, seconds = divmod(seconds,60)
    if then <= now:
        diff_str = "DONE"
    else:
        diff_str = "{}D:{}H:{}M:{}S".format(days,hours,minutes,seconds)

    # Draw
    screen.fill(BLACK)
    font = pygame.font.SysFont('Calibri', 220, True, False)
    text = font.render(diff_str,True,WHITE)
    screen.blit(text, [250, 250])

    # Display time, and set frames per second
    pygame.display.flip()
    clock.tick(20)
