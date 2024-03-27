# ========== Edit student info ===================#
name = 'Heng Yi Lee'  # (1) REPLACE THE STRING VARIABLE WITH YOUR NAME in string type
student_num = '-'  # (2) REPLACE THIS STRING VARIABLE WITH YOUR UOW ID in string type
subject_code = '-'
# ========== End of student info =================#
# ========== Define function definitions here ====#

# Question 1
def compute_tax(taxableAmount, taxRate = 0.18):
    # return the product of the two arguments
    return taxableAmount * taxRate

# Question 2
def get_class(object1):
    # return type of object1
    return type(object1)

# Question 3
def formulate_equation():
    # prompt user to enter two numbers and convert them to float type
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # add the two numbers
    num3 = num1 + num2
    
    # convert num1 and num2 to string type and concatenate them
    string1 = str(num1) + " + " + str(num2)
    return num3, string1

# Question 4
def filter_by(fcn, N):
    # Store value return by fcn() into A
    A = fcn()

    # Check if A is greater than N
    if A > N:
        return True
    else:
        return False
    
# Question 5
def format_price(price):
    # format a string obect and display it on the console
    strObject = f"${price:.2f}"
    print(strObject)

    #return string object 
    return strObject

# ========== End of function definition===========#

def main():  # DO NOT EDIT THIS LINE.
    print("Assignment2")  # DO NOT EDIT THIS LINE.
    # ========== Call your functions here ========#
    
    print()
    # Question 1
    print("Question 1")
    x = compute_tax(2)
    print(x)
    y = compute_tax(2,1.1)
    print(y)
    print()

    # Question 2
    print("Question 2")
    x = "Hello"
    y = get_class(x)
    z = get_class(123)
    print(y)
    print(z)
    print()

    # Question 3
    print("Question 3")
    x, y = formulate_equation()
    print(x)
    print(y)
    print()

    # Question 4
    print("Question 4")
    def test_fcn1():
        return 3*3
    
    x = filter_by(test_fcn1,16)
    y = filter_by(test_fcn1,4)
    print(x)
    print(y)
    print()

    # Question 5
    print("Question 5")
    x = format_price(2.3)
    print(x)

    # ========== End of function calls ===========#

if __name__ == '__main__':  # DO NOT EDIT THIS LINE.
    main()  # DO NOT EDIT THIS LINE.
