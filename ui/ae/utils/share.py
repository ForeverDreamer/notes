import json

from engine import AE_JSInterface

# def ensure_ok(error_code):
#     assert error_code == 0, '脚本执行错误'


class Share:

    def __init__(self, api):
        self._api = api

    def set_anchor_point(self, layer_index, direction, extents):
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
        tail = f'jsonUtil.write("D:/data_files/notes/ui/ae/力扣/剑指Offer/07_重建二叉树/ae_temp_ret.json", data)'
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
        script = f'layer("Transform")("Anchor Point").setValue({value});'
        head = 'var project = app.project;\nvar comp = project.activeItem;\n'
        head += f'var layer = comp.layer({layer_index});\n'
        script = head + script
        print(script)
        self._api.aeCom.jsNewCommandGroup()
        self._api.aeCom.addCommand(script)
        self._api.aeCom.jsExecuteCommand()



api = AE_JSInterface(ae_version="18.0", base_dir='D:\\data_files\\notes\\ui\\ae\\力扣\\剑指Offer\\07_重建二叉树\\')
Share(api).set_anchor_point(3, 'LEFT', 'false')
