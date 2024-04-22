## COBOL Code Analysis: Student's Grades Evaluation 

This COBOL program evaluates a student's academic performance based on two input grades and calculates the average score. It then classifies the student's academic standing as 'APROVADO' (passed), 'RECUPERACAO' (needs recovery), or 'REPROVADO' (failed).

**Data Division:**
*   **Working-Storage Section:**
    *   Three numeric variables are defined:
        *   `WRK-NOTA1`: A two-digit integer to hold the first grade.
        *   `WRK-NOTA2`: A two-digit integer to hold the second grade.
        *   `WRK-MEDIA`: A two-digit integer to hold the average of the two grades.

**Procedure Division:**
1.  **Input Acquisition:** The `ACCEPT` verb is used twice to read the first and second grades from the user and store them in `WRK-NOTA1` and `WRK-NOTA2`, respectively.
2.  **Average Calculation:** The `COMPUTE` verb calculates the average of the two grades and stores the result in `WRK-MEDIA`.
3.  **Output and Evaluation:** The `DISPLAY` verb is used to output the following information:
    *   `WRK-NOTA1`: The value of the first grade.
    *   `WRK-NOTA2`: The value of the second grade.
    *   `WRK-MEDIA`: The calculated average.
4.  **Grading Evaluation:** Using nested `IF` statements, the program evaluates the average score and displays the corresponding grade status:
    *   **Passed:** If the average is greater than or equal to 7, it displays 'APROVADO'.
    *   **Needs Recovery:** If the average is between 2 and 6.99 (inclusive), it displays 'RECUPERACAO'.
    *   **Failed:** If the average is less than 2, it displays 'REPROVADO'.

**Summary:**
This COBOL program demonstrates basic data processing and conditional branching. It calculates the average of two input grades, displays the result, and evaluates the student's academic standing based on the calculated average. The output provides a clear assessment of the student's performance in the form of a grading status.