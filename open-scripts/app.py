from pathlib import Path
import threading
import argparse
from inspect_file import InspectFile, LINE_LENGTH_LIMIT
from open_scripts import OpenScript


def main():
    parser = argparse.ArgumentParser(description="Open student's scritps and run them")
    parser.add_argument('ide')
    parser.add_argument('submissions_path')
    parser.add_argument('assignment_stub')
    args = parser.parse_args()
    while True:
        student_id = input("Please input the student's id: ")
        if not student_id:
            break
##        submissions_path = Path(args.submissions_path) / 'Assignment 3' / student_id
##        last_submission = sorted(list(submissions_path.iterdir()))[-1] / 'files'
        submission_path = Path(args.submissions_path) / student_id
        a1 = submission_path / 'a1.py'
        # player = last_submission / 'player.py'
        
        if not a1.exists():
            input("Warning: a1.py does not exist."
                  " Please go check")
            continue
##        if not player.exists():
##            input("Warning: player.py does not exist. player.py from the assignment stub will be "
##                  "used.[Press Enter to continue]")
        
        support_code_path = Path(args.assignment_stub)
        # open and run assignments
        open_script = OpenScript(student_id, submission_path, support_code_path,
                                 args.ide, "a1.py",
                                 keep_temp=True)  # Change this if you dont want to keep your marking folders
        opening = threading.Thread(target=open_script.open_scripts, daemon=True)
        opening.start()
        #running = threading.Thread(target=open_script.run_script, daemon=True)
        #running.start()
        
        marking_path = open_script.get_marking_folder()
        # Test stuffs
        with open(marking_path / 'a1.py', encoding='utf-8') as a1_in:
            inspect = InspectFile(a1_in)
            inspect.test_line_length()
            inspect.test_naming()
##            inspect.test_encapsulation()
        print(("#" * LINE_LENGTH_LIMIT + '\n') * 2)
        
        opening.join()
        #running.join()
        

if __name__ == '__main__':
    main()
