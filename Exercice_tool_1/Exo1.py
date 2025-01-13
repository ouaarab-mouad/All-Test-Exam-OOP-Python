from math import hypot as ily, pi as p
r=float(input("saisir R :"))
h=float(input("saisir H : "))
ily(r,h)
s=p*r*ily(r,h)
print("Surface et : ", round(s,2))
