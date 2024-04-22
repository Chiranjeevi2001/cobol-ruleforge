# Business Rules Summary
This document outlines one business rule related to a player's turn in a game.
## Rule 1: Player's Turn (BR-001)
* Description: This rule determines a player's turn based on their bidding strategy.
* Condition: `PLAYER-BID = 0`
* Output:
	* If the condition is met, the player can choose to:
		* `bid on the next card`
		* `bid on the highest card`
		* `bid on the nearest card to the prize`
	* If the player's strategy is not recognized, `Display error message.`