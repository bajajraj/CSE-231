# -*- coding: utf-8 -*- 
"""
Created on Wed Jan 22 21:58:21 2020

@author: Rajaditya Bajaj
"""
##############################################################
#    Computer Project #3
#    
#    This assignment focuses on the design, implementation \
#    and testing of a Python program to compute tuition \
#    charges at MSU. 
#    The program uses the knowledge of the strings and the \
#    while and for loop that is learned.
##############################################################

print("2019 MSU Undergraduate Tuition Calculator.")
print()

another_cal = 'yes'

while another_cal == 'yes':
    # put everything
    resident_input = input("Resident (yes/no): ")
    resident_input = resident_input.lower() #to make sure that all the inputs are same.
    while not(resident_input == 'yes' or resident_input== 'no'):#if input is not yes or no
        print("Invalid input. Try again.")
        resident_input = input("Resident (yes/no): ")
        resident_input = resident_input.lower()
    
    else:
        if resident_input == 'yes': #if the input is resident
           level_input = input("Level—freshman, sophomore, junior, senior: ")
           level_input = level_input.lower()
           while not(level_input == 'freshman' or level_input == 'sophomore' or level_input == 'junior' or level_input == 'senior'):
               print("Invalid input. Try again.")
               level_input = input("Level—freshman, sophomore, junior, senior: ")
               level_input = level_input.lower()
           else: #if level_input is correct
                if level_input == 'freshman': #loop for freshman starts.
                   freshman_one = input("Are you admitted to the College of Engineering (yes/no): ")
            
                   if freshman_one == 'yes': #loop for admitted in college of engineering.
                       credits = int(input("Credits: "))
                       while not (credits):
                            print("Invalid input. Try again.")
                            credits = int(input("Credits: "))
                       else:
                            if credits < 0:#loop for credit less than 0
                               print("Invalid input. Try again.")
                            elif 0 < credits <= 4: #loop for credits till 4
                               tution = (482*credits) + 402 + 21 + 3 
                            elif credits == 5: #loop for 5 credits
                               tution = (482*credits) + 21 + 3 + 670
                            elif 6 <= credits <= 11: #loop for credits from 6 to 11
                               tution = (482*credits) + 670 + 5 + 21 + 3 
                            elif 12 <= credits <= 18:#loop for 12 to 18 credits
                               tution = 7230 + 670 + 21 + 3 + 5 
                            else: #loop for more than 18 credits
                               tution = 7230 + (482*(credits-18)) + 670 + 21 + 3 + 5   
                   
                     
            
                   else: #loop for not admitted in college of engineering.
                        freshman_two = input("Are you in the James Madison College (yes/no): ")
               
                        if freshman_two == 'yes': #loop for James Madison.
                           credits = int(input("Credits: "))
                           while not (credits):
                               print("Invalid input. Try again.")
                               credits = int(input("Credits: "))
                           else:
                                if credits < 0:#loop for credit less than 0
                                   print("Invalid input. Try again.")
                                elif 0 < credits <= 4: #loop for credits till 4
                                     tution = (482*credits) + 21 + 3 + 7.50
                                elif credits == 5: #loop for 5 credits
                                      tution = (482*credits) + 21 + 3 + 7.50 
                                elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                      tution = (482*credits) + 5 + 21 + 3 + 7.50
                                elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                      tution = 7230 + 21 + 3 + 5 + 7.50
                                else: #loop for more than 18 credits
                                      tution = 7230 + (482*(credits-18)) + 21 + 3 + 5 +7.50 
              
                        else: #loop for not admitted in James Madison
                            credits = int(input("Credits: "))
                            while not (credits):
                                print("Invalid input. Try again.")
                                credits = int(input("Credits: "))
                            else:
                                 if credits < 0:#loop for credit less than 0
                                    print("Invalid input. Try again.")
                                 elif 0 < credits <= 4: #loop for credits till 4
                                     tution = (482*credits) + 21 + 3 
                                 elif credits == 5: #loop for 5 credits
                                     tution = (482*credits) + 21 + 3 
                                 elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                     tution = (482*credits) + 5 + 21 + 3 
                                 elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                     tution = 7230  + 21 + 3 + 5 
                                 else: #loop for more than 18 credits
                                      tution = 7230 + (482*(credits-18)) + 21 + 3 + 5  
                   
            
                    
                elif level_input == 'sophomore': #loop for sophomore starts.
                     sophomore_one = input("Are you admitted to the college of Engineering (yes/no): ")
            
                     if sophomore_one == 'yes': #loop for admitted in college of engineering.
                        credits = int(input("Credits: "))
                        while not (credits):
                                print("Invalid input. Try again.")
                                credits = int(input("Credits: "))
                        else:
                             if credits < 0:#loop for credit less than 0
                                print("Invalid input. Try again.")
                             elif 0 < credits <= 4: #loop for credits till 4
                                  tution = (494*credits) + 402 + 21 + 3 
                             elif credits == 5: #loop for 5 credits
                                  tution = (494*credits) + 21 + 3 + 670
                             elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                   tution = (494*credits) + 670 + 5 + 21 + 3 
                             elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                 tution = 7230 + 670 + 21 + 3 + 5 
                             else: #loop for more than 18 credits
                                  tution = 7230 + (494*(credits-18)) + 670 + 21 + 3 + 5  
            
                     else: #loop for not admitted in college of engineering.
                         sophomre_two = input("Are you in James Madison College: ")
               
                         if sophomre_two == 'yes': #loop for James Madison.
                            credits = int(input("Credits: "))
                            while not (credits):
                                  print("Invalid input. Try again.")
                                  credits = int(input("Credits: "))
                            else:
                                if credits < 0:#loop for credit less than 0
                                   print("Invalid input. Try again.")
                                elif 0 < credits <= 4: #loop for credits till 4
                                    tution = (494*credits) + 21 + 3 + 7.50
                                elif credits == 5: #loop for 5 credits
                                    tution = (494*credits) + 21 + 3 + 7.50 
                                elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                     tution = (494*credits) + 5 + 21 + 3 + 7.50
                                elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                     tution = 7230 + 21 + 3 + 5 + 7.50
                                else: #loop for more than 18 credits
                                      tution = 7230 + (494*(credits-18)) + 21 + 3 + 5 +7.50 
              
                         else: #loop for not admitted in James Madison
                             credits = int(input("Credits: "))
                             while not (credits):
                                   print("Invalid input. Try again.")
                                   credits = int(input("Credits: "))
                             else:
                                  if credits < 0:#loop for credit less than 0
                                     print("Invalid input. Try again.")
                                  elif 0 < credits <= 4: #loop for credits till 4
                                      tution = (494*credits) + 21 + 3 
                                  elif credits == 5: #loop for 5 credits
                                       tution = (494*credits) + 21 + 3 
                                  elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                      tution = (494*credits) + 5 + 21 + 3 
                                  elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                      tution = 7230  + 21 + 3 + 5 
                                  else: #loop for more than 18 credits
                                      tution = 7230 + (494*(credits-18)) + 21 + 3 + 5  
         
                else:  #loop for junior and senior starts
                      junior_one = input("Enter college as business, engineering, health, sciences, or none: ")
                      if junior_one == 'business': #loop for business college
                         cmse = input("Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ")
                         cmse = cmse.lower()
                         if cmse == 'no': #if major is not CMSE
                            credits = int(input("Credits: "))       
                            while not (credits):
                                  print("Invalid input. Try again.")
                                  credits = int(input("Credits: "))
                            else:
                                if credits < 0:#loop for credit less than 0
                                   print("Invalid input. Try again.")
                                elif 0 < credits <= 4: #loop for credits till 4
                                    tution = (573*credits) + 21 + 3 + 113 
                                elif credits == 5: #loop for 5 credits
                                      tution = (573*credits) + 21 + 3 + 226 
                                elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                       tution = (573*credits) + 5 + 21 + 3 + 226 
                                elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                      tution = 8595  + 21 + 3 + 5 + 226
                                else: #loop for more than 18 credits
                                       tution = 8595 + (573*(credits-18)) + 21 + 3 + 5 + 226  
             
                         else: #if major is CMSE
                              credits = int(input("Credits: "))       
                              while not (credits):
                                  print("Invalid input. Try again.")
                                  credits = int(input("Credits: "))
                              else: 
                                   if credits < 0:#loop for credit less than 0
                                      print("Invalid input. Try again.")
                                   elif 0 < credits <= 4: #loop for credits till 4
                                        tution = (573*credits) + 21 + 3 + 113 + 402
                                   elif credits == 5: #loop for 5 credits
                                        tution = (573*credits) + 21 + 3 + 226 + 670
                                   elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                        tution = (573*credits) + 5 + 21 + 3 + 226 + 670
                                   elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                        tution = 8595  + 21 + 3 + 5 + 226 + 670
                                   else: #loop for more than 18 credits
                                        tution = 8595 + (573*(credits-18)) + 21 + 3 + 5 + 226 + 670 
                      
                      elif junior_one == 'engineering': #if college is college of engineering
                          cmse = input("Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ")
                          cmse = cmse.lower()
                          if cmse == 'no': #if major is not CMSE
                             credits = int(input("Credits: "))       
                             while not (credits):
                                 print("Invalid input. Try again.")
                                 credits = int(input("Credits:"))
                             else:
                                 if credits < 0:#loop for credit less than 0
                                    print("Invalid input. Try again.")
                                 elif 0 < credits <= 4: #loop for credits till 4
                                    tution = (573*credits) + 21 + 3 + 402
                                 elif credits == 5: #loop for 5 credits
                                    tution = (573*credits) + 21 + 3 + 670 
                                 elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                      tution = (573*credits) + 5 + 21 + 3 + 670 
                                 elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                       tution = 8595  + 21 + 3 + 5 + 670
                                 else: #loop for more than 18 credits
                                      tution = 8595 + (573*(credits-18)) + 21 + 3 + 5 + 670  
             
                          else: #if major is CMSE
                               credits = int(input("Credits:"))       
                               while not (credits):
                                     print("Invalid input. Try again.")
                                     credits = int(input("Credits:"))
                               else:
                                   if credits < 0:#loop for credit less than 0
                                      print("Invalid input. Try again.")
                                   elif 0 < credits <= 4: #loop for credits till 4
                                        tution = (573*credits) + 21 + 3  + 402
                                   elif credits == 5: #loop for 5 credits
                                       tution = (573*credits) + 21 + 3  + 670
                                   elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                       tution = (573*credits) + 5 + 21 + 3 + 670
                                   elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                       tution = 8595  + 21 + 3 + 5 + 670
                                   else: #loop for more than 18 credits
                                        tution = 8595 + (573*(credits-18)) + 21 + 3 + 5 + 226 + 670 
               
                      elif junior_one == 'sciences' or junior_one == 'health':# if the college is sciences or health
                           cmse = input("Is your major CMSE (\"Computational Mathematics and Engineering)")
                           cmse = cmse.lower()
                           if cmse == 'no': #if major is not CMSE
                              credits = int(input("Credits:"))       
                              while not (credits):
                                    print("Invalid input. Try again.")
                                    credits = int(input("Credits:"))
                              else:
                                   if credits < 0:#loop for credit less than 0
                                      print("Invalid input. Try again.")
                                   elif 0 < credits <= 4: #loop for credits till 4
                                        tution = (555*credits) + 21 + 3 + 50
                                   elif credits == 5: #loop for 5 credits
                                        tution = (555*credits) + 21 + 3 + 100 
                                   elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                        tution = (555*credits) + 5 + 21 + 3 + 100 
                                   elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                        tution = 8325  + 21 + 3 + 5 + 100
                                   else: #loop for more than 18 credits
                                        tution = 8325 + (555*(credits-18)) + 21 + 3 + 5 + 100  
             
                           else: #if major is CMSE
                                credits = int(input("Credits:"))       
                                while not (credits):
                                      print("Invalid input. Try again.")
                                      credits = int(input("Credits:"))
                                else:
                                     if credits < 0:#loop for credit less than 0
                                        print("Invalid input. Try again.")
                                     elif 0 < credits <= 4: #loop for credits till 4
                                        tution = (555*credits) + 21 + 3  + 402
                                     elif credits == 5: #loop for 5 credits
                                        tution = (555*credits) + 21 + 3  + 670
                                     elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                         tution = (555*credits) + 5 + 21 + 3 + 670
                                     elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                         tution = 8325  + 21 + 3 + 5 + 670
                                     else: #loop for more than 18 credits
                                         tution = 8325 + (573*(credits-18)) + 21 + 3 + 5 + 226 + 670 
           
                      else: #if any other college
                          cmse = input("Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ")
                          cmse = cmse.lower()
                          if cmse == 'no': #if major is not CMSE
                             james_madison = input("Are you in the James Madison College (yes/no): ")
                             if james_madison == 'yes': #if in JAmes Madison
                                credits = int(input("Credits: "))       
                                while not (credits):
                                      print("Invalid input. Try again.")
                                      credits = int(input("Credits:"))
                                else:
                                     if credits < 0:#loop for credit less than 0
                                        print("Invalid input. Try again.")
                                     elif 0 < credits <= 4: #loop for credits till 4
                                        tution = (555*credits) + 21 + 3 + 50 + 7.50
                                     elif credits == 5: #loop for 5 credits
                                          tution = (555*credits) + 21 + 3 + 100 + 7.50
                                     elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                          tution = (555*credits) + 5 + 21 + 3 + 100 + 7.50 
                                     elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                          tution = 8325  + 21 + 3 + 5 + 100 + 7.50
                                     else: #loop for more than 18 credits
                                           tution = 8325 + (555*(credits-18)) + 21 + 3 + 5 + 100 + 7.50  
                             else:#if not in james madison
                                  credits = int(input("Credits: "))       
                                  
                                  while not (credits) :
                                        print("Invalid input. Try again.")
                                        credits = int(input("Credits:"))
                                  else:
                                        if credits < 0:#loop for credit less than 0
                                           print("Invalid input. Try again.")
                                        elif 0 < credits <= 4: #loop for credits till 4
                                            tution = (555*credits) + 21 + 3 + 50
                                        elif credits == 5: #loop for 5 credits
                                             tution = (555*credits) + 21 + 3 + 100 
                                        elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                             tution = (555*credits) + 5 + 21 + 3 + 100 
                                        elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                             tution = 8325  + 21 + 3 + 5 + 100
                                        else: #loop for more than 18 credits
                                             tution = 8325 + (555*(credits-18)) + 21 + 3 + 5 + 100  
                    
                          else: #if major is CMSE
                               james_madison = input("Are you in the James Madison College (yes/no): ")
                               if james_madison == 'yes':
                                  credits = int(input("Credits: "))       
                                 
                                  while not credits:
                                        print("Invalid input. Try again.")
                                        credits = int(input("Credits:"))
                                  else:
                                       credits = int(credits)
                                       if credits < 0:#loop for credit less than 0
                                          print("Invalid input. Try again.")
                                       elif 0 < credits <= 4: #loop for credits till 4
                                           tution = (555*credits) + 21 + 3 + 50 + 7.50 + 402
                                       elif credits == 5: #loop for 5 credits
                                           tution = (555*credits) + 21 + 3 + 100 + 7.50 + 670
                                       elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                           tution = (555*credits) + 5 + 21 + 3 + 100 + 7.50 + 670 
                                       elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                           tution = 8325  + 21 + 3 + 5 + 100 + 7.50 + 670
                                       else: #loop for more than 18 credits
                                            tution = 8325 + (555*(credits-18)) + 21 + 3 + 5 + 100 + 7.50 + 670  
                               else:
                                    credits = input("Credits: ")       
                                    while credits == "0" or credits == 'ab' or credits == '3.5':
                                          print("Invalid input. Try again.")
                                          credits = input("Credits: ")
                                    else:
                                         credits = int(credits)
                                         
                                         if 1 <= credits <= 4: #loop for credits till 4
                                                  tution = (555*credits) + 21 + 3 + 402
                                         elif credits == 5: #loop for 5 credits
                                              tution = (555*credits) + 21 + 3 + 670 
                                         elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                              tution = (555*credits) + 5 + 21 + 3 + 670 
                                         elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                              tution = 8325  + 21 + 3 + 5 + 670
                                         else: #loop for more than 18 credits
                                               tution = 8325 + (555*(credits-18)) + 21 + 3 + 5 + 670 
   

        else: #loop for non-resident students   (start from here)
            international = input("International (yes/no): ")
            international = international.lower()
            
            if international == 'no':
               level_input = input("Level—freshman, sophomore, junior, senior: ")
               level_input = level_input.lower()
               while not(level_input == 'freshman' or level_input == 'sophomore' or level_input == 'junior' or level_input == 'senior'):
                     print("Invalid input. Try again.")
                     level_input = input("Level—freshman, sophomore, junior, senior: ")
                     level_input = level_input.lower()
               else:
                 if level_input == 'freshman': #loop for freshman starts.
                    freshman_one = input("Are you admitted to the college of Engineering (yes/no): ")
            
                    if freshman_one == 'yes': #loop for admitted in college of engineering.
                       credits = int(input("Credits: "))
                       while not (credits):
                             print("Invalid input. Try again.")
                             credits = int(input("Credits:"))
                       else:
                            if credits < 0:#loop for credit less than 0
                               print("Invalid input. Try again.")
                            elif 0 < credits <= 4: #loop for credits till 4
                               tution = (1325*credits) + 402 + 21 + 3 
                            elif credits == 5: #loop for 5 credits
                               tution = (1325*credits) + 21 + 3 + 670
                            elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                tution = (1325*credits) + 670 + 5 + 21 + 3 
                            elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                 tution = 19883 + 670 + 21 + 3 + 5 
                            else: #loop for more than 18 credits
                                 tution = 19883 + (1325*(credits-18)) + 670 + 21 + 3 + 5 + 660   
                   
                     
            
                    else: #loop for not admitted in college of engineering.
                         freshman_two = input("Are you in James Madison College.")
               
                         if freshman_two == 'yes': #loop for James Madison.
                            credits = int(input("Credits:"))
                            while not (credits):
                                  print("Invalid input. Try again.")
                                  credits = int(input("Credits: "))
                            else:
                                 if credits < 0:#loop for credit less than 0
                                    print("Invalid input. Try again.")
                                 elif 0 < credits <= 4: #loop for credits till 4
                                     tution = (1325*credits) + 21 + 3 + 7.50
                                 elif credits == 5: #loop for 5 credits
                                     tution = (1325*credits) + 21 + 3 + 7.50 
                                 elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                     tution = (1325*credits) + 5 + 21 + 3 + 7.50
                                 elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                      tution = 19883 + 21 + 3 + 5 + 7.50
                                 else: #loop for more than 18 credits
                                       tution = 19883 + (1325*(credits-18)) + 21 + 3 + 5 +7.50 
              
                         else: #loop for not admitted in James Madison
                              credits = int(input("Credits:"))
                              while not (credits):
                                    print("Invalid input. Try again.")
                                    credits = int(input("Credits:"))
                              else:
                                  if credits < 0:#loop for credit less than 0
                                     print("Invalid input. Try again.")
                                  elif 0 < credits <= 4: #loop for credits till 4
                                       tution = (1325*credits) + 21 + 3 
                                  elif credits == 5: #loop for 5 credits
                                       tution = (1325*credits) + 21 + 3 
                                  elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                        tution = (1325*credits) + 5 + 21 + 3 
                                  elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                        tution = 19883 + 21 + 3 + 5 
                                  else: #loop for more than 18 credits
                                       tution = 19883 + (1325*(credits-18)) + 21 + 3 + 5  
                   
                 elif level_input == 'sophomore': #loop for sophomore starts.
                      sophomore_one = input("Are you admitted to the College of Engineering (yes/no): ")
            
                      if sophomore_one == 'yes': #loop for admitted in college of engineering.
                         credits = int(input("Credits: "))
                         while not (credits):
                                print("Invalid input. Try again.")
                                credits = int(input("Credits: "))
                         else:
                              if credits < 0:#loop for credit less than 0
                                 print("Invalid input. Try again.")
                              elif 0 < credits <= 4: #loop for credits till 4
                                   tution = (494*credits) + 402 + 21 + 3 
                              elif credits == 5: #loop for 5 credits
                                   tution = (494*credits) + 21 + 3 + 670
                              elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                    tution = (494*credits) + 670 + 5 + 21 + 3 
                              elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                   tution = 7230 + 670 + 21 + 3 + 5 
                              else: #loop for more than 18 credits
                                   tution = 19883 + (1325.50*(credits-18)) + 670 + 21 + 3 + 5 + 750 
            
                      else: #loop for not admitted in college of engineering.
                           sophomre_two = input("Are you in James Madison College: ")
               
                           if sophomre_two == 'yes': #loop for James Madison.
                              credits = int(input("Credits: "))
                              while not (credits):
                                    print("Invalid input. Try again.")
                                    credits = int(input("Credits: "))
                              else:
                                   if credits < 0:#loop for credit less than 0
                                      print("Invalid input. Try again.")
                                   elif 0 < credits <= 4: #loop for credits till 4
                                        tution = (494*credits) + 21 + 3 + 7.50
                                   elif credits == 5: #loop for 5 credits
                                        tution = (494*credits) + 21 + 3 + 7.50 
                                   elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                        tution = (494*credits) + 5 + 21 + 3 + 7.50
                                   elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                         tution = 7230 + 21 + 3 + 5 + 7.50
                                   else: #loop for more than 18 credits
                                         tution = 7230 + (494*(credits-18)) + 21 + 3 + 5 +7.50 
              
                           else: #loop for not admitted in James Madison
                                credits = int(input("Credits: "))
                                while not (credits):
                                      print("Invalid input. Try again.")
                                      credits = int(input("Credits: "))
                                else:
                                     if credits < 0:#loop for credit less than 0
                                        print("Invalid input. Try again.")
                                     elif 0 < credits <= 4: #loop for credits till 4
                                          tution = (494*credits) + 21 + 3 
                                     elif credits == 5: #loop for 5 credits
                                          tution = (494*credits) + 21 + 3 
                                     elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                          tution = (494*credits) + 5 + 21 + 3 
                                     elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                          tution = 7230  + 21 + 3 + 5 
                                     else: #loop for more than 18 credits
                                           tution = 7230 + (494*(credits-18)) + 21 + 3 + 5  
         
        
                 else:  #loop for junior and senior starts
                      junior_one = input("Enter college as business, engineering, health, sciences, or none:")
                      if junior_one == 'business': #loop for business college
                         cmse = input("Is your major CMSE (\"Computational Mathematics and Engineering)")
                         cmse = cmse.lower()
                         if cmse == 'no': #if major is not CMSE
                            credits = int(input("Credits:"))       
                            while not (credits):
                                  print("Invalid input. Try again.")
                                  credits = int(input("Credits:"))
                            else:
                                 if credits < 0:#loop for credit less than 0
                                    print("Invalid input. Try again.")
                                 elif 0 < credits <= 4: #loop for credits till 4
                                      tution = (1366*credits) + 21 + 3 + 113 
                                 elif credits == 5: #loop for 5 credits
                                      tution = (1366*credits) + 21 + 3 + 226 
                                 elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                      tution = (1366*credits) + 5 + 21 + 3 + 226 
                                 elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                      tution = 20501 + 21 + 3 + 5 + 226
                                 else: #loop for more than 18 credits
                                      tution = 20501 + (1325*(credits-18)) + 21 + 3 + 5 + 226  
             
                         else: #if major is CMSE
                              credits = int(input("Credits:"))       
                              while not (credits):
                                    print("Invalid input. Try again.")
                                    credits = int(input("Credits:"))
                              else: 
                                   if credits < 0:#loop for credit less than 0
                                      print("Invalid input. Try again.")
                                   elif 0 < credits <= 4: #loop for credits till 4
                                        tution = (1366*credits) + 21 + 3 + 113 + 402
                                   elif credits == 5: #loop for 5 credits
                                        tution = (1366*credits) + 21 + 3 + 226 + 670
                                   elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                        tution = (1366*credits) + 5 + 21 + 3 + 226 + 670
                                   elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                        tution = 20501  + 21 + 3 + 5 + 226 + 670
                                   else: #loop for more than 18 credits
                                         tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 226 + 670 
                      
                      elif junior_one == 'engineering': #if college is college of engineering
                           cmse = input("Is your major CMSE (\"Computational Mathematics and Engineering)")
                           cmse = cmse.lower()
                           if cmse == 'no': #if major is not CMSE
                              credits = int(input("Credits:"))       
                              while not (credits):
                                    print("Invalid input. Try again.")
                                    credits = int(input("Credits:"))
                              else:
                                   if credits < 0:#loop for credit less than 0
                                      print("Invalid input. Try again.")
                                   elif 0 < credits <= 4: #loop for credits till 4
                                         tution = (1366*credits) + 21 + 3 + 402
                                   elif credits == 5: #loop for 5 credits
                                         tution = (1366*credits) + 21 + 3 + 670 
                                   elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                         tution = (1366*credits) + 5 + 21 + 3 + 670 
                                   elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                         tution = 20501  + 21 + 3 + 5 + 670
                                   else: #loop for more than 18 credits
                                         tution = 20501+ (573*(credits-18)) + 21 + 3 + 5 + 670  
             
                           else: #if major is CMSE
                                credits = int(input("Credits:"))       
                                while not (credits):
                                      print("Invalid input. Try again.")
                                      credits = int(input("Credits:"))
                                else:
                                     if credits < 0:#loop for credit less than 0
                                        print("Invalid input. Try again.")
                                     elif 0 < credits <= 4: #loop for credits till 4
                                          tution = (1366*credits) + 21 + 3  + 402
                                     elif credits == 5: #loop for 5 credits
                                          tution = (1366*credits) + 21 + 3  + 670
                                     elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                          tution = (1366*credits) + 5 + 21 + 3 + 670
                                     elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                          tution = 20501 + 21 + 3 + 5 + 670
                                     else: #loop for more than 18 credits
                                          tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 226 + 670 
               
                      elif junior_one == 'sciences' or junior_one == 'health':# if the college is sciences or health
                          cmse = input("Is your major CMSE (\"Computational Mathematics and Engineering)")
                          cmse = cmse.lower()
                          if cmse == 'no': #if major is not CMSE
                             credits = int(input("Credits:"))       
                             while not (credits):
                                   print("Invalid input. Try again.")
                                   credits = int(input("Credits:"))
                             else:
                                  if credits < 0:#loop for credit less than 0
                                     print("Invalid input. Try again.")
                                  elif 0 < credits <= 4: #loop for credits till 4
                                       tution = (1366*credits) + 21 + 3 + 50
                                  elif credits == 5: #loop for 5 credits
                                       tution = (1366*credits) + 21 + 3 + 100 
                                  elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                       tution = (1366*credits) + 5 + 21 + 3 + 100 
                                  elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                       tution = 20501 + 21 + 3 + 5 + 100
                                  else: #loop for more than 18 credits
                                       tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 100  
             
                          else: #if major is CMSE
                               credits = int(input("Credits:"))       
                               while not (credits):
                                     print("Invalid input. Try again.")
                                     credits = int(input("Credits:"))
                               else:
                                    if credits < 0:#loop for credit less than 0
                                       print("Invalid input. Try again.")
                                    elif 0 < credits <= 4: #loop for credits till 4
                                         tution = (1366*credits) + 21 + 3  + 402
                                    elif credits == 5: #loop for 5 credits
                                         tution = (1366*credits) + 21 + 3  + 670
                                    elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                         tution = (1366*credits) + 5 + 21 + 3 + 670
                                    elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                         tution = 20501  + 21 + 3 + 5 + 670
                                    else: #loop for more than 18 credits
                                         tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 226 + 670 
           
                      else: #if any other college
                           cmse = input("Is your major CMSE (\"Computational Mathematics and Engineering)")
                           cmse = cmse.lower()
                           if cmse == 'no': #if major is not CMSE
                              james_madison = input("Are you in James Madison College.")
                              if james_madison == 'yes':
                                 credits = int(input("Credits:"))       
                                 while not (credits):
                                       print("Invalid input. Try again.")
                                       credits = int(input("Credits:"))
                                 else:
                                      if credits < 0:#loop for credit less than 0
                                         print("Invalid input. Try again.")
                                      elif 0 < credits <= 4: #loop for credits till 4
                                           tution = (1366*credits) + 21 + 3 + 50 + 7.50
                                      elif credits == 5: #loop for 5 credits
                                           tution = (1366*credits) + 21 + 3 + 100 + 7.50
                                      elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                           tution = (1366*credits) + 5 + 21 + 3 + 100 + 7.50 
                                      elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                           tution = 20501  + 21 + 3 + 5 + 100 + 7.50
                                      else: #loop for more than 18 credits
                                           tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 100 + 7.50  
                              else:
                                   credits = int(input("Credits:"))       
                                   while not (credits):
                                         print("Invalid input. Try again.")
                                         credits = int(input("Credits:"))
                                   else:
                                        if credits < 0:#loop for credit less than 0
                                           print("Invalid input. Try again.")
                                        elif 0 < credits <= 4: #loop for credits till 4
                                             tution = (1366*credits) + 21 + 3 + 50
                                        elif credits == 5: #loop for 5 credits
                                             tution = (1366*credits) + 21 + 3 + 100 
                                        elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                             tution = (1366*credits) + 5 + 21 + 3 + 100 
                                        elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                             tution = 20501  + 21 + 3 + 5 + 100
                                        else: #loop for more than 18 credits
                                             tution = 20501 + (555*(credits-18)) + 21 + 3 + 5 + 100  
                    
                           else: #if major is CMSE
                                james_madison = input("Are you in James Madison College.")
                                if james_madison == 'yes':
                                   credits = int(input("Credits:"))       
                                   while not (credits):
                                         print("Invalid input. Try again.")
                                         credits = int(input("Credits:"))
                                   else:
                                        if credits < 0:#loop for credit less than 0
                                           print("Invalid input. Try again.")
                                        elif 0 < credits <= 4: #loop for credits till 4
                                             tution = (1366*credits) + 21 + 3 + 50 + 7.50 + 402
                                        elif credits == 5: #loop for 5 credits
                                             tution = (1366*credits) + 21 + 3 + 100 + 7.50 + 670
                                        elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                              tution = (1366*credits) + 5 + 21 + 3 + 100 + 7.50 + 670 
                                        elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                              tution = 20501  + 21 + 3 + 5 + 100 + 7.50 + 670
                                        else: #loop for more than 18 credits
                                               tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 100 + 7.50 + 670  
                                else:
                                      credits = int(input("Credits: "))       
                                      while not (credits):
                                            print("Invalid input. Try again.")
                                            credits = int(input("Credits:"))
                                      else:
                                           if credits < 0:#loop for credit less than 0
                                              print("Invalid input. Try again.")
                                           elif 0 < credits <= 4: #loop for credits till 4
                                                tution = (1366*credits) + 21 + 3 + 402
                                           elif credits == 5: #loop for 5 credits
                                                 tution = (1366*credits) + 21 + 3 + 670 
                                           elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                                  tution = (1366*credits) + 5 + 21 + 3 + 670 
                                           elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                                tution = 20501  + 21 + 3 + 5 + 670
                                           else: #loop for more than 18 credits
                                                tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 670  

            else: #loop for international student    
                level_input = input("Level—freshman, sophomore, junior, senior: ")
                level_input = level_input.lower()
                while not(level_input == 'freshman' or level_input == 'sophomore' or level_input == 'junior' or level_input == 'senior'):
                      print("Invalid input. Try again.")
                      level_input = input("Level—freshman, sophomore, junior, senior: ")
                      level_input = level_input.lower()
                else:
                  if level_input == 'freshman': #loop for freshman starts.
                     freshman_one = input("Are you admitted to the college of Engineering (yes/no): ")
            
                     if freshman_one == 'yes': #loop for admitted in college of engineering.
                       credits = int(input("Credits: "))
                       while not (credits):
                             print("Invalid input. Try again.")
                             credits = int(input("Credits:"))
                       else:
                            if credits < 0:#loop for credit less than 0
                               print("Invalid input. Try again.")
                            elif 0 < credits <= 4: #loop for credits till 4
                               tution = (1325*credits) + 402 + 21 + 3 
                            elif credits == 5: #loop for 5 credits
                               tution = (1325*credits) + 21 + 3 + 670
                            elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                tution = (1325*credits) + 670 + 5 + 21 + 3 
                            elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                 tution = 19883 + 670 + 21 + 3 + 5 
                            else: #loop for more than 18 credits
                                 tution = 19883 + (1325*(credits-18)) + 670 + 21 + 3 + 5 + 660   
                   
                     
            
                     else: #loop for not admitted in college of engineering.
                         freshman_two = input("Are you in James Madison College.")
               
                         if freshman_two == 'yes': #loop for James Madison.
                            credits = int(input("Credits:"))
                            while not (credits):
                                  print("Invalid input. Try again.")
                                  credits = int(input("Credits: "))
                            else:
                                 if credits < 0:#loop for credit less than 0
                                    print("Invalid input. Try again.")
                                 elif 0 < credits <= 4: #loop for credits till 4
                                     tution = (1325*credits) + 21 + 3 + 7.50
                                 elif credits == 5: #loop for 5 credits
                                     tution = (1325*credits) + 21 + 3 + 7.50 
                                 elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                     tution = (1325*credits) + 5 + 21 + 3 + 7.50
                                 elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                      tution = 19883 + 21 + 3 + 5 + 7.50
                                 else: #loop for more than 18 credits
                                       tution = 19883 + (1325*(credits-18)) + 21 + 3 + 5 +7.50 
              
                         else: #loop for not admitted in James Madison
                              credits = int(input("Credits:"))
                              while not (credits):
                                    print("Invalid input. Try again.")
                                    credits = int(input("Credits:"))
                              else:
                                  if credits < 0:#loop for credit less than 0
                                     print("Invalid input. Try again.")
                                  elif 0 < credits <= 4: #loop for credits till 4
                                       tution = (1325*credits) + 21 + 3 
                                  elif credits == 5: #loop for 5 credits
                                       tution = (1325*credits) + 21 + 3 
                                  elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                        tution = (1325*credits) + 5 + 21 + 3 
                                  elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                        tution = 19883 + 21 + 3 + 5 
                                  else: #loop for more than 18 credits
                                       tution = 19883 + (1325*(credits-18)) + 21 + 3 + 5  
                   
                  elif level_input == 'sophomore': #loop for sophomore starts.
                      sophomore_one = input("Are you admitted to the College of Engineering (yes/no): ")
            
                      if sophomore_one == 'yes': #loop for admitted in college of engineering.
                         credits = int(input("Credits: "))
                         while not (credits):
                                print("Invalid input. Try again.")
                                credits = int(input("Credits: "))
                         else:
                              if credits < 0:#loop for credit less than 0
                                 print("Invalid input. Try again.")
                              elif 0 < credits <= 4: #loop for credits till 4
                                   tution = (494*credits) + 402 + 21 + 3 
                              elif credits == 5: #loop for 5 credits
                                   tution = (494*credits) + 21 + 3 + 670
                              elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                    tution = (494*credits) + 670 + 5 + 21 + 3 
                              elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                   tution = 7230 + 670 + 21 + 3 + 5 
                              else: #loop for more than 18 credits
                                   tution = 19883 + (1325.50*(credits-18)) + 670 + 21 + 3 + 5 + 750 
            
                      else: #loop for not admitted in college of engineering.
                           sophomre_two = input("Are you in James Madison College: ")
               
                           if sophomre_two == 'yes': #loop for James Madison.
                              credits = int(input("Credits: "))
                              while not (credits):
                                    print("Invalid input. Try again.")
                                    credits = int(input("Credits: "))
                              else:
                                   if credits < 0:#loop for credit less than 0
                                      print("Invalid input. Try again.")
                                   elif 0 < credits <= 4: #loop for credits till 4
                                        tution = (494*credits) + 21 + 3 + 7.50
                                   elif credits == 5: #loop for 5 credits
                                        tution = (494*credits) + 21 + 3 + 7.50 
                                   elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                        tution = (494*credits) + 5 + 21 + 3 + 7.50
                                   elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                         tution = 7230 + 21 + 3 + 5 + 7.50
                                   else: #loop for more than 18 credits
                                         tution = 7230 + (494*(credits-18)) + 21 + 3 + 5 +7.50 
              
                           else: #loop for not admitted in James Madison
                                credits = int(input("Credits: "))
                                while not (credits):
                                      print("Invalid input. Try again.")
                                      credits = int(input("Credits: "))
                                else:
                                     if credits < 0:#loop for credit less than 0
                                        print("Invalid input. Try again.")
                                     elif 0 < credits <= 4: #loop for credits till 4
                                          tution = (494*credits) + 21 + 3 
                                     elif credits == 5: #loop for 5 credits
                                          tution = (494*credits) + 21 + 3 
                                     elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                          tution = (494*credits) + 5 + 21 + 3 
                                     elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                          tution = 7230  + 21 + 3 + 5 
                                     else: #loop for more than 18 credits
                                           tution = 7230 + (494*(credits-18)) + 21 + 3 + 5  
         
        
                  else:  #loop for junior and senior starts
                      junior_one = input("Enter college as business, engineering, health, sciences, or none:")
                      if junior_one == 'business': #loop for business college
                         cmse = input("Is your major CMSE (\"Computational Mathematics and Engineering)")
                         cmse = cmse.lower()
                         if cmse == 'no': #if major is not CMSE
                            credits = int(input("Credits:"))       
                            while not (credits):
                                  print("Invalid input. Try again.")
                                  credits = int(input("Credits:"))
                            else:
                                 if credits < 0:#loop for credit less than 0
                                    print("Invalid input. Try again.")
                                 elif 0 < credits <= 4: #loop for credits till 4
                                      tution = (1366*credits) + 21 + 3 + 113 
                                 elif credits == 5: #loop for 5 credits
                                      tution = (1366*credits) + 21 + 3 + 226 
                                 elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                      tution = (1366*credits) + 5 + 21 + 3 + 226 
                                 elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                      tution = 20501 + 21 + 3 + 5 + 226
                                 else: #loop for more than 18 credits
                                      tution = 20501 + (1325*(credits-18)) + 21 + 3 + 5 + 226  
             
                         else: #if major is CMSE
                              credits = int(input("Credits:"))       
                              while not (credits):
                                    print("Invalid input. Try again.")
                                    credits = int(input("Credits:"))
                              else: 
                                   if credits < 0:#loop for credit less than 0
                                      print("Invalid input. Try again.")
                                   elif 0 < credits <= 4: #loop for credits till 4
                                        tution = (1366*credits) + 21 + 3 + 113 + 402
                                   elif credits == 5: #loop for 5 credits
                                        tution = (1366*credits) + 21 + 3 + 226 + 670
                                   elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                        tution = (1366*credits) + 5 + 21 + 3 + 226 + 670
                                   elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                        tution = 20501  + 21 + 3 + 5 + 226 + 670
                                   else: #loop for more than 18 credits
                                         tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 226 + 670 
                      
                      elif junior_one == 'engineering': #if college is college of engineering
                           cmse = input("Is your major CMSE (\"Computational Mathematics and Engineering)")
                           cmse = cmse.lower()
                           if cmse == 'no': #if major is not CMSE
                              credits = int(input("Credits:"))       
                              while not (credits):
                                    print("Invalid input. Try again.")
                                    credits = int(input("Credits:"))
                              else:
                                   if credits < 0:#loop for credit less than 0
                                      print("Invalid input. Try again.")
                                   elif 0 < credits <= 4: #loop for credits till 4
                                         tution = (1366*credits) + 21 + 3 + 402
                                   elif credits == 5: #loop for 5 credits
                                         tution = (1366*credits) + 21 + 3 + 670 
                                   elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                         tution = (1366*credits) + 5 + 21 + 3 + 670 
                                   elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                         tution = 20501  + 21 + 3 + 5 + 670
                                   else: #loop for more than 18 credits
                                         tution = 20501+ (573*(credits-18)) + 21 + 3 + 5 + 670  
             
                           else: #if major is CMSE
                                credits = int(input("Credits:"))       
                                while not (credits):
                                      print("Invalid input. Try again.")
                                      credits = int(input("Credits:"))
                                else:
                                     if credits < 0:#loop for credit less than 0
                                        print("Invalid input. Try again.")
                                     elif 0 < credits <= 4: #loop for credits till 4
                                          tution = (1366*credits) + 21 + 3  + 402
                                     elif credits == 5: #loop for 5 credits
                                          tution = (1366*credits) + 21 + 3  + 670
                                     elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                          tution = (1366*credits) + 5 + 21 + 3 + 670
                                     elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                          tution = 20501 + 21 + 3 + 5 + 670
                                     else: #loop for more than 18 credits
                                          tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 226 + 670 
               
                      elif junior_one == 'sciences' or junior_one == 'health':# if the college is sciences or health
                          cmse = input("Is your major CMSE (\"Computational Mathematics and Engineering)")
                          cmse = cmse.lower()
                          if cmse == 'no': #if major is not CMSE
                             credits = int(input("Credits:"))       
                             while not (credits):
                                   print("Invalid input. Try again.")
                                   credits = int(input("Credits:"))
                             else:
                                  if credits < 0:#loop for credit less than 0
                                     print("Invalid input. Try again.")
                                  elif 0 < credits <= 4: #loop for credits till 4
                                       tution = (1366*credits) + 21 + 3 + 50
                                  elif credits == 5: #loop for 5 credits
                                       tution = (1366*credits) + 21 + 3 + 100 
                                  elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                       tution = (1366*credits) + 5 + 21 + 3 + 100 
                                  elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                       tution = 20501 + 21 + 3 + 5 + 100
                                  else: #loop for more than 18 credits
                                       tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 100  
             
                          else: #if major is CMSE
                               credits = int(input("Credits:"))       
                               while not (credits):
                                     print("Invalid input. Try again.")
                                     credits = int(input("Credits:"))
                               else:
                                    if credits < 0:#loop for credit less than 0
                                       print("Invalid input. Try again.")
                                    elif 0 < credits <= 4: #loop for credits till 4
                                         tution = (1366*credits) + 21 + 3  + 402
                                    elif credits == 5: #loop for 5 credits
                                         tution = (1366*credits) + 21 + 3  + 670
                                    elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                         tution = (1366*credits) + 5 + 21 + 3 + 670
                                    elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                         tution = 20501  + 21 + 3 + 5 + 670
                                    else: #loop for more than 18 credits
                                         tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 226 + 670 
           
                      else: #if any other college
                           cmse = input("Is your major CMSE (\"Computational Mathematics and Engineering)")
                           cmse = cmse.lower()
                           if cmse == 'no': #if major is not CMSE
                              james_madison = input("Are you in James Madison College.")
                              if james_madison == 'yes':
                                 credits = int(input("Credits:"))       
                                 while not (credits):
                                       print("Invalid input. Try again.")
                                       credits = int(input("Credits:"))
                                 else:
                                      if credits < 0:#loop for credit less than 0
                                         print("Invalid input. Try again.")
                                      elif 0 < credits <= 4: #loop for credits till 4
                                           tution = (1366*credits) + 21 + 3 + 50 + 7.50
                                      elif credits == 5: #loop for 5 credits
                                           tution = (1366*credits) + 21 + 3 + 100 + 7.50
                                      elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                           tution = (1366*credits) + 5 + 21 + 3 + 100 + 7.50 
                                      elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                           tution = 20501  + 21 + 3 + 5 + 100 + 7.50
                                      else: #loop for more than 18 credits
                                           tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 100 + 7.50  
                              else:
                                   credits = int(input("Credits:"))       
                                   while not (credits):
                                         print("Invalid input. Try again.")
                                         credits = int(input("Credits:"))
                                   else:
                                        if credits < 0:#loop for credit less than 0
                                           print("Invalid input. Try again.")
                                        elif 0 < credits <= 4: #loop for credits till 4
                                             tution = (1366*credits) + 21 + 3 + 50
                                        elif credits == 5: #loop for 5 credits
                                             tution = (1366*credits) + 21 + 3 + 100 
                                        elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                             tution = (1366*credits) + 5 + 21 + 3 + 100 
                                        elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                             tution = 20501  + 21 + 3 + 5 + 100
                                        else: #loop for more than 18 credits
                                             tution = 20501 + (555*(credits-18)) + 21 + 3 + 5 + 100  
                    
                           else: #if major is CMSE
                                james_madison = input("Are you in James Madison College.")
                                if james_madison == 'yes':
                                   credits = int(input("Credits:"))       
                                   while not (credits):
                                         print("Invalid input. Try again.")
                                         credits = int(input("Credits:"))
                                   else:
                                        if credits < 0:#loop for credit less than 0
                                           print("Invalid input. Try again.")
                                        elif 0 < credits <= 4: #loop for credits till 4
                                             tution = (1366*credits) + 21 + 3 + 50 + 7.50 + 402
                                        elif credits == 5: #loop for 5 credits
                                             tution = (1366*credits) + 21 + 3 + 100 + 7.50 + 670
                                        elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                              tution = (1366*credits) + 5 + 21 + 3 + 100 + 7.50 + 670 
                                        elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                              tution = 20501  + 21 + 3 + 5 + 100 + 7.50 + 670
                                        else: #loop for more than 18 credits
                                               tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 100 + 7.50 + 670  
                                else:
                                      credits = int(input("Credits: "))       
                                      while not (credits):
                                            print("Invalid input. Try again.")
                                            credits = int(input("Credits:"))
                                      else:
                                           if credits < 0:#loop for credit less than 0
                                              print("Invalid input. Try again.")
                                           elif 0 < credits <= 4: #loop for credits till 4
                                                tution = (1366*credits) + 21 + 3 + 402
                                           elif credits == 5: #loop for 5 credits
                                                 tution = (1366*credits) + 21 + 3 + 670 
                                           elif 6 <= credits <= 11: #loop for credits from 6 to 11
                                                  tution = (1366*credits) + 5 + 21 + 3 + 670 
                                           elif 12 <= credits <= 18:#loop for 12 to 18 credits
                                                tution = 20501  + 21 + 3 + 5 + 670
                                           else: #loop for more than 18 credits
                                                tution = 20501 + (1366*(credits-18)) + 21 + 3 + 5 + 670  

                      tution += 750
    tution = float(tution)

    print("Tuition is ${:,.2f}.".format(tution)) 
    another_cal = input("Do you want to do another calculation (yes/no): ")
    another_cal = another_cal.lower()
