import re  # Import regular expression module
from tabulate import tabulate # Import tabulate module

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code.upper()  # Upper case the code
        self.product = product
        self.cost = int(cost)  # Always integer no matter source
        self.quantity = int(quantity)  # Always integer no matter source

    def get_cost(self):
        '''
        Code to return the cost of the shoe in this method.
        '''
        return self.cost
    
    def get_quantity(self):
        '''
        Code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Code to return a string representation of the class.
        '''
        return f"""
{{
    country: {self.country},
    code: {self.code},
    product: {self.product},
    cost: {self.cost},
    quantity: {self.quantity} 
}}"""


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with 
    this data and append this object into the shoes list. One line in 
    this file represents data to create one object of shoes. You must 
    use the try-except in this function for error handling. Remember to 
    skip the first line using your code.
    '''
    print("\nReading data from 'inventory.txt' file...", end='')
    try:
        with open("inventory.txt", "r") as file:
            # Skip first line. Strip off newline and split into Shoe
            # attributes list. Then unpack the list into a Shoe object
            # and append to the Shoe list
            for line_index, line in enumerate(file):
                if line_index == 0:
                    continue
                line = line.strip('\n').split(',')
                shoe_list.append(Shoe(*line))
            print("Done")  # Done reading data
    except FileNotFoundError:
        raise FileNotFoundError("No such file or directory: 'inventory.txt'")

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    print("\nAdding shoe to inventory...\n")

    # Get the shoe details from the user. Improve data quality and 
    # uniformity by validating and sanitising input, converting text to 
    # uppercase or titlecase and stripping whitespaces
    country = input("Enter the country: ").strip().title()
    if not re.fullmatch(r"[a-zA-Z ]+", country):
        raise ValueError("Enter a valid country name")
    country = re.sub(r" +", " ", country)
    code = input("Enter the code: ").strip().upper()
    if not code.isalnum():  # e.g. ABC123
        raise ValueError(
            "Enter a valid code. No special characters. E.g. 'ABC123'"
        )
    product = input("Enter the product: ").strip().title()
    try:
        cost = int(input("Enter the cost: ").strip())
    except ValueError:
        raise ValueError("Enter a valid cost. No currency symbols")
    try:
        quantity = int(input("Enter the quantity: ").strip())
    except ValueError:
        raise ValueError("Enter a valid number for quantity")

    # Add shoe to inventory
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    with open("inventory.txt", "a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")

    print("\nShoe successfully added to inventory")

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''
    print("\nShoe Inventory:\n")

    table = []  # For the tabulate function

    for shoe in shoe_list:
        table.append(
            [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        )

    # For the tabulate function
    headers=["Country","Code", "Product", "Cost", "Quantity"]

    print(tabulate(table, headers, tablefmt="pretty"))

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # The first quantity will always be the first lowest
    lowest_quantity = float('inf') 

    # Dictionary to store shoes with the lowest quantity and their index
    lowest_stock = {}

    # Find the shoe(s) with the lowest quantity
    for index, shoe in enumerate(shoe_list):
        if shoe.quantity < lowest_quantity:
            lowest_quantity = shoe.quantity
            lowest_stock = {index: shoe}
        elif shoe.quantity == lowest_quantity:
            lowest_stock[index] = shoe

    # There can be more than one shoe with the lowest quantity
    for index, shoe in lowest_stock.items():
        # Ask the user if they want to add this quantity of shoes
        add_quantity = input(
            f"\nDo you want to add to the quantity of \n{shoe}\nin stock? \
(y/n): "
        ).strip().lower()  # User can enter option in any case

        if add_quantity == 'y':
            # Update the quantity of the shoe
            quantity = int(input("\nEnter the quantity: ").strip())
            shoe.quantity += quantity
            # Update the quantity of the shoe in the shoe list
            shoe_list[index] = shoe
        elif add_quantity == 'n':
            print("\nQuantity not updated")
        else:
            raise ValueError("Invalid input. Enter 'y' or 'n'")
        
    # Write the updated quantity to the file
    if add_quantity == 'y':
        with open("inventory.txt", "w") as file:
            # Write the header
            file.write("Country,Code,Product,Cost,Quantity\n")
            for index, shoe in enumerate(shoe_list):
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},\
{shoe.quantity}"
                )
                # Do not write a newline character after the last line
                if index != len(shoe_list) - 1:
                    file.write('\n')
        print("\nQuantity updated successfully")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be 
     printed.
    '''
    # Ask the user for the shoe code. Improve data quality and 
    # uniformity by converting text to uppercase and stripping 
    # whitespaces
    shoe_code = input("\nEnter the shoe code: ").strip().upper()

    for shoe in shoe_list:
        if shoe.code == shoe_code:
            print("\nFound:\n", shoe)
            break
    else:
        print("\nShoe not found")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    table = []  # For the tabulate function

    for shoe in shoe_list:
        table.append(
            [shoe.code, shoe.cost * shoe.quantity]
        )

    headers=["Item Code", "Total Value"]  # For the tabulate function

    print("\nTotal Value per Item:\n")

    print(tabulate(table, headers, tablefmt="pretty"))

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # The first quantity will always be assigned to highest_quantity
    highest_quantity = -float('inf') 

    # List stores shoes with the highest quantity and their index
    highest_stock = []

    # Find the shoe(s) with the highest quantity
    for shoe in shoe_list:
        if shoe.quantity > highest_quantity:
            highest_quantity = shoe.quantity
            highest_stock = [shoe]
        elif shoe.quantity == highest_quantity:
            highest_stock.append(shoe)

    print("\nShoe(s) on SALE:")
    
    # There can be more than one shoe with the highest quantity
    for shoe in highest_stock:
        print(shoe, '\n')

def utility_func():
    '''Call read_shoes_data() if it has not been called before'''
    if not shoe_list:
        read_shoes_data()

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    # Present the menu to the user
    menu = input('''\nSelect one of the following options:\n
rd - read 'inventory.txt' file and populate shoe list
cs - Add a shoe to the shoe list
va - view all shoes
rs - re-stock shoe with the lowest quantity
se - search for a shoe from the shoe list
tv - calculate the total value for each shoe
os - show shoe(s) on sale
e - exit\n
: ''').strip().lower()  # User can enter option in any case

    try:
        if menu == "rd":
            utility_func()
            user_input = input("\nPress enter to return to the main menu: ")
        elif menu == "cs":
            utility_func()
            capture_shoes()
            user_input = input("\nPress enter to return to the main menu: ")
        elif menu == "va":
            utility_func()
            view_all()
            user_input = input("\nPress enter to return to the main menu: ")
        elif menu == "rs":
            utility_func()
            re_stock()
            user_input = input("\nPress enter to return to the main menu: ")
        elif menu == "se":
            utility_func()
            search_shoe()
            user_input = input("\nPress enter to return to the main menu: ")
        elif menu == "tv":
            utility_func()
            value_per_item()
            user_input = input("\nPress enter to return to the main menu: ")
        elif menu == "os":
            utility_func()
            highest_qty()
            user_input = input("\nPress enter to return to the main menu: ")
        elif menu == 'e':
            print("\nGoodbye...\n")
            exit()
        else:
            raise ValueError("Invalid input. Try again.")
    except Exception as e:
        print(f"\nError: {e}")