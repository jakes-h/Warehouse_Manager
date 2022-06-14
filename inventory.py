from tabulate import tabulate

#  Empty lists to be used in functions below.
shoe_list = []
value_list = []

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''Shoe object constructor method with instance variables.'''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def read_data():
        '''Function to read the data from the inventory file.

        Open inventory.txt and read every line using for loop.

        Use try - except block to handle exception if file doesn't exist.

        Split the line where there is a comma and assign to
        respective variables depending on the type of data.

        Create shoe object for every line/shoe and append it to the shoe list.

        Finally block used to close the file.
        '''
        inventory_file = None
        try:
            inventory_file = open('inventory.txt', 'r')
            
            for line in inventory_file:
                country, code, product, cost, quantity = line.split(',')
                quantity = quantity.strip('\n')  # Remove line break.
                quantity = quantity

                shoe_list.append(Shoe(country, code, product, cost, quantity))

            # Remove first index in list containing headers in the txt file.
            del shoe_list[0]

        except FileNotFoundError:
            print('The file that you are trying to open does not exist.')
        
        finally:
            if inventory_file is not None:
                inventory_file.close()

    def search_product():
        '''Function to search for a shoe by code.
        
        User to input code of the shoe to search for.

        Use list comprehension to search for the code in shoe_list.
       
        If the code is in the list, return a new list with the object(s).
        
        Print details of the new list of objects in an easy to read format.

        If the code is not in the list, print appropriate message.
        '''
        search_code = input('Enter the code of the product you would '
                            'like to search for: ')

        search_code_list = [code for code in shoe_list \
                            if code.code == search_code]

        for shoe in search_code_list:
            print(f'''
Country:            {shoe.country}
Code:               {shoe.code}
Product:            {shoe.product}
Cost:               {shoe.cost}
Quantity:           {shoe.quantity}
''')    
       
        if search_code_list == []:
            print(f'No product with code {search_code} found.')

    def lowest_quantity():
        '''Function to determine the product with the lowest quantity.
        
        Loop through every object in the shoe_list and append the quantity
        to the quantity_list.

        Search for the lowest quantity in quantity_list using min function.

        Then loop through the shoe_list again and find the object with the 
        same quantity value as the lowest variable and print the details of
        that object.
        '''
        quantity_list = []
        for shoe in shoe_list:
            quantity_list.append(int(shoe.quantity))
        lowest = min(quantity_list)
        print('The product with the lowest quantity is: ')
        for shoe in shoe_list:
            if str(lowest) == shoe.quantity:
                print(f'''\
Country:            {shoe.country}
Code:               {shoe.code}
Product             {shoe.product}
Cost                {shoe.cost}
Quantity            {shoe.quantity}

An order has been placed to restock this product.
''')

    def highest_quantity():
        '''Function to determine the product with the highest quantity.
        
        Loop through every object in the shoe_list and append the quantity
        to the quantity_list.

        Search for the highest quantity in quantity_list using max function.

        Then loop through the shoe_list again and find the object with the 
        same quantity value as the highest variable and print the details of
        that object.
        '''
        quantity_list = []
        for shoe in shoe_list:
            quantity_list.append(int(shoe.quantity))
        highest = max(quantity_list)
        print('The product with the highest quantity is: ')
        for shoe in shoe_list:
            if str(highest) == shoe.quantity:
                print(f'''\
Country:            {shoe.country}
Code:               {shoe.code}
Product             {shoe.product}
Cost                {shoe.cost}
Quantity            {shoe.quantity}

This product will be palced on sale.
''')

    def value_per_item():
        '''Function to calculate the value of each shoe.
        
        Loop thorugh every object in the shoe_list and caluclate the value
        by multiplying cost by quantity.

        Append the value to the value_list.
        '''
        for shoe in shoe_list:
            value = int(shoe.cost) * int(shoe.quantity)
            value_list.append(value)

    def inventory_table():
        '''Function to represent the inventory data in a table format.'''
        # Create empty 2D list.
        no_of_rows = len(shoe_list)
        no_of_columns = 6
        table = [[] * no_of_columns for _ in range(no_of_rows)]
        count = 0

        # Loop through shoe_list objects and append each shoe object's
        # attribute to the empty 2D list as well as the values calculated
        # in the value_list.
        for shoe in shoe_list:
            table[count].append(shoe.country)
            table[count].append(shoe.code)
            table[count].append(shoe.product)
            table[count].append(shoe.cost)
            table[count].append(shoe.quantity)
            table[count].append(value_list[count])
            count += 1

        # Print the data from the table 2D list in a table format.
        print(tabulate(table, headers=['Country', 'Code', 'Product', 'Cost',\
                                       'Quantity', 'Value'], tablefmt='psql'))


# Start the program by calling the read_data() function.
Shoe.read_data()

print('Welcome to the inventory management system!')

while True:
    menu = input('''Please select one of the following options:
s - search product
l - determine product with lowest quantity and restock it
h - determine product with highest quantity and mark up as sale
i - view all inventory
e - exit
''').lower()

    # Call search_product() function to allow the user to search
    # for a product by code.
    if menu == 's':
        Shoe.search_product()
    
    # Call the lowest_quantity() function to determine the product
    # with the lowest quantity and restock it.
    elif menu == 'l':
        Shoe.lowest_quantity()

    # Call the highest_quantity() function to determine the product
    # with the highest quantity and place it on sale.
    elif menu == 'h':
        Shoe.highest_quantity()   

    # Call the value_per_item() and inventory_table() functions to
    # calculate the value for each shoe and display the inventory
    # data in an easy to read table.
    elif menu == 'i':
        Shoe.value_per_item()
        Shoe.inventory_table()

    # Exit the program.
    elif menu == 'e':
        print('Goodbye!')
        exit()

    # Error message if user inputs incorrect option.
    else:
        print("\nYou have made a wrong choice, please try again.")
