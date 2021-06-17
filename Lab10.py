# 1. Name:
#      -Baden Hanchett-
# 2. Assignment Name:
#      Lab 10: Fibonacci
# 3. Assignment Description:
#      -This program will prompt the user for a positive integer n and then display 
#       the nth Fibonacci number. It will do so without using recurision.-
# 4. What was the hardest part? Be as specific as possible.
#      -The hardest part of the assignemnt for me was thinking of the best way to store 
#       the values without using recursion. Thankfully we had disussed different ways to
#       store data in my CSE212 class and I was able to apply that here remembering that
#       using variables was more efficent. The next hardest part was thinking of how to 
#       count the variables, and make uure it calculated correctly. Then the asserts were 
#       difficult as well, it doesn't seem necessary here. After that the return and set 
#       up was quite simple, I like usuing functions. -
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

def calculate_fibonacci(num):
    assert (type(num) == int) # Make sure the number getting passed in is a number we can calculate. 
    # Initialize Variables
    num_1 = 0
    num_2 = 1
    # Make sure fibonacci input starts at 1.
    if num < 0:
        print("Fibonacci does not work with negative numbers!")
        return -1  
    # Just return if it's 0, no calculation needed (not Fibonacci).
    if num == 0:
        return 0 
    # If n is equal to 1 just return it, no calculation needed.
    if num == 1:
        return num_2
    # Run through each value from 1  up to number given.
    else:
        for number in range(1, num):
            num_3 = num_1 + num_2
            # Reset numbers for next loop around. 
            num_1 = num_2
            num_2 = num_3
        return num_2
# Ask user for number to compute. 
get_fib_num = int(input("Which Fibonacci number would you like to see? "))
# Run Function
fibonacci_number = calculate_fibonacci(get_fib_num)
assert (type(fibonacci_number) == int) # Make sure the number on the output in is an actual number.
if fibonacci_number >= 0:
    print (f'Fibonacci number {get_fib_num} is {fibonacci_number}.')
