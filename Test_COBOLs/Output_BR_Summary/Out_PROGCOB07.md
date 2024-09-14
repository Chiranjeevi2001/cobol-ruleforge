# Business Rules Summary
This document outlines one business rule related to student status determination.

## Rule 1: Student Status Determination (BR-001)
* Description: This rule determines the status of a student based on the average of two entered grades.
* Condition: (This rule does not specify any conditions.)
* Output:
	* If the average is greater than or equal to 7: `SITUACAO: APROVADO`
	* If the average is less than 7 and greater than or equal to 5: `SITUACAO: RECUPERACAO`
	* If the average is less than 5: `SITUACAO: REPROVADO`