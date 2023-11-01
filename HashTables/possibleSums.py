from collections import defaultdict


def solution(coins, quantity):
    # let coins = (x1, x2, ..., xn)
    # let quantity = (z1, z2, ..., zn)
    # let quantitySelected = (y1, y2, ..., yn)
    # how many unique combinations of x1y1 + x2y2 + ... + xnyn can we achieve?
    # constraints: 0 <= y1 <= z1; 0<= y2 <= z2; ...; 0 <= yn <= zn 
    # max possible combinations = (z1 + 1) * (z2 + 1) * ... * (zn + 1) - 1
    coinTracker = defaultdict(int)
    coinTracker[0] += 1
    currentCoinTracker = defaultdict(int)
    i = 0
    for k in quantity: 
        for sumSoFar in coinTracker:
            for j in range(k+1):
                coinSum = j*coins[i] + sumSoFar
                if coinSum not in coinTracker: 
                    currentCoinTracker[coinSum] += 1
        i += 1
        coinTracker.update(currentCoinTracker)
    return (len(coinTracker) - 1)  
