import time
import ctypes

from ae.constants.share import AE_WINDOW_NAME, INIT_ENV
from ae.utils.py.date import now


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

    def log_execute(self, statements):
        pass

    def eval(self, path):
        statements = [
            f'var file = new File("{path}");',
            'file.open("r");',
            'eval(file.read());',
            'file.close();',
        ]
        return self._engine.execute('ShareUtil.eval', statements)

    def open_project(self, path):
        statements = [
            f'var aepFile = new File("{path}");',
            "app.open(aepFile);"
        ]
        return self._engine.execute('ShareUtil.open_project', statements)

    def import_files(self, files):
        statements = []
        for conf in files:
            statements.append(f'shareUtil.importFile(project, {conf});')
        return self._engine.execute('ShareUtil.import_files', statements)

    def create_subtitles(self, subtitles):
        placeholder = {"text": subtitles[0]["text"], "pos": [960, 1050, 0], "font": "KaiTi", "fontSize": 50}
        statements = [
            # f'var subtitles = {subtitles};',
            f'var textLayer = textUtil.add(mainComp, "视频字幕", {placeholder});',
            'effectsUtil.add(textLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 20, "Opacity": 180});'
        ]
        for conf in subtitles:
            text = conf["text"]
            start = conf["start"]
            statements.append(f'textLayer("Source Text").setValuesAtTimes({[start]}, {[text]})')
        return self._engine.execute('ShareUtil.create_subtitles', statements)

    def create_annotations(self, annotations):
        statements = ['var textLayer;',]
        for annotation in annotations:
            span = annotation['span']
            keyframes = annotation.get('keyframes')
            presets = annotation.get('presets')
            statements += [
                f'textLayer = textUtil.add(mainComp, "{annotation["name"]}", {annotation});',
                f'textLayer.inPoint = {span["inPoint"]}',
                f'textLayer.outPoint = {span["outPoint"]}'
            ]
            if keyframes:
                for keyframe in keyframes:
                    for key, value in keyframe.items():
                        statements.append(f'textLayer("Transform")("{key}").setValuesAtTimes({value[0]}, {value[1]})')
            if presets:
                for preset in presets:
                    statements.append(f'presetsUtil.add(textLayer, {preset})')
        return self._engine.execute('ShareUtil.create_annotations', statements)

    # 此接口没必要搞这么复杂，直接调用jsx代码更科学，不要过度滥用Python，但代码可以留着供有需要时参考
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
        # head = '#includepath "../utils";\n#include "json.jsx";\nvar project = app.project;\nvar comp = project.activeItem;\nvar data = {};\n'
        head = 'var data = {};\n'
        head += f'var layer = mainComp.layer({layer_index});\n'
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
        return self._engine.execute(script)
