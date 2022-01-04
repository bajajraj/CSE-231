##########################################################################
#   This assignment focuses on the design, implementation and \
#    testing of a Python program to find the desired value display the \
#    values of selected display functions. It also tests the \
#    knowledge about the function, files, and their implementaion.
##########################################################################

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
        fp = input("Input a file name: ")
        try:
            fp = open(fp, 'r')
            return fp
        except FileNotFoundError:
            print("Error: file not found. Please try again.")

def get_us_value(fp):
    '''
    This function find the percentage out of the specify state.
    fp = file pointer
    return = float( specified percentage)
    '''
    fp.seek(0)
    fp.readline()
    fp.readline()
    for line in fp:
        states = line[:25].strip()
        percentage = line[25:29].strip()
        if states == "United States":
            return (float(percentage))

def get_min_value_and_state(fp):
    ''' 
    This function finds the minimum value of the given percentages.
    fp = file pointer
    return = string(state), float(percentage)
    '''
    fp.seek(0)
    fp.readline()
    fp.readline()
    min_value = 1000
    min_state = ''
    for line in fp:
        states = line[:25].strip()
        percentage = line[25:29].strip()
        if percentage == "NA": #to ignore the NA values.
            continue
        percentage = float(percentage)
        if percentage < min_value: #to have the minimum percentage
            min_value = percentage
            min_state = states
    return (min_state, min_value)

def get_max_value_and_state(fp):
    ''' This function finds the maximum value of the given percentages.
    fp = file pointer
    return = string(state), float(percentage)'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    max_value = 0
    max_state = ''
    for line in fp:
        states = line[:25].strip()
        percentage = line[25:29].strip()
        if percentage == "NA":   #to ignore the NA values
            continue
        percentage = float(percentage)
        if percentage > max_value: #to have the maximum value
            max_value = percentage
            max_state = states
    return (max_state, max_value)

def display_herd_immunity(fp):
    ''' 
    This function displays the  of the given percentages and states which are less \
    than 90%.
    fp = file pointer
    return = string(state), string(percentage)
    '''
    fp.seek(0)
    fp.readline()
    fp.readline()
    print("\nStates with insufficient Measles herd immunity.")
    print("{:<25s}{:>5s}".format("State", "Percent"))
    for line in fp:
        states = line[:25].strip()
        percentage = line[25:29].strip()
        if percentage == "NA":
            continue
        percentage = float(percentage)
        if percentage < 90:
            percentage = str(percentage)
            print("{:<25s}{:>5s}%".format(states, percentage))
            continue
        
def write_herd_immunity(fp):
    ''' 
    This function creates a new file named herd.txt of the given \
    percentages and states which are less than 90%.
    fp = file pointer
    return = new file
    '''
    herd_file = open("herd.txt", 'w')
    fp.seek(0)
    fp.readline()
    fp.readline()
    herd_file.write("\nStates with insufficient Measles herd immunity." + '\n')
    herd_file.write("{:<25s}{:>5s}".format("State", "Percent") + '\n')
    for line in fp:
           states = line[:25].strip()
           percentage = line[25:29].strip()
           if percentage == "NA":
               continue
           percentage = float(percentage)
           if percentage < 90:
               percentage = str(percentage)
               herd_file.write("{:<25s}{:>5s}%".format(states, percentage) + '\n')
               continue
    herd_file.close()
        
    
def main():
    ''' 
    It is the function which interacts with the user and displays all the values.
    '''
    gp = open_main()
    
    print()
    print(gp.readline())
    
    guv = get_us_value(gp)
    
    print()
    print("Overall US MMR coverage: {}%".format(guv))
    
    min_value_answer = get_min_value_and_state(gp)
    print("State with minimal MMR coverage: {} {}%".format(min_value_answer[0], min_value_answer[1])) 
    
    max_value_answer = get_max_value_and_state(gp)
    print("State with maximum MMR coverage: {} {}%".format(max_value_answer[0], max_value_answer[1]))
    

    display_herd_immunity(gp)
    write_herd_immunity(gp)
    gp.close()
    
if __name__ == "__main__":
    main()   