# Write and test a function to meet this specification:
# squareEach(nums) nums is a list of numbers. Modifies the list by squaring each entry

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] *= nums[i]

def main():
    test = [1, 2, 3, 4, 5]
    squareEach(test)
    print(test)

if __name__ == "__main__":
    main()