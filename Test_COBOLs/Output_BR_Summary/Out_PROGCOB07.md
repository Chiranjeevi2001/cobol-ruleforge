# Business Rules Summary

## 1. Grade Evaluation Rule (BR-001)
* Description: This rule evaluates a student's academic performance based on two grades.
* Condition: `WRK-MEDIA >= 2`
* Output:
	* If `WRK-MEDIA >= 7`: `SITUACAO: APROVADO` (Approved)
	* If `WRK-MEDIA >= 2` and `WRK-MEDIA < 7`: `SITUACAO: RECUPERACAO` (Recovery)
	* If `WRK-MEDIA < 2`: `SITUACAO: REPROVADO` (Failed)