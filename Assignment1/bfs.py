def bfs(N):
    # N 값이 1일 때에 예외처리
    if N ==1:
        return [1]
    
    #bfs 를 위한 초기값 넣어주기
    queue = []
    for i in range (1, N):
        arr = [0]*(N+1)
        arr[1] = i
        arr[0] = 1
        queue.append(arr)
    #큐가 empty일 때까지 동작
    while(len(queue) != 0 ):
        cur = queue.pop(0)
        
        #print(cur)
        if(cur[0] == N): 
            return cur
        else :     
            for i in range(1, N+1):
                arr = cur[:]
                arr[arr[0]+1] = i
                #pruning 을 하기 위해 지금까지 조건을 위배하지 않는지 확인
                if(check(arr[0]+1, arr)):
                    arr[0] += 1
                    queue.append(arr)
                
            
    return None   


def check(i, ans):
    for k in range(1,i):
        if(ans[i] == ans[k]) or (abs(ans[i]-ans[k]) == i-k):
            return False
    return True
