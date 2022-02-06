import time

M = 7
K = 2
L = [3,4,3,4,3,4,3]
answer = 0

L.sort()

class loopbreak(Exception):
    pass

try:
    while M > 0:
        for i in range(K):
            answer += L[len(L) - 1]
            M -= 1
            if M == 0:
                raise loopbreak()

        answer += L[len(L) - 2]
        M -= 1
        if M == 0:
            break
except loopbreak:
    pass

print(answer)
