## COBOL Code Analysis: End-of-Month Calculation Program
The provided COBOL code performs computations to check if a given date falls on the last day of the month. The program uses a predefined table of days in each month and performs comparisons to determine if the input date matches the last day of the corresponding month. An overview of its functionality is as follows:

**Data Division:**

*   **Working-Storage Section:** 
    *   **DATE-TABLE:** A table containing the number of days in each month.
    *   **WORK-AREAS:** Working variables for temporary storage and control flags.
    *   **HOLD-YEARS**, **EXTRA-YEARS**: Temporary variables for leap year calculations.
    *   **CHECKED-FOR-EOM-SW**: Flag indicating whether end-of-month check has been performed.
    
*   **Linkage Section:** 
    *   **EOM-SW**: Output flag indicating whether the input date is the end of the month.
    *   **YRS-OF-SERVICE**: Years of service calculation output.
    *   **RUN-DATE**: Input date in YYMMDD format.
    *   **HIRE-DATE**: Input date in YYMMDD format, used for years of service calculation.

**Procedure Division:**

1.  **Main Logic (0000-MAINLINE):** The program starts by checking if the end-of-month check has been performed. If not, it executes the `2000-CALC-END-OF-MONTH` paragraph to calculate if the input date is the last day of the month. Otherwise, it proceeds with the `1000-CALC-YRS-OF-SERVICE` paragraph for years of service calculation.
2.  **Years of Service Calculation (1000-CALC-YRS-OF-SERVICE):**  This paragraph calculates the years of service based on the input hire date and run date. It compares the years, months, and days of the two dates to determine the number of years of service.
3. **End-of-Month Calculation (2000-CALC-END-OF-MONTH):** This paragraph checks if the input date is the last day of the month. It considers the number of days in the month (`DATE-DD(RUN-MM)`) and compares it to the day of the input date (`RUN-DD`). If they match, it sets the `EOM-SW` output flag to 'Y'.
4.  **Leap Year Calculation (3000-CALC-LEAP-YEAR):** This paragraph is executed only if the input month is February (`RUN-MM = 02`). It calculates whether the year is a leap year by dividing the year (`RUN-YY`) by 4. If the remainder is 0 and the day of the month (`RUN-DD`) is 29, it sets the `EOM-SW` output flag to 'Y'.

**Summary:**

This COBOL program demonstrates the use of table lookups, date calculations, and conditional branching to determine whether a given date is the last day of the month. It also calculates the years of service based on two input dates. The program follows a structured approach, separating different calculations into distinct paragraphs, making it easier to understand and modify.