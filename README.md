                           # Learn Python with a Calculator
This  is a simple calculator built using Python. It performs basic arithmetic operations such as :  addition, subtraction, multiplication, and division.

 *we use three methods to  implement simple calculator operations*:

    1.Using functions and a dictionary
    2. if, elif, and else statements
    3.Python dictionaries with the keys(), values(), and items() methods.
                #Features of this calculator 

➕ Addition of two numbers
➖ Subtraction of two numbers
✖️ Multiplication of two numbers
➗ Division of two numbers
🛡️ Handles division by zero
📚 Uses functions to organize code
🗂️ Demonstrates dictionary operations
🔀 Supports operation selection using conditional statements

                                   ** How It Works**
              #Method 1: Using Functions and a Dictionary
 **four functions for the arithmetic operations:**

**add(x, y)** → *Returns the sum of two numbers*.
**subtract(x, y)** → *Returns the difference between two numbers*.
**multiply(x, y)** →  *Returns the product of two numbers*.
**divide(x, y)** → *Returns the quotient and checks for division by zero*.
  *Each dictionary key is the operation name  and its value is the corresponding function*
calculator = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}
.

              **three useful Python dictionaries methods**:


     **Method	 **                       **Description**
calculator.keys()	      *Returns the dictionary operation names*.
calculator.values()	      *Returns the function objects stored in the dictionary*.
calculator.items()	      *Returns the key-value pairs*.
        


                        **Method 2: if, elif, and else statements**
*uses if, elif, and else statements to determine which operation to perform*.

*selects an operation by entering a number*:


Choice	Operation
1	Addition
2	Subtraction
3	Multiplication
4	Division

*this calls the proper function and outputs the result.*
*If the user selects an invalid choice, the output will be an error message.*

