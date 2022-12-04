def ensure_ok(error_code):
    assert error_code == 0, '脚本执行错误'


class Share:

    def __init__(self, api):
        self._api = api

    def set_anchor_point(self, layer_name, direction, extents):
        n = 4
        var_keywords = ['var']*n
        var_names = ['top', 'left', 'width', 'height']
        equal_signs = ['=']*n
        expressions = []
        for var_name in var_names:
            expressions.append(f'layer.sourceRectAtTime(0, {extents}).{var_name}')
        semicolons = [';']*n
        snippets = []
        for va_keyword, var_name, equal_sign, expression, semicolon in zip(var_keywords, var_names, equal_signs, expressions, semicolons):
            snippets.append(' '.join([va_keyword, var_name, equal_sign, expression, semicolon]))
        script = '\n'.join(snippets)+'\n'
        head = 'var project = app.project;\nvar comp = project.activeItem;\nvar layer = comp.layer(1);\n'
        tail = f'alert({",".join(var_names)})'
        script = head + script + tail
        print(script)
        # self._api.aeCom.addCommand(script)
        # ensure_ok(self._api.aeCom.jsExecuteCommand())
        # # 返回之封装成json，json.loads()
        # rect = self.aeCom.readReturn()[0]
        # # 再执行后边代码，这种方式好像把过程复杂化了，而且影响执行速度，测试一下再说！


Share(None).set_anchor_point('Node1', 'TOP', 'false')
