s=input()
n=int(s.split()[0])
m=int(s.split()[1])
k1=int(s.split()[2])
k2=int(s.split()[3])
x=int(s.split()[4])

def maximum(n,m,k1,k2,x):
    x2=x
    count=0
    for i in range(x2):
        if x>0:
            if (k1<k2 and n!=0) or m==0:
                if x-k1>=0:
                    x=x-k1
                    count+=1
                    n-=1
            elif (k2<k1 and m!=0) or n==0:
                if x-k2>=0:
                    x=x-k2
                    count+=1
                    m-=1

        else:
            break
    return count
def minimum(n,m,k1,k2,x):
    x2=x
    count=0
    for i in range(x2):
        if x>0:
            if ((k1>k2) and x-(k1-1)>=0):
                while n>0:
                    if x>0:
                        x=x-(k1-1)
                        n-=1
                    else:
                        break
            elif ((k2>=k1) and x-(k2-1)>=0):
                while m>0:
                    if x>0:
                        x=x-(k2-1)
                        m-=1
                    else:
                        break
        else:
            break
    if n==0 and m==0:
        count=x
    elif n==0 and m!=0:
        while m>0:
            if x>=0:
                x=x-(k2-1)
                m-=1
            else:
                count=x
    elif m==0 and n!=0:
        while n>0:
            if x>=0:
                x=x-(k1-1)
                n-=1
            else:
                count=x
    else:
        x=0
    count=x
    return(count)
n1=maximum(n,m,k1,k2,x)
n2=minimum(n,m,k1,k2,x)
print(n2,n1)