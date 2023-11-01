def solution(a):
    n = 0
    answer = []
    while n < len(a):
        outputRow = []
        for i in range(len(a) - 1, -1, -1):
            row = a[i]
            outputRow.append(row[n])
        n += 1
        answer.append(outputRow)
    return answer
