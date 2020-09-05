from pathlib import Path
from pprint import pprint
import argparse
import zipfile
import rarfile

import shutil

EXTRACT_TYPE = {
    '.zip': zipfile.ZipFile,
    '.rar': rarfile.RarFile,
    '.7z': zipfile.ZipFile
}


def extract_file(path: Path, dest: Path):
    with EXTRACT_TYPE[path.suffix](path) as file:
        file.extractall(dest)


def main():
    parser = argparse.ArgumentParser(description="Detect path error of marking tool")
    parser.add_argument('submissions_path')
    args = parser.parse_args()
    task3_students = []
    something_wrong = []
    students_path = Path(args.submissions_path) / 'Assignment 3'
    for student_dir in students_path.iterdir():
        pdf_found = False
        zip_found = False
        
        last_submission = sorted(student_dir.iterdir())[-1] / 'files'
        py_files = list(last_submission.glob('*.py'))
        if not py_files:
            for file in last_submission.iterdir():
                if file.suffix in EXTRACT_TYPE:
                    try:
                        extract_file(file, last_submission)
                        zip_found = True
                    except Exception as e:
                        something_wrong.append([student_dir.stem, file.name, str(e)])
            if not zip_found:
                print(f"student {student_dir.stem} didn't submit a supported file type")
        macosx_dirs = last_submission.glob('**/__MACOSX*/')
        for macosx in macosx_dirs:
            shutil.rmtree(macosx)
        pdf_files = list(last_submission.glob('**/*.pdf'))
        if pdf_files:
            task3_students.append([student_dir.stem, zip_found, pdf_files])
    pprint(task3_students)
    pprint(something_wrong)


if __name__ == '__main__':
    main()
