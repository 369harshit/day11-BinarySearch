#from typing import List


def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2, 3]
    target = 3
    print("The index in which the target is present is", search(nums, target))