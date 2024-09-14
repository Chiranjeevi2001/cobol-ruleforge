#!/bin/bash

# Execute preprocess file
python ./src/preprocess.py

# Extract BRs
python ./src/BR_generator.py

# Execute Code Summarizer
python ./src/CodeSummarizer.py

# Execute BR Summarizer
python ./src/BRSummarizer.py