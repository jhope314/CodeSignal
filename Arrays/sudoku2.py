from collections import defaultdict

def solution(grid):
    # horizontal check
    for h in range(0,9):
        count = defaultdict(int)
        horizontalLine = grid[h]
        for entry in range(0,9):
            if horizontalLine[entry] != "." and count[horizontalLine[entry]] != 0:
                return False
            else:
                count[horizontalLine[entry]] += 1
    # vertical check
    element = 0
    while element < 9:      
        count = defaultdict(int)
        for v in range(0,9):
            currentLine = grid[v]
            if currentLine[element] != "." and count[currentLine[element]] != 0:
                return False
            else: 
                count[currentLine[element]] += 1
        element += 1
    # grid check
    for startingIndex in range (0, 9, 3):
        for subgrid in range(0,9,3):
            subgridRow = subgrid
            count = defaultdict(int)
            for subLine in range(0,3):
                currentRow = grid[subgridRow]
                for item in range(0,3):
                    if currentRow[item + startingIndex] != "." and count[currentRow[item + startingIndex]] != 0:
                        return False
                    else: 
                        count[currentRow[item + startingIndex]] += 1
                subgridRow += 1
                     
    return True
    
