import numpy as np
import sys


print("Num of row: ")
row= int(input())
print("Num of col: ")
col=int(input())

m=[]
for i in range(row):
    a=[]
    for j in range(col):
        print("A[",i,"][",j,"]")
        n=float(input())
        a.append(n)
    m.append(a) 



b=[]

for i in range(1):
    for j in range(row):
        print("B[",i,"][",j,"]")
        n=float(input())
        b.append(n)

n=len(b)

for i in range(n):
    if m[i][i]==0:
        sys.exit('Divisor by zero')
    for j in range(n):
        if i!=j:
            ratio=m[j][i]/m[i][i]
            for k in range(n):
              m[j][k]-= ratio*m[i][k]
            b[j] -= ratio*b[i]

x=np.zeros(n)

for i in range(n):
    x[i]=b[i]/m[i][i]
print(m)
print("   ")
print(x)