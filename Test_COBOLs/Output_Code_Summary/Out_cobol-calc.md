## COBOL Code Analysis: Simple Calculator Program

### Overview

This COBOL program acts as a basic calculator, allowing users to perform arithmetic operations on two input numbers. The supported operations include addition, subtraction, multiplication, and division.

### Data Division

* **Working-Storage Section:**
    *   Four numeric variables are declared:
        *   `firstnum`: A four-digit packed-decimal integer to store the first input number.
        *   `oper`: A one-character alphabetic field to store the mathematical operation.
        *   `secondnum`: A four-digit packed-decimal integer to store the second input number.
        *   `total`: An eight-digit display field to store the result of the calculation.

### Procedure Division

1.  **Input Acquisition:** The program accepts the three input values (`firstnum`, `oper`, and `secondnum`) from the calling environment using the `ACCEPT` statements.
2.  **Input Validation:** Basic validation is performed to ensure that the operation character (`oper`) is one of the supported operators ('+', '-', '*', or '/').
3.  **Calculation:** The `COMPUTE` statement is used to perform the appropriate arithmetic operation based on the operation character:
    *   Addition: `total = firstnum + secondnum`
    *   Subtraction: `total = firstnum - secondnum`
    *   Multiplication: `total = firstnum * secondnum`
    *   Division: `total = firstnum / secondnum`
4.  **Output:** The program displays the initial values and the result of the calculation:
    *   The input values are displayed along with the operator.
    *   The calculated `total` is displayed with a descriptive message.
5.  **Termination:** The program concludes its execution with the `STOP RUN` statement.

### Summary

This COBOL program provides a straightforward example of arithmetic operations and conditional logic. It supports basic mathematical operations and provides a user-friendly interface for input and output. The program effectively performs calculations based on user-provided operands and displays the results accordingly.