       IDENTIFICATION DIVISION.
       PROGRAM-ID. player-turn.
       DATA DIVISION.
       LOCAL-STORAGE SECTION.
          01 I PIC 9(2).
          78 STRATEGY-NEXT    VALUE 1.
          78 STRATEGY-MAX     VALUE 2.
          78 STRATEGY-NEAREST VALUE 3.
       LINKAGE SECTION.
       78 NUM-CARDS        VALUE 4.
       01 PRIZE-CARD PIC 9(2).
       01 PLAYER-REC.
         02 PLAYER-NAME PIC X(6).      
         02 PLAYER-BID PIC 9(2).
         02 PLAYER-POINTS PIC 9(2).
         02 PLAYER-STRATEGY PIC 9(1).
         02 PLAYER-HAND PIC 9(2) OCCURS NUM-CARDS TIMES.
       PROCEDURE DIVISION USING PRIZE-CARD, PLAYER-REC.
          MOVE 0 TO PLAYER-BID.
          PERFORM PICK-CARD VARYING I FROM 1 BY 1 UNTIL I > NUM-CARDS.
          GOBACK
          .
       PICK-CARD.
         IF PLAYER-BID = 0
           IF PLAYER-STRATEGY = STRATEGY-NEXT
             CALL "strategy-next" USING PRIZE-CARD, PLAYER-REC
           ELSE IF PLAYER-STRATEGY = STRATEGY-MAX
             CALL "strategy-max" USING PRIZE-CARD, PLAYER-REC
           ELSE IF PLAYER-STRATEGY = STRATEGY-NEAREST
             CALL "strategy-nearest" USING PRIZE-CARD, PLAYER-REC
           ELSE 
             DISPLAY "TRACER SEVERE ERROR P-S: " PLAYER-STRATEGY
           END-IF
         END-IF.
