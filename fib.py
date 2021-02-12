def fib(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1, k) + fib(n - 2, k)*k

f = open("rosalind_fib.txt")
n, k = map(int, f.readline().split())
print(fib(n, k))