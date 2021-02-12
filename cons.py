def consensus(l):
    cons = ""
    A = []
    C = []
    T = []
    G = []
    dic = {"A" : 0, "C" : 0, "T" : 0, "G" : 0}
    for i in range(len(l[0])):
        for j in l:
            if j[i] == "A":
                dic["A"] = dic["A"] + 1
            elif j[i] == "C":
                dic["C"] = dic["C"] + 1
            elif j[i] == "T":
                dic["T"] = dic["T"] + 1
            elif j[i] == "G":
                dic["G"] = dic["G"] + 1
        cons = cons + max(dic, key=dic.get)
        A.append(dic["A"])
        C.append(dic["C"])
        T.append(dic["T"])
        G.append(dic["G"])
        dic = {"A": 0, "C": 0, "T": 0, "G": 0}
    print(cons)
    print("A:", *A)
    print("C:", *C)
    print("G:", *G)
    print("T:", *T)

f = open("rosalind_cons.txt")
s = ""
for i in f.readlines():
    if i.startswith(">"):
        s = s + " "
    else:
        s = s + i[:-1]
l = list(map(str, s.split()))
consensus(l)