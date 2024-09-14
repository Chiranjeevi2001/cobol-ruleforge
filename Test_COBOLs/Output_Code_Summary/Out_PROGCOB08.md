## COBOL Code Analysis: Student Grade Assessment Program
The COBOL code you provided implements an algorithm to evaluate a student's grade based on two numeric inputs: `WRK-NOTA1` and `WRK-NOTA2`. A summary of the code's structure and functionality is provided below:

**Data Division:**

*   **Working-Storage Section:**
    *   Three numeric variables are declared:
        *   `WRK-NOTA1`: A two-digit integer to store the first grade input.
        *   `WRK-NOTA2`: A two-digit integer to store the second grade input.
        *   `WRK-MEDIA`: A two-digit packed decimal variable to store the average of the two grades.

**Procedure Division:**

1.  **Input Acquisition:** The `ACCEPT` verb prompts the user for two numeric inputs and stores them in the `WRK-NOTA1` and `WRK-NOTA2` variables.
2.  **Grade Calculation:** The `COMPUTE` verb calculates the average grade (`WRK-MEDIA`) as the mean of the two input grades.
3.  **Grade Evaluation:** An `EVALUATE` statement assesses the value of `WRK-MEDIA` and displays different messages based on the following grading scheme:
    *   **10:** "APROVADO + BONUS"
    *   **6 through 9.9:** "SITUACAO: APROVADO"
    *   **2 through 5.9:** "RECUPERACAO"
    *   **Any other value:** "REPROVADO"

**Summary:**

This COBOL program showcases data input, arithmetic operations, and conditional branching to determine a student's academic standing based on two input grades. It provides various grade categories and displays appropriate messages for each.