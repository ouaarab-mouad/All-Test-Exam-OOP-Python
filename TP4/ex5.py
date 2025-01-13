N=int(input("entrez la valeure : "))
M=int(input("entrez le clés : "))
dictionnaire={}
for i in range(N,M+1):
    dictionnaire[i]=i**2

print(dictionnaire)