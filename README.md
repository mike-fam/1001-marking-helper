# Marking helper

## Introduction

The purpose of this tool is to set up a convenient environment for your marking so 
(hopefully) the marking process is less painful. You *don't* have to use this tool 
if you don't want to. This documentation shows how to set up the tool as well as 
how to use it.

## Setup

1. You **must** have Python 3.8 or above in order for this to work. 

2. Clone this repository, using ether https or ssh if you've set up a public key.
	```shell
	git clone https://github.com/mike-fam/1001-marking-helper.git
	```

3. Download the assignments from Gradescope and extract them to `submissions/`.
	* Go to https://gradescope.com, log in and choose **CSSE1001/CSSE7030**
	  
	* Click on **Assignment 3**
	  
	* Click on **Review Grades** on the left toolbar
	  
	* Click on the **Export submissions** button at the bottom to batch download
	all the submissions in a zip file. You might need to wait a few minutes.
	  
	* Extract the zip file to the `submissions/` folder in the repo.
	
	* Your folder structure should look like this
		```
        assignment_stub
        helpers
        submissions
           └── submission_77830837
           └── submission_79073266
           └── submission_79601236
           └── ...
           └── submission_metadata.yml
        app.py
        README.md
        requirements.txt
  		```
  
4. Set up a new virtual environment and activate it and install
   the required packages.
	* On Mac or Linux, open the terminal and run
		```shell
		python3.9 -m venv venv
		source venv/bin/activate # Activate virtual environment
		pip install -r requirements.txt
		```
  
	* On Windows, open PowerShell and run
		```shell
		py -3.9 -m venv venv
		venv\Scripts\Activate.ps1 # Activate virtual environment
		pip install -r requirements.txt
		```
  
5. You should be ready to roll. You'll have to stay in the virtual 
   environment while marking. After quitting the shell session, remember
   to activate the virtual environment again.

## Usage
1. In the repo, run `python app.py <section> --ide <ide>` where `<section>` 
   is the name of your marking section and `<ide>` 
   is your editor of choice (e.g. `code` for VS Code, `subl` for Sublime Text, etc.). 
   You can even set it up with PyCharm and other editors, but you'll have to 
   go through the code and change the flags to match the configurations of your editor.
2. The script will loop through all the students of your section. For each student, a
   new directory called `temp_marking` will be created and opened. 
   The structure of that directory is:
	```
    temp_marking
       └── a3.py
       └── constants.py
       └── task1.py
       └── images
            └── ...
	```

3. You can also see the file the students have submitted printed out in the shell.

4. The assignment files are opened in your IDE if you supplied the `--ide` flag.

4. `a3.py` is also opened in IDLE. You can run the code here.

5. After you've done marking the assignment, close everything, including your IDE,
   the gui and IDLE. The tool will wipe `temp_marking` and move on to the next student. 

*Note:* I've tried to make this cross-platform, but I use this mostly on Windows and tested it on MacOS, so there might be some issues with other OSes.

If you have any issue, feel free to DM me on Facebook.