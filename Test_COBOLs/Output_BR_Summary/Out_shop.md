# Business Rules Summary

This summary provides an overview of seven business rules related to product purchasing and shop availability.

## Rule 1: Shop Availability (BR-002)
* Description: This rule determines whether the store is open.
* Condition: `OP = 1`
* Output:
    * If the condition is met: `SHOP IS OPEN`, otherwise: `SHOP IS CLOSED`

## Rule 2: Product Initialization (BR-003)
* Description: This rule initializes random product quantities and prices.
* Condition: `N/A`
* Output:
    * Product quantity: `QT-VEG/QT-MEAT/QT-BREAD/QT-MILK/QT-FRUIT`
    * Product price: `PR-VEG/PR-MEAT/PR-BREAD/PR-MILK/PR-FRUIT`

## Rule 3: Product Need Determination (BR-004)
* Description: This rule determines product need based on a random number generator.
* Condition: `FUNCTION RANDOM (1) * 2`
* Output:
    * If the condition is met: `NEED = 1`, otherwise: `NEED = 0`

## Rule 4: Product Purchase Conditions (BR-005)
* Description: This rule checks if a product can be bought based on quantity, money, and bag capacity.
* Condition: `QT > 0 AND MONEY > PR AND BAG < MAX-CAP`
* Output:
    * If all conditions are met: Product is purchased and relevant updates are made.

## Rule 5: Product Purchase Termination (BR-006)
* Description: This rule determines if the program should stop buying products.
* Condition: `MONEY <= 0 OR BAG >= MAX-CAP`
* Output:
    * If any condition is met: The program stops buying products.

## Rule 6: Program Completion (BR-007)
* Description: This rule displays remaining money and the number of products bought at the end of the program.
* Condition: `N/A`
* Output:
    * Remaining money: `REST`
    * Products bought: `BAG`