# Business Rules Summary
This document outlines four business rules related to the FizzBuzz game.
## Rule 1: FizzBuzz Identification (BR-002)
* Description: This rule identifies if a number is divisible by both 3 and 5, in which case the output is "FizzBuzz".
* Condition: `FUNCTION MOD(COUNTER, 3) IS EQUAL TO ZERO AND FUNCTION MOD(COUNTER, 5) IS EQUAL TO ZERO`
* Output:
    * If the condition is met: `FizzBuzz`
## Rule 2: Fizz Identification (BR-003)
* Description: This rule identifies if a number is divisible by 3, in which case the output is "Fizz".
* Condition: `FUNCTION MOD(COUNTER, 3) IS EQUAL TO ZERO`
* Output:
    * If the condition is met: `Fizz`
## Rule 3: Buzz Identification (BR-004)
* Description: This rule identifies if a number is divisible by 5, in which case the output is "Buzz".
* Condition: `FUNCTION MOD(COUNTER, 5) IS EQUAL TO ZERO`
* Output:
    * If the condition is met: `Buzz`
## Rule 4: Number Identification (BR-005)
* Description: This rule identifies if a number is not divisible by either 3 or 5, in which case the output is the number itself.
* Condition: `WHEN OTHER`
* Output:
    * If the condition is met: `COUNTER`