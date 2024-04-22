       IDENTIFICATION DIVISION.
       PROGRAM-ID.    FIZZBUZZ.
       AUTHOR.        CHIPMAN.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 COUNTER        PIC 999.
       01 NONSENSE       PIC X(8).
       PROCEDURE DIVISION.
       100-MAIN-PARA.
           PERFORM VARYING COUNTER FROM 1 BY 1
                   UNTIL COUNTER IS EQUAL TO 101
                   MOVE ALL SPACES TO NONSENSE
                   EVALUATE TRUE
                   WHEN (FUNCTION MOD(COUNTER, 3) IS EQUAL TO ZERO
                    AND  FUNCTION MOD(COUNTER, 5) IS EQUAL TO ZERO)
                        MOVE "FizzBuzz" TO NONSENSE
                   WHEN FUNCTION MOD(COUNTER, 3) IS EQUAL TO ZERO
                        MOVE "Fizz" TO NONSENSE
                   WHEN FUNCTION MOD(COUNTER, 5) IS EQUAL TO ZERO
                        MOVE "Buzz" TO NONSENSE
                   WHEN OTHER
                        MOVE COUNTER TO NONSENSE
                   END-EVALUATE
                   DISPLAY NONSENSE
           END-PERFORM
           STOP RUN.