# Business Rules Summary
This document outlines four business rules related to rental car fee calculations.
## Rule 1: Initial Kilometer Subtraction (BR-001)
* Description: This rule subtracts the first 75 kilometers from the total kilometers, if applicable.
* Condition: `KILOMETERS > 75`
* Output:
	* If the condition is met: `KILOMETERS = KILOMETERS - 75`
## Rule 2: Volkswagen Cars Payment Calculation (BR-002)
* Description: This rule calculates the payment for Volkswagen cars.
* Condition: `CAR_TYPE = 1`
* Output:
	* Kilometer Payment: `KILOMETERS_PAYMENT = KILOMETERS * 0.5`
	* Rental Days Payment: `RENTAL_DAYS_TOTAL = 10 * NUM_DAYS`
	* Total Payment: `PAYMENT = KILOMETERS_PAYMENT + RENTAL_DAYS_TOTAL`
## Rule 3: Toyota Cars Payment Calculation (BR-003)
* Description: This rule calculates the payment for Toyota cars.
* Condition: `CAR_TYPE = 2`
* Output:
	* Kilometer Payment: `KILOMETERS_PAYMENT = KILOMETERS * 0.55`
	* Rental Days Payment: `RENTAL_DAYS_TOTAL = 12.5 * NUM_DAYS`
	* Total Payment: `PAYMENT = KILOMETERS_PAYMENT + RENTAL_DAYS_TOTAL`
## Rule 4: Mercedes Cars Payment Calculation (BR-004)
* Description: This rule calculates the payment for Mercedes cars.
* Condition: `CAR_TYPE = 3`
* Output:
	* Kilometer Payment: `KILOMETERS_PAYMENT = KILOMETERS * 0.65`
	* Rental Days Payment: `RENTAL_DAYS_TOTAL = 16 * NUM_DAYS`
	* Total Payment: `PAYMENT = KILOMETERS_PAYMENT + RENTAL_DAYS_TOTAL`