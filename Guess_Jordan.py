import sys

import numpy as np

print("Num Of Variable: ")
n=int(input())
a=np.array([
    [3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]
])

for i in range(n):
    if a[i][i]==0:
        sys.exit('Divition by zero')
    for j in range(n):
        if i != j:
            ratio=a[j][i]/a[i][i]
            for k in range(n+1):
              a[j][k]-=ratio*a[i][k]
x=np.zeros(n)
for i in range(n):
    x[i]=a[i][n]/a[i][i]

print(a)
print("   ")
print(x)