def check(s):
    if 'iecse' in s.lower():
        print("YES")
    else:
        print("NO")
        
n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
for i in l:
    check(i)