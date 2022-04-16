# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    minA = min(A)
    maxA = max(A)
    notinA = []
    for i in range(minA, maxA+1):
        if i in A:
            pass
        else:
            notinA.append(i)
    if len(notinA) == 0:
        smallestPosInt = max(A)+1
    else:
        smallestPosInt = max(notinA)
    return smallestPosInt

A = [-1, -3]

smallestPosInt = solution(A)
print(smallestPosInt)
