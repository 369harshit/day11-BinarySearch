from typing import List

def is_possible(a, pages, students) -> bool:
    cnt = 0
    sum_allocated = 0
    for i in range(len(a)):
        if sum_allocated + a[i] > pages:
            cnt += 1
            sum_allocated = a[i]
            if sum_allocated > pages:
                return False
        else:
            sum_allocated += a[i]

    if cnt < students:
        return True
    return False


def books(a, b) -> int:
    if b > len(a):
        return -1


    low = a[0]
    high = 0
    for i in range(len(a)):
        high += a[i]
        low = min(low, a[i])


    while low <= high:
        mid = (low + high) //2
        if is_possible(a, mid, b):
            high = mid - 1
        else:
            low = mid + 1

    return low


if __name__ == '__main__':
    a = [12, 34, 67, 90]
    b = 2
    print("Minimum Possible Number is", books(a, b))