from itertools import product

def lexf(l, n):
    for i in list(product(l, repeat=n)):
        print("".join(list(i)))

f = open("rosalind_lexf.txt")
l = "".join(f.readline().split())
n = int(f.readline())
lexf(l, n)