import random
import copy

TIME = 1000 #hill climb 을 시도할 횟수

def hc(N):
    
    if N == 1:
        return [1]

    
    # 해를 항상 찾는 방법이 아니기 때문에 반복해서 시도
    for i in range(TIME):
        
        board = random_board(N)
        '''
        for i in range(N):
            print(board[i])
        '''
        
        result = climb(board, N)
        
        if result :
           
            return result

    #주어진 횟수만큼 시도한 후에도 해를 못 찾는 다면 솔루션이 없다고 판단
    return None
    
def climb(board, N):

    min_board = board
    min_h = heuristic(board, N)
    
    cur_h = min_h    
    for i in range(N):
        idx = board[i].index(1)

        board[i][idx] = 0
        
        for j in range(N):

            if j != idx:
                board[i][j] = 1

                h = heuristic(board, N)
                
                if h < min_h:
                    min_h = h
                    min_board = copy.deepcopy(board)
                    
            board[i][j] = 0

        board[i][idx] = 1

    if cur_h == min_h:
        return None

    if min_h == 0:
        return min_board
    
    return climb(min_board, N)

def random_board(N):
    board = []
    rlist = []
    for i in range(N):
        
        r = random.randint(0, N-1)
        #행 하나에 하나의 값만 들어가도록 중복 제거
        while r in rlist :
            r = random.randint(0,N-1)
        rlist.append(r)
        
        row = [0]*N
        row[r] = 1
        board.append(row)
    return board



def heuristic(board, N):
    h = 0
    for i in range(N) :
        for j in range(N):
            if board[i][j] :

                #가로 공격 계산
                for k in range(N):
                    if board[i][k] and k != j:
                        h += 1

                #세로 공격 계산        
                for k in range(N):
                    if board[k][j] and k != i:
                        h += 1

                #대각선 공격 계산
                x, y = i-1, j-1
                while x >= 0 and y >= 0:
                    if board[x][y] :
                        h += 1
                    x, y = x-1, y-1

                x, y = i+1, j+1
                while x < N and y < N :
                    if board[x][y]:
                        h += 1
                    x, y = x+1, y+1

                x, y = i-1, j+1
                while x >= 0 and y < N :
                    if board[x][y]:
                        h += 1
                    x, y = x-1, y+1

                x, y = i+1, j-1
                while x < N and y >= 0 :
                    if board[x][y]:
                        h += 1
                    x, y = x+1, y-1

    # 중복 체크를 안했기 때문에 2로 나누어 준다.
    return h/2

