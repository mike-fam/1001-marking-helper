from pathlib import Path
import threading
import argparse
from inspect_file import InspectFile, LINE_LENGTH_LIMIT
from open_scripts import OpenScript


def main():
    parser = argparse.ArgumentParser(description="Open student's scripts and run them")
    parser.add_argument('ide')
    args = parser.parse_args()
    while True:
        student_id = input("Please input the student's id: ")
        if not student_id:
            break

        submission_path = Path('normalised_submissions') / student_id
        a3 = submission_path / 'a3.py'

        if not a3.exists():
            input("Warning: a3.py does not exist."
                  " Please go check")
            continue
        
        support_code_path = Path('assignment_stub')
        # open and run assignments
        open_script = OpenScript(student_id, submission_path, support_code_path,
                                 args.ide, "a3.py",
                                 keep_temp=True)  # Change this if you dont want to keep your marking folders
        opening = threading.Thread(target=open_script.open_scripts, daemon=True)
        opening.start()
        opening_idle = threading.Thread(target=open_script.open_scripts_in_idle, daemon=True)
        opening_idle.start()
        running = threading.Thread(target=open_script.run_script, daemon=True)
        running.start()
        
        marking_path = open_script.get_marking_folder()
        # Test stuffs
        with open(marking_path / 'a3.py', encoding='utf-8') as a3_in:
            inspect = InspectFile(a3_in)
            inspect.test_line_length()
            inspect.test_naming()
            inspect.test_encapsulation()
        print(("#" * LINE_LENGTH_LIMIT + '\n') * 2)
        
        opening.join()
        opening_idle.join()
        running.join()
        

if __name__ == '__main__':
    main()
