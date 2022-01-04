###############################################################################
#                                                                             # 
# This assignment focuses on the design, implementation and testing of a \    #
# Python program which uses control structures to solve the problem described\# 
# for the assignment. The project tests the ability to lists, dictionaries, \ # 
# data structures, iterations, functions, and data analysis.                  #
#                                                                             #
###############################################################################

import csv
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from operator import itemgetter


def open_main():
    '''
    This function open the data file if it is correct, otherwise prints \
    the error message and continues to ask the user till the coorect file is \
    entered.
    value = None
    return = file pointer
    '''
    
    fp = input("Data file: ")
    while fp != '': #for input with something
        try:
            fp = open(fp, encoding='utf-8')#it will open the required file
            break
        except FileNotFoundError: #will print error message.
            print("Error. Try again.")
        fp = input("Data file: ")
    else: #if nothing is entered
        fp = open("ncov.csv", encoding='utf-8')
    return fp

def build_dictionary(fp):
    '''
    This function accepts the previously generated file pointer as input and \
    returns the required dictionary. This function iterates over the CSV \
    reader and within each iteration, extracts the needed data and then \
    creates a dictionary that holds all of the data.
    value = fp (file pointer)
    return = master_dict ( nested dictionary)
    '''
    master_dict = {} #creating a new dictionary
    file = csv.reader(fp)
    next(file, None) #skipping the header line
    
    for line in file:
        country = line[2].strip() #stripping the space
        area = line[1].strip()
        if area == '':
            area = "N/A" #assigning strip N/A to empty strings
        else:
            area = line[1]
        last_update = line[3].strip()
        cases = int(line[4])
        deaths = int(line[5])
        recovered = int(line[6])
        D = {area : (last_update, cases, deaths, recovered)} #creating a sub-dictionary
        list1 = []
        list1.append(D) 
        if country not in master_dict: #checking if country exists, if not not creating a one
            master_dict[ country ] = list1 #adding the list in dictionary 
        else:
            master_dict[ country ] += list1

    return master_dict
        
def top_affected_by_spread(master_dict):
    '''
    This function accepts the data dictionary as created by the build_dictionary \
    function and returns a sorted list (in descending order) of the top 10 \
    countries with the most areas affected by nCoV. 
    value = master_dict (nested dictionary)
    return = top_affected_by_spread_list (list of tuples)
    '''
    top_affected_by_spread_list = []
    for k, L in master_dict.items():
        top_affected_by_spread_list.append((k, len(L))) #appending the country and number of areas affected
    #sorting the list according to the number of people affected    
    top_affected_by_spread_list = sorted(top_affected_by_spread_list,key=itemgetter(1), reverse = True) 
    top_affected_by_spread_list = sorted(top_affected_by_spread_list) #sorting countries in alphabetical order 
    top_affected_by_spread_list = sorted(top_affected_by_spread_list,key=itemgetter(1), reverse = True)
    top_affected_by_spread = top_affected_by_spread_list[0:10] #returning the top ten countries
    return(top_affected_by_spread)

    

    

def top_affected_by_numbers(master_dict):
    '''
    This function accepts the data dictionary and produces a sorted list of \
    the top 10 countries with the most total people affected within every country. 
    value = master_dict (nested dictionary)
    return = top_affed\cted_by_numbers_list (list of tuples)
    '''
    
    top_affected_by_numbers_list = []
    for k, L in master_dict.items(): #this is for the master_dict
        count = 0
        for D in L: #this is for the list inside master_dict
            for key, value in D.items(): #dictionaries inside master_dict
                count += value[1]
        top_affected_by_numbers_list.append((k, count)) #appening the country and total cases
    #sorting the list according to the number of people affected
    top_affected_by_numbers_list = sorted(top_affected_by_numbers_list,key=itemgetter(1), reverse = True) 
    top_affected_by_numbers_list = sorted(top_affected_by_numbers_list) #sorting countries in alphabetical order
    top_affected_by_numbers_list = sorted(top_affected_by_numbers_list,key=itemgetter(1), reverse = True)
    
    return(top_affected_by_numbers_list[0:10]) #returning the top ten countries

def affected_states_in_country(master_dict, country):

    '''
    This function takes in the data dictionary and the name of a country \
    (string) and returns a set of affected areas within a country.
    value = master_dict (nested dictionary), country (string)
    return = affected_states_in_country_set (set)
    '''
    country = country.lower()
    affected_states_in_country_set = set() #creating an empty set
    for k, L in master_dict.items(): #this is for master_dict
        k = k.lower()
        if country == k: 
            for D in L: #for list master_dict
                for key, value in D.items():
                    affected_states_in_country_set.add(key) #adding the area to the set
    
    return affected_states_in_country_set
            
def is_affected(master_dict, country):
    '''
    This function takes in the data dictionary and the name of a country \
    (string) and returns a Boolean (True or False) depending on whether a \
    country is affected by nCoV.
    value = master_dict (nested dictionary), country(string)
    return = Boolean
    '''
    country = country.lower()
    basic_set = set()
    for k, L in master_dict.items():
        k = k.lower()
        basic_set.add(k)
        
    return (country in basic_set) #boolean for checking if country is in dictionary
    
def plot_by_numbers(list_of_countries, list_of_numbers):
    '''
        This function plots the number of areas/people inffected by country.
        
        parameters: 
            list_of_countries: list of countries
            list_of_numbers: list of the number of areas/people inffected
            
        Returns: None
    '''
    fig, ax = plt.subplots()
    
    x_pos = [i for i, _ in enumerate(list_of_countries)]
    
    ax.barh(x_pos, list_of_numbers, align='center', color='red')
    ax.set_yticks(x_pos)
    ax.set_yticklabels(list_of_countries)
    ax.invert_yaxis()
    ax.set_xlabel('Count')
    ax.set_title('Novel Coronavirus statistics')
    
    plt.show()

def main():
    ''' This is the main function and commands every other function. '''
    
    BANNER = '''
.__   __.   ______   ______   ____    ____
|  \ |  |  /      | /  __  \  \   \  /   /
|   \|  | |  ,----'|  |  |  |  \   \/   / 
|  . `  | |  |     |  |  |  |   \      /  
|  |\   | |  `----.|  `--'  |    \    /   
|__| \__|  \______| \______/      \__/  
    '''
    print(BANNER)
    MENU = ''' 
[1] Countries with most areas infected
[2] Countries with most people affected
[3] Affected areas in a country
[4] Check if a country is affected
[5] Exit

Choice: '''
    fp = open_main()
    master_dict = build_dictionary(fp)
    start = ''
    while start != '5':
        choice = input(MENU)
        
        #Option 1: Countries with most affected areas
        if choice == '1':
            print("{:<20s} {:15s}".format("Country", "Areas affected"))
            print("-"*40)
            top_affected_spread = top_affected_by_spread(master_dict)
            for value in top_affected_spread:
                print("{:<20s} {:5d}".format(value[0], value[1]))
            print()
            plot = input('Plot? (y/n) ')
            if plot == 'y': #if plot = y
                top_five = top_affected_spread[0:5] #only top five needed
                L1 = []
                L2 = []
                #making corresponding list
                for value in top_five:
                    L1.append(value[0])
                    L2.append(value[1])
                plot_by_numbers(L1, L2)
            else:
                continue
        
        #Option 2: Countries with most affected people
        elif choice == '2':
            print("{:<20s} {:15s}".format("Country", "People affected"))
            print("-"*40)
            top_affected_people = top_affected_by_numbers(master_dict)
            for value in top_affected_people:
                print("{:<20s} {:5d}".format(value[0], value[1]))
            print()
            plot = input('Plot? (y/n) ')
            if plot == 'y': #if plot = y
                top_five1 = top_affected_people[1:6] #only top five needed
                L3 = []
                L4 = []
                #making corresponding list
                for value in top_five1:
                    L3.append(value[0])
                    L4.append(value[1])
                plot_by_numbers(L3, L4)
            else:
                continue
            
        #Option 3: Areas affected
        elif choice == '3':
            country = input("Country name: ")
            print("-"*30)
            states = affected_states_in_country(master_dict, country)
            if len(states) != 0:#if set is  not empty
                print("{:<30s}".format("Affected area"))
                print("-"*30)
                list6 = []
                for value in states:
                    list6.append(value)
                list6.sort()
                for i, c in enumerate(list6):#enumerating beacuse we want index
                    print( "[{:02d}] {:<30s}".format((i+1),c))
            else:
                print("Error. Country not found.")
                
        #Option 4: is country affected
        elif choice == '4':
            country = input("Country name: ")
            print("-"*30)
            boolean_is = is_affected(master_dict, country) 
            if boolean_is == True:
                print("{} is affected.".format(country))
            else:
                print("{} is not affected.".format(country))
            
        #Option 5: Exiting the program    
        elif choice == '5':
            print("Stay at home. Protect your community against COVID-19")
            break
        
        #if wrong choice is entered    
        else:
            print("Error. Try again.")
    

    
if __name__ == "__main__":    
    main()
