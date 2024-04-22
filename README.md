# COBOL RuleForge - Extracting Clarity from Complexity

This work deals with extracting business rules from legacy COBOL codebases and summarizing them. These summaries are then compared with conventional code summaries to emphasise the need to extract business rules for efficient code maintenance and migration.

## Running the project
First, you will need to store your COBOL files in the folder `Test_COBOLs/InputFiles`. After making sure that all files are placed in the folder, follow the steps given below:
	1. Execute the `preprocess.py` file by running the command `python preprocess.py`. This will remove comment lines and extra spaces in your COBOL files.
	2. Run the `BR_generator.ipynb` file completely. Make sure you have the codeSystemMessage.txt file before you run the Notebook.
	3. Run the `Summarizer.sh` script file by executing the command `./Summarizer.sh`, to produce code summaries and BR summaries. Be sure to grant execute access to the script file before you execute it.
	4. Finally, to evaluate the results, run the `CompareSummaries.ipynb` file to get the BLEU ROUGE scores of the generated summaries


## Dependencies

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `geminiApiKey` | `string` |  Google's Gemini-Pro API key |

## Libraries used

1. `google.generativeai` - Google's generative AI library to import models and infer from them.
2. `glob` - To traverse file system efficiently.
3. `evaluate` - To analyze and compare the results of conventional code summarization and BR summarization.

## Author

[@Chiranjeevi](https://github.com/Chiranjeevi2001)


## Contributing

Contributions are always welcome! Make the changes you wish to see and create a pull request.



## Support

For support, email cs23m104@iittp.ac.in

