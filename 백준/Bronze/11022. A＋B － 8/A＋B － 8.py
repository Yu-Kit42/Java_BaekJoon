T = int(input())
for x in range(1, T + 1):
    a,b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(x, a, b, a + b))