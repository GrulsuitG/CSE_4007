import random


BOMB_REWARD = -100.0
GOAL_REWARD = 100.0
BONUS_REWARD = 1.0
WEIGHT = 0.9
TIMES = 5000
WIDTH = 5
HEIGHT = 5

def main():
    
    board = make_board()
    
    table = Q_learning(board)
    row, col = find_start(board)
    path = get_path(table, board)
    max_Q = get_next_reward(table, row, col)
    with open("output.txt", 'w') as f:
        size = len(path)
        for i in range(size):
            f.write(str(path[i])+' ')
        f.write('\n')    
        f.write(str(max_Q))
    
    
    
def make_board():
    with open("input.txt", 'r') as f:
        lines = f.readlines()

    t = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
    row = 0
    for l in lines:
        for col in range(WIDTH):
            t[row][col] = l[col]
        row += 1

    return t

def find_start(board):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] == 'S':
                return i, j

    return -1, -1

def Q_learning(board):
    table = [[.0 for i in range(WIDTH)] for j in range(HEIGHT)]

    start_row, start_col = find_start(board)
    if start_row == -1 and start_col == -1 :
        print("There is no Strat Point")
        exit()
    
    for i in range(TIMES):
        cur_row = start_row
        cur_col = start_col
        Done = False
        while not Done:
            if board[cur_row][cur_col] == 'G':
                table[cur_row][cur_col] = GOAL_REWARD
                Done = True
            elif board[cur_row][cur_col] == 'B':
                table[cur_row][cur_col] = BOMB_REWARD
                Done = True
            else :
                cur_reward = get_reward(board, cur_row, cur_col)
                next_reward = get_next_reward(table, cur_row, cur_col)
                table[cur_row][cur_col] =cur_reward + (WEIGHT * next_reward)
                cur_row, cur_col = random_direction(cur_row, cur_col)
    #  for i in range(HEIGHT):
    #      print(table[i])
    #  print()
    return table

#find next step having highest Q
def next_step(table, row, col):
    
    max_Q = .0
    
    #down direct check
    if row-1 > -1 :
        next_Q = table[row-1][col]
        if max_Q < next_Q :
            max_Q = next_Q
            next_row = row-1
            next_col = col

    #up direct check
    if row+1 < HEIGHT:
        next_Q = table[row+1][col]
        if max_Q < next_Q :
            max_Q = next_Q
            next_row = row+1
            next_col = col

    #left direct check
    if col-1 > -1:
        next_Q = table[row][col-1]
        if max_Q < next_Q :
            max_Q = next_Q
            next_row = row
            next_col = col-1

    #right direct check
    if col+1 < WIDTH:
        next_Q = table[row][col+1]
        if max_Q < next_Q :
            max_Q = next_Q
            next_row = row
            next_col = col+1

    return next_row, next_col

#get current reward
def get_reward(board, row, col):
    tile = board[row][col]

    if tile == 'P' or tile == 'S':
        reward = 0
    elif tile == 'B':
        reward = BOMB_REWARD
    elif tile == 'G':
        reward = GOAL_REWARD
    elif tile == 'T':
        reward = BONUS_REWARD

    return reward

def get_next_reward(table, row, col):
    max_Q = .0
    #down direct check
    if row-1 > -1 :
        next_Q = table[row-1][col]
        if max_Q < next_Q :
            max_Q = next_Q

    #up direct check
    if row+1 < HEIGHT:
        next_Q = table[row+1][col]
        if max_Q < next_Q :
            max_Q = next_Q
        
    #left direct check
    if col-1 > -1:
        next_Q = table[row][col-1]
        if max_Q < next_Q :
            max_Q = next_Q

    #right direct check
    if col+1 < WIDTH:
        next_Q = table[row][col+1]
        if max_Q < next_Q :
            max_Q = next_Q

    return max_Q

def random_direction(row, col):
    can_move = [0, 0, 0, 0]

    up = 0
    down = 1
    right = 2
    left = 3
    if row - 1 > -1 :
        can_move[up] = 1
    if row + 1 < HEIGHT :
        can_move[down] = 1
    if col + 1 < WIDTH :
        can_move[right] = 1
    if col - 1 > -1 :
        can_move[left] = 1
    while True:
        direction = random.randrange(0,4)
        if can_move[direction] == 1:
            break

    next_row = row
    next_col = col
    if direction == up:
        next_row = row-1

    elif direction == down:
        next_row = row+1

    elif direction == right:
        next_col = col+1

    elif direction == left:
        next_col = col-1

    return next_row, next_col
    
        
def get_path(table, board):
    cur_row, cur_col = find_start(board)
    path = []
    while True:    
        path.append(cur_row*WIDTH + cur_col)
        if board[cur_row][cur_col] == 'G':
            break

        cur_row, cur_col = next_step(table, cur_row, cur_col)

    return path
    

if __name__ == "__main__":
    main()

