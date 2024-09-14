# Business Rules Summary
This document outlines three business rules related to data type identification.

## Rule 1: Alphabetic Variable Identification (BR-001)
* Description: This rule checks if a given variable contains only letters.
* Condition: STR01 IS ALPHABETIC
* Output:
	* If the condition is met: STR01 IS ALPHABETIC

## Rule 2: Numeric Variable Identification (BR-002)
* Description: This rule checks if a given variable contains only digits, a sign, and a decimal point.
* Condition: NUM01 IS NUMERIC
* Output:
	* If the condition is met: NUM01 IS NUMERIC

## Rule 3: Non-numeric Variable Identification (BR-003)
* Description: This rule checks if a given variable does not contain only digits, a sign, and a decimal point.
* Condition: STR01 IS NUMERIC
* Output:
	* If the condition is not met: STR01 ISNT NUMERIC IS ALPHABETIC