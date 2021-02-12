def revc(s):
    n = ""
    for i in s:
        if i == "A":
            n = n + "T"
        elif i == "T":
            n = n + "A"
        elif i == "C":
            n = n + "G"
        elif i == "G":
            n = n + "C"
    return n[::-1]


f = open("rosalind_revc.txt")
s = f.readline()
print(revc(s))