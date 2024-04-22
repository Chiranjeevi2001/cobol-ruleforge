# Business Rules Summary
This document provides an overview of a single business rule related to student evaluation.

## Rule 1: Student Evaluation (BR-002)
* Description: This rule evaluates a student's situation based on their average grade (MEDIA).
* Condition: `MEDIA is evaluated`
* Output:
	* If `MEDIA is 10`: `approved with bonus`
	* If `MEDIA is between 6 and 9.9`: `approved`
	* If `MEDIA is between 2 and 5.9`: `in recovery`
	* For any other value of `MEDIA`: `failed`