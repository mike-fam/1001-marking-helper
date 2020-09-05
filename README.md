# Marking helper

## Introduction

The purpose of this tool is to setup a convenient environment for your marking so (hopefully) the marking process is less painful. You *don't* have to use this tool if you don't want to. This documentation shows how to setup the tool as well as how to use it.

## Setup

1. You must have Python 3.8 in order for this to work. 

2. Copy this directory to your own marking folder, do not mark your assignments directly in this repo.

3. Download the assignments from Blackboard and extract them to `submissions/`. ONLY download the latest version of the submissions and not all of them. The tool MIGHT open an older version of the submission if you have multiple versions. This hasn't been tested yet.

4. Copy the supported files to the `assignment_stub` folder. The supported files can be the supported code (e.g. `a1_support.py`), the test files and the text files containing all the words.

5. Run `normalise_files.py`. This will create a directory called `normalised_submissions`. The structure of this folder is:
   ```
   normalised_submissions
   ├── s0000001
   │   ├── a1.py
   └── s0000002
       └── a1.py
   ```
   Where `sXXXXXXX` denotes the student IDs.

## Usage 
1. In your making directory, run `python ./open-scripts/app.py <ide> normalised_submissions assignment_stub`, where `<ide>` is your editor of choice (e.g. `code` for VS Code, `subl` for Sublime Text, etc.). You can even set it up with PyCharm and other editors, but you'll have to go through the code and change the flags to match the configuration of your editor.
* **Note:** you have to use Python 3.8 for this command. On Windows, if you don't have Python 3.8 setup in your Path environment variable, you can replace `python` with `py -3.8`. On Unix-like systems, you can replace `python` with typically something like `python3.8`.
2. You'll be prompted for a student id. Enter the id of the student you want to mark. 
  * If their `a1.py` is not found, it's likely that they submitted a zip file. In this case you'll have to manually set it up.
  * If `a1.py` is found, a new directory called `temp_sXXXXXXX` will be created and opened. where `sXXXXXXX` is the id of the student. The structure of that directory is.
	```
    temp_sXXXXXXX
       └── a1.py
       └── a1_support.py
       └── test_a1.py
       └── testrunner.py
	   └── ...
	```

3. `a1.py` will also be opened your editor of choice.

4. On the console, you can see that the tool has performed some static analysis on the assignment. Things that the tool checks for include:

   * Line length: Any line longer than 120 characters is reported. The general convention is <= 100 characters. There's a 20 character window for leniency

   * Naming: Any camelCase name is reported (although this is still a bit buggy and can have false positives). The tool can also detect potential improper variable naming for for loops (e.g. `for i in word_list`)

     ![Static Analysis screenshot](https://i.imgur.com/0n0fiEK.png)

5. After you've done marking the assignment, close your editor. The tool will prompt for another student id.

*Note:* I've tried to make this cross platform, but I use this mostly on Windows and tested it on MacOS, so there might be some issues with other OSes.

If you have any issue, feel free to DM me on Facebook.