def add(matrix,i,j,m,n):
    newRow=[-1,-1,-1,0,1,1,1,0]
    newCol=[-1,0,1,1,1,0,-1,-1]
    sum=0
    for x in range(8):
        row=i+newRow[x]
        col=j+newCol[x]
        if(check(row,col,m,n)):
            sum=sum+matrix[row][col]
    return sum
def check(row,col,m,n):
    if row>-1 and col >-1 and row<m and col<n:
        return True
    else:
        return False

m,n=map(int,input().split())
matrix=[]

for i in range(m):
	li=list(map(int,input().split()))
	matrix.append(li)
a = [[int(0) for j in range(n)] for i in range(m)]

for i in range(m):
	for j in range(n):
		a[i][j]=add(matrix,i,j,m,n)

for i in range(m):
	for j in range(n):
	    print(a[i][j],end="")
	    if(j<n-1):
	        print(end=" ")
	print()
