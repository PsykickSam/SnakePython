import pygame
import time

pygame.init()

# Game Variables
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
# Positions
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
display_width = 800
display_height = 600
# Clock
clock = pygame.time.Clock()
# Player
snake_block_size = 10
snake_speed = 30
# Font
font_style = pygame.font.SysFont(None, 50)
# Game
display = pygame.display.set_mode((display_width, display_height))
game_over = False
game_over_screen_wait = 2

# Functions
def message(msg, color):
  renderedMessage = font_style.render(msg, True, color)
  display.blit(renderedMessage, [display_width/2, display_height/2])

# Init
pygame.display.update()
pygame.display.set_caption('Snake')

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      print("Snake position: X: {:.2f} | Y: {:.2f}".format(x1, y1))
      if event.key == pygame.K_RIGHT:
        print("Snake moves: RIGHT")
        x1_change = snake_block_size
        y1_change = 0
      elif event.key == pygame.K_LEFT:
        print("Snake moves: LEFT")
        x1_change = -snake_block_size
        y1_change = 0
      elif event.key == pygame.K_UP:
        print("Snake moves: UP")
        x1_change = 0
        y1_change = -snake_block_size
      elif event.key == pygame.K_DOWN:
        print("Snake moves: DOWN")
        x1_change = 0
        y1_change = snake_block_size

  # Check for wall collition
  if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
    game_over = True

  # Update the position of the snake
  x1 += x1_change
  y1 += y1_change

  # Fill the display with white background
  display.fill(white)

  # Draw snake in the screen
  pygame.draw.rect(display, black, [x1, y1, snake_block_size, snake_block_size])

  # Update the screen
  pygame.display.update()

  # Update screen in every 'some' seconds [Define as snake speed]
  clock.tick(snake_speed)

# 'Game Over' Screen
message("Game Over", red)

# Update the screen
pygame.display.update()

# Wait for some time
time.sleep(game_over_screen_wait)

# Exit
pygame.quit()
quit()
