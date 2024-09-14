# Business Rules Summary
This document outlines two business rules related to date and seniority calculations.

## Rule 1: Years of Service Calculation (BR-002)
* Description: This rule calculates the number of years of service based on the difference between the current year and the year of hire, with adjustments for months and days if necessary.
* Condition: `HIRE-YY > RUN-YY || HIRE-MM > RUN-MM || HIRE-DD > RUN-DD`
* Output:
	* If the condition is met: `YRS-OF-SERVICE`

## Rule 2: End of Month Identification (BR-003)
* Description: This rule identifies if the current date is the end of the month.
* Condition: `RUN-MM = 02 && RUN-DD = 29 || DATE-DD(RUN-MM) = RUN-DD`
* Output:
	* If the condition is met: `EOM-SW`