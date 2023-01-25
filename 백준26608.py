import math
N,M,k=input().split()
N,M,k=int(N),int(M),int(k)
# print(N,M,k)
# if(not(1<=N<=300000 and 1<=M<=100000 and 1<=k<=100)):
#     raise Exception("범위 밖의 값입니다.")
A=[]#걸리는 시간
B=[]#만족도
for i in range(N):
    a,b=input().split()
    a,b=int(a),int(b)
    # if(not(1<=a<=10e9 and 1<=b<=10e9)):
    #     raise Exception("범위 밖의 값입니다.")
    A.append(a)
    B.append(b)
# print(A,B)
# print("-------------")
for j in range(1,M+1):
    result=[]
    for i in range(N):
        result.append((B[i]-k*j)/(A[i]+k*j))
    # print(max(result))
    r=max(result)
    a=A[result.index(r)]+k*j
    b=B[result.index(r)]-k*j
    GCD=math.gcd(a,b)
    if(r==0):
        print("0/0")
    else:
        print(str(int(b/GCD))+"/"+str(int(a/GCD)))