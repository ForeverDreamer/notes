"""
Script which builds a .jsx file, sends it to After Effects and then waits for data to be returned.
"""
import os
import sys
import subprocess
import time
import winreg
import json


# A Mini Python wrapper for the JS commands...
class Engine:

    def __init__(self, version, base_dir):
        self._version = version
        # Get the AE_ exe path from the registry.
        try:
            self._regkey = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                "SOFTWARE\\Adobe\\After Effects\\" + self._version
            )
        except FileNotFoundError:
            print(
                f'ERROR: Unable to find After Effects version {self._version} on this computer\n'
                f'To get correct version number please check https://en.wikipedia.org/wiki/Adobe_After_Effects\n'
                f'For example, After Effect CC 2021 is version 18.0',
                file=sys.stderr)
            sys.exit(1)
        self._app = winreg.QueryValueEx(self._regkey, 'InstallPath')[0] + 'AfterFX.exe'
        self.res_file = os.path.join(base_dir, "tmp/res.json")
        # Ensure the return file exists...
        with open(self.res_file, 'w') as f:
            f.close()
        # Establish the last time the temp file was modified. We use this to listen for changes.
        self._last_mod_time = os.path.getmtime(self.res_file)
        # Temp file to store the .jsx commands.
        self._tmp_file = os.path.join(base_dir, "tmp/script.jsx")

    def start_app(self):
        cmd = [self._app]
        subprocess.Popen(cmd)

    def _compile(self, script):
        with open(self._tmp_file, "wb") as f:
            f.write(script.encode('utf-8'))

    def execute(self, script):
        self._compile(script)
        cmd = [self._app, "-r", self._tmp_file]
        return subprocess.Popen(cmd)

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


# An interface to actually call those commands.
# class AE_JSInterface:
#
#     def __init__(self, ae_version, base_dir):
#         self.aeWindowName = "Adobe After Effects"
#         self.aeCom = Engine(ae_version, base_dir)  # Create wrapper to handle JSX
#
#     def openAE(self):
#         self.aeCom.openAE()
#
#     def waitingAELoading(self):
#         loading = True
#         attempts = 0
#         while loading and attempts < 60:
#             for t in CurrentWindows().getTitles():
#                 if self.aeWindowName.lower() in t.lower():
#                     loading = False
#                     break
#
#             attempts += 1
#             time.sleep(0.5)
#
#         return not loading
#
#     def jsAlert(self, msg):
#         self.aeCom.jsNewCommandGroup()  # Clean JSX command list
#
#         # Write new JSX commands
#         jsxTodo = "alert(\"" + msg + "\");"
#         self.aeCom.addCommand(jsxTodo)
#
#         self.aeCom.jsExecuteCommand()  # Execute command list
#
#     def jsOpenProject(self, path):
#         self.aeCom.jsNewCommandGroup()  # Clean JSX command list
#
#         # Write new JSX commands
#         jsxTodo = "var aepFile = new File(\"" + path + "\");"
#         jsxTodo += "app.open(aepFile);"
#         self.aeCom.addCommand(jsxTodo)
#
#         self.aeCom.jsExecuteCommand()  # Execute command list
#
#     def jsGetActiveDocument(self):
#         self.aeCom.jsNewCommandGroup()  # Clean JSX command list
#
#         # Write new JSX commands
#         resultVarName = "aeFilePath"
#         jsxTodo = ("var %s = app.project.file.fsName;" % resultVarName)
#         self.aeCom.addCommand(jsxTodo)
#         self.aeCom.jsWriteDataOut(resultVarName)  # Add JSX commands to write result in temp file
#
#         self.aeCom.jsExecuteCommand()  # Execute command list
#
#         return self.aeCom.readReturn()[0]  # Read the temp file to get the JSX returned value
#
#
#     def jsAlert(self, msg):
#         self.aeCom.jsNewCommandGroup()  # Clean JSX command list
#         extents = 'false'
#         layer_index = 1
#         # Write new JSX commands
#         # jsxTodo = "alert(\"" + msg + "\");"
#         n = 4
#         data = ['data.'] * n
#         var_names = ['top', 'left', 'width', 'height']
#         equal_signs = ['='] * n
#         expressions = []
#         for var_name in var_names:
#             expressions.append(f'layer.sourceRectAtTime(0, {extents}).{var_name}')
#         semicolons = [';'] * n
#         snippets = []
#         for field, var_name, equal_sign, expression, semicolon in zip(data, var_names, equal_signs, expressions,
#                                                                       semicolons):
#             snippets.append(' '.join([field + var_name, equal_sign, expression, semicolon]))
#         script = '\n'.join(snippets) + '\n'
#         head = '#includepath "../utils";\n#include "json.jsx";\nvar project = app.project;\nvar comp = project.activeItem;\nvar data = {};\n'
#         head += f'var layer = comp.layer({layer_index});\n'
#         # tail = f'alert({",".join(var_names)})'
#         tail = f'jsonUtil.write("D:/data_files/notes/ui/ae/力扣/剑指Offer/07_重建二叉树/ae_temp_ret.json", data)'
#         script = head + script + tail
#         print(script)
#         self.aeCom.addCommand(script)
#
#         self.aeCom.jsExecuteCommand()
#         return self.aeCom.readReturn()
#
# if __name__ == '__main__':
#     # Create the wrapper
#     aeApp = AE_JSInterface(ae_version="18.0", base_dir='D:\\data_files\\notes\\ui\\ae\\力扣\\剑指Offer\\07_重建二叉树\\')
#
#     # Open AE if needed
#     # aeApp.openAE()
#     if aeApp.waitingAELoading():
#         # Launch function if AE is ready
#         aeApp.jsOpenProject("D:/Untitled Project.aep")
#         # aeApp.jsGetActiveDocument()
#         # print(aeApp.jsAlert(''))