###############################################################################
#    This assignment focuses on the design, implementation and \
#    testing of a Python program to find the desired value display the \
#    values of given and progeammed functions and also about the lists \
#    and the tuples. It also tests the knowledge about the comma seperated \
#    files(csv), files, lists, tuples,try and except, and their implementaion.
###############################################################################

import math
import csv

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
            fp = open(fp) #it will open the required file
            return fp
        except FileNotFoundError: #will print error message.
            print("File not found! Please try again!")

def calc_multipliers():
    '''
    This function calculates the multipliers and returns them in a form of list.
    value = None
    return = multipliers(list)
    '''
   
    multipliers = []
   
    for n in range(2, 61): #specifing the range
        v = 1/math.sqrt(n*(n-1)) #formula to be used
        multipliers.append(v) #appending the multipliers to form a list
    return multipliers

def calc_priorities(state,population,list_of_multipliers):
    '''
    This function takes the state(string), population(string), and \
    list_of_multipliers to return a list of priorities of each state.
    value = state(string), population(string), list_of_multipliers(list)
    return = a list of tuples(priority value, state)
    '''
    data = []
    for number in list_of_multipliers:
        priority = number * population
        priority = int(priority) #converting string to an integer
        data.append((priority,state)) #appending the tuples to form a list
       
    data.sort(reverse = True) #arranging it in decreasing order of number
    return (data)

def read_file_make_priorities(fp, multipliers):
    '''
    This function accepts a file pointer and a list of floats (returned from \
    the calc_multipliers function) and returns two lists. The first list is \
    list of lists where each list is a state and a count of representatives \
    for the state and the second list is  a list of priority tuples \
    (priority, state) sorted in decreasing order of priority. 
    value = fp(file pointer), multipliers(list of floats)
    returns = state_reps(a list of lists), priorities(a list of tuples)
    '''
    state_reps = []
    priority = []
    reader = csv.reader(fp)
    next(reader, None)
   
    for line_list in reader:
        s = line_list[1].strip().strip('"')
        p = line_list[2]
        if s == "Puerto Rico" or s == "District of Columbia":
            continue
        else:
            p = int(p)
            n = []
            n.append(s)
            n.append(1)
            state_reps.append(n)
            state_list = calc_priorities(s, p, multipliers)
            priority += state_list
    state_reps.sort()
    priorities = sorted(priority,reverse=True)
    return state_reps, priorities[0:385] 
   
def add_to_state(state, list_of_states):
    '''
    This function accepts a state (str) and the list_of_states which is a \
    list of lists representing a state’s name and a count of its \
    representatives. The purpose of this function is to find the state in \
    the list of states and add one to its representative count.
    value = state (str), list_of_states (a list of lists)
    return = a list of lists
    '''
    for n in list_of_states:
        if n[0] == state:
            n[1] += 1
            
def display(list_of_states):
    '''
    This function accepts the list_of_states (a list of list) and displays them\
    in a particular order.
    '''
    print("{:<15s}{:>4s}".format("State", "Representatives"))
    for n in list_of_states:
        print("{:<15s}{:>4d}".format(n[0], n[1]))
        
            
def main():
    '''
    It is the function which interacts with the user and displays all the values.
    '''
    fp = open_main()
    multipliers = calc_multipliers()
    state_reps, priorities = read_file_make_priorities(fp, multipliers)
    list_of_states = state_reps
    for n in range(0,385):
        state = priorities[n][1]
        add_to_state(state, list_of_states)
    list_of_states.sort()
    print()
    display(list_of_states)
    
if __name__ == "__main__":
    main()