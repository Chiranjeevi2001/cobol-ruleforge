# COBOL RuleForge - Extracting Clarity from Complexity

This work deals with extracting business rules from legacy COBOL codebases and summarizing them. These summaries are then compared with conventional code summaries to emphasise the need to extract business rules for efficient code maintenance and migration.

## Running the project
First, you will need to store your COBOL files in the folder `Test_COBOLs/InputFiles`. After making sure that all files are placed in the folder, follow the steps given below:
1.  Clone the repository
	```
	git clone https://github.com/Chiranjeevi2001/cobol-ruleforge.git
	```

2. Go to (Google's AI Studio)[https://aistudio.google.com/app/] and get the `Gemini API Key`, and paste it inside the codes in `./src`.

3. Give execution permission to Summarize.sh
	```
	chmod +x Summarize.sh
	```

4. Run the shell script
	```
	./Summarize.sh
	```


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

