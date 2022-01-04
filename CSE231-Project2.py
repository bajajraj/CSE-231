
##############################################################
#    Computer Project #2
#    The program will compute and display information \
#    for a company which rents vehicles to its customers.\
#    For a specified customer, the program will compute \
#    and display the amount of money charged for that \
#    customer’s vehicle rental.
###############################################################
print("\nWelcome to car rentals. ") #Banner for introduction
 
print()
print("At the prompts, please enter the following: ") #Prompts for the input
print("\tCustomer's classification code (a character: BDW) ")  
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)") 
print()

input_one = input('''Would you like to continue (Y/N)? ''') #Asking to continue

while input_one != 'N' : #if answer is Y, the loop will start or it will be skipped
      input_two = input("\nCustomer code (BDW): ") #asking for the customer code
      
      while not(input_two == 'B' or input_two == 'D' or input_two == 'W'): #if the customer code\
                                                                            #is not B, D,or W,this loop will start.
         
            print("\n\t*** Invalid customer code. Try again. ***") #message printing the incorrect input
            input_two = input("\nCustomer code (BDW): ")#input asking again for the correct code.
   
      else:   
          input_three = int(input("\nNumber of days: ")) #input for number of days.
          input_four = int(input("Odometer reading at the start: ")) #input for reading at the start.
          input_five = int(input("Odometer reading at the end:   ")) #input for reading at the end.
          
          if input_four < input_five: #this is for input four smaller than input five, because it is in correct sequemce.
             distance = abs(input_five/10 - input_four/10) #calculating distance travelled.
          
             if input_two == 'B': #loop if the code is B
                code_b = 40*input_three + 0.25*distance #calculating the amount due.
             
             elif input_two == 'D':
                 distance_d = distance/input_three #average distance per day.
                 if distance_d > 100: 
                    code_b = 60*input_three + 0.25*(distance_d-100)*input_three
                 else:
                     code_b = 60*input_three
             
             elif input_two == 'W':
                  if input_three % 7 == 0: #for multiples of seven
                     money_day = input_three/7 #number of weeks
                     distance_w = distance/money_day #average distance travelled in week.
                     if distance_w < 900:
                        code_b = 190*money_day 
                     elif 900 < distance_w < 1500 :
                         code_b = 190*money_day + 100*money_day 
                     elif distance_w > 1500:
                         code_b = 190*money_day + 200*money_day + 0.25*(distance_w-1500)*money_day
                  else: 
                      money_day = (input_three/7) + 1
                      money_day = int(money_day)
                      distance_w = distance/money_day
                      if distance_w < 900:
                         code_b = 190*money_day 
                      elif 900 < distance_w < 1500 :
                           code_b = 190*money_day + 100*money_day 
                      elif distance_w > 1500:
                           code_b = 190*money_day + 200*money_day + 0.25*(distance_w-1500)*money_day
          
          else: #for the situation when it is showing that reading at the end is less than reading at the start.
               distance = abs(((1000000-input_four)/10) + (input_five/10)) #total distance travelled.
               
               if input_two == 'B':
                  code_b = 40*input_three + 0.25*distance
               
               elif input_two == 'D':
                    distance_d = distance/input_three #average distance travelled in a day.
                    if distance_d > 100:
                       code_b = 60*input_three + 0.25*(distance_d-100)*input_three
                    else:
                     code_b = 60*input_three
             
               elif input_two == 'W':
                    if input_three % 7 == 0:
                       money_day = input_three/7 #number of weeks
                       distance_w = distance/money_day #average distance travelled in a week.
                       if distance_w < 900:
                          code_b = 190*money_day 
                       elif 900 < distance_w < 1500 :
                           code_b = 190*money_day + 100*money_day 
                       elif distance_w > 1500:
                            code_b = 190*money_day + 200*money_day + 0.25*(distance_w-1500)*money_day
                    else:
                         money_day = (input_three/7) + 1
                         money_day = int(money_day)
                         distance_w = distance/money_day
                         if distance_w < 900:
                            code_b = 190*money_day 
                         elif 900 < distance_w < 1500 :
                              code_b = 190*money_day + 100*money_day 
                         elif distance_w > 1500:
                              code_b = 190*money_day + 200*money_day + 0.25*(distance_w-1500)*money_day
        
      code_b = float(code_b) #converting integer to float
      print("\nCustomer summary:",)#printing the summary
      print("\tclassification code:", input_two) 
      print("\trental period (days):", input_three)
      print("\todometer reading at start:", input_four)
      print("\todometer reading at end:  ", input_five)
      print("\tnumber of miles driven: ", round(distance, 1)) #the distance travelled should be rounded to one place.
      print("\tamount due: $", round(code_b, 2)) #distance travelled should be rounded to two place.
     
      input_one = input('''\nWould you like to continue (Y/N)? ''') #asking to continue the loop or break it.

     
print("Thank you for your loyalty.")    #closing message.
 