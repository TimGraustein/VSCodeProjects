# import pygame
# from sys import exit
# # Initialize Pygame
# pygame.init()

# # Set up the display
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 400
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Connect Four")
# clock = pygame.time.Clock()
# test_font = pygame.font.Font('graphics/Pixeltype.ttf', 50)

# sky_surface = pygame.image.load('graphics/Sky.png').convert()
# ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('My game',False,'Black').convert()
# score_rect = score_surf.get_rect(center = (400, 50))


# snail_surface = pygame.image.load('graphics/snail1.png').convert_alpha()
# snail_rect = snail_surface.get_rect(midbottom = (600,300))

# player_surface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
# player_rect = player_surface.get_rect(midbottom = (80,300))

# # Main game loop
# run = True
# while run:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       pygame.quit()
#       exit()
#     #if event.type == pygame.MOUSEMOTION:
#     #  if player_rect.collidepoint(event.pos): print('colision')

#   screen.blit(sky_surface,(0,0))
#   screen.blit(ground_surface,(0,300))
#   pygame.draw.rect(screen, 'Pink', score_rect)
#   screen.blit(score_surf,score_rect)
  
#   snail_rect.x -= 4
#   if snail_rect.right <= 0: snail_rect.left = 800
#   screen.blit(snail_surface,snail_rect)
#   screen.blit(player_surface,player_rect)

#   #if player_rect.colliderect(snail_rect):

#  #mouse_pos = pygame.mouse.get_pos()
#   #if player_rect.collidepoint((mouse_pos)):
#     #print(pygame.mouse.get_pressed())
  

#   #update the display
#   pygame.display.update()
#   clock.tick(60)

import pygame
import numpy as np
from sys import exit
#constants for connect 4 logic
ROWS = 6
COLS = 7
SPACES = ROWS * COLS

#board and logic
board_array = np.zeros((6,7))
current = 1
total_turns = 0
# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Connect Four")
#font
font = pygame.font.SysFont("sans-serif", 100)
#background
background_surf = pygame.image.load('graphics/background.png').convert()
background_rect = background_surf.get_rect(topleft = (0, 0))
#board 
board_surf = pygame.image.load('graphics/board.png').convert_alpha()
board_rect = board_surf.get_rect(topleft = (0, 0))
#token load
token_blue_surf = pygame.image.load('graphics/blue_chip.png').convert_alpha()
token_red_surf = pygame.image.load('graphics/red_chip.png').convert_alpha()
#Game Over text
red_wins_surf = font.render("Red Wins!", True, "Black")
red_rect = red_wins_surf.get_rect()
red_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
blue_wins_surf = font.render("Blue Wins!", True, "Black")
blue_rect = blue_wins_surf.get_rect()
blue_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#functions
def drop_piece(board, col, player):
  for row in range(ROWS-1,-1, -1):
    if board[row, col] == 0:
      board[row, col] = player
      return row
  return None



def check_win(board, row, col, player):
  counter = 1
  #vert
  for r in range(row-1, -1, -1):
    if board[r, col] == player:
      counter += 1
    else:
      break
  for r in range(row+1, ROWS):
    if board[r, col] == player:
      counter += 1
    else:
      break
  if counter >= 4:
    return True
  counter = 1
  #horiz
  for c in range(col-1, -1, -1):
    if board[row, c] == player:
      counter += 1
    else:
      break
  for c in range(col+1, COLS):
    if board[row, c] == player:
      counter += 1
    else:
      break
  if counter >= 4:
    return True
  counter = 1
  #down right
  for i in range(1, min(ROWS-row, COLS-col)):
    if board[row+i, col+i] == player:
      counter += 1
    else:
      break
  #upleft
  for i in range(1, min(row+1, col+1)):
    if board[row-i, col-i] == player:
      counter += 1
    else:
      break
  if counter >= 4:
    return True
  counter = 1
  #upright 
  for i in range(1, min(row+1, COLS-col)):
    if board[row+i, col-i] == player:
      counter += 1
    else:
      break
  #downleft
  for i in range(1, min(ROWS-row, col+1)):
    if board[row-i, col+i] == player:
      counter += 1
    else:
      break
  if counter >= 4:
    return True
  
  return False

clock = pygame.time.Clock()

#adding invisible rectangle to detect clicks
#there are commented out colors for the rectangles for testing
col1 = pygame.Rect(215,50,78,500)
#pygame.draw.rect(screen, 'Red', col1, width=5)
col2 = pygame.Rect(298,50,78,500)
#pygame.draw.rect(screen, 'Red', col2, width=5)
col3 = pygame.Rect(377,50,78,500)
#pygame.draw.rect(screen, 'Red', col3, width=5)
col4 = pygame.Rect(460,50,78,500)
#pygame.draw.rect(screen, 'Red', col4, width=5)
col5 = pygame.Rect(540,50,78,500)
#pygame.draw.rect(screen, 'Red', col5, width=5)
col6 = pygame.Rect(620,50,78,500)
#pygame.draw.rect(screen, 'Red', col6, width=5)
col7 = pygame.Rect(705,50,78,500)
#pygame.draw.rect(screen, 'Red', col7, width=5)



# winner variable for checkwin
winner = 0
# Main game loop
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if col1.collidepoint(mouse_pos):
            row = drop_piece(board_array, 0, current)
            if row is not None:
              total_turns += 1
              if check_win(board_array, row, 0, current):
                winner = current
              current = 1 if current == 2 else 2
        if col2.collidepoint(mouse_pos):
            row = drop_piece(board_array, 1, current)
            if row is not None:
              total_turns += 1
              if check_win(board_array, row, 1, current):
                winner = current
              current = 1 if current == 2 else 2
        if col3.collidepoint(mouse_pos):
            row = drop_piece(board_array, 2, current)
            if row is not None:
              total_turns += 1
              if check_win(board_array, row, 2, current):
                winner = current
              current = 1 if current == 2 else 2
        if col4.collidepoint(mouse_pos):
            row = drop_piece(board_array, 3, current)
            if row is not None:
              total_turns += 1
              if check_win(board_array, row, 3, current):
                winner = current
              current = 1 if current == 2 else 2
        if col5.collidepoint(mouse_pos):
            row = drop_piece(board_array, 4, current)
            if row is not None:
              total_turns += 1
              if check_win(board_array, row, 4, current):
                winner = current
              current = 1 if current == 2 else 2
        if col6.collidepoint(mouse_pos):
            row = drop_piece(board_array, 5, current)
            if row is not None:
              total_turns += 1
              if check_win(board_array, row, 5, current):
                winner = current
              current = 1 if current == 2 else 2
        if col7.collidepoint(mouse_pos):
            row = drop_piece(board_array, 6, current)
            if row is not None:
              total_turns += 1
              if check_win(board_array, row, 6, current):
               winner = current
              current = 1 if current == 2 else 2

  screen.blit(background_surf, background_rect)
  screen.blit(board_surf, board_rect)
  
  for r in range(ROWS):
    for c in range(COLS):
      if board_array[r,c] != 0:
          if board_array[r,c] == 1:
            token_rect = token_red_surf.get_rect(midtop=(253 + c*82, -200 + r*80))
            screen.blit(token_red_surf, token_rect)
          elif board_array[r,c] == 2:
            token_rect = token_blue_surf.get_rect(midtop=(253 + c*82, -200 + r*80))
            screen.blit(token_blue_surf, token_rect)
  if winner == 1:
    screen.blit(red_wins_surf, red_rect)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    exit()

  elif winner == 2:
    screen.blit(blue_wins_surf, blue_rect)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    exit()

  
 #this stuff is just for testing
 #Get current mouse position (x, y)
  #pos = pygame.mouse.get_pos()
  #print(pos) 

    


#update the display
  pygame.display.update()
  clock.tick(60)