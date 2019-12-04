def fun(a,n,l,s):
    if n==0:
        return
    else:
        for i in range(s,l):
            for j in range(s,l):
                if((i==s and j==s) or (i==l-1 and j==l-1) or (i==s and j==l-1) or (i==l-1 and j==s)):
                    a[i][j]=n
                elif(i==s or i==l-1):
                    if(j<int(len(a)+1)/2):
                        a[i][j]=a[i][j-1]-1
                    else:
                        a[i][j]=a[i][j-1]+1
            for k in range(s+1,l-1):
                if(i==s or i==l-1):
                    if(k<int(len(a)+1)/2):
                        a[k][i]=a[k-1][i]-1 
                    else:
                        a[k][i]=a[k-1][i]+1 
        fun(a,n-1,l-1,s+1)
    return a
n=int(input())
row=n
col=n
l=(n*2)-1
a = [[int(0) for j in range(l)] for i in range(l)]
x=fun(a,col,l,s=0) 
for i in range(l):
    for j in range(l):
        print(x[i][j],end="")
        if(j<l-1):
            print(end=" ")
    print()
