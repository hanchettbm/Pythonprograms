# 1. Name: 
#      -Baden Hanchett-
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      -The Purpose of this assignment is to inform the user 
#       if they are able to build a hotel on Pennsylvania Avenue. 
#       This program will ask the user several questions and, based 
#       on these questions, tell the user whether a hotel can be purchased 
#       for Pennsylvania and how much it will cost.-
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of the assignement was not the syntax, I'm
#      getting used to it now, and I have worked with functions before.
#      For me the hardest part was an aspect of the problem to solve. 
#      Specifically, it was making sure I checked for each case as soon 
#      as possible, and also making sure I added the total cost of housing 
#      correctly. It was also difficult to figure out the fastest way to exit  
#      the program. Thankfully the instructions were clear and straightfoward 
#      so I understood the problem deffinition and the focus on the program 
#      to build on Penn Ave. The only part I got confused on was that you could
#      swap hotels without any money, so I had to reorder the if statements just 
#      a bit. The submission process was also straightfoward. Although I am not a 
#      huge fan of the video submission I understand why it needs to be included. 
#      Overall the assignment wen't smoothley due to the planning from last week.  
# 5. How long did it take for you to complete the assignment?
#      -The total time in hours including reading the assignment and submitting the program was 2.5 Hours-

def hotel_on_penn():
    
     #Do we own the properties?
     own = input("Do you own all the green properties? (y/n)\n: ")
     if own == "n":
         print("You cannot purchase a hotel until you own all the properties of a given color group.")
         return
     
     #Ask what is on Penn Ave, and if there is a hotel, end.
     number_of_pe_houses = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel)\n: "))
     if number_of_pe_houses == 5:
         print("You cannot purchase a hotel if the property already has one.")
         return
     
     #Ask what is on North Caroline Ave.
     number_of_nc_houses = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel)\n: "))
     
     #Ask what is on Pacific Ave and check if we can swap.
     number_of_pa_houses = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel)\n: "))
     
     #Check if we can swap NC hotel.
     if number_of_pe_houses == 4 and number_of_nc_houses == 5:
         print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
         return
     #Check if we can swap PA hotel.
     if number_of_pe_houses == 4 and number_of_pa_houses == 5:
         print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
         return
     
     #Ask for Cash and make sure we have enough to buy at least 1 hotel. 
     cash = float(input("How much cash do you have to spend? $")) 
     if cash < 200:
         print("You do not have sufficient funds to purchase a hotel at this time.")
         return
     
     #Check if bank has at least 1 hotel.     
     bank_hotels = int(input("How many hotels are there to purchase? "))
     if bank_hotels < 1:
         print("There are not enough hotels available for purchase at this time.")
         return 
     
     #Ask for bank houses.    
     bank_houses = int(input("How many houses are there to purchase? "))
     
     #Calculate cost of houses needed on each property.     
     if number_of_pe_houses < 4:
         cost_of_pe_houses = int((4 - number_of_pe_houses) * 200)
     else: 
         cost_of_pe_houses = 0
         
     if number_of_nc_houses < 4:
         cost_of_nc_houses = int((4 - number_of_nc_houses) * 200)
     else: 
         cost_of_nc_houses = 0   
          
     if number_of_pa_houses < 4:
         cost_of_pa_houses = int((4 - number_of_pa_houses) * 200)
     else: 
         cost_of_pa_houses = 0   
         
     #Calculate total houses needed. 
     total_houses_needed = ((4 - number_of_pe_houses) + (4 - number_of_nc_houses) + (4 - number_of_pa_houses))      
     
     #Calculate Total housing Cost.
     total_cost = (cost_of_nc_houses + cost_of_pa_houses + cost_of_pe_houses + 200)
     
     #Make sure there is enough houses in the bank to buy. If not end. 
     if total_houses_needed > bank_houses:
         print("There are not enough houses available for purchase at this time.")
         return
     
     #Make sure we have enough to buy houses and hotels.
     if total_cost <= cash:

         #Output if just hotel needed.
         if  cost_of_nc_houses == 0 and cost_of_pa_houses == 0:
             print(f"This will cost ${total_cost}.")
             print("\tPurchase 1 hotel and", total_houses_needed, "house(s).")
             print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
             return 
         
         #Output if need houses on just NC.
         if cost_of_pa_houses == 0:
             print(f"This will cost ${total_cost}.")
             print("\tPurchase 1 hotel and", total_houses_needed, "house(s).")
             print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
             print("\tPut", (4 - number_of_nc_houses), "house(s) on North Carolina.")
             return
         
         #Output if need houses on just PA.
         if cost_of_nc_houses == 0:
             print(f"This will cost ${total_cost}.")
             print("\tPurchase 1 hotel and", total_houses_needed, "house(s).")
             print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
             print("\tPut", (4 - number_of_pa_houses), "house(s) on Pacific.")
             return
         
         #Output if everthing needed. 
         else:
             print(f"This will cost ${total_cost}.")
             print("\tPurchase 1 hotel and", total_houses_needed, "house(s).")
             print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
             print("\tPut", (4 - number_of_nc_houses), "house(s) on North Carolina.")
             print("\tPut", (4 - number_of_pa_houses), "house(s) on Pacific.")
             return
     else:
         print("You do not have sufficient funds to purchase a hotel at this time.")
         return    

#Call the function so the program will run.        
hotel_on_penn()