## COBOL Code Analysis: Grade Calculation and Evaluation Program
The provided COBOL code processes two input grades and calculates their average to assess a student's academic standing. Below is a detailed breakdown of its structure and functionality:

**Data Division:**

*   **Working-Storage Section:** 
    *   Three numeric variables are declared:
        *   `WRK-NOTA1`: A two-digit integer to store the first grade.
        *   `WRK-NOTA2`: A two-digit integer to store the second grade.
        *   `WRK-MEDIA`: A two-digit integer to store the average of the two grades.

**Procedure Division:**

1.  **Input Acquisition:** The `ACCEPT` verb prompts the user for two grades, which are stored in `WRK-NOTA1` and `WRK-NOTA2`.
2.  **Grade Calculation:** The `COMPUTE` statement calculates the average of the two grades and stores it in `WRK-MEDIA`.
3.  **Output:** The `DISPLAY` verb displays the values of `WRK-NOTA1`, `WRK-NOTA2`, and the calculated average  `WRK-MEDIA`.
4.  **Grade Evaluation:** An `IF` statement chain evaluates the calculated average to determine the student's academic standing:
    *   **Approved Condition:** If `WRK-MEDIA` is greater than or equal to 7, the program displays a message indicating that the student is approved.
    *   **Recovery Condition:** If `WRK-MEDIA` is greater than or equal to 2 but less than 7, the program displays a message indicating that the student is in recovery. 
    *   **Failed Condition:** Otherwise, the program displays a message indicating that the student is failed.
5.  **Termination:** The program concludes its execution with the `STOP RUN` statement.

**Summary:**

This COBOL program demonstrates the use of input processing, arithmetic operations, and conditional branching to calculate a student's average grade and evaluate their academic standing based on predefined criteria. It provides a straightforward example of grade processing and evaluation in a structured programming environment.