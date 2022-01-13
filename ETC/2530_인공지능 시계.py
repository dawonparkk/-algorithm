a, b, c = map(int, input().split())
d = int(input())
k = c + d
b += k//60
a += (b//60)
print(a%24, b%60, k%60 )
