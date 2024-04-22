## COBOL Code Analysis: Command-Line Calculator

The provided COBOL code is a command-line calculator that takes three parameters: two numeric values and an arithmetic operator. Here's a summary of its functionality and structure:

**Data Division:**

*   **Working-Storage Section:** 
    *   Four numeric variables are declared to hold the input values and results:
        *   `firstnum`: A four-digit packed decimal integer to store the first input number.
        *   `oper`: A one-character variable to store the arithmetic operator.
        *   `secondnum`: A four-digit packed decimal integer to store the second input number.
        *   `total`: An eight-digit display integer to store the result of the calculation.

**Procedure Division:**

1.  **Input Acquisition:** The `ACCEPT` statements obtain the values of `firstnum`, `oper`, and `secondnum` from the command-line arguments.
2.  **Arithmetic Operation:** An `IF` statement chain determines the appropriate arithmetic operation based on the value of `oper`:
    *   `+`: The `COMPUTE` statement adds `firstnum` and `secondnum` and stores the result in `total`.
    *   `-`: The `COMPUTE` statement subtracts `secondnum` from `firstnum` and stores the result in `total`.
    *   `*`: The `COMPUTE` statement multiplies `firstnum` and `secondnum` and stores the result in `total`.
    *   `/`: The `COMPUTE` statement divides `firstnum` by `secondnum` and stores the result in `total`.
    *   In case of an invalid operator, an error message is displayed.
3.  **Output Display:** The final result is displayed on the console using the `DISPLAY` statement.
4.  **Termination:** The program concludes its execution with the `STOP RUN` statement.

**Summary:**

This COBOL program demonstrates the handling of command-line arguments, conditional branching, and basic arithmetic operations. It provides users with a convenient tool for performing simple calculations from the command line.