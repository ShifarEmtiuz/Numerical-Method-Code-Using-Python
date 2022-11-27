import numpy as np

print("NUM Of Row: ")
row=int(input())
print("NUM Of Col: ")
col=int(input())
m=[]
b=[]
for i in range(row):
    a=[]
    for j in range(col-1):
        print("A[",i,"][",j,"] :")
        n=float(input())
        a.append(n)
    m.append(a)

for i in range(1):
    for j in range(row):
        print("B[",i,"][",j,"] :")
        n=float(input())
        b.append(n)

n=len(b)

for k in range(n-1):
    for i in range(k+1, n):
        ratio=m[i][k]/m[k][k]
        for j in range(k,n-1):
            m[i][j]-=ratio*m[k][j]
        b[i]-=ratio*b[k]

print(m)

x=np.zeros(n)
x[n-1]=b[n-1]/m[n-1][n-1]
for k in range(n-2,-1,-1):
      sum_j=0
      for j in range(k+1,n):
        sum_j+=m[k][j]*x[j]
      x[k]=(b[k]-sum_j)/m[k][k]

print(x)
      
       
    




