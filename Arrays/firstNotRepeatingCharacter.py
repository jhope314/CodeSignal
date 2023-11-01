from collections import defaultdict

def solution(s):
    unique = []
    count = defaultdict(int)
    for i in range(len(s)):
        if count[s[i]] == 0:
            unique.append(s[i])
            count[s[i]] += 1
        elif s[i] in unique: 
            unique.remove(s[i])
            count[s[i]] += 1
        else:
            count[s[i]] += 1
    if unique == []:
        return "_"
    else: 
        return unique[0]        
        