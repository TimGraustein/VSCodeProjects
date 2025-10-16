import pygame
from sys import exit
# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Connect Four")
clock = pygame.time.Clock()
test_font = pygame.font.Font('graphics/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game',False,'Black').convert()

snail_surface = pygame.image.load('graphics/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

# Main game loop
run = True
while run:
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  screen.blit(sky_surface,(0,0))
  screen.blit(ground_surface,(0,300))
  screen.blit(text_surface,(300,50))
  
  snail_rect.x -= 4
  if snail_rect.right <= 0: snail_rect.left = 800
  screen.blit(snail_surface,snail_rect)
  screen.blit(player_surface,player_rect)

  #if player_rect.colliderect(snail_rect):

  mouse_pos = pygame.mouse.get_pos()
  if player_rect.collidepoint((mouse_pos)):
    print(pygame.mouse.get_pressed())
  

  #update the display
  pygame.display.update()
  clock.tick(60)
