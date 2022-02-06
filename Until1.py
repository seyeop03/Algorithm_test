N = 25
K = 3
cnt = 0
while(True):
    if N == 1:
        break
    elif N % K == 0:
        N /= K
        cnt+=1
    else:
        N -= 1
        cnt += 1
    print(N)
print('Execute count: ',cnt)