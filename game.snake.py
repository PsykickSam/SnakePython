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
yellow = (255, 255, 102)
green = (50, 153, 213)
# Clock
clock = pygame.time.Clock()
# Snake
snake_block_size = 20
snake_speed = 20
snake_list = []
snake_length = 1
# Food
food_block_size = 20
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
# scrore_font = pygame.font.SysFont("comicsansms", font_size)
# Game
display = pygame.display.set_mode((display_width, display_height))
game_quit_screen_wait = 2
game_over = False
game_close = False
should_quit = False
score = 0

# Init
pygame.display.update()
pygame.display.set_caption('Snake')

# Functions
def quit():
  pygame.quit()
  quit()

def snake(snake_list):
  global display, snake_block_size

  for body in snake_list:
    pygame.draw.rect(display, black, [int(body[0]), int(body[1]), snake_block_size, snake_block_size])

def reset():
  global game_over, game_close, x1, y1, foodx, foody, snake_list, snake_length

  score = 0
  game_over = False
  game_close = False
  x1 = display_width / 2
  y1 = display_height / 2
  snake_list = []
  snake_length = 1
  foodx = round(random.randrange(0, display_width - snake_block_size) / 10.00) * 10.00
  foody = round(random.randrange(0, display_height - snake_block_size) / 10.00) * 10.00

def message(msg, color, top_placement = 50):
  global font_style, display_width, display_height

  halfLengthOfMsg = int(len(msg) / 2)
  renderedMessage = font_style.render(msg, True, color)
  display.blit(renderedMessage, [int((display_width / 2) - (halfLengthOfMsg * font_size_factor)), top_placement])

def loop():
  global x1, x1_change, y1, y1_change, foodx, foody, snake_speed, \
    game_over, game_close, should_quit, snake_length, score

  if game_over == True:
    return

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
      should_quit = True
    if event.type == pygame.KEYDOWN:
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

  # Draw food in the screen
  pygame.draw.rect(display, green, [int(foodx), int(foody), food_block_size, food_block_size])

  # Draw snake in the screen
  snake_head = []
  snake_head.append(x1)
  snake_head.append(y1)
  snake_list.append(snake_head)
  if len(snake_list) > snake_length:
    del snake_list[0]

  # Check snake head collition
  for x in snake_list[:-1]:
    if x == snake_head:
      game_close = True

  # Create the snake
  snake(snake_list)

  # Update the screen
  pygame.display.update()

  # Collide with food
  # Checking the head is coliding with any part of the food
  if (abs(x1 - foodx) >= (0) and abs(x1 - foodx) <= (food_block_size)) and \
  (abs(y1 - foody) >= (0) and abs(y1 - foody) <= (food_block_size)):
    print("Collide with food!!!")
    foodx = round(random.randrange(0, display_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block_size) / 10.0) * 10.0
    snake_length += 1
    score += 1

  # Update screen in every 'some' seconds [Define as snake speed]
  clock.tick(snake_speed)

  print("Snake X: {:.2f} | Y: {:.2f}, Food X: {:.2f} | Y: {:.2f}".format(x1, y1, foodx, foody))
  print("Score: " + str(score))

def close():
  global game_close, game_over, should_quit, score

  display.fill(white)
  message("Score: " + str(score), red)
  message("Game Over! Press (Q) - Quit or (P) - Play Again", red, top_placement=100)

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
  global should_quit, game_over, game_close, game_quit_screen_wait, display

  # Main game loop
  while not game_over:
    # Close loop
    while game_close == True:
      close()
    loop()

  # Trigger direct quit
  if should_quit == True:
    print("Quit!!!")
    quit()

  # Fill screen
  display.fill(white)

  # 'Game Over' screen
  message("Finish", red)

  # Update the screen
  pygame.display.update()

  # Wait for some time
  time.sleep(game_quit_screen_wait)

  # Quit game
  quit()

if __name__ == '__main__':
  main()
