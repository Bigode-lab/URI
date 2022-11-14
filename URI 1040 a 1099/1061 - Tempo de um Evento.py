def fibonacci (n):
    v = [0, 1]
    if n > 1:
        for i in range(2, n + 1):
            f = v[i - 1] + v[i - 2]
            v.append(f)
    return v[n]

t = int(input())
for x in range(t):
    n = int(input())
    print(f'Fib({n}) = {fibonacci(n)}')