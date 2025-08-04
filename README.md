Function Definitions
add(nums):
Takes a list of numbers (nums).
Starts with total = 0.
Adds each number in the list to total.
Returns the final sum.
Example: add([3, 5, 2]) returns 10.
sub(nums):
Takes a list of numbers (nums).
Starts with total = nums[0] (the first number).
Subtracts each subsequent number in the list from total.
Returns the result.
Ex: sub([10, 3, 2]) returns 5 (10 - 3 - 2).
mul(nums):
Takes a list of numbers (nums).
Starts with total = 1 (since multiplying by 0 would always give 0).
Multiplies each number in the list with total.
Returns the product.
Ex mul([2, 3, 4]) returns 24.
div(num1, num2):
Takes two numbers (num1 and num2).
Tries to return num1 / num2.
If num2 is 0 (division by zero), it returns the string "invalid error" instead of crashing.
Example: div(10, 2) returns 5.0; div(5, 0) returns "invalid error".
Addition (Choice 1):
Prompts: "Enter numbers separated by space: ".
Converts the input (e.g., "5 3 2") into a list of integers ([5, 3, 2]).
Calls add() and prints the result (e.g., 10).
Subtraction (Choice 2):
Same input prompt as addition.
Converts input (e.g., "10 4 1") into a list ([10, 4, 1]).
Calls sub() and prints the result (e.g., 5).
Multiplication (Choice 3):
Same input prompt as addition.
Converts input (e.g., "3 4 2") into a list ([3, 4, 2]).
Calls mul() and prints the result (e.g., 24).
Division (Choice 4):
"Enter first number: " (e.g., 10)
"Enter second number: " (e.g., 2)
Calls div() and prints the result (e.g., 5.0).
Invalid Choice:
If the user enters anything other than 1-4, it prints "Invalid choice!".
