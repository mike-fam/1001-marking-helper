from pathlib import Path
import threading
import argparse
from helpers.inspect_file import InspectFile, LINE_LENGTH_LIMIT
from helpers.open_scripts import OpenScript


SUBMISSION_DIR = Path("submissions")
SUPPORT_CODE_PATH = Path('assignment_stub')


def main():
    parser = argparse.ArgumentParser(description="Open student's scripts and run them")
    parser.add_argument('ide')
    args = parser.parse_args()
    while True:
        submission_id = input("Please input the submission's id: ")
        if not submission_id:
            break

        submission_path = SUBMISSION_DIR / f"submission_{submission_id}"
        a3 = submission_path / 'a3.py'

        if not a3.exists():
            input("Warning: a3.py does not exist."
                  " Please go check")
            continue
        
        # open and run assignments
        # Change keep_temp if you dont want to keep your marking folders
        open_script = OpenScript(submission_id, submission_path,
                                 SUPPORT_CODE_PATH,
                                 args.ide,
                                 "a3.py",
                                 "task1.py",
                                 "task2.py",
                                 "csse7030.py",
                                 keep_temp=False)
        opening = threading.Thread(target=open_script.open_scripts, daemon=True)
        opening.start()
        opening_idle = threading.Thread(target=open_script.open_scripts_in_idle,
                                        daemon=True)
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
