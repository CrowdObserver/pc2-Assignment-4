def dnaBaseCounter(string):
    print(string.count("A"), string.count("C"), string.count("G"), string.count("T"))

f = open("rosalind_dna.txt")
string = f.readline()
dnaBaseCounter(string)