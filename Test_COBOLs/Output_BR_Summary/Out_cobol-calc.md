# Business Rules Summary
This document outlines one business rule related to mathematical operations.
## Rule 1: Validating Mathematical Operators (BR-002)
* Description: This rule validates if the provided operand is one of the following: '+', '-', '*', '/'.
* Condition: `oper NOT IN {'+', '-', '*', '/'}``
* Output:
  * If the condition is met: `Sorry, I do not know that operator.`