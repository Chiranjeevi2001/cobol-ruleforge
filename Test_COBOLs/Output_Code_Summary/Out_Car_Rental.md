## COBOL Code Analysis: Rental Car Invoice Generator

**Purpose:**

Determines the rental fee for a customer based on the type of car rented, the number of kilometers driven, and the number of rental days.

**Input File:**

*RENTAL-IN.txt*: Contains data for each rental. Each record includes the following fields:

 - Client name (CLIENT_NAME)
 - Rental type (RENTAL-TYPE)
   - Initial of car type (NAME_INITIAL)
   - Type of car rented (CAR_TYPE)
   - Kilometers driven (KILOMETERS)
   - Number of rental days (NUM_DAYS)

**Output File:**

*RENTAL-OUT.txt*: Generates an invoice for each rental. Each record includes:

 - Client name (CLIENT_NAME_OUT)
 - Initial of car type (NAME_INITIAL_OUT)
 - Car brand (CAR_BRAND)
 - Kilometers driven (KILOMETERS_OUT)
 - Number of rental days (NUM_DAYS_OUT)
 - Payment amount (PAYMENT)

**Data Structures:**

**Rental File (RENTAL)**:

 - CLIENT_NAME (20 characters)
 - RENTAL-TYPE:
   - NAME_INITIAL (1 character)
   - CAR_TYPE (1 digit)
   - KILOMETERS (5 digits)
   - NUM_DAYS (3 digits)

**Rental Output File (RENTAL-OUT)**:

 - CLIENT_NAME_OUT (20 characters)
 - NAME_INITIAL_OUT (1 character)
 - CAR_BRAND (10 characters)
 - KILOMETERS_OUT (5 digits with decimal separator)
 - NUM_DAYS_OUT (3 digits)
 - PAYMENT (5 digits with 2 decimal places)

**Working Storage:**

 - END-LOOP (3 characters): Flag to control the loop
 - KILOMETERS_PAYMENT (9 digits with 2 decimal places): Calculated payment for kilometers driven
 - RENTAL_DAYS_TOTAL (9 digits): Calculated total rental days

**Procedure Division:**

1. **Main Procedure:**
   - Opens the input and output files.
   - Reads the first rental record.
   - Performs the `CALCULATIONS` paragraph for each record until the `END-LOOP` flag is set to "YYY".
   - Closes the input and output files.
   - Stops the program.

2. **CALCULATIONS Paragraph:**
   - Moves customer and rental details to the output record.
   - Calculates the discounted kilometers (if applicable).
   - Determines the car brand based on the car type.
   - Computes the payment based on the car type, kilometers driven, and rental days.
   - Writes the output record to the file and displays it on the screen.
   - Reads the next rental record.

**Summary:**

This COBOL program takes rental data, calculates the payment based on car type, kilometers driven, and rental days, and generates an invoice for each rental. It processes a series of rental records from an input file and writes the invoice records to an output file.