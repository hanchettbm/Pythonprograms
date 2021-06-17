# 1. Name:
#      -Baden Hanchett-
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      -This program will read a list of names from a file and sort 
#       them.the program will reorder the list so the resulting list 
#       is sorted.When finished, the program will display the sorted 
#       list.-
# 4. What was the hardest part? Be as specific as possible.
#      -For me the hardest part was done last week, it took me a 
#       while to learn the swap function in python to swap the values 
#       once I found the highest one, but I was able to learn that 
#       last week. This week the hardest part was figuring out 
#       where to put the asserts so that all cases of error in 
#       my program were checked for. I also wasn't sure if using
#       a function woud be the best option but it worked out in 
#       the end. It worked well for separating the parts of the 
#       prgram and passing in the correct data.-
# 5. How long did it take for you to complete the assignment?
#      -The total time in hours including reading the assignment and submitting the program was 3 Hours.-


# Importing json requirements
import json

# Word sort Function. 
def word_sort(word_list):
    assert (type(word_list) == list) # Make sure the list getting passed in is a list. 
    i_pivot = len(word_list) - 1
    assert (type(i_pivot) == float or type(i_pivot) == int) # Make sure i_pivot is the correct variable type.
    i_check = i_pivot -1
    assert (type(i_check) == float or type(i_check) == int) # Make sure i_check is the correct variable type.
    i_largest = '0'
    assert (type(i_largest) == str) # Make sure i_largest is the correct variable type.
    
    # Loop that moves pivot point. 
    while i_pivot > 0:
        
        # Check each item in list lower than pivot.
        while i_check >= 0:
            if word_list[i_check] > i_largest:
                # Find the largest value in the array less than Pivot.
                i_largest = word_list[i_check]
            i_check = i_check - 1
        
        # Make sure Pivot is not the highest.    
        if i_largest < word_list[i_pivot]:
            # If it is, make Pivot largest.
            i_largest = word_list[i_pivot]
       
        # Get the index of the largest value.    
        largest_index = word_list.index(i_largest)
        assert (type(largest_index) == int) # Make sure the index for largest is an int. (Indexes are always only ints.)
        # Peform a swap of the highest value and the pivot value.     
        word_list[i_pivot], word_list[largest_index] = word_list[largest_index], word_list[i_pivot]
        
        # Reset variables for next big loop iteration.  
        i_pivot = i_pivot - 1
        assert (type(i_pivot) == float or type(i_pivot) == int) # Make sure i_pivot is the correct variable type before reusing.
        i_check = i_pivot -1 
        assert (type(i_check) == float or type(i_check) == int) # Make sure i_check is the correct variable type before reusing.
        i_largest = '0' 
        assert (type(i_largest) == str) # Make sure i_largest is the correct variable type before reusing.
        assert (i_largest == '0') # Make sure i_largest is reset so we can give it the next correct value in the string. 
    
    return word_list

# Get the filename from the user. 
file_name = input("What is the name of the file? ")
assert (type(file_name) == str) # Make sure they gave us a filename, not something else.

# Try to open and read file (Try used for the user to know).
try:
    file = open(file_name, 'r')
    word_text = file.read()
    file.close()
    
# If above code does not work (can't open file) print error. 
except:
    print("Unable to open file", file_name)
    word_text = ""

# Make sure we have something to read. 
# (If Statement used here for the user, don't want to run if not true so should be built into program).    
if len(word_text) > 0:
    # Load file to an array.
    word_json = json.loads(word_text)
    word_list = word_json["array"]
    assert (len(word_list) > 0) # Make sure the array has something in it to sort.
    # Run word sort function.
    word_sort(word_list)
    # Display Results. 
    print ("The values in",file_name, "are:")
    for word in word_list:
        print ("\t",word)