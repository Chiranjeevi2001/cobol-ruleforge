# Business Rules Summary
## Rule 1: Student Course Status Determination (BR-001)
* Description: This rule determines the course status of a student based on their weighted average.
* Condition: `WRK-MEDIA >= 10`
* Output:
	* If the condition is met: `APROVADO + BONUS`
	* If the condition is not met, check the following conditions:
		* `WRK-MEDIA >= 6 AND WRK-MEDIA <= 9,9`: `SITUACAO: APROVADO`
		* `WRK-MEDIA >= 2 AND WRK-MEDIA <= 5,9`: `RECUPERACAO`
		* Otherwise: `REPROVADO`