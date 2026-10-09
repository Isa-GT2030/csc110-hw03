"""
Name: Isa Graham Torres
References: Class slides & my class notes
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    global grades #using the global context of 'grades'
    
    for idx in range(5): #defining the input ranges of 1,2,3,4,and 5
        in_str = input("Give me the first grade in [0 to 10]: ") #get the first grade
        
     #If the input is not a string, send an error & exit loop   
        if not in_str.isdigit():
            print("Error in read_five_ints: input string is not for an integer")
            exit()
        
        grade = int(in_str) #define variable 'grade' as the int casted user inputs
        
        #If the input is outside the accepted values of 1 through 10, send error & exit loop
        if grade < 0 or grade > 10:
            print("Error in read_five_ints: input integer outside of range")
            exit()
        
        #if the input is within range, index it into grades
        grades[idx] = grade
        print(grades)
          

    #Anything with this indentation is NO LONGER inside the loop


# Task 2:
#  Complete the function "pick_averaging_method" below:

def pick_averaging_method():
    #define math as a a string from user's input
    math = str(input("Pick 'a' for mean, 'b' for median,  'c' for mode: "))
    
    # if math is 'a', calculate the mean of the values within grade's index and return value
    if math == "a":
        avg = statistics.mean(grades)
        print("picked: Mean")
        return(avg)
    
    # if math is 'b', calculate the median of the values within grade's index and return value
    elif math == "b":
        avg = statistics.median(grades)
        print("picked: Median")
        return(avg)
    
    # if math is 'c', calculate the mode of the values within grade's index and return value
    elif math == "c":
        avg = statistics.mode(grades)
        print("picked: Mode")
        return(avg)
    
    # if math is not 'a', 'b', or 'c', run an invalid error and exit 
    else:
        print("Error in pick_averaging_method: incorrect option picked")
        exit()
    
     

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    # define results as the string input from the user
    results = str(input("Pick '1' for print average, or '2' for plot average: "))
    
    # if the user inputs '1', run the print_list_and_average function
    if results == "1":
        print_list_and_average(average)
    
    # if the user inputs '2', run the plot_grades function
    elif results == "2":
        plot_grades(average)
    
    # if the user input is anything but '1' or '2', print an error and exit
    else:
        print("Error in pick_visualization: incorrect option picked")
        exit()


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
