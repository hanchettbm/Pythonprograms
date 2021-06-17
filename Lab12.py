# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 12: Prime Numbers
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

n = int(input ("This program will find all the prime numbers at or below N. Select that N: "))

if n > 1:
    
    prime_numbers = []
    
    #Count every number within the rage 2 through n
    for number in range(2, n + 1):
        for counter in range(2, number):
            if (number % counter) == 0:
                break
        else:
            prime_numbers.append(number)
        
    print("The prime numbers at or below", n, "are", prime_numbers)

else:
    print("There are no prime numbers less than 2")            