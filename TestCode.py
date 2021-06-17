import json

# Get the filename from the user. 
file_name = input("What is the name of the file? ")

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
    

remove_duplicates = sorted(set(word_list))

file = open("test2.json", "w")
json.dump(remove_duplicates, file)
file.close()

print(len(word_list))      
print(len(remove_duplicates))
print (remove_duplicates)