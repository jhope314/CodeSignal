from collections import defaultdict

def solution(a):
    answer = -1
    indexer = defaultdict(int)
    indexer[a[0]] = 0.5 
    for i in range(1, len(a)): 
        if indexer[a[i]] == 0:
            indexer[a[i]] = i
        else: 
            return a[i]
    return answer



