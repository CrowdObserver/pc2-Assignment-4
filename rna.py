def dnaToRna(s):
    n = ""
    for i in s:
        if i == "T":
            n = n + "U"
        else:
            n = n + i
    return n

f = open("rosalind_rna.txt")
s = f.readline()
print(dnaToRna(s))