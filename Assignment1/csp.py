def csp(N):
    if N ==1:
        return [1]
    
    s = []
    for i in range(N, 0, -1):
        arr = [0]*(N+1)
        arr[1] = i
        arr[0] = 1
        s.append(arr)
    
    while(len(s) != 0):
        cur = s.pop()
        print(cur)
        if(cur[0] == N):
            return cur
        else :
            for i in range(1, N+1):
                arr = cur[:]
                arr[arr[0]+1] = i

                if(check(arr[0]+1, arr)):
                    arr[0] += 1
                    s.append(arr)
    
    return None


def check(i, ans):
    for k in range(1,i):
        if(ans[i] == ans[k]) or (abs(ans[i]-ans[k]) == i-k):
            return False
    return True


    
