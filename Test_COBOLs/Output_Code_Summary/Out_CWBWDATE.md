## COBOL Program Analysis: Date Calculation Utility

The provided COBOL program serves as a utility for performing date calculations and determining end-of-month (EOM) status. Let's break down its structure and functionality:

**Data Division:**

-   **Working-Storage Section:** 
    *   `DATE-TABLE`: A table containing the number of days in each month for a non-leap year.
    *   `DATE-TABLE-REDEFINED`: A redefinition of `DATE-TABLE` that allows access to individual month and day values.
    *   `WORK-AREAS`: An area for temporary storage, including variables for holding various date components and a flag to indicate whether EOM checks have been performed.

-   **Linkage Section:**
    *   Variables and fields used for data exchange with the calling program or external sources:
        *   `EOM-SW`: Indicator of end-of-month status.
        *   `YRS-OF-SERVICE`: Number of years of service calculated based on hire and run dates.
        *   `RUN-DATE`: Current date consisting of year, month, and day.
        *   `HIRE-DATE`: Employee's hire date with year, month, and day.

**Procedure Division:**

1.  **Main Logic (0000-MAINLINE):**
    *   Checks if EOM checks have been performed; if not, it executes `2000-CALC-END-OF-MONTH` to determine EOM status.
    *   Otherwise, it executes `1000-CALC-YRS-OF-SERVICE` to calculate years of service.

2.  **Years of Service Calculation (1000-CALC-YRS-OF-SERVICE):**
    *   Compares hire year and run year to calculate years of service. 
    *   Adjusts for months and days if necessary.

3.  **End-of-Month Calculation (2000-CALC-END-OF-MONTH):**
    *   Checks if the current month is February and, if so, executes `3000-CALC-LEAP-YEAR` to determine leap year status.
    *   Otherwise, it compares the run day to the number of days in the current month to determine EOM status.

4.  **Leap Year Calculation (3000-CALC-LEAP-YEAR):**
    *   Performs integer division of the run year by 4 to determine leap year status.
    *   Adjusts for February 29th accordingly.

**Summary:**

This COBOL program offers a robust set of functions for date calculations and EOM determination. It leverages data tables and conditional logic to handle various date-related scenarios, providing valuable support for applications that require accurate date processing.