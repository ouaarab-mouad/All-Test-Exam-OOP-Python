N = int(input('N='))
M = int(input('M='))
D = {k:k**2 for k in range(N,M+1)}
'''
equivalent à:
for k in range(N,M+1):
    D[k]=k**2
    '''


print(D)