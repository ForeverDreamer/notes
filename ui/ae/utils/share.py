import json

from engine import AE_JSInterface


# def ensure_ok(error_code):
#     assert error_code == 0, '脚本执行错误'


class Share:

    def __init__(self, api):
        self._api = api

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
        returnFileClean = self._api.aeCom.returnFile.replace("\\", "/")
        tail = f'jsonUtil.write("{returnFileClean}", data);'
        script = head + script + tail
        print(script)
        self._api.aeCom.jsNewCommandGroup()
        self._api.aeCom.addCommand(script)
        self._api.aeCom.jsExecuteCommand()
        # # 返回之封装成json，json.loads()
        data = self._api.aeCom.readReturn()
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
        self._api.aeCom.jsNewCommandGroup()
        self._api.aeCom.addCommand(script)
        self._api.aeCom.jsExecuteCommand()


api = AE_JSInterface(ae_version="18.0", base_dir='D:\\data_files\\notes\\ui\\ae\\力扣\\剑指Offer\\07_重建二叉树\\')
Share(api).set_anchor_point(2, ['Transform', 'Anchor Point'], 'TOP_RIGHT', 'false')
