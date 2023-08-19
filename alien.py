import sys
invasion.py
import pygame
def run_game():
 # Initialize game and create a screen object.
u pygame.init()
v screen = pygame.display.set_mode((1200, 800))
 pygame.display.set_caption("Alien Invasion")
 # Start the main loop for the game.
w while True:
 # Watch for keyboard and mouse events.
x for event in pygame.event.get():
y if event.type == pygame.QUIT:
 sys.exit()
 
 # Make the most recently drawn screen visible.
z pygame.display.flip()
run_game()
