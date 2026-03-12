# We create an empty list where all sales information will be stored
salesList = []

# Function responsible for requesting and storing the information of each sale
def registerSale(): 
    # We ask the user if they want to register a sale
    answer = input("Do you want to register a sale?: yes/no ").lower()
    
    # The loop will repeat as long as the user answers "yes"
    while answer == "yes":
        print("\n-----NEW SALE REGISTRATION-----\n")
        
        # We use try/except to prevent the program from crashing if the user enters incorrect data
        try:
            # We request the product data
            name = input("Enter the product name: ")
            price = float(input("Enter the price per unit: "))
            quantity = int(input("Enter the quantity of products: "))
            
            # We create a dictionary with the sale information
            newSale = {
                "product": name,
                "quantity": quantity,
                "subtotal": price * quantity
            }
            
            # We add the dictionary to the sales list
            salesList.append(newSale)
            
        # If the user enters letters where numbers are expected, we catch the error
        except ValueError:
            print("Error: invalid information")
            
        # We ask if they want to register another sale to continue or exit the loop
        answer = input("Do you want to register another sale?: yes/no ").lower()

# Function that goes through the list and adds all subtotals to get the grand total
def calculateTotal():
    grandTotal = 0
    # We go through each sale registered in the list
    for sale in salesList:
        grandTotal += sale["subtotal"]  # We add each sale's subtotal to the accumulator
    return grandTotal  # We return the calculated total


# Function that displays a complete summary of all sales on screen
def summary():
    print("\n-----SALES SUMMARY-----\n")
    
    # We go through the list and print each sale's data
    for sale in salesList:
        print ("-----------------------------")
        print(f"Product:  {sale['product']}")
        print(f"Quantity: {sale['quantity']}")
        print(f"price per unit: {sale['subtotal'] / sale['quantity']}")
        print(f"Subtotal: {sale['subtotal']}")
    
    # We call calculateTotal() to get the sum of all sales
    total = calculateTotal()
    print(f"\nTOTAL COLLECTED: {total}\n")


# ---- PROGRAM EXECUTION ----
registerSale()
calculateTotal()
summary()
