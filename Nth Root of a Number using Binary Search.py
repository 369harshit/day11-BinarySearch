def multiply(number, n):
    ans = 1.0
    for i in range(1, n + 1):
        ans = ans * number
    return ans




def getNthRoot(n, m):
    low = 1
    high = m
    eps = 1e-7


    while (high - low) > eps:
        mid = (low + high) / 2.0
        if multiply(mid, n) < m:
            low = mid
        else:
            high = mid


    print(n, "th root of ", m, " is ", low)




n = 3
m = 27
getNthRoot(n, m)