# MAX=100000
class Func: # Func(x)=ax+b
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.s=0
def cross(f,g):
    return (g.b-f.b)/(f.a-g.a)

F=[]
dp=[0]
N=int(input())
for i in range(N):F.append(0)
A=list(map(int,input().split()))
B=list(map(int,input().split()))
top=0
fpos=0
for i in range(1,N):
    G=Func(B[i-1],dp[i-1])
    while(top>0):
        G.s=cross(F[top-1],G)
        if(F[top-1].s<G.s):break
        top-=1
        if(top==fpos):fpos-=1
    F[top]=G
    top+=1
    X=A[i]
    while(fpos+1<top and F[fpos+1].s<X):fpos+=1
    dp.append(F[fpos].a*X+F[fpos].b)
print(dp[N-1])

