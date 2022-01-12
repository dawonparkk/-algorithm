a,b= map(int,input().split())
c = int(input())
d = int(b+c)
if (d)>=60:
    if a+int(d/60) >23:
        print('%s %s'%(a+int(d/60)-24,d%60))
    
    else:
        print('%s %s'%(a+int(d/60),d%60))  
else:
    print('%s %s'%(a,d))
