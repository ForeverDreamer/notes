import time
import ctypes

from ae.constants.share import AE_WINDOW_NAME, IMPORT_AS_TYPE
from ae.utils.py.date import now


# def ensure_ok(error_code):
#     assert error_code == 0, '脚本执行错误'


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

    def init(self):
        statements = ['//shareUtil.init']
        statements += [
            '#includepath "../utils/jsx";',
            '#include "constants.jsx";',
            '#include "json.jsx";',
            '#include "color.jsx";',
            '#include "text.jsx";',
            '#include "shape.jsx";',
            '#include "share.jsx";',
            '#include "effects.jsx";',
            '#include "precomp.jsx";',
            '#include "animation.jsx";',
            '#include "presets.jsx";',
            # 'app.purge(PurgeTarget.ALL_CACHES);',
            'var project = app.project;',
            'shareUtil.delItems(project.items);',
            'var mainComp = project.items.addComp("Main", 1920, 1080, 1, 90, 30);',
            'mainComp.openInViewer();',
            'var bgLayer = mainComp.layers.addSolid(colorUtil.hexToRgb1("#0B0909"), "BG", 1920, 1080, 1);',
            'bgLayer.moveToEnd();',
        ]
        statements.append('\n')
        # return self._engine.execute('ShareUtil.eval', statements)
        return statements

    def eval(self, path):
        statements = ['//shareUtil.eval']
        statements += [
            f'var file = new File("{path}");',
            'file.open("r");',
            'eval(file.read());',
            'file.close();',
        ]
        statements.append('\n')
        # return self._engine.execute('ShareUtil.eval', statements)
        return statements

    def open_project(self, path):
        statements = [
            f'var aepFile = new File("{path}");',
            "app.open(aepFile);"
        ]
        return self._engine.execute('ShareUtil.open_project', statements)

    def configLayer(self, layer, conf, parent=None):
        statements = []
        layer_name = conf.get('layerName')
        if layer_name:
            statements.append(f'{layer}.name = "{layer_name}";')
        anchor = conf.get('anchor')
        if anchor:
            statements.append(f'shareUtil.setAnchorPoint({layer}, "{anchor}");')
        pos = conf.get('pos')
        if pos:
            statements.append(f'{layer}("Transform")("Position").setValue({pos});')
        scale = conf.get('scale')
        if scale:
            statements.append(f'{layer}("Transform")("Scale").setValue({scale});')
        rotation = conf.get('rotation')
        if rotation:
            statements.append(f'{layer}("Transform")("Rotation").setValue({rotation});')
        start_time = conf.get('startTime')
        if start_time:
            statements.append(f'{layer}.startTime = {start_time};')
        span = conf.get('span')
        if span:
            statements += [
                f'{layer}.inPoint = {span["inPoint"]};',
                f'{layer}.outPoint = {span["outPoint"]};'
            ]
        if conf.get('3D'):
            statements.append(f'{layer}.threeDLayer = true;')
        if parent:
            statements.append(f'{layer}.setParentWithJump({parent})')

        masks = conf.get('Masks')
        if masks:
            for mask in masks:
                statements += [
                    f'var mask = {layer}.Masks.addProperty("Mask");',
                    f'maskShape = mask("maskShape");',
                    'var shape = maskShape.value;',
                ]
                vertices = mask.get('vertices')
                if vertices:
                    statements.append(f'shape.vertices = {vertices};')
                in_tangents = mask.get('inTangents')
                if in_tangents:
                    statements.append(f'shape.inTangents = {in_tangents};')
                out_tangents = mask.get('outTangents')
                if out_tangents:
                    statements.append(f'shape.vertices = {out_tangents};')
                closed = mask.get("closed", 'true')
                statements += [
                    f'shape.closed =  {closed};',
                    'maskShape.setValue(shape);'
                ]
                mask_feather = mask.get('Mask Feather')
                if mask_feather:
                    statements.append(f'{layer}.Masks("Mask 1")("Mask Feather").setValue({mask_feather});')

        keyframes = conf.get('keyframes')
        if keyframes:
            for key_chain, value in keyframes.items():
                key = ''.join([f'("{k}")' for k in key_chain.split('.')])
                statements.append(f'{layer}{key}.setValuesAtTimes({value[0]}, {value[1]})')
                for i in range(1, len(value[0])+1):
                    statements.append(f'var easeIn = new KeyframeEase({value[2][i-1][0][0]}, {value[2][i-1][0][1]});')
                    statements.append(f'var easeOut = new KeyframeEase({value[2][i-1][1][0]}, {value[2][i-1][1][1]});')
                    statements.append(f'{layer}{key}.setTemporalEaseAtKey({i}, [easeIn], [easeOut])')
        return statements


    def import_files(self, files):
        statements = ['//shareUtil.import_files', f'shareUtil.importFiles({files});', '\n']
        # statements = [
        #     '//shareUtil.import_files',
        #     'var importOptions = new ImportOptions();',
        # ]
        # for conf in files:
        #     statements.append(f'importOptions.file = new File("{conf["path"]}");')
        #     statements.append(f'importOptions.importAs = ImportAsType.{conf["import_as_type"]};')
        #     statements.append('project.importFile(importOptions);')
        #     conf_layers = conf.get('layers')
        #     if conf_layers:
        #         for conf in conf_layers:
        #             parent_layer = 'parentLayer'
        #             statements.append(f'var {parent_layer} = mainComp.layers.add(shareUtil.findItemByName("{conf["name"]}"));',)
        #             statements += self.configLayer(parent_layer, conf)
        #             children = conf.get('children')
        #             if children:
        #                 for child in children:
        #                     child_layer = 'childLayer'
        #                     statements.append(f'var {child_layer} = mainComp.layers.add(shareUtil.findItemByName("{child["name"]}"));')
        #                     statements += self.configLayer(child_layer, child, parent_layer)
        # return self._engine.execute('ShareUtil.import_files', statements)
        return statements

    def create_subtitles(self, subtitles):
        statements = ['//shareUtil.create_subtitles', f'shareUtil.createSubtitles({subtitles})']
        # # placeholder = {"text": subtitles[0]["text"], "Position": [960, 1025, 0], "font": "KaiTi", "fontSize": 50, "fillColor": '#FD9F18'}
        # placeholder = {"text": subtitles[0]["text"], "Position": [960, 1025, 0], "font": "KaiTi", "fontSize": 40,
        #                "fillColor": '#F8F9FB'}
        # statements += [
        #     # f'var subtitles = {subtitles};',
        #     f'var textLayer = textUtil.add(mainComp, "视频字幕", {placeholder});',
        #     # 'effectsUtil.add(textLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 20, "Opacity": 180});',
        #     # 'effectsUtil.add(textLayer, "ADBE Glo2");'
        # ]
        # for conf in subtitles:
        #     text = conf["text"]
        #     start = conf["start"]
        #     statements.append(f'textLayer("Source Text").setValuesAtTimes({[start]}, {[text]})')
        # return self._engine.execute('ShareUtil.create_subtitles', statements)
        statements.append('\n')
        return statements

    def create_annotations(self, annotations):
        statements = ['//shareUtil.create_annotations', f'shareUtil.createAnnotations({annotations})']
        # statements.append('var textLayer;')
        # for annotation in annotations:
        #     span = annotation['span']
        #     keyframes = annotation.get('keyframes')
        #     presets = annotation.get('presets')
        #     statements += [
        #         f'textLayer = textUtil.add(mainComp, "{annotation["name"]}", {annotation});',
        #         f'textLayer.inPoint = {span["inPoint"]}',
        #         f'textLayer.outPoint = {span["outPoint"]}'
        #     ]
        #     if keyframes:
        #         for keyframe in keyframes:
        #             for key, value in keyframe.items():
        #                 statements.append(f'textLayer("Transform")("{key}").setValuesAtTimes({value[0]}, {value[1]})')
        #     if presets:
        #         for preset in presets:
        #             statements.append(f'presetsUtil.add(textLayer, {preset})')
        # return self._engine.execute('ShareUtil.create_annotations', statements)
        statements.append('\n')
        return statements

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
