# ========== Edit student info ===================#
name = 'Heng Yi Lee'  # (1) REPLACE THE STRING VARIABLE WITH YOUR NAME in string type
student_num = '-'  # (2) REPLACE THIS STRING VARIABLE WITH YOUR UOW ID in string type
subject_code = '-'
# ========== End of student info =================#
# ========== Define function definitions here ====#

# Question 1
def noisy_traffic(N): # has a parameter N
    # declare an empty string
    str_object = ""

    # loop in range starting from 1 to N + 1 (excluding n + 1)
    for num in range(1, N + 1):
        # check if num is divisible by 5 and 7 using modulo %
        if num % 5 == 0 and num % 7 == 0: 
            # add "VroomHonk" to str_object
            str_object += "VroomHonk"
        # check if num is divisible by 5
        elif num % 5 == 0:
            # add "Vroom" to str_object
            str_object += "Vroom"
        # check if num is divisible by 7
        elif num % 7 == 0:
            # add "Honk" to str_object
            str_object += "Honk"
        # if num is not divisible by 5 or 7
        else:
            # cast num to string type and add to str_object
            str_object += str(num)
        
        # if not end of loop add ","
        if (num != N):
            str_object += ","
        # if end of loop add "." instead
        else:
            str_object += "."

    return str_object
        
# Question 2
def get_cpf_interest_rates():
    # prompt user for inputs
    age = int(input("Enter current age: "))
    OA = float(input("Enter current amount in OA: "))
    SA = float(input("Enter current amount in SA: "))
    MA = float(input("Enter current amount in MA: "))

    # sum up OA, SA and MA
    total_funds = OA + SA + MA

    # check if user is below 55 years old
    if age < 55:
        # calculate base interest
        # check if OA is less than $20,000
        if OA <= 20000:
            total_interest = OA * 0.025 + SA * 0.04 + MA * 0.04 
        else: # OA is more than $20,000
            # OA can only contribute up to $20,000
            total_interest = 20000 * 0.025 + SA * 0.04 + MA * 0.04 

        # Calculate extra interest
        # if total funds less than or equal to $60k
        if total_funds <= 60000:
            total_interest += total_funds * 0.01
        # if total funds more than $60k
        else: 
            total_interest += 60000 * 0.01
    # if user is 55 years old and above
    else:
        # prompt user to enter amount in RA account
        RA = float(input("Enter current amount in RA: "))
        # add RA amount to total funds
        total_funds += RA

        # calculate base interest
        # check if OA is less than or equal to $20k
        if OA <= 20000:
            total_interest = OA * 0.025 + SA * 0.04 + MA * 0.04 + RA * 0.04
        else:
            # OA can only contribute up to $20,000
            total_interest = 20000 * 0.025 + SA * 0.04 + MA * 0.04 + RA * 0.04 

        # calculate extra interest
        # check if total funds less than or equals to $30k
        if total_funds <= 30000:
            total_interest += total_funds * 0.02 # 2% for first $30k
        elif total_funds > 30000 and total_funds <= 60000:
            total_interest += 30000 * 0.02 # 2% for first $30k
            total_interest += ((total_funds - 30000) * 0.01) # 1% for next $30k
        else:
            total_interest += 30000 * 0.02 # 2% for first $30k
            total_interest += 30000 * 0.01 # 1% for next $30k

    # format string in 2 decimal place
    total_interest = f"${total_interest:.2f}"
    print("Your interest rate this year will be " + total_interest)

# Question 3
def get_car_rental_booking():
    # rental rates of each type of vehicle
    economy = 40
    standard = 70
    premium = 100
    suv = 130

    # prompt user to input number of cars for each type
    # and rent duration
    ecoNum = int(input("Number of Economy cars: "))
    stNum = int(input("Number of Standard cars: "))
    preNum = int(input("Number of Premium cars: "))
    suvNum = int(input("Number of SUVs: "))
    rentDuration = int(input("Rental duration (number of days): "))
    print()

    # calculate total num of cars rented
    totalNum = ecoNum + stNum + preNum + suvNum
    # calculate sub total
    subtotal = (ecoNum * economy + stNum * standard + preNum * premium + suvNum * suv) * 4

    # display details of the booking
    # value of column3 variable is changed accordingly
    # when displaying a new row
    print("Summary of your car rental for", rentDuration, "day(s)")
    column3 = f"${ecoNum * economy * rentDuration:.2f}"
    print(f"{"Economy":<13}{ecoNum:^3}{column3:>10}")
    column3 = f"${stNum * standard * rentDuration:.2f}"
    print(f"{"Standard":<13}{stNum:^3}{column3:>10}")
    column3 = f"${preNum * premium * rentDuration:.2f}"
    print(f"{"Premium":<13}{preNum:^3}{column3:>10}")
    column3 = f"${suvNum * suv * rentDuration:.2f}"
    print(f"{"SUV":<13}{suvNum:^3}{column3:>10}")
    column3 = f"${subtotal:.2f}"
    print(f"{"Subtotal":<13}{totalNum:^3}{column3:>10}")
    column3 = f"${subtotal * 1.18:.2f}"
    print(f"{"Total (18% tax)":16}{column3:>10}")

# Question 4
def sanitize_vehicle_filenames():
    # declare an empty named string clean_filenames
    # stores all filenames that have been cleaned
    clean_filenames = ""

    # loop repeatedly
    while True:
        # prompt user for filename
        filename = input("Filename?")

        # stops the loop when filename is an empty string
        if filename == "":
            break
        
        # declare another empty string
        # store each character of filename 
        # excluding angled brackets and the contents within
        string_obj = ""
        inside_bracket = False
        counter = 0
        
        # iterate through each character in filename
        for character in filename:
            # if character is an open angle bracket
            # and current loop iteration is in another
            # set of angled brackets (nested angle brackets)
            if character == "<" and inside_bracket == True:
                # add 1 to counter
                counter += 1
            # else if character is an open angle bracket
            # and current loop iteration is not in another
            # set of angled brackets 
            elif character == "<":
                inside_bracket = True
            # if char is a closing angle bracket
            # and loop iteration is in a nested angle bracket
            elif character == ">" and counter > 0:
                counter -= 1
            # if char is a closing angle bracket
            # and loop iteration is not in a nested angle bracket
            elif character == ">" and counter == 0:
                inside_bracket = False
            # add char to str obj if not in a angled bracket
            elif inside_bracket == False and counter == 0:
                string_obj += character

        # add cleaned filename followed by a comma 
        clean_filenames += string_obj + ","

    # return 1st char to 2nd last char of clean_filenames
    # exclude the last comma in clean_filenames
    return clean_filenames[:-1]

# ========== End of function definition===========#

def main():  # DO NOT EDIT THIS LINE.
    print("Assignment2")  # DO NOT EDIT THIS LINE.
    # ========== Call your functions here ========#
    #result = noisy_traffic(48)
    #print(result)

    #get_cpf_interest_rates()
    #get_car_rental_booking()
    x = sanitize_vehicle_filenames()
    print(x)

    # ========== End of function calls ===========#

if __name__ == '__main__':  # DO NOT EDIT THIS LINE.
    main()  # DO NOT EDIT THIS LINE.

    