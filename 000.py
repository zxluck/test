import sys


if __name__ == '__main__':
    # 手机数k，楼层高h, 次数n
    phone = 3
    height = int(input())

    # 1.创建dp数组(表格)[横轴h][纵轴k]
    dp = [[0 for h in range(height)] for k in range(phone)]

    # 2.填充第一行[k=1, h变, n=h]
    for h in range(height):
        dp[0][h] = h+1

    # 3.填充第一列[k变, h=1, n=1]
    for k in range(phone):
        dp[k][0] = 1

    # 4.根据公式求取其它值
    for h in range(1, height):
        for k in range(1, phone):
            minNum = sys.maxsize
            for t in range(1, h+1):
                minNum = min(minNum, 1 + max(dp[k-1][t-1], dp[k][h-t-1]))
            dp[k][h] = minNum

    print(dp[phone-1][height-1])

