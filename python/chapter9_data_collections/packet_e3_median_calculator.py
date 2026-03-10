# Collect 10 numbers, sort them, and compute the median

def main():
    print("Enter 10 numbers")

    nums = []
    for i in range(10):
        num = float(input("Enter a number: "))
        nums.append(num)
    
    nums.sort()

    median = 0
    mid = len(nums) // 2
    if len(nums) % 2 == 1:
        median = nums[mid]
    else:
        median = (nums[mid] + nums[mid - 1]) / 2
    
    print("Median:", median)

if __name__ == "__main__":
    main()