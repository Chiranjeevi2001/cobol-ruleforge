# Business Rules Summary
This document outlines two business rules for initializing a player's bid and selecting a strategy for bidding.

## Rule 1: Player Bid Initialization (BR-001)
* Description: This rule ensures that a player's bid is set to 0 before starting the bidding process.
* Condition: `PLAYER-BID = 0`
* Output:
	* If the condition is met: `MOVE 0 TO PLAYER-BID.`

## Rule 2: Player Bid Strategy (BR-002)
* Description: This rule determines the strategy to use for bidding based on whether the player has already placed a bid.
* Condition: `PLAYER-BID = 0`
* Output:
	* If the condition is met:
		* `CALL "strategy-next" USING PRIZE-CARD, PLAYER-REC`
		* `CALL "strategy-max" USING PRIZE-CARD, PLAYER-REC`
		* `CALL "strategy-nearest" USING PRIZE-CARD, PLAYER-REC`
	* If the condition is not met:
		* `DISPLAY "TRACER SEVERE ERROR P-S: " PLAYER-STRATEGY`