# Business Rules Summary
This document outlines the business rules for car rental charges and rental days calculation.

## Rule 1: Kilometer Charge (BR-001)
* Description: This rule determines whether a charge is applied based on the number of kilometers driven.
* Condition: `KILOMETERS <= 75`
* Output:
    * If the condition is met: `No charge`
## Rule 2: Per-Kilometer Charge (BR-002)
* Description: This rule calculates the per-kilometer charge based on the car type.
* Condition: `KILOMETERS > 75`
* Output:
    * For kilometers over 75:
        * For Volkswagen: `0.5` currency units per kilometer
        * For Toyota: `0.55` currency units per kilometer
        * For Mercedes: `0.65` currency units per kilometer
## Rule 3: Rental Days Charge (BR-003)
* Description: This rule calculates the rental days charge based on the car type.
* Condition: N/A
* Output:
    * Rental days charge multiplier:
        * For Volkswagen: `10`
        * For Toyota: `12.5`
        * For Mercedes: `16`