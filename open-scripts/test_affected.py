import argparse
from pathlib import Path
import os
from pprint import pprint
import csv


def main():
    parser = argparse.ArgumentParser(description="Detect path error of marking tool")
    parser.add_argument('submissions_path')
    parser.add_argument('student_ids', metavar='SID', type=str, nargs='*',
                        help='Students to check')
    args = parser.parse_args()
    students_path = Path(args.submissions_path) / 'Assignment 3'
    
    if len(args.student_ids) != 0:
        sids = args.student_ids
    else:
        sids = [os.path.basename(path) for path in sorted(students_path.iterdir())]
    affected = []
    for sid in sids:
        submissions_path = students_path / sid
        if not submissions_path.exists():
            print(f"Student {sid} cannot be found")
            continue
        submissions = list(submissions_path.iterdir())
        sorted_submissions = sorted(submissions)
        if submissions[-1].resolve() != sorted_submissions[-1].resolve():
            print(f"Student {sid} is affected.")
            affected.append([sid])
    with open('affected_students.csv', 'w') as fout:
        writer = csv.writer(fout)
        for row in affected:
            writer.writerow(row)

if __name__ == '__main__':
    main()