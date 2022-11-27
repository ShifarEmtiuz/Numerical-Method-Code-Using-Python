import numpy as np

def determineOfMatrix(mat):
    determine=  mat[0][0]*(mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1])-mat[0][1]*(mat[1][0]*mat[2][2]-mat[2][0]*mat[1][2])+mat[0][2]*(mat[1][0]*mat[2][1]-mat[1][1]*mat[2][0])
    return determine

def soluton(cofe):
    Dx=[
      [cofe[0][3],cofe[0][1],cofe[0][2]],
      [cofe[1][3],cofe[1][1],cofe[1][2]],
      [cofe[2][3],cofe[2][1],cofe[2][2]],



    ]

    Dy=[
      [cofe[0][0],cofe[0][3],cofe[0][2]],
      [cofe[1][1],cofe[1][3],cofe[1][2]],
      [cofe[2][0],cofe[2][3],cofe[2][2]],



    ]
    Dz =[
      [cofe[0][0],cofe[0][1],cofe[0][3]],
      [cofe[1][0],cofe[1][1],cofe[1][3]],
      [cofe[2][0],cofe[2][1],cofe[2][3]],



    ]

    D=determineOfMatrix(cofe)
    Dx=determineOfMatrix(Dx)
    Dy=determineOfMatrix(Dy)
    Dz=determineOfMatrix(Dz)

    x=Dx/D
    y=Dy/D
    z=Dz/D
    print("value of main: ",D)
    print("value of Dx: ",Dx)
    print("value of Dy: ",Dy)
    print("value of Dz: ",Dz)
    return [x,y,z]

def main():
    cofe=[]
    row=3
    col=4
    for i in range(row):
        arr=[]
        print("i :",i)
        for j in range(col):
            n=float(input())
            arr.append(n)
        cofe.append(arr)
    print(cofe)
    result=soluton(cofe)
    print("value of x y z:",result)
if __name__=="__main__":
    main()