import pygame

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

display = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption('Snake')
game_over = False

# Position
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0

# Clock
clock = pygame.time.Clock()

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      print("Snake position: X: {:.2f} | Y: {:.2f}".format(x1, y1))
      if event.key == pygame.K_RIGHT:
        print("Snake moves: RIGHT")
        x1_change = 10
        y1_change = 0
      elif event.key == pygame.K_LEFT:
        print("Snake moves: LEFT")
        x1_change = -10
        y1_change = 0
      elif event.key == pygame.K_UP:
        print("Snake moves: UP")
        x1_change = 0
        y1_change = -10
      elif event.key == pygame.K_DOWN:
        print("Snake moves: DOWN")
        x1_change = 0
        y1_change = 10

  x1 += x1_change
  y1 += y1_change

  display.fill(white)

  pygame.draw.rect(display, black, [x1, y1, 10, 10])
  pygame.display.update()

  clock.tick(30)

pygame.quit()
quit()
