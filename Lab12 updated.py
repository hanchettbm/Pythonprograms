# 1. Name:
#      -Baden Hanchett-
# 2. Assignment Name:
#      Lab 12: Prime Numbers
# 3. Assignment Description:
#      -This program will display all the prime numbers at 
#       or below a value given by the user. It will prompt the 
#       user for an integer. If the integer is less than 2, 
#       then the program will prompt the user again. 
#       The program will then compute all the prime numbers below 
#       (and including) the given number. When finished, the program 
#       will display the list of prime numbers.-
# 4. What was the hardest part? Be as specific as possible.
#      -This assignment was the most difficult for me, I had the most
#       troubble understanding the solution that crosssed out values with 
#       another array of true false values. I had a sloution that worked, 
#       but I had to reformat it to work with the lab design. The harderst 
#       part of that was the multiple loop. I had to spend some time understanding 
#       the range, that mutiple had to start at factor * 2 and then increase by 
#       factor. Once I understood the range needed I was able to use it to set 
#       the true false values correctly.-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program was 4 Hours.-
import math

# Set variables and prompt user for a number, that's greater than 1.
number = 0
while number < 2:
    number = int(input ("This program will find all the prime numbers at or below N. Select that N: "))

assert(number > 1) # Make sure code above worked and number is greater than 1.
primes = []
# Fill numbers array with True values up to number.
numbers = [True for index in range(number + 1 )]
  
numbers[0] = False
numbers[1] = False

assert(len(numbers) == number + 1) # Check length of the array, make sure it's full.

# Check each value up until the square root of the number 
# because nothing above that will be prime.
for factor in range(2, int(math.sqrt(number)) + 1):
    if numbers[factor]:
        # Rule out every mutiple of the factor becuase mutiples are never prime.
        for multiple in range((factor * 2), (number + 1), factor):
            numbers[multiple] = False
            multiple = (factor * 2)
            assert(type(multiple) == int) # Check multpiple type.           

# Use the numbers array to add values to primes array.
for index in range(2, (number + 1)):
    if numbers[index]:
        primes.append(index)                
    
print("The prime numbers at or below", number, "are", primes)          