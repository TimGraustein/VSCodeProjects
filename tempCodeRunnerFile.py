def check_win(board, row, col, player):
#   counter = 1
#   #vert
#   for r in range(row-1, -1, -1):
#     if board[r, col] == player:
#       counter += 1
#     else:
#       break
#   for r in range(row+1, ROWS):
#     if board[r, col] == player:
#       counter += 1
#     else:
#       break
#   if counter >= 4:
#     return True
#   counter = 1
#   #horiz
#   for c in range(col-1, -1, -1):
#     if board[row, c] == player:
#       counter += 1
#     else:
#       break
#   for c in range(col+1, COLS):
#     if board[row, c] == player:
#       counter += 1
#     else:
#       break
#   if counter >= 4:
#     return True
#   counter = 1
  
#   #upleft
#   for i in range(1, min(row+1, col+1)):
#     if board[row-i, col-i] == player:
#       counter += 1
#     else:
#       break
#   if counter >= 4:
#     return True
#   #down right
#   for i in range(1, min(ROWS-row, COLS-col)):
#     if board[row+i, col+i] == player:
#       counter += 1
#     else:
#       break
#   counter = 1
#   #downleft
#   for i in range(1, min(ROWS-row, col+1)):
#     if board[row-i, col+i] == player:
#       counter += 1
#     else:
#       break
#   if counter >= 4:
#     return True
#   #upright 
#   for i in range(1, min(row+1, COLS-col)):
#     if board[row+i, col-i] == player:
#       counter += 1
#     else:
#       break
#   return False