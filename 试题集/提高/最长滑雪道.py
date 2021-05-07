def dfs(arr, dp, x, y):
    mHeight =1
    temp = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(4):
        tx = x + temp[i][0]
        ty = y + temp[i][1]
        if tx < 0 or tx >= row or ty < 0 or ty >= col:
            continue
        if arr[x][y] <= arr[tx][ty]:
            continue
        mHeight = max(mHeight, dfs(arr, dp, tx, ty) + 1)
        dp[x][y] = mHeight
    return mHeight


if __name__ == "__main__":
    row, col = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(row)]
    dp = [[0 for _ in range(col)] for _ in range(row)]

    res = 0
    for i in range(row):
        for j in range(col):
            res = max(res,dfs(arr, dp, i, j))

    print( res,arr, dp)
