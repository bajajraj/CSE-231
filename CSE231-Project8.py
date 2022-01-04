# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:07:45 2020

@author: Rajaditya Bajaj
"""

###############################################################################
#                                                                             # 
#   This assignment focuses on the design, implementation and \               #
#   testing of a Python program to find the desired value, display the \      # 
#   values of given and progeammed functions and also about the lists \       #
#   and the tuples and the dictionaries. It also tests the knowledge about \  #
#   the comma seperated files(csv), files, lists, tuples,try and except, \    # 
#   dictionaries and their implementaion.                                     #
#                                                                             #
###############################################################################

import csv
import pylab
from operator import itemgetter


def open_main():
    '''
    This function open the data file if it is correct, otherwise prints \
    the error message and continues to ask the user till the coorect file is \
    entered.
    value = None
    return = file pointer
    '''
   
    while True: #making the loop forever
        fp = input("Enter filename: ")
        try:
            fp = open(fp, encoding='utf-8') #it will open the required file
            return fp
        except FileNotFoundError: #will print error message.
            print("File not found! Please try again!")

def read_file(fp):
    '''
    This function takes the file pointer and then sorts the data in the file \
    into a dictionary according to the required order.
    value = fp (file pointer)
    return = D1, D2, D3 (Dictionaries containing list of tuples)
    '''
    #creating empty dictionaries
    V2 = {}
    V3 = {} 
    V1 = {}
    file = csv.reader(fp)
    next(file, None)
    
    for line in file:
        name = line[0].strip().lower()
        platform = line[1].strip().lower()
        if line[2] == "N/A": #ignoring the N/A present in file.
            continue
        else:
            year = int(line[2]) #converting string to intger
        genre = line[3].strip().lower() #stripping and lowering the string
        publisher = line[4].strip().lower()
        na_sales = float(line[5]) #converting string to float
        europe_sales = float(line[6])
        japan_sales = float(line[7])
        other_sales = float(line[8])
        
        na_sales = na_sales * 1000000
        europe_sales = europe_sales * 1000000
        japan_sales = japan_sales * 1000000
        other_sales = other_sales * 1000000
        
        global_sales = na_sales + europe_sales + japan_sales + other_sales
        #creating empty dictionaries
        list1 = []
        list2 = []
        list3 = []
        #appending the tuples in a list to for further step
        list1.append((name, platform, year, genre, publisher,global_sales))
        list2.append((genre, year, na_sales, europe_sales, japan_sales, \
                      other_sales, global_sales))
        list3.append((publisher, name, year, na_sales, europe_sales, \
                      japan_sales, other_sales, global_sales))
        # adding list in the dictionary if it is present or creating a new key, 
        #if not present
        if name not in V1:
            V1[ name ] = list1
        else:
            V1[ name ] += list1
            
        if genre not in V2:
            V2[ genre ] = list2
        else:
            V2[ genre ] += list2
            
        if publisher not in V3:
            V3[ publisher ] = list3
        else:
            V3[ publisher ] += list3
    D1 = {}
    D2 = {}
    D3 = {}
    # sorting the dictionaries according to the alphabetical order and tuple order.
    for key in sorted(V1):
        D1[ key ] = sorted(V1[ key ], key=itemgetter(5),reverse=True)
    for key in sorted(V2):
        D2[ key ] = sorted(V2[ key ], key=itemgetter(6),reverse=True)
    for key in sorted(V3):
        D3[ key ] = sorted(V3[ key ], key=itemgetter(7),reverse=True)
    
    return D1, D2, D3
    

   

def get_data_by_column(D1, indicator, c_value):
    '''
    This function iterates through the dictionary D1 and return a subset of \
    the data of the global value sales.
    value = D1(dictionary), indicator(string), c_value(string or intger)
    return = list of tuples
    '''
    L = []
    if indicator == 'year': #choosing the indicator
        for key,val in D1.items(): #val in this case is a list of tuples
            for tup in val:
                if tup[2] == c_value:
                    L.append(tup) #appending the tuple
        L.sort(key = itemgetter(5), reverse=True) #sorting it according to the global sales.
        L.sort(key = itemgetter(1)) #sorting it according to the platform
    
    elif indicator == 'platform':  
        for key,val in D1.items(): #val in this case is a list of tuples
            for tup in val:
                if tup[1] == c_value:
                    L.append(tup) #appending the tuples
        L.sort(key = itemgetter(5), reverse = True) #sorting it according to the global sales
        L.sort(key = itemgetter(2)) #sorting it according to the year.
        
    
    return L


def get_publisher_data(D3, publisher):
    '''
    This function iterates through the dictionary D3 and return a subset of \
    the data of the global value sales based on the publisher.
    value = D3(dictionary), publisher(string)
    return = list of tuples
    '''
    pub_list = []
    for key, value in D3.items(): #val in this case is a list of tuples
        if key == publisher:
            pub_list.extend(value)
    
    pub_list.sort(key = itemgetter(1)) # sorting according to publisher
    pub_list.sort(key = itemgetter(7), reverse = True) #sorting according to the global sales.
    return pub_list

def display_global_sales_data(L, indicator):
    '''
    This function prints a table of all the global game sales stored in L1 by \
    either all platforms in a single year or all years for a single platform.
    value = L(list of tuples), indicator(string or integer)
    return = none
    '''
    count = 0
    if indicator == 'year':
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Platform', 'Genre', 'Publisher', 'Global Sales'))
        for value in L:
            name = value[0][0:25]
            platform = value[1]
            genre = value[3][0:15]
            publisher = value[4][0:25]
            count += value[5]
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(name, platform, genre, publisher, value[5]))
        print("\n{:90s}{:<12,.02f}".format('Total Sales', count))
    
    elif indicator == 'platform':
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Year', 'Genre', 'Publisher', 'Global Sales'))
        for value in L:
            name = value[0][0:25]
            genre = value[3][0:25]
            publisher = value[4][0:25]
            count += value[5]
            print("{:30s}{:<10}{:20s}{:30s}{:<12,.02f}".format(name, value[2], genre, publisher, value[5]))
        print("\n{:90s}{:<12,.02f}".format('Total Sales', count))
    

def get_genre_data(D2, year):
    '''
    This function iterates through the dictionary D2 (which contains the list \
    of regional sales by genre) and return a list of the total regional sales \
    per genre whose value at the year column is equal to ‘year’.
    value = D2(dictionary), year(integer)
    return = list of tuples
    '''
    genre_list = []
    for key, value in D2.items():
        total_na_sales = 0
        total_eur_sales = 0
        total_jpn_sales = 0
        total_other_sales = 0
        total_global_sales = 0
        count = 0
#        [(genre, count, total_na_sales, total_eur_sales,
#total_jpn_sales, total_other_sales, total_global_sales),
        for c in value:
            if c[1] == year: 
                total_na_sales += c[2]
                total_eur_sales += c[3]
                total_jpn_sales += c[4]
                total_other_sales += c[5]
                total_global_sales += c[6]
                count += 1
        
        if count != 0:
            genre_list.append((c[0], count, total_na_sales, total_eur_sales, \
                                    total_jpn_sales, total_other_sales, total_global_sales))
            
    genre_list.sort() #sorting according to the genre
    genre_list.sort(key = itemgetter(6), reverse = True) #sorting according to the global sales
    
    return genre_list
            
def display_genre_data(genre_list):
    '''
    This function prints a table of all the total regional sales for each \
    genre stored in genre_list.
    value = genre_list(list of tuples)
    return = none
    '''
    
    header = ['Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    count = 0
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(*header))
    for value in genre_list:
            genre = value[0][0:15]
            na_sales= value[2]
            eur_sales = value[3]
            jpn_sales = value[4]
            other_sales = value[5]
            global_sales = value[6]
            count += value[6]
            print("{:30s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(\
                  genre, na_sales, eur_sales, jpn_sales, other_sales, global_sales))
    print("\n{:90s}{:<15,.02f}".format('Total Sales', count))
    
    
    

def display_publisher_data(pub_list):
    '''
    This function prints a table of all the total regional sales for each \
    genre stored in pub_list. 
    value = pub_list(list of tuples)
    return = none
    '''
   # pub = pub_list[0][0]
    header = ['Title', 'North America', 'Europe', 'Japan', 'Other', 'Global']

    count = 0
    print("{:30s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(*header))
    for value in pub_list:
            title = value[1][0:25]
            na_sales= value[3]
            eur_sales = value[4]
            jpn_sales = value[5]
            other_sales = value[6]
            global_sales = value[7]
            count += value[7]
            print("{:30s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(\
                  title, na_sales, eur_sales, jpn_sales, other_sales, global_sales))
    print("\n{:90s}{:<15,.02f}".format("Total Sales", count))

    
def get_totals(L, indicator):
    '''
    This function takes the list L from get_data_column and iterates through it \
    and creates new lists based on the indicator. The new lists are sorted.
    value = L(list of tuples), indicator(string or integer)
    return = L1 (list), L2 (list)
    '''
    D = {} # creating a new dictionary
    L1 = []
    L2 = []
    if indicator == 'year':
        for platform in L:
            #adding the values in the dictioanry
            if platform[1] not in D:
                D[ platform[1] ] = platform[5]
            else:
                D[ platform[1] ] += platform[5]
        L1 = sorted(D)
        for key in L1:
            L2.append(D[key])
            
    if indicator == 'platform':
        for year in L:
            if year[2] not in D:
                D[ year[2] ] = year[5]
            else:
                D[ year[2] ] += year[5]
        L1 = sorted(D)
        for key in L1:
            L2.append(D[key])
            
    return L1, L2

def prepare_pie(genres_list):
    '''
    This function takes the list, genres_list from the get_genres_data function \
    and returns new lists based on the genre and the global sales.
    value = genres_list(list of tuples)
    return = L1 (list), L2 (list)
    '''
    
    main_list = []
    for genre in genres_list:
        main_list.append((genre[0], genre[6]))
        
    main_list.sort(key = itemgetter(1), reverse = True)
    L1 = []
    L2 = []
    for value in main_list:
        L1.append(value[0])
        L2.append(value[1])
        
    return L1, L2

def plot_global_sales(x,y,indicator, value):
    '''
        This function plots the global sales per year or platform.
        
        parameters: 
            x: list of publishers or year sorted in ascending order
            y: list of global sales that corresponds to x
            indicator: "publisher" or "year"
            value: the publisher name (str) or year (int)
        
        Returns: None
    '''
    
    if indicator == 'year':    
        pylab.title("Video Game Global Sales in {}".format(value))
        pylab.xlabel("Platform")
    elif indicator == 'platform':    
        pylab.title("Video Game Global Sales for {}".format(value))
        pylab.xlabel("Year")
    
    pylab.ylabel("Total copies sold (millions)")
    
    pylab.bar(x, y)
    pylab.show()

def plot_genre_pie(genre, values, year):
    '''
        This function plots the global sales per genre in a year.
        
        parameters: 
            genre: list of genres that corresponds to y order
            values: list of global sales sorted in descending order 
            year: the year of the genre data (int)
        
        Returns: None
    '''
            
    pylab.pie(values, labels=genre,autopct='%1.1f%%')
    pylab.title("Video Games Sales per Genre in {}".format(year))
    pylab.show()
    
def main():
    ''' This is the main function and commands every other function. '''
    
    fp = open_main()
    D1, D2, D3 = read_file(fp)
    # Menu options for the program
    MENU = '''Menu options
    
    1) View data by year
    2) View data by platform
    3) View yearly regional sales by genre
    4) View sales by publisher
    5) Quit
    
    Enter choice: '''
    start = ''
    
    while start != '5': #continue the loop till option is not eqyual to 5
        choice = input(MENU)
        
        #Option 1: Display all platforms for a single year
        if choice == '1':
            try: #for making sure that the input is an integer
                global_sales_input = int(input("Enter year: "))
                L = get_data_by_column(D1, 'year', global_sales_input)
                if len(L) < 1: #to make sure that it is correct year
                    print("The selected year was not found in the data.")
                else:
                    print("\n{:^80s}".format("Video Game Sales in {}".format(str(global_sales_input))))
                    display_global_sales_data(L, 'year')
                    plot_input = input("Do you want to plot (y/n)? ")
                    if plot_input == 'y':
                        L1 , L2 = get_totals(L, 'year')
                        plot_global_sales(L1, L2, 'year', global_sales_input)
                    else:
                        continue  
            except ValueError:
                    print("Invalid year")
                    
        #Option 2: Display all year for a single platform
        elif choice == '2':
            try:
                global_sales_input = str(input("Enter platform: "))
                L = get_data_by_column(D1, 'platform', global_sales_input)
                if len(L) < 1:
                    print("The selected platform was not found in the data.")
                else:
                    print("\n{:^80s}".format("Video Game Sales for {}".format(global_sales_input)))
                    display_global_sales_data(L, 'platform')
                    plot_input = input("Do you want to plot (y/n)? ")
                    if plot_input == 'y':
                        L1 , L2 = get_totals(L, 'platform')
                        plot_global_sales(L1, L2, 'platform', global_sales_input)
                    else:
                        continue    
            except ValueError:
                    print("Invalid platform.")
                    
        #Option 3: Display the regional sales for all video game genres
        elif choice == '3':
            try:
                genre_sales_input = int(input("Enter year: "))
                genre_list = get_genre_data(D2, genre_sales_input)
                if len(genre_list) < 1:
                    print("The selected year was not found in the data.")
                else:
                    print("\nRegional Video Games Sales per Genre")
                    display_genre_data(genre_list)
                    plot_input = input("Do you want to plot (y/n)? ")
                    if plot_input == 'y':
                        L1 , L2 = prepare_pie(genre_list)
                        plot_genre_pie(L1, L2, genre_sales_input)
                    else:
                        continue  
            except ValueError:
                    print("Invalid year")
                    
        #Option 4: Display publisher data
        elif choice == '4':
            # Enter keyword for the publisher name
            publisher_key = input("Enter keyword for publisher: ")
            
            # search all publisher with the keyword
            match = []
            index_list = []
            for key, value in D3.items():
                if publisher_key in key:
                    match.append(D3[key]) #appending the publishers having the publisher_key
            if len(match) > 1:    
                print("There are {} publisher(s) with the requested keyword!".format(len(match)))
                for i,t in enumerate(match):
                    index_list.append((i, t[0][0]))
                    print("{:<4d}{}".format(i,t[0][0]))
                index = int(input("Select the index for the publisher to use: "))
                for value in index_list:
                    if index == value[0]:
                        publisher_name = value[1]
                        pub_list = get_publisher_data(D3, publisher_name)
                        print("\nVideo Games Sales for {}".format(publisher_name))
                        display_publisher_data(pub_list)
                
            
            else:
                print('No publisher name containing "{}" was found!'.format(publisher_key))
                continue
                
#        
        #Option 5: Exiting the program
        elif choice == '5':
            print("\nThanks for using the program!")
            print("I'll leave you with this: \"All your base are belong to us!\"")
            break
        
        else:
            print("Invalid option. Please Try Again!")
        
if __name__ == "__main__":
    main()
#video_game_sales_small.csv
