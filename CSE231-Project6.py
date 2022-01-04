# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:08:48 2020

@author: Rajaditya Bajaj
"""
#########################################################################
#   This assignment focuses on the design, implementation and \
#    testing of a Python program to find the desired value display the \
#    values of given and progeammed functions. It also tests the \
#    knowledge about the comma seperated files(csv), files, lists, \
#    tuples,try and except, and their implementaion.
#########################################################################

import csv
from operator import itemgetter
def open_main():
    '''
    This function open the data file if it is correct, otherwise prints \
    the error message and continues to ask the user till the coorect file is \
    entered.
    value = None
    return = file pointer
    '''
    fun = ''
    while fun == '': #it will make loop go on forever till the correct value is entered.
        fp = input("Enter filename: ")
        try:
            fp = open(fp) #it will open the required file
            return fp
        except FileNotFoundError: #will print error message.
            print("File not found! Please try again!")
            
def read_file(fp):
    '''
    This function takes the file pointer from the open_main() function and \
    creates a master list of the information which is going to be used for \
    future function.
    fp = file pointer
    return = list
    '''
    data = [] #empty list for the start
    reader = csv.reader(fp) #marking the first line
    next(reader, None) #skipping the first line
    for line_list in reader: 
        data.append(line_list) #adding everything in a master list
    return data

def shoots_left_right(master_list):
    '''
    This function takes in the master list from read_file function and will \
    then show the number of shoots that right or left respectively.
    master_list = read_file(fp)
    return = int(left shoot), int(right shoot)
    '''
    left = 0
    right = 0
    for ch in master_list:
        if ch[1] == 'L': #left sided throws in S/C
            left += 1
        elif ch[1] == 'R': #left sided throws in S/c
            right += 1
    return(left, right)

def position(master_list):
    '''
    This function takes in the master list from the read_file function and \
    will then show the number of player in a given position, i.e., left, \
    right, center, or defence.
    master_list = read_file(fp)
    return = int(left), int(right), int(center), int(defence)
    '''
    left = 0
    right = 0
    center = 0
    defence = 0
    for ch in master_list:
        if ch [2] == 'L': #left position in Pos
            left += 1
        elif ch[2] == 'R': #right position in Pos
            right += 1
        elif ch[2] == 'C': #center position in Pos
            center += 1
        elif ch[2] == 'D': #defence position in Pos
            defence += 1
    return(left, right, center, defence)

def off_side_shooter(master_list):
    '''
    This function takes in the master list from the read_file function and \
    then will return the number of players throwing right(S/C) and having \
    left position(Pos) or throwing left(S/C) and having right position(Pos).
    master_list = read_file(fp)
    return = int(right-left), int(left-right)
    '''
    left_right = 0
    right_left = 0
    for ch in master_list:
        if (ch[1] == 'R' and ch[2] == 'L'): #right throw and left position
           left_right += 1
           continue
        elif (ch[1] == 'L' and ch[2] == 'R'): #left throw and right position
            right_left += 1
            continue
    return(left_right, right_left)

    
def points_per_game(master_list):
    '''This function takes in information from the read_file() function and \
    will return the list of top ten players having maximum points per game(S\GP) \
    and have it arranged in decreasing and sorted order.
    master_list = read_file(fp)
    return = a tuple having float(point per game), str(player name) and str(position)
    '''
    data = [] #empty list for appending the tuple
    for line_list in master_list:
        num_list = float(line_list[18]) #converting string to float
        data.append((num_list, line_list[0], line_list[2])) #adding the tupple into list
        
    
    data = sorted(data,key=itemgetter(1),reverse=True) #sorting the name
    data = sorted(data,reverse=True) #sorting the points in decreasing order
    return(data[0:10]) #returning the top ten player
    
def games_played(master_list):
    '''
    This function takes in information from the read_file() function and \
    will return the list of top ten players having played game(GP) \
    and have it arranged in decreasing and sorted order.
    master_list = read_file(fp)
    return = a tuple having int(games played) and str(player name)
    '''
    data = [] #empty list for appending the tuple
    for line_list in master_list:
        num_list = int(line_list[3].replace(',','')) #replacing comma and converting to an integer
        data.append((num_list, line_list[0])) #adding tupple to the list
        
    data = sorted(data,key=itemgetter(1),reverse=True) #sorting the name
    data = sorted(data,reverse=True) #sorting the points in decreasing order
    return(data[0:10]) #returning the top ten player
    
def shots_taken(master_list):
    '''
    This function takes in information from the read_file() function and \
    will return the list of top ten players having maximum number of \
    shots taken(S) and have it arranged in decreasing and sorted order.
    master_list = read_file(fp)
    return = a tuple having int(shots taken) and str(player name)
    '''
    data = [] #empty list for adding the tuple
    for line_list in master_list:
        if line_list[9] == '--': #to ignore the '--' which is not an integer
            continue 
        num_list = int(line_list[9].replace(',','')) #replacing comma and converting to an integer
        data.append((num_list, line_list[0])) #adding tupple to the list
        
    data = sorted(data,key=itemgetter(1),reverse=True) #sorting the name
    data = sorted(data,reverse=True) #sorting the points in decreasing order
    return(data[0:10]) #returning the top ten player
    
    
def main():
    '''
    It is the function which interacts with the user and displays all the values.
    '''
    open_function = open_main()
    print()
    
    read_file_function = read_file(open_function)
    
    shoots_left_right_function = shoots_left_right(read_file_function)
    print("{:^10s}".format("Shooting"))
    print("left:  {:4d}".format(shoots_left_right_function[0]))
    print("right: {:4d}".format(shoots_left_right_function[1]))
    print()
    
    position_function = position(read_file_function)
    print("{:^12s}".format("Position"))
    print("left:    {:4d}".format(position_function[0]))
    print("right:   {:4d}".format(position_function[1]))
    print("center:  {:4d}".format(position_function[2]))
    print("defense: {:4d}".format(position_function[3]))
    print()
    
    off_side_shooter_function = off_side_shooter(read_file_function)
    print("{:^24s}".format("Off-side Shooter"))
    print("left-wing shooting right: {:4d}".format(off_side_shooter_function[0]))
    print("right-wing shooting left: {:4d}".format(off_side_shooter_function[1]))
    print()
    
    points_per_game_function = points_per_game(read_file_function)
    print("{:^36s}".format("Top Ten Points-Per-Game"))
    print("{:<20s}{:>8s}{:>16s}".format("Player", "Position", "Points Per Game"))
    for people in points_per_game_function: #for printing a list form of a columns
        print("{:<20s}{:>8s}{:>16.2f}".format(people[1], people[2], people[0]))
    print()
    
    games_played_function = games_played(read_file_function)
    print("{:^36s}".format("Top Ten Games-Played"))
    print("{:<20s}{:>16s}".format("Player", "Games Played"))
    for people in games_played_function: #for printing the list in form of a column
        print("{:<20s}{:>16,d}".format(people[1], people[0]))
    print()
    
    shots_taken_function = shots_taken(read_file_function)
    print("{:^36s}".format("Top Ten Shots-Taken"))
    print("{:<20s}{:>16s}".format("Player", "Shots Taken"))
    for people in shots_taken_function: #for printing a list in form of a columns
        print("{:<20s}{:>16,d}".format(people[1], people[0]))

if __name__ == "__main__":
    main()