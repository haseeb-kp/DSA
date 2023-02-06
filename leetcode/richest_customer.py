def maximumWealth(accounts):
    max = float('-inf')
    for i in range(len(accounts)):
        wealth = 0
        for j in range(len(accounts[i])):
            wealth += accounts[i][j]
        if wealth > max :
            max = wealth
    return max

print(maximumWealth([[1,5],[7,3],[3,5]]))