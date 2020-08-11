import time
import pygame
import random

# Initialize
pygame.init()

# Game Variables
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
# Clock
clock = pygame.time.Clock()
# Snake
snake_block_size = 10
snake_speed = 30
# Food
food_block_size = 10
# Positions
display_width = 800
display_height = 600
x1 = display_width / 2
y1 = display_height / 2
x1_change = 0
y1_change = 0
foodx = round(random.randrange(0, display_width - snake_block_size) / 10.00) * 10.00
foody = round(random.randrange(0, display_height - snake_block_size) / 10.00) * 10.00
# Font
font_size = 30
font_size_factor = 10 # Factor: 30 -> 10, 60 -> 20, 50 -> 16.5 [(Centralization) Divisible of 3 (Normalize Float with {}.5)]
font_style = pygame.font.SysFont(None, font_size)
# Game
display = pygame.display.set_mode((display_width, display_height))
game_quit_screen_wait = 2
game_over = False
game_close = False
should_quit = False

# Init
pygame.display.update()
pygame.display.set_caption('Snake')

# Functions
def quit():
  pygame.quit()
  quit()

def reset():
  global game_over, game_close, x1, y1, foodx, foody

  game_over = False
  game_close = False
  x1 = display_width / 2
  y1 = display_height / 2
  foodx = round(random.randrange(0, display_width - snake_block_size) / 10.00) * 10.00
  foody = round(random.randrange(0, display_height - snake_block_size) / 10.00) * 10.00

def message(msg, color):
  global display_width, display_height

  halfLengthOfMsg = int(len(msg) / 2)
  renderedMessage = font_style.render(msg, True, color)
  display.blit(renderedMessage, [int((display_width / 2) - (halfLengthOfMsg * font_size_factor)), 50])

def loop():
  global x1, x1_change, y1, y1_change, foodx, foody, snake_speed, game_over, game_close, should_quit

  if game_over == True:
    return

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
      should_quit = True
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
    print("Snake collide with the wall")
    game_close = True

  # Update the position of the snake
  x1 += x1_change
  y1 += y1_change

  # Fill the display with white background
  display.fill(white)

  # Draw snake and food in the screen
  pygame.draw.rect(display, red, [int(foodx), int(foody), food_block_size, food_block_size])
  pygame.draw.rect(display, black, [int(x1), int(y1), snake_block_size, snake_block_size])

  # Update the screen
  pygame.display.update()

  # Collide with food
  if x1 == foodx and y1 == foody:
    print("Food is yummy!!!")

  # Update screen in every 'some' seconds [Define as snake speed]
  clock.tick(snake_speed)

def close():
  global game_close, game_over, should_quit

  display.fill(white)
  message("Game Over! Press (Q) - Quit or (P) - Play Again", red)

  # Update the current screen
  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
      should_quit = True
      game_close = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        game_over = True
        game_close = False
      if event.key == pygame.K_p:
        reset()
        main()

def main():
  global should_quit, game_over, game_close, game_quit_screen_wait

  while not game_over:
    while game_close == True:
      close()
    loop()

  if should_quit == True:
    print("Exit from game!!!")
    quit()

  # 'Game Over' Screen
  message("Finish", red)

  # Update the screen
  pygame.display.update()

  # Wait for some time
  time.sleep(game_quit_screen_wait)

  # Quit game
  quit()

if __name__ == '__main__':
  main()
