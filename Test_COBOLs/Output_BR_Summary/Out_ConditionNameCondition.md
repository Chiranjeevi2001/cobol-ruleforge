# Business Rules Summary
This document outlines a single business rule related to student grading.

## Rule 1: Student Grading (BR-002)
* Description: This rule evaluates student marks and provides a pass or fail status based on the marks.
* Condition: `M_NUMBER`
* Output:
	* If the condition is met, and marks are between 30 and 100 (inclusive): `Passed with \\n${M_NUMBER} marks`
	* If the condition is not met: `FAILED with \\n${M_NUMBER} marks`