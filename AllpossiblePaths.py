def numberofPaths(m,n):
    if m==1 or n==1:
        return 1
    return numberofPaths(m-1,n)+numberofPaths(m,n-1)
m=5
n=3
print("Number of Paths:", numberofPaths(m, n))