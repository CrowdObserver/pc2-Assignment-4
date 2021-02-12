def MotifFinder(s, m):
    l = []
    for i in range(len(s)):
        if s.startswith(m, i):
            l.append(i+1)
    print(*l)

f = open("rosalind_subs.txt")
s = str(f.readline())[:-1]
m = str(f.readline())[:-1]
MotifFinder(s, m)