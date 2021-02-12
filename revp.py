def rever(s):
    s = s[::-1]
    t = s.maketrans("ACTG", "TGAC")
    return s.translate(t)

def rev(s):
    se = set()
    for j in range(4, 13):
        for i in range(len(s)):
            g = s[i:i+j]
            if g == rever(g) and len(g) >= 4 and len(g) <= 12:
                se.add((i+1, len(g)))
    return list(se)

f = open("rosalind_revp.txt")
s = ""
for i in f.readlines():
    if i.startswith(">"):
        s = s + ""
    else:
        s = s + i[:-1]

for i in sorted(rev(s)):
    print(*i)