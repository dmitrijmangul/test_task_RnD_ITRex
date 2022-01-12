# A script to find the difference between two JSON files.

The script provides for cases: 
* the names(keys) is in different positions in the first and second files
* the names(keys) include different characters and has a different case of letters
* the name(key) is not specified in one of the files
* both files are identical

You must have the Python interpreter installed to use the script.

Instructions: 
* open a Command Prompt
* enter the name of the interpreter (python)
* enter the path to the script after a space 
* enter the path to the first file after a space 
* enter the path to the second file after a space
* run the line

Input format: \
python <\pathtoapp> <\pathtofile1> <\pathtofile2>

Output format example: 

The difference between two input JSON files:

file A: firstName - John \
file B: first_name - Alex

file A: postalCode - 10021-3100 \
file B: not set

The comparison is complete.
