###############################################################################
#   
#   Project 11
#   
#   This assignment focuses on the design, implementation and testing of a \     
#   Python program which uses control structures to solve the problem described\  
#   for the assignment. The main goal of the project is to make students 
#   comfortable with classes. The project tests the ability to lists, \
#   manipulation of iteration of classes, calling the classes, and use of \
#   while, if, and for loop.                                      
#                                                                               
###############################################################################

MAP = {"U":"Up","D":"Down","L":"Left","R":"Right"}

class Student(object):
    '''
        This class tells the ID of a student has a list of inventory of student 
        in a room.
    '''
    def __init__(self, item_list=None, classroom_id=-1):
        '''Initializes yourself, with an empty backpack by default. The default position of the student is room -1.'''
        
        if item_list == None:
            self.backpack = []
        else:
            self.backpack = item_list
        self.classroom_id = classroom_id

    def __repr__(self):
        '''Returns a string representation of the student.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the student's inventory.'''
        s = "Backpack: "
        if len(self.backpack) == 0:
            s += "Empty"
        else:
            for item in self.backpack:
                s += item + ", "
            else:
                s = s[:-2] # remove trailing comma and space
        return s

    def __eq__( self, S ):
        '''
            It returns True if  Student ‘s classroom id and backpack are equal to
            the classroom id and backpack of S, otherwise returns False.
            Value = S
            Return = Boolean
        '''
        # if the value classroom of backpack is equal to S 
        if self.backpack == S.backpack and self.classroom_id == S.classroom_id:
            return True
        else:
            return False
     
    def place(self, classroom_id):
        '''
             This function places a student in a classroom.
             Value = classroom_id (string)
             Return = None
        '''
        self.classroom_id = classroom_id
        
    
    def add_item(self, item):
        '''
            If the items in backpack is not more than six, then it adds the item
            in the backpack, otherwise prints an error message.
            Value = item (string)
            Return = None
        '''
        if len(self.backpack) >= 6: #if there are more than six items
            print("Backpack is full.")
        else:
            self.backpack.append(item) #appending the item in the backpack
            

    def remove_item(self, item):
        '''
            If the items in in backpack it removes the item in the backpack, 
            otherwise prints an error message.
            Value = item (string)
            Return = None
        '''
        if item in self.backpack: #if item is in backpack, append it
            self.backpack.remove(item)
        else: #else, print an error message
            print("Failed to remove item from backpack.")
            


class Classroom(object):
    '''
         It is a class that represents a single classroom at a time. It is associated
         with each classroom is a unique id, an int, and a course. It may also
         have one or more directions to other rooms in the hallway – which gives many 
         options to run to other classrooms – and there are one or more items in the classrooms.
    '''
    def __init__(self, text_desc="0 empty"):
        '''Initialzes a classroom. By default it has id 0 and is a "empty" room with no inventory or exits.'''
        description = text_desc.split()

        self.id = int(description[0])
        self.course = description[1]

        # Initialize a list of items as empty
        self.backpack = []
        
        # Initialize a dictionary of potential exits as empty
        self.exits = {}
        
        if len(description) > 2: #if there is something more than two.
            for i in description[2:]:
                direction = i[0]
                if direction in "UDLR": #if it is direction or not.
                    classroom_id = int(i[1:])
                    self.exits[ direction ] = classroom_id
                else:
                    self.backpack.append(i)
            

    def __repr__(self):
        '''Returns a string representation of the classroom.'''
        classroom_repr = '''Classroom("''' + repr(self.id) + " " + self.course

        for direction in self.exits:
            classroom_repr += " {}".format(direction) + repr(self.exits[direction])

        for item in self.backpack:
            classroom_repr += " " + item

        classroom_repr += '''")'''

        return classroom_repr

    def __str__(self):
        '''Returns a string representing the room in a nice conversational style.'''

        # Basic classroom description
        classroom_str = "You see a " + self.course + " classroom."

        # List the things in the classroom
        if len(self.backpack) == 1:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + "."
        if len(self.backpack) == 2:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + \
                             " and a " + self.backpack[1] + "."
        elif len(self.backpack) > 2:
            classroom_str += " On the desk you see "
            for item in self.backpack[:-1]:
                classroom_str += "a " + item + ", "
            classroom_str += "and a " + self.backpack[-1] + "."

        # List the exits
        if len(self.exits) == 0:
            classroom_str += " Run through the classroom grab what you need (if possible). Exit and run to the exam!"
        elif len(self.exits) == 1:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + "."
        elif len(self.exits) == 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + " or " + MAP[list(self.exits.keys())[1]] + "."
        elif len(self.exits) > 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go "
            for direction in list(self.exits.keys())[:-1]:
                classroom_str += MAP[direction] + ", "
            classroom_str += "or " + MAP[list(self.exits.keys())[-1]] + "."

        return classroom_str
    
    def __eq__( self, C ):
        '''
            This function returns True if Classroom id, course, exits and backpack
            are equal to the id, course, exits and backpack of C. Otherwise, returns False.
            Value = C
            Return = Boolean
        '''
        #if the backpack, course_id and the exits are equal
        if self.backpack == C.backpack and self.id == C.id and self.exits == C.exits:
            return True
        else:
            return False
            
    def add_item(self, item):
        '''
            This function adds an item to the classroom's inventory or the backpack.
            Value = item (String)
            Return = None
        '''
        self.backpack.append(item)
        

    def remove_item(self, item):
        '''
            This function removes an item from the room's inventory, if it is 
            there, else prints an error message.
            Value = item (string)
            return = None
        '''
        if item in self.backpack:
            self.backpack.remove(item)
        else:
            print("Failure to find the item in the classroom.")

    def get_room(self, direction):
        '''
            This function returns the room id in the given direction, or False
            if there is no such room.
            direction = U (string)
            Return = L (string) or Boolean
        '''
    
        for k, L in self.exits.items():
            if k == direction:
                return L
        return False
    

        

class Rush(object):
    '''
        It is the class that governs the main function itself. It is responsible for
        interactions between the user, the character, and the rooms.
    '''

    def __init__(self, filename="rushing.txt"):
        '''Initializes the student rushing to class.  The student starts in the classroom with the lowest id.'''

        # First make a student start with an empty inventory
        self.student = Student()

        # Create classrooms are an empty dictionary
        self.classrooms = {}
        
        # Now read the file to get the classroom lines
        fp = open(filename, 'r')
        for line in fp:
            line = line.strip()
            line_list = line.split()
            classroom_id = int(line_list[0])
            if classroom_id not in self.classrooms.keys():
                self.classrooms[classroom_id] = Classroom(line)
    
        # Place the student in the room with lowest id
        self.student.place(min(self.classrooms.keys()))
        

    def __repr__(self):
        '''Returns a string representation.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the journey to the class, simply giving the number of rooms.'''
        search_str = "You are searched in "
        if len(self.classrooms) == 0:
            search_str += "no classrooms at all, you are in the hallway. You are late run in a random class and get items from the desks."
        elif len(self.classrooms) == 1:
            search_str += "a classroom."
        else:
            search_str += "a set of " + str(len(self.classrooms)) + \
                          " classrooms."

        return search_str

    def intro(self):
        '''Prints an introduction to the search for items because you are late
        This prompt includes the commands.'''
        print("\nAHHHH! I'm late for class\n")
        print("*runs out the house to catch the bus with an empty backpack*")

        print("\nYou're popular and have friends in many classes. Find and collect any items you find useful for your exam.")
        print("You are already late, and have a CSE231 Final Exam in 10 mins.\n")
        self.print_help()


    def print_help(self):
        '''Prints the valid commands.'''
        print("Use your instincts: ")
        print("*thinks*.. *thinks*.. what to do?!?!?!?!")
        print("*running*")
        print("S or search -- prints a description of the classroom you ran into")
        print("B or backpack - prints a list of items in your backpack")
        print("P pencil or pickup pencil - *mental* instruction to pick up an item called pencil")
        print("DR pencil or drop pencil - *mental* instruction to drop off an item called pencil")
        print("U or up - *mental* instruction to up the hallway to find another classroom")
        print("D or down - *mental* instruction to down the hallway to find another classroom")
        print("R or right - *mental* instruction to right in the hallway to find another classroom")
        print("L or left - *mental* instruction to left in the hallway to find another classroom")
        print("G or giveup - I have no more time, I need to get to class!!!")
        print("H or help - prints this list of options again")
        print()
        print("Remember that uppercase and lowercase SHOULD NOT matter. ")
        print("JUST GRAB WHAT YOU NEED AND GET TO CLASS TO START YOUR FINAL EXAM!!! HURRYYYY!!!")
        print()

    def prompt(self):
        '''Prompts for input and handles it, whether by error message or handling a valid command.
        Returns True as long as the user has not chosen to quit, False if they have.'''

        print("In room {} with course {}".format(self.student.classroom_id,self.classrooms[self.student.classroom_id].course))
        print(self.student)
        user_input = input("Enter a command (H for help): ")
        print()

        # Handle input: split for pickup/drop, capitalization unimportant for commands
        input_list = user_input.split()

        if len(input_list) == 0:
            user_input = "?"  # No command is not a valid command
            return False
        else:
            try:
                command = input_list[0].upper()  # The command
                if len(input_list) > 1:
                    item = input_list[1]
                if command == 'S':
                    self.search()
                elif command == 'B':
                    self.backpack()
                elif command == 'P':
                    self.pickup(item)
                elif command == 'DR':
                    self.drop(item)
                elif command in "UDLR":
                    self.move(command)
                elif command == 'G':
                    print("I have no more time, I need to get to class!!!")
                    return False
                elif command == 'H':
                     self.print_help() 
                else:
                    print("Unfortunately, that's not a valid option.")
                    return False
            except:
                print("Problem with the option or the item.")
                return False
        if self.win():
            return "win"
        return True

    def search(self):
        '''Prints the description of the current room.'''
        current_classroom = self.classrooms[self.student.classroom_id]
        print(current_classroom)

    def backpack(self):
        '''
            Prints the student’s inventory in their backpack.
        '''
        print(self.student)

    def pickup(self, item):
        '''
            This function removes an item from the classroom and add it to the 
            student’s backpack.
            Value = item (string)
            Return = None
        '''
        #description of current classroom
        classroom = self.classrooms[self.student.classroom_id] 
        classroom_items = classroom.backpack[:] #copying the backpack list
        classroom.remove_item(item) #remove if present
        if classroom.backpack != classroom_items:
            self.student.add_item(item)
           
    def drop(self, item):
        '''
            This removes item from the student’s backpack and places it in the classroom.
            Value = item (string)
            Return = None
        '''
        #description of current classroom
        classroom = self.classrooms[self.student.classroom_id]
        student_items = self.student.backpack[:] #copying the student backpack list
        self.student.remove_item(item) #remove if present
        if self.student.backpack != student_items:
            classroom.add_item(item)

    def move(self, direction):
        '''
            This function moves the student in the specified direction if the
            current classroom has that direction in its attribute, otherwie 
            prints an error message.
        '''
        #description of current classroom
        current_classroom = self.classrooms[self.student.classroom_id]
        if current_classroom.get_room(direction): #direction in current class
            self.student.place(current_classroom.get_room(direction))        
            print("You went " + MAP[direction] + " and found a new classroom.")
        else:                   
            errMsg = "Unfortunately, you went " + MAP[direction] + " and there was no classroom."
            print(errMsg)
        

    def win(self):
        '''
            This method checks that the student has entered the given string and
            has in their backpack the required item. 
        '''
        winning_backpack = ['cheatsheet', 'eraser', 'paper', 'pencil']
        current_classroom = self.classrooms[self.student.classroom_id]
        if set(winning_backpack).issubset(set(self.student.backpack))and current_classroom.course == 'CSE231':
            return True
        return False
        
            

    
def main():
    '''
    Prompts the user for a file, then plays that file until the user chooses to give up.
    '''

    while True:
        try:
            filename = input("Enter a text filename: ")
            escapade = Rush(filename)
            break
        except IOError:
            print("Cannot open file:{}. Please try again.".format(filename))
            continue
    
    escapade.intro()
    escapade.__str__()
    escapade.search()
    
    keep_going = True
    while keep_going:
        keep_going = escapade.prompt()
        if keep_going == 'win':
            break
    if keep_going == 'win':
        print("You succeeded!")
    else:
        print("Thank you for playing")

if __name__ == "__main__":    
    main()