def lcsm(l):
    short = l[0]
    l2 = l[1:]
    res = ""
    for i in range(len(short)):
        for j in range(i, len(short)):
            m = short[i:j + 1]
            found = False
            for _ in l2:
                if m in _:
                    found = True
                else:
                    found = False
                    break
            if found and len(m) > len(res):
                res = m
    return res

f = open("rosalind_lcsm.txt")
l = []
n = ""
for i in f.readlines():
    if i.startswith(">"):
        n = n + " "
    else:
        n = n + i[:-1]
l = sorted(list(map(str, n.split())), key=len)

print(lcsm(l))