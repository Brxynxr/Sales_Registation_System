# Sales Registration System

Program in Python to register sales and calculate the total collected.

## What does the program do?

- Registers sales one by one until the user decides to stop
- Stores each sale (product, quantity, subtotal) in a dictionary inside a list
- Calculates the grand total of all sales
- Shows a complete summary at the end

<img width="651" height="556" alt="diagramaB drawio" src="https://github.com/user-attachments/assets/ece472db-ecab-496c-8eb2-09b11dff332b" />

## How to run it?

1. Have Python installed
2. Run the file with:
```
python sales.py
```

## Example usage
```
Do you want to register a sale?: yes/no yes

-----NEW SALE REGISTRATION-----

Enter the product name: Notebook
Enter the price per unit: 2.50
Enter the quantity of products: 4
Do you want to register another sale?: yes/no no
```

## Example output
```
-----SALES SUMMARY-----

Product:  Notebook
Quantity: 4
Subtotal: 10.0

TOTAL COLLECTED: 10.0
```

## Validations

- If letters are entered where a number is expected, the program shows an error and continues
- The loop only continues if the user types "yes"

## Functions

- **registerSale():** asks the user for sale data and stores it in the list
- **calculateTotal():** adds all subtotals and returns the grand total
- **summary():** prints all registered sales and the total collected

## Repositoy's link
  https://github.com/Brxynxr/Sales_Registation_System
