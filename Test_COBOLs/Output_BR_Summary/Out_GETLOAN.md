# Business Rules Summary
This document summarizes one business rule for determining the loan rate based on customer number.
## Rule 1: Loan Rate Assignment (BR-002)
* Description: This rule assigns a loan rate based on the customer number.
* Condition: `ACCOUNT-NUMBER-IN = '0001'`
* Output:
	* If the condition is met: 'Loan rate set to 1.25%'
	* If the condition is not met: 'Loan rate set to 7.20%'