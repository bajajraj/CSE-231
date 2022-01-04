#######################################################################
#    Computer Project #4
#    This assignment focuses on the design, implementation and \
#    testing of a Python program to calculate and display the \
#    values of selected mathematical functions. It also tests the \
#    knowledge about the functions and their implementation.
#######################################################################  

import math 
EPSILON = 1.0e-7 #Constant used in sine and cosine function

def display_options():
    #''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Display the sum of squares of the first N natural numbers.
             B. Display the approximate value of Pi.
             C. Display the approximate value of the sine of X.
             D. Display the approximate value of the cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
       
    print(MENU)
    

    
def sum_natural_squares(N):
    '''
    Calculates the sum of the squares of a natural number.
    N: enter a string.
    return: sum of the squares if int or none if not int.
    '''
    pass
    if N.isdigit() == True: #to check if its integer or not.
        N = int(N)
        if N > 0: #to have only natural numbers
           answer = (N*(N + 1)*(2*N + 1))/6
           answer = int(answer)
           return answer
        else:
           return None
    else:
        return None
   
def approximate_pi():
    '''
    Calculates the approximate value of pi.
    It takes no parameters.
    return: the approximate value of pi.
    '''
    pass
    term = float(1)
    value_pi = 0
    n = 0
    term = (((-1)**n)/(2*n + 1))
    while abs(term)>EPSILON: #given condition
        value_pi += term
        n+=1
        term = (((-1)**n)/(2*n + 1))
    return round(4*value_pi, 10)   #final value

def approximate_sin(x): 
    '''
    Finds the approximate value of sine function.
    x = a string
    return = approximate value of sine (if float) or None (if a string)
    '''
    pass
    def is_float(s):
        '''
        It checks is the value is entered is float or not.
        s = a string
        return = True (if float) or False (if not float)
        '''
        pass
        try: #to make sure that the give value is float
            s = float(s)
            return True #if float return true.
        except ValueError:
                 return False  #if not float, returns false.
    
    if is_float(x) == True:
        x = float(x)
        term = 1
        sum_sin = 0
        n = 0
        term = (((-1)**n)*(x**(2*n + 1)))/math.factorial(2*n + 1)
        while abs(term)>EPSILON: #given condition
              sum_sin += term
              n+=1
              term = (((-1)**n)*(x**(2*n + 1)))/math.factorial(2*n + 1)
        return round(sum_sin, 10)
    
    else:
        return None
    
           
def approximate_cos(x):
    '''
    Finds the approximate value of cosine function.
    x = a string
    return = approximate value of cosine (if float) or None (if a string)
    '''
    pass
    def is_float(s):
        '''
        It checks is the value is entered is float or not.
        s = a string
        return = True (if float) or False (if not float)
        '''
        pass
        try:
            s = float(s)
            return True #if float return true.
        except ValueError:
              return False  #if not float, returns false.
    if is_float(x) == True:
        x = float(x)
        term = 1
        sum_cos = 0
        n = 0
        term = (((-1)**n)*(x**(2*n)))/math.factorial(2*n)
        while abs(term)>EPSILON:
              sum_cos += term
              n+=1
              term = (((-1)**n)*(x**(2*n)))/math.factorial(2*n)
        return round(sum_cos, 10)
    
    else:
        return None

display_options()

def main():
    ''' 
    It is the function which interacts with the user. The function will prompt \
    if the entered option is incorrect.
    This function also makes sure that the proper prompt is displayed if the user\
    enters a wrong input.
    '''
    pass
    start = ''
    while start != 'x': #starting with any function else x or it will break the loop.
        input_one_lower = input("\n\tEnter option: ").lower()
        if input_one_lower == 'a':
            a_input = input("\nEnter N: ")
            a_answer = a_input
            if sum_natural_squares(a_answer) == None:
                print("\n\tError: N was not a valid natural number. [{}]".format(a_input))
            else:
                print("\n\tThe sum: {}".format(sum_natural_squares(a_answer)))
        
        elif input_one_lower == 'b':
            p = approximate_pi()
            print("\n\tApproximation: {:.10f}".format(p))
            print("\tMath module:   {:.10f}".format(math.pi))
            final_answer = abs(math.pi - p)
            print("\tdifference:    {:.10f}".format(final_answer))
            
        elif input_one_lower == 'c':
            c_input = input("\n\tEnter X: ")
            if approximate_sin(c_input) == None:
                print("\n\tError: X was not a valid float. [{}]".format(c_input))
            else:
                c_input = float(c_input)
                print("\n\tApproximation: {:.10f}".format(approximate_sin(c_input)))
                print("\tMath module:   {:.10f}".format(math.sin(c_input)))
                final_difference = abs(approximate_sin(c_input) - math.sin(c_input))
                print("\tdifference:    {:.10f}".format(final_difference))
            
        elif input_one_lower == 'd':
             d_input = input("\n\tEnter X: ")
             if approximate_cos(d_input) == None:
                print("\n\tError: X was not a valid float. [{}]".format(d_input))
             else:
                d_input = float(d_input)
                print("\n\tApproximation: {:.10f}".format(approximate_cos(d_input)))
                print("\tMath module:   {:.10f}".format(math.cos(d_input)))
                final_difference = abs(approximate_cos(d_input) - math.cos(d_input))
                print("\tdifference:    {:.10f}".format(final_difference))
        
        elif input_one_lower == 'm':
            display_options()
            
        elif input_one_lower == 'x':
            print('Hope to see you again.')
            break
        
        else:
            print("\nError:  unrecognized option [{}]".format(input_one_lower.upper()))
            display_options()

if __name__ == "__main__": 
    main()
    