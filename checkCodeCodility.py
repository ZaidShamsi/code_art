def sumDigit(N):
    N = list(str(N))
    sum = 0
    for i in range(0, len(N)):
        sum = sum + int(N[i])
    return sum

def solution(N):
    # write your code in Python 3.6
    ans = sumDigit(N)
    check = N
    for i in range(0, 1000000):
        check = check + 1
        hola = sumDigit(check)
        if hola != ans:
            pass
        else:
            break
    return check

a = 28
sumDigit45 = sumDigit(a)
print(sumDigit45)
smallestInt = solution(a)
print(smallestInt)
