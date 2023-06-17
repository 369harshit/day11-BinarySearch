def is_possible(cows, stalls, mid):
    cow_count = 1
    prev_position = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - prev_position >= mid:
            cow_count += 1
            prev_position = stalls[i]
    return cow_count >= cows


def aggressive_cows(stalls, cows):
    stalls.sort()
    low = 0
    high = stalls[-1] - stalls[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if is_possible(cows, stalls, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return result


# Example usage
stalls = [1, 2, 8, 4, 9]
cows = 3

max_distance = aggressive_cows(stalls, cows)
print("The largest minimum distance is", max_distance)
