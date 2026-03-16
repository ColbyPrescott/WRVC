# Modify stats.py from this chapter so that client programs have more flexibility in computing the mean and/or standard deviation.
# Specifically, redesign the library to have the following functions:
# mean(nums) Returns the mean of numbers in nums
# stdDev(nums) Returns the standard deviation of nums
# meanStdDev(nums) Retrns both the mean and standard deviation of nums

from math import sqrt

def getNumbers():
    nums = []
    # Sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) -> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)
        xStr = input("Enter a number (<Enter> to quit) -> ")
    return nums

def mean(nums):
    total = 0.0
    for num in nums:
        total += num
    return total / len(nums)

def stdDev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq += dev * dev
    return sqrt(sumDevSq / (len(nums) - 1))

def meanStdDev(nums):
    xbar = mean(nums)
    return xbar, stdDev(nums, xbar)

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        med = (nums[midPos] + nums[midPos - 1]) / 2.0
    else:
        med = nums[midPos]
    return med

def main():
    print("This program computed mean, median, and standard deviation.")
    data = getNumbers()
    xbar, std = meanStdDev(data)
    med = median(data)

    print("\nThe mean is", xbar)
    print("The standard deviation is", std)
    print("The median is", med)

if __name__ == "__main__":
    main()