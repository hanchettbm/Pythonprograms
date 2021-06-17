# 1. Name:
#      -Baden Hanchett-
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      -This program is meant to prompt the user for a filename. 
#        It will then read the contents of the file into a list. 
#        The program will then prompt the user for a name. Finally, 
#        it will tell the user whether the name is in the list. It
#         will do this with an O(log n) efficency.-
# 4. Algorithmic Efficiency
#      -The algorithmic efficiency of this algorithm is O(log n) 
#       it is this because as you double the size of the input you
#       slow the execution by one time unit. What this means is that 
#       although the size of the input data does have an effect on the 
#       run time it takes a large amount of increase in input for it to 
#       change just one unit, this is because the algorithim is 
#       constantly cutting the data in half, and then in half again, 
#       so it can find things pretty quick, I've found that it usually
#       only takes about 2 tries to find my word and if I double the size 
#       of the input it only goes up to about 3 tries to find the word.-
# 5. What was the hardest part? Be as specific as possible.
#      -This project went very well for me because we spent time planning 
#       before. The hardest part for me however, was finding the most efficent
#       way to exit the program if the contents could not be read. I didn't want
#       to use the quit function so I used an if statement instead. I also had to 
#       make sure the math to find the middle was correct, and needed to remember
#       that indexes go from 0-9. It was also a bit difficult to read the file 
#       into the correct format so the right information was being checked at the
#       right index. The syntax was good, thanks to the psudocode, and the logic
#       of the search made sense. Overall it went quite smooth due to previous
#       planning.-
# 6. How long did it take for you to complete the assignment?
#      -The total time in hours including reading the assignment and submitting the program was about 1 hour.-

# Importing json requirements
import json

# Search function will find a word in a list using an O(log n) algorithim.
def advanced_search(word_list, word):
    start = 0
    end = len(word_list) - 1
    
    while start <= end:
        
        # Find the midde.
        middle = int((start + end) / 2)
        if word_list[middle] == word:
            return print("We found", word, "In", file_name)
        
        # If the word is less than the middle, move to the left half of the data.
        elif word_list[middle] < word:
            start = middle + 1
        
        # If the word is more than the middle, move to the right half of the data.
        else:
            end = middle - 1
            
    return print("Item not in list") # Didn't find it

# Get the filename from the user. 
file_name = input("What is the name of the file? ")

# Try to open and read file.
try:
    file = open(file_name, 'r')
    word_text = file.read()
    file.close()
    
# If above code does not work (can't open file) print error. 
except:
    print("Unable to open file", file_name)
    word_text = ""

#Make sure we have something to read.    
if len(word_text) > 0:
    # Load file to an array.
    word_json = json.loads(word_text)
    word_list = word_json["array"]
    # Get word from user. 
    word = input("What name are we looking for? ")
    # Run word search function.
    advanced_search(word_list, word)