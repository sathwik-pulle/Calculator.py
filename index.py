# Calculator.py
def add(nums):
    total = 0
    for num in nums:
        total += num
    return total

def sub(nums):
    total = nums[0]  # start with the first number
    for num in nums[1:]: 
        total -= num
    return total

def mul(nums):
    total = 1  # multiplication must start with 1
    for num in nums:
        total *= num
    return total

def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "invalid error"


choice = int(input("Enter your choice\n1-Add\n2-Sub\n3-Mul\n4-Div: "))

if choice == 1:
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Result:", add(nums))

elif choice == 2:
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Result:", sub(nums))

elif choice == 3:
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Result:", mul(nums))

elif choice == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result:", div(num1, num2))

else:
    print("Invalid choice!")
