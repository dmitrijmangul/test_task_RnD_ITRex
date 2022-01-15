# A script to find the difference between two JSON files.

### The script provides for cases: 
* the names(keys) is in different positions in the first and second files
* the names(keys) include different characters and has a different case of letters
* one of the files does not contain a name(key)
* both files are identical

___You must have the [Python interpreter](https://www.python.org/downloads/) installed to use the script.___

### Manual: 
* open a [Command Prompt](https://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/)
* enter the name of the interpreter (python)
* enter the [path](https://www.thedataschool.co.uk/robbin-vernooij/easy-access-folder-paths-command-prompt-cmd-windows-windows-server) to the script after a space 
* enter the path to the first file after a space 
* enter the path to the second file after a space
* run the command

### Input format:
```
python <pathtoscript> <pathtofile1> <pathtofile2>
```

### Output format example: 

```
The difference between two input JSON files:

file A: firstName - John
file B: first_name - Alex

file A: postalCode - 10021-3100
file B: not set

The comparison is complete.
```
