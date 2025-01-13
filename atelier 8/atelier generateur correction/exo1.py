n=int(input('N : '))
the_generator = (x*n  for x in range(n+1))

for v in the_generator:
    print(v, end=" ")
print()