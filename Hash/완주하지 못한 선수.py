# 프로그래머스
def solution(participant, completion):
    d = dict()
    for p in participant:
        d[p] = d.get(p,0) + 1
        print(d[p], d)
    for c in completion:
        d[c] -=1
        if d[c] == 0:
            del d[c]    
    return list(d.keys()).pop()
