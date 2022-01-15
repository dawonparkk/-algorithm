def calc(n,emo):
    if emo =='@':
        return (n*3)
    elif emo =='%':
        return (n+5)
    elif emo =='#':
        return (n-7)

a = int(input())
for i in range(a):
    list=input().split()
    c = float(list.pop(0))
    for j in list:
        c = calc(c,j)
    print("%.2f" % c)
