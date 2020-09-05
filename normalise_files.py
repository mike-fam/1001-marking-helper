from pathlib import Path
import shutil

NORMALISED_SUNMISSIONS_DIR = Path('normalised_submissions')

py_files = list(Path().glob(r'submissions/*.py'))

if not NORMALISED_SUNMISSIONS_DIR.exists():
    NORMALISED_SUNMISSIONS_DIR.mkdir()

for file in py_files:
    _, sid, _, _, file_name = file.name.split('_', maxsplit=4)

    new_dir = Path('normalised_submissions') / sid
    if not new_dir.exists():
        new_dir.mkdir()
    shutil.copy(file, new_dir / file_name)
