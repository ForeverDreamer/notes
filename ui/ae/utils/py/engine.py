"""
Script which builds a .jsx file, sends it to After Effects and then waits for data to be returned.
"""
import os
import sys
import subprocess
import time
import winreg
import json

from Ae.constants.share import BASE_DIR
from Ae.utils.py.date import now


# A Mini Python wrapper for the JS commands...
class Engine:

    def __init__(self, version):
        self._version = version
        # 上次编辑界面反复抖动有可能是注册表Key打开太频繁导致损坏引起的，重置Ae程序才解决
        # Get the AE_ exe path from the registry.
        # try:
        #     self._regkey = winreg.OpenKey(
        #         winreg.HKEY_LOCAL_MACHINE,
        #         "SOFTWARE\\Adobe\\After Effects\\" + self._version
        #     )
        # except FileNotFoundError:
        #     print(
        #         f'ERROR: Unable to find After Effects version {self._version} on this computer\n'
        #         f'To get correct version number please check https://en.wikipedia.org/wiki/Adobe_After_Effects\n'
        #         f'For example, After Effect CC 2021 is version 18.0',
        #         file=sys.stderr)
        #     sys.exit(1)
        # self._app = winreg.QueryValueEx(self._regkey, 'InstallPath')[0] + 'AfterFX.exe'
        self._app = 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/AfterFX.exe'
        self.res_file = os.path.join(BASE_DIR, "tmp/res.json")
        # Ensure the return file exists...
        with open(self.res_file, 'w') as f:
            f.close()
        # Establish the last time the temp file was modified. We use this to listen for changes.
        self._last_mod_time = os.path.getmtime(self.res_file)

    def start_app(self):
        cmd = [self._app]
        subprocess.Popen(cmd)

    def _compile(self, func_name, script):
        tmp_file = os.path.join(BASE_DIR, f"tmp/{func_name}.jsx")
        with open(tmp_file, "wb") as f:
            f.write(script.encode('utf-8'))
        return tmp_file

    def execute(self, func_name, statements):
        script = '\n'.join(statements)
        print(f'{now()}, {func_name}=====================================', file=sys.stderr, flush=True)
        print(script + '\n', flush=True)
        tmp_file = self._compile(func_name, script)
        cmd = [self._app, "-r", tmp_file]
        result = subprocess.run(cmd)
        # with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as proc:
        #     with open("run.log", "a", encoding='utf-8') as f:
        #         # f.write(f'returncode: {result.returncode}\n')
        #         f.write(f'stdout: {proc.stdout.read()}\n')
        # result = subprocess.run(
        #     cmd,
        #     stdout=subprocess.PIPE,
        #     stderr=subprocess.STDOUT,
        #     # check=True,
        #     text=True
        # )
        # with open("run.log", "a", encoding='utf-8') as f:
        #     f.write(f'returncode: {result.returncode}\n')
        #     f.write(f'stdout: {result.stdout}\n')
        # if result.returncode != 1:
        #     sys.exit(1)

    def get_res(self):
        """Helper function to wait for AE to write some output for us."""
        while True:
            mod_time = os.path.getmtime(self.res_file)
            if mod_time != self._last_mod_time:
                self._last_mod_time = mod_time
                break
            else:
                # Give time for AE to close the file...
                time.sleep(0.1)

        with open(self.res_file, "r") as f:
            return json.loads(f.read())
