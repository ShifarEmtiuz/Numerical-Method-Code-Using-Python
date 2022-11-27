import numpy as np


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


for k in range(n-1):
    for i in range(k+1, n):
        ratio= m[i][k]/m[k][k]
        for j in range(k, n-1):
            m[i][j]=m[i][j]-ratio*m[k][j]
        b[i]=b[i]-ratio*b[k]


x=np.zeros(n)

x[n-1]=b[n-1]/m[n-1][n-1]

for k in range(n-2,-1,-1):
    sum_j=0
    for j in range(k+1,n):
        sum_j+=m[j][k]*b[j]
    x[k]=b[k]-sum_j/m[k][k]
print(m)
print("     ")
print(b)
print("     ")
print(x)

