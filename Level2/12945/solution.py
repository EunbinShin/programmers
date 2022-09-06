def solution(n):
    fibo = []
    fibo.append(0) # F(0) = 0
    fibo.append(1)  # F(1) = 1

    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo[n] % 1234567