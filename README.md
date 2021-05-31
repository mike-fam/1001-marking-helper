# Marking helper

## Introduction

The purpose of this tool is to setup a convenient environment for your marking so (hopefully) the marking process is less painful. You *don't* have to use this tool if you don't want to. This documentation shows how to setup the tool as well as how to use it.

## Setup

1. You must have Python 3.8 in order for this to work. 

2. You can now mark directly in this repo. Everything downloaded/generated for marking will be ignored 

3. Download the assignments from Gradescope and extract them to `submissions/`. 

## Usage 
1. In your making directory, run `python ./open-scripts/app.py <ide>` where `<ide>` is your editor of choice (e.g. `code` for VS Code, `subl` for Sublime Text, etc.). You can even set it up with PyCharm and other editors, but you'll have to go through the code and change the flags to match the configuration of your editor.
* **Note:** you have to use Python 3.8 for this command. On Windows, if you don't have Python 3.8 setup in your Path environment variable, you can replace `python` with `py -3.8`. On Unix-like systems, you can replace `python` with typically something like `python3.8`.
2. You'll be prompted for a student id. Enter the id of the student you want to mark. 
  * If their `a3.py` is not found, it's likely that they submitted a zip file. In this case you'll have to manually set it up.
  * If `a3.py` is found, a new directory called `temp_marking` will be created and opened. where `sXXXXXXX` is the id of the student. The structure of that directory is.
	```
    temp_marking
       └── a3.py
       └── constants.py
       └── task1.py
       └── images
            └── ...
	```

3. `a3.py`, `task1.py` and the other files will also be opened your editor of choice.

4. The assignment is also run (the script runs `python a3.py`). You can also see the errors printed out in stderr

5. The assignment is also opened in IDLE. This is helpful if you want to change the student's code (e.g. running a different game or task) and rerun it.

6. After you've done marking the assignment, close everything, including your editor, the gui and idle. The tool will prompt for another student id. Enter a blank line to close the tool.

*Note:* I've tried to make this cross-platform, but I use this mostly on Windows and tested it on MacOS, so there might be some issues with other OSes.

If you have any issue, feel free to DM me on Facebook.