# Business Rules Summary
This document presents a summary of the business rule related to loan rate determination:
## Rule 1: Loan Rate Determination (BR-002)
* Description: This rule defines the loan rate based on the account number.
* Condition: `ACCOUNT-NUMBER-IN = '0001'`
* Output:
    * If the condition is met (i.e., the account number is '0001'):
        * `LOAN-RATE = '1.25'` (loan rate is set to 1.25)
    * If the condition is not met (i.e., the account number is not '0001'):
        * `LOAN-RATE = '7.20'` (loan rate is set to 7.20)