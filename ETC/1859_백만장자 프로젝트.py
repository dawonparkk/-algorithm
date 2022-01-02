#처음에는 생각을 리스트로 만들어서 max값의 index를 구한 뒤 그 index값보다 작은 index 값을 가지고 있는 애들을 찾아 연산을 하면된다고 생각했다.
#그런데 그 이후에 1, 1, 3, 1, 2의 경우와 같이 제일 큰값 뒤에 전날보다 큰값이 생기게 되면 오류가 난다는 것을 알 수 있었다. 
#그래서 max값의 index를 제외하고 다시 리스트를 만들어서 하려고 했는데 코드가 너무 복잡해져 아래와 같이 리스트를 뒤집어서 하는걸 참고해서 해결.

a = int(input())
for i in range(1,a+1):
    b = int(input())
    w = list(map(int,input().split()))
    w=w[::-1]
    m=w[0]
    result=0
    for j in range(len(w)):
        if m>w[j]:
            result+= m -w[j]
        else:
            m=w[j]

    print("#{} {}".format(i,result))

## 잘못된 코드
#a = int(input())
# for i in range(1,a+1):
#     b = int(input())
#     w = list(map(int,input().split()))
#     index  = w.index(max(w))
#     result = 0
#     for j in range(b):
#         if (w.index(w[j]))<index:
#             result+=max(w)-w[j]
#     print("#{} {}".format(i,result))
