# Business Rules Summary

This document outlines three business rules related to date and time calculations.

## Rule 1: Years of Service Calculation (BR-001)
* Description: This rule calculates the number of years of service based on the current date and the hire date.
* Condition: The current month or day is not equal to the hire month or day.
* Output:
  * If the condition is met:
    * Calculate years of service as the difference between the current year and the hire year, minus one if the current month is earlier than the hire month, and minus one again if the current day is earlier than the hire day.

## Rule 2: End of Month Switch for February (BR-002)
* Description: This rule determines if the current date is the last day of February in a leap year, and sets the EOM-SW to 'Y' if so.
* Condition: The current month is February.
* Output:
  * If the condition is met and the current day is February 29th:
    * Set EOM-SW to 'Y'.
  * Otherwise:
    * Do nothing.

## Rule 3: End of Month Switch for Last Day of Month (BR-003)
* Description: This rule sets the EOM-SW to 'Y' if the current day is the last day of the current month.
* Condition: The current day is equal to the last day of the current month.
* Output:
  * If the condition is met:
    * Set EOM-SW to 'Y'.
  * Otherwise:
    * Do nothing.
