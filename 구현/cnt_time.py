### 00시 00분 00초 ~ N시 59분 59초까지 3이 하나라도 들어있다면 count!

N = 5

cnt = 0


for i in range(N+1):
    for j in range(60):
        for k in range(60):
           if '3' in str(i) or '3' in str(j) or '3' in str(k):
               cnt += 1

print(cnt)