def solution(N):
    # write your code in Python 3.6
    i=N
    
    find_one=False
    cnt=0
    result=0
    while i:
            
        if i & 1:
            if find_one:
                result = max(cnt,result)
            else:
                find_one=True
            cnt=0
        else:
            cnt+=1
        
        i >>= 1
    return result
