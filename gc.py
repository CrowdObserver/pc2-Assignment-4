def GCcontent(n, s):
    l = []
    for i in range(len(n)):
        count = 0
        count += s[i].count("G") + s[i].count("C")
        l.append(count/len(s[i]))
    print(n[l.index(max(l))])
    print(str(max(l)*100)[:9])

f = open("rosalind_gc.txt")
n = []
tmp = ""
for i in f.readlines():
    if i.startswith(">"):
        n.append(i[1:-1])
        tmp = tmp + " "
    else:
        tmp = tmp + i[:-1]
s = tmp.split()

GCcontent(n, s)