import time
import ctypes

from ae.constants.share import AE_WINDOW_NAME, INIT_ENV


# def ensure_ok(error_code):
#     assert error_code == 0, '脚本执行错误'

def js_bool(v):
    return 'true' if v else 'false'


def js_null(v):
    if v is None:
        return 'null'
    else:
        return v


class AppNotStartedError(Exception):
    pass


# Tool to get existing windows, useful here to check if AE is loaded
class CurrentWindows:

    def __init__(self):
        self.EnumWindows = ctypes.windll.user32.EnumWindows
        self.EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int),
                                                  ctypes.POINTER(ctypes.c_int))
        self.GetWindowText = ctypes.windll.user32.GetWindowTextW
        self.GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
        self.IsWindowVisible = ctypes.windll.user32.IsWindowVisible

        self.titles = []
        self.EnumWindows(self.EnumWindowsProc(self.foreach_window), 0)

    def foreach_window(self, hwnd, lParam):
        if self.IsWindowVisible(hwnd):
            length = self.GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            self.GetWindowText(hwnd, buff, length + 1)
            self.titles.append(buff.value)
        return True


def ensure_app_started():
    started = False
    for t in CurrentWindows().titles:
        if AE_WINDOW_NAME.lower() in t.lower():
            started = True
            break
    if not started:
        raise AppNotStartedError('请先手动启动Ae程序')


class ShareUtil:

    def __init__(self, engine):
        self._engine = engine

    def eval(self, path):
        statements = [
            f'var file = new File("{path}");',
            'file.open("r");',
            'eval(file.read());',
            'file.close();',
        ]
        script = '\n'.join(statements)
        self._engine.execute(script)

    def open_project(self, path):
        script = f'var aepFile = new File("{path}");'
        script += "app.open(aepFile);"
        self._engine.execute(script)

    def import_files(self, files):
        statements = []
        for conf in files:
            conf['addToLayers'] = js_bool(conf['addToLayers'])
            statements.append(f'shareUtil.importFile(project, {conf});')
        script = '\n'.join(statements)
        print(script)
        print('=====================================')
        self._engine.execute(script)

    def create_precomps(self, precomps):
        statements = []
        for conf in precomps:
            # conf['elems'] = list(map(js_null, conf['elems']))
            if conf['type'] == 'STACK':
                pass
            elif conf['type'] == 'QUEUE':
                pass
            elif conf['type'] == 'LINKED_LIST':
                pass
            elif conf['type'] == 'BINARY_TREE':
                statements.append(f'animationUtil.buildBinaryTree(project.items, mainComp, {conf});')
            elif conf['type'] == 'GRAPH':
                pass
        script = '\n'.join(statements)
        print(script)
        print('=====================================')
        self._engine.execute(script)

    def set_anchor_point(self, layer_index, props_chain, direction, extents):
        n = 4
        data = ['data.'] * n
        var_names = ['top', 'left', 'width', 'height']
        equal_signs = ['='] * n
        expressions = []
        for var_name in var_names:
            expressions.append(f'layer.sourceRectAtTime(0, {extents}).{var_name}')
        semicolons = [';'] * n
        snippets = []
        for field, var_name, equal_sign, expression, semicolon in zip(data, var_names, equal_signs, expressions,
                                                                      semicolons):
            snippets.append(' '.join([field + var_name, equal_sign, expression, semicolon]))
        script = '\n'.join(snippets) + '\n'
        head = '#includepath "../utils";\n#include "json.jsx";\nvar project = app.project;\nvar comp = project.activeItem;\nvar data = {};\n'
        head += f'var layer = comp.layer({layer_index});\n'
        # tail = f'alert({",".join(var_names)})'
        res_file = self._engine.res_file.replace("\\", "/")
        tail = f'jsonUtil.write("{res_file}", data);'
        script = head + script + tail
        print(script)
        self._engine.execute(script)
        # # 返回之封装成json，json.loads()
        data = self._engine.get_res()
        print(data)
        top = data['top']
        width = data['width']
        left = data['left']
        height = data['height']
        value = [0, 0, 0]

        if direction == 'LEFT':
            value[0] = left
            value[1] = top + height / 2
        elif direction == 'LEFT_TOP':
            value[0] = left
            value[1] = top
        elif direction == 'LEFT_DOWN':
            value[0] = left
            value[1] = top + height
        elif direction == 'RIGHT':
            value[0] = left + width
            value[1] = top + height / 2
        elif direction == 'RIGHT_TOP':
            value[0] = left + width
            value[1] = top
        elif direction == 'RIGHT_DOWN':
            value[0] = left + width
            value[1] = top + height
        elif direction == 'TOP':
            value[0] = left + width / 2
            value[1] = top
        elif direction == 'TOP_LEFT':
            value[0] = left
            value[1] = top
        elif direction == 'TOP_RIGHT':
            value[0] = left + width
            value[1] = top
        elif direction == 'DOWN':
            value[0] = left + width / 2
            value[1] = top + height
        elif direction == 'DOWN_LEFT':
            value[0] = left
            value[1] = top + height
        elif direction == 'DOWN_RIGHT':
            value[0] = left + width
            value[1] = top + height
        else:
            # MIDDLE
            value[0] = left + width / 2
            value[1] = top + height / 2

        prop = 'layer' + ''.join([f'("{prop}")' for prop in props_chain])
        script = f'{prop}.setValue({value});'
        head = 'var project = app.project;\nvar comp = project.activeItem;\n'
        head += f'var layer = comp.layer({layer_index});\n'
        script = head + script
        print(script)
        self._engine.execute(script)
