from math import*
N=float(input("Saisir N(0) la quantité initiale de la substance."))
T=float(input("Saisir La demi-vie de la quantité en décomposition ."))
a=float(input(" le nombre d'Euler pour ans."))
t=a*365*24*360
x=(-693*t)/T
print(x)

N1=N*exp(x)
print("la quantité qui reste et n'a pas encore diminué après un temps (t) : ",N1)