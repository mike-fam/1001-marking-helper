import os
import sys
from typing import List
from pathlib import Path
import shutil
import platform
import subprocess

SHELL = platform.system() == 'Windows'


def open_dir(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.call(["open", str(path)])
    elif platform.system() == "Linux":
        subprocess.call(["gnome-terminal", f"--working-directory={path}"])


class OpenScript:
    TEMP_FOLDER = "temp_{sid}"
    
    def __init__(self, sid, submission_path, support_code, ide, *args,
                 keep_temp=False):
        self._sid = sid
        self._submission_path = submission_path
        self._support_code_path = support_code
        self._keep_temp = keep_temp
        self._to_open: List[str] = list(str(arg) for arg in args)
        self._to_run = str(args[0])
        self._ide = ide
        self._new_dir: Path = None
        self.create_marking_dir()
        
    def create_marking_dir(self):
        if self._keep_temp:
            self._new_dir = self.TEMP_FOLDER.format(sid=self._sid)
        else:
            self._new_dir = "temp_marking"
        self._new_dir = Path(self._new_dir)
        if self._new_dir.is_dir():
            shutil.rmtree(self._new_dir)
        self._new_dir.mkdir()
        # for root, dir, file in os.walk(self._support_code_path):
        #     pass
        
        shutil.copytree(self._support_code_path, self._new_dir, dirs_exist_ok=True)
        shutil.copytree(self._submission_path, self._new_dir, dirs_exist_ok=True)
    
    def open_scripts(self):
        open_dir(self._new_dir.resolve())
        to_opens = []
        for to_open in self._to_open:
            if not (self._new_dir.resolve() / to_open).exists():
                print(f"{to_open} does not exist")
                continue
            to_opens.append(to_open)
        subprocess.call([self._ide, '-n', '-w'] +
                        [self._new_dir.resolve() / to_open for
                         to_open in to_opens],
                        shell=SHELL)
        
    def run_script(self):
        subprocess.call([sys.executable, self._new_dir.resolve() / self._to_run],
                        cwd=self._new_dir.resolve())

    def open_scripts_in_idle(self):
        subprocess.call([sys.executable,
                         "-m",
                         "idlelib",
                         self._new_dir.resolve() / self._to_run],
                        cwd=self._new_dir.resolve())
        
    def get_marking_folder(self):
        return self._new_dir
        

if __name__ == '__main__':
    print("Please run app.py instead")
