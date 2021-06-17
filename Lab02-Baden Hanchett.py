# 1. Name:
#      Baden Hanchett
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      The Program will read a list of names from a Json file 
#      and then see if a user-provided username and password is 
#      in our list, if it is it will see if the both match and
#      then give the correct response.  
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of the assignment was figuring out how to 
#      compare the username and passwords to the list and then to 
#      each other. The syntx was not the hardest part now that I 
#      am more familiar with it. One especially difficult bug was
#      that my if statement was wrong and no password combo worked.
#      I solved it by comparing the index of the items indead of the
#      actual strings. Thankfully there was no difficulty with the 
#      instructions or any part of the problem definition.
# 5. How long did it take for you to complete the assignment?
#      The total time in hours including reading the assignment and submitting the program was 2.5 Hours.

# Importing json requirements
import json
#Try to open file.
try:
    with open('Lab02.json') as Lab2file:
        names = json.load(Lab2file)
#If aboove code does not work (can't open file) print error. 
except:
    print("Unable to open file Lab02.json.")

#Store file data in 2 seperate arrays.    
usernames = names["username"]
passwords = names["password"]

#Prompt user for username and password.
prompt_username = input("Username: ")
prompt_password = input("Password: ")

#If the username entered matches a username on file get the index of that username in the array.
user_index = -1;
for name in usernames:
    if name == prompt_username:
        user_index = usernames.index(name)

#If the passwrod enterd matches a password on file get the index of that password in the array.       
password_index = -2;
for word in passwords:
    if word == prompt_password:
        password_index = passwords.index(word)

#Check to see if the Username index matches the Password index and print correct response.      
if user_index == password_index:
    print("You are authenticated!")
else:
    print("You are not authorized to use the system.")

