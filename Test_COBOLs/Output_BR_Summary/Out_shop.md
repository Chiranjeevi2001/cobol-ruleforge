#  Business Rules Summary
This document outlines five  business rules that collectively govern the process of grocery shopping.

## Rule 1: Shop Status (BR-002)
* Description: This rule determines if the shop is open or closed based on the "Operation" status (OP).
* Condition: `OP = 1`
* Output:
	* If the condition is met: `SHOP IS OPEN`
	* If the condition is not met: `SHOP IS CLOSED`

## Rule 2: Product Purchase (BR-003)
* Description: This rule defines the conditions under which a buyer can purchase a product.
* Condition: `NEED =1 AND QT-1 > 0 AND MONEY > PR-*AND BAG < MAX-CAP`
* Output:
	* If all conditions are met: `Product purchased, new MONEY: {"$MONEY"}, new BAG: {"$BAG"}`
	* If `MONEY <= 0 or BAG >= MAX-CAP`:"Not enough money, product not purchased"
    * If `BAG >= MAX-CAP`: "Bag is full, product not purchased"

## Rule 3: Shopping Continuation (BR-004)
* Description: This rule determines if the shopping process should continue or stop based on the customer's financial situation and bag capacity.
* Condition: `MONEY <= 0 or BAG >= MAX-CAP`
* Output:
	* If `MONEY > 0 and BAG < MAX-CAP`: "Continue shopping"
    * If `MONEY <= 0 or BAG >= MAX-CAP`: "Stop shopping"

## Rule 4: Product Initialization (BR-005)
* Description: This rule describes the random generation of product quantity and price during initialization.
* Output: Initialization of `QT` and `PR` values for each product

## Rule 5: Customer Need Generation (BR-006)
* Description: This rule explains the generation of a random number to determine if the customer needs a product.
* Output: Generation of a random number to determine `NEED` status for each product