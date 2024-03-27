""" Template for Assignment 3
    Use this template for submission.
    - This template includes an example function.
"""
# ========== Edit student info ===================#
name = 'Heng Yi Lee'  # (1) REPLACE THE STRING VARIABLE WITH YOUR NAME in string type
student_num = '-'  # (2) REPLACE THIS STRING VARIABLE WITH YOUR UOW ID in string type
subject_code = '-'
# ========== End of student info =================#

def myClass_demo_unit_test(inputClass):
    """ 
    This example takes in a class definition as input,
    then instantiates a class object and test its method
    in a try except system. 
    """
    try:
        obj = inputClass()
        obj.demo()
    except ValueError as e:
        print('A ValueError was raised because ' + str(e))


def example():
    # A class with one method
    class MyClass(): 
        def __init__(self):
            pass
        def demo(self):
            raise ValueError('Wrong input given!')
        
    # test the demo method
    myClass_demo_unit_test(MyClass)

class Price:
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return f"${self.value:.2f}"

    def __repr__(self):
        return f"${self.value:.2f}"

# ========== Define function and class definitions here ====#

from random import randint

# Question 1
def myClass_get_int_unit_test(class_input):
    try:
        # Instantiate an instance of the input class
        class_obj = class_input()
        # Call instance method get_integer()
        var1 = class_obj.get_integer()
        
        # Argument has the right type but an inappropriate value
        if type(var1) == int and var1 < 0:
            raise ValueError

    except AttributeError:
        return 'A'
    except ValueError:
        return 'V'
    except:
        return 'O'
    else:
        return class_obj.get_integer()

# Question 2
def compute_unit_prices(Dict, List):
    return_value = {}
    
    # loop through each element in list
    for goods in List:
        try:
            # Get value of key in Dict (list)
            # Store float and int value of list in good_cost and quantity
            goods_cost, quantity = Dict[goods]
            # Add unit price of goods to dictionary return_value
            return_value[goods] = goods_cost / quantity
        except ZeroDivisionError: # if goods is out of stock
            # add key value pair: goods : -1 to return_value
            return_value[goods] = -1
        except KeyError: # if goods does not exist
            # add key value pair: goods : None to return_value
            return_value[goods] = None

    return return_value

# Question 3a
class OutOfStockError(Exception):
    def __init__(self, item):
        self.item = item

    def __str__(self):
        return f"The following item {self.item} is out of stock!"

# Question 3b 3c and 3d
class Inventory:
    # Class variables
    hotline = "1800-1333-5432"
    items = {}

    @classmethod
    def set_items_from_list(cls, alist):
        # loop through parameter list
        for list in alist:
            name = list[0]
            # store price and stock quantity in list
            price_obj = Price(list[1])
            stock = list[2]
            # store price and stock quantity in a dictionary
            dict = {'price' : repr(price_obj),
                    'stock' : stock}
            # Add key-value pair to class variable items
            Inventory.items[name] = dict

    @classmethod
    def order(cls):
        Y = {}
        # iterate through the keys in inventory.items
        for key in Inventory.items:
            quantity = int(input(f"How many {key} would you like to order? "))
            
            # if user input is 0, proceed to the next iteration
            if quantity == 0:
                continue
            
            # if stock value is less than user input
            # raise outofstockerror 
            if Inventory.items[key].get('stock') < quantity:
                raise OutOfStockError(key)

            Y[key] = quantity

        return Y

# Question 3e
def collate_orders(N):
    Z = {
        "invalid": 0,
        "valid_items": 0,
        "oos": 0
    }

    # call order() N times
    for x in range(N):
        try:
            order_dict = Inventory.order()
        except OutOfStockError:
            Z["oos"] += 1
        except:
            Z["invalid"] += 1
        else:
            for key in order_dict:
                Z["valid_items"] += order_dict[key]

    return Z

# Question 4a
class InvalidDepthError(Exception):
    def __str__(self):
        return "Invalid Depth"

# Question 4b - 4f
class WaterBody:
    # class attributes 
    RHO = 997
    G = 9.81

    def __init__(self, volume):
        self.volume = volume

    @classmethod
    def get_hydrostatic_pressure(cls, depth):
        if depth < 0:
            raise InvalidDepthError
        
        hydrostatic_pressure = WaterBody.RHO * WaterBody.G * depth
        
        return hydrostatic_pressure
    
    def get_water_mass(self):
        return WaterBody.RHO * self.volume
    
    @staticmethod
    def is_large(volume):
        return volume > 100
    
    @staticmethod
    def is_medium(volume):
        return 50 <= volume <= 100
    
    @staticmethod
    def is_small(volume):
        return volume < 50
    
    @classmethod
    def spawn(cls):
        return cls(randint(1, 200))


# Question 5 a and b
class SingaporeNumbers:
    @staticmethod
    def car_plate_checksum(reg_no):
        checksum_letters = ["A", "Z", "Y", "X", "U", "T", "S", "R", "P", "M", "L", "K", "J", "H", "G", "E", "D", "C", "B"]
        multiply_by_list = [9, 4, 5, 4, 3, 2]
        alist = []
        letter_counter = 0
        sum = 0

        # Iterate through each character in string
        # convert letters to number and add them into alist
        for char in reg_no:
            try:
                num = int(char)
                alist.append(num)
            except ValueError:
                ascii_value = ord(char) - 64
                alist.append(ascii_value)
                letter_counter += 1
        
        # remove or insert into alist based on num of letters in reg_no
        if letter_counter == 3:
            # Remove the first element of alist
            alist.pop(0)
        elif letter_counter == 1:
            # Insert 0 into first element of alist
            alist.insert(0, 0)

        # Multiple each element in alist with 
        # element in multiply_by_list of the same index 
        for x in range(len(multiply_by_list)):
            alist[x] *= multiply_by_list[x]

        # sum up numbers in alist
        for num in alist:
            sum += num

        
        return reg_no + checksum_letters[sum % 19]
    
    @staticmethod
    def magic_sum_checksum(numString):
        weights = [2, 7, 6, 5, 4, 3, 2]
        check_digit_list = ["J", "Z", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
        num_list = []
        sum = 0

        for char in numString:
            num_list.append(int(char))

        for x in range(len(weights)):
            num_list[x] *= weights[x]

        for num in num_list:
            sum += num

        return check_digit_list[sum % 11]

# =========== End of function and class definitions ========#

def main():
    print("Assignment3")
    #example()

    """
    v1 = myClass_get_int_unit_test(Price)
    print(v1)
    """
    """
    an example function that creates a class and feeds into
    the class into the myClass_demo_unit_test for testing
    You are free to create your own test subjects that raise
    errors to test your code here.
    """
    # example()
    # call your functions or instantiate objects of the classes
    # you have defined in the main() definition. Make sure the 
    # code has at least one level of indentation.
    
    """
    dict1 = {
    "vinegar": [120.0, 100],
    "ketchup": [950, 1000],
    "apples": [850, 1100],
    "oranges": [1050, 0]
    }

    list1 = ["ketchup", "oranges", "pear"]

    dict2 = compute_unit_prices(dict1, list1)
    print(dict2)
    """

    # test 3a
    """  
    try:
        raise OutOfStockError("Eggs")
    except OutOfStockError as e:
        print(e)
    """

    # test 3b
    #print(Inventory.hotline)
    #print(Inventory.items)

    # test 3c
    """
    print(Inventory.items)
    Inventory.set_items_from_list(
    [["Eggs", 2.98, 12],["Milk", 4.65, 3]])
    print(Inventory.items)
    """

    # test 3d
    """
    Inventory.set_items_from_list(
        [
            ["Eggs", 2.98, 12],
            ["Milk", 4.65, 8],
            ["Tea", 1.50, 6]]
    )

    print(Inventory.order())
    Inventory.order()
    """

    # test 3e
    """
    Inventory.set_items_from_list(
        [
            ["Eggs", 2.98, 12],
            ["Milk", 4.65, 8],
            ["Teas", 1.50, 6]]
    )
    print(collate_orders(4))
    """

    """
    # test q4
    pool = WaterBody(10)
    print(pool.get_hydrostatic_pressure(1)) # prints 9780.57
    print(pool.get_water_mass()) # prints 9970
    try:
        pool.get_hydrostatic_pressure(-1)
    except Exception as e:
        print(e) # prints Invalid Depth
    """

    """
    # test 5a
    reg_no = SingaporeNumbers.car_plate_checksum("SBS3229")
    print(reg_no)
    """

    """
    # test 5b
    char = SingaporeNumbers.magic_sum_checksum("1234567")
    print(char)
    """

if __name__ == '__main__':  ## DO NOT EDIT THESE TWO LINES.Y
    main()