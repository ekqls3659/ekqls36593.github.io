h, m = map(int, input().split())
sum = h * 60 + m
if sum < 45:
    sum = 24 * 60 + m
sum -= 45
print('%d %d' %(sum // 60, sum % 60))