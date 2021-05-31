from pathlib import Path
import threading
import argparse
from helpers.open_scripts import OpenScript
import yaml
from datetime import datetime, timezone
import pytz


SUBMISSION_DIR = Path("submissions")
SUPPORT_CODE_PATH = Path('assignment_stub')
DUE_DATE = datetime(2021, 5, 28, 20, 0, 0,
                    tzinfo=pytz.timezone("Australia/Brisbane"))


def print_data(submission):
    submitter = submission[":submitters"][0]
    print(f"Student name: {submitter[':name']}")
    print(f"Student id: {submitter[':sid']}")
    submit_time: datetime = submission[':created_at']
    print(f"Submit time: {submit_time}")
    if submit_time > DUE_DATE:
        print("Late submission by", (submit_time - DUE_DATE).seconds, "seconds")


def get_section(submission):
    submitter = submission[":submitters"][0]
    return submitter.get("Section", "")


def main():
    parser = argparse.ArgumentParser(
        description="Open student's scripts and run them")
    parser.add_argument("section")
    parser.add_argument("--ide", required=False)
    args = parser.parse_args()
    with open(SUBMISSION_DIR / "submission_metadata.yml") as data_file:
        submission_data = yaml.load(data_file, Loader=yaml.SafeLoader)
    for submission_name, submission in submission_data.items():
        submission_path = SUBMISSION_DIR / submission_name
        if get_section(submission) != args.section:
            continue

        # print student data
        print("Submission id:", submission_name)
        print_data(submission)

        # open and run assignments
        # Change keep_temp if you dont want to keep your marking folders
        open_script = OpenScript(submission_name, submission_path,
                                 SUPPORT_CODE_PATH,
                                 args.ide,
                                 "a3.py",
                                 "task1.py",
                                 "task2.py",
                                 "csse7030.py",
                                 "constants.py",
                                 keep_temp=False)
        if args.ide:
            opening = threading.Thread(target=open_script.open_scripts,
                                       daemon=True)
            opening.start()
        opening_idle = threading.Thread(target=open_script.open_scripts_in_idle,
                                        daemon=True)
        opening_idle.start()
        running = threading.Thread(target=open_script.run_script, daemon=True)
        running.start()
        if args.ide:
            opening.join()
        opening_idle.join()
        running.join()
        

if __name__ == '__main__':
    main()
