from constants.share import BASE_DIR


class ShareUtil:
    def __init__(self, engine):
        self._engine = engine

    def log_execute(self, statements):
        pass

    def head(self, conf_path):
        statements = [
            '//share_util.head',
            '#includepath "../utils/jsx";',
            '#include "json.jsx";',
            f'var conf = jsonUtil.read("{conf_path}");',
            '#include "constants.jsx";',
            '#include "color.jsx";',
            '#include "text.jsx";',
            '#include "shape.jsx";',
            '#include "share.jsx";',
            '#include "effects.jsx";',
            '#include "presets.jsx";',
            '#include "camera.jsx";',
            '#include "comp.jsx";',
            '#include "dsa/binarytree.jsx"',
            '#include "dsa/codes.jsx"',
            '#include "dsa/queue.jsx"',
            '#include "dsa/stack.jsx"',
            '#include "dsa/dsa.jsx"',
            '\n',
        ]
        # return self._engine.execute('ShareUtil.eval', statements)
        return statements

    def body(self):
        statements = [
            '//share_util.body',
            'app.purge(PurgeTarget.ALL_CACHES);',
            'var project = app.project;',
            'shareUtil.configShots(conf["shots"]);',
            '\n',
        ]
        # return self._engine.execute('ShareUtil.eval', statements)
        return statements

    def tail(self):
        statements = [
            '//share_util.tail',
            'subtitlesCnLayer.moveToBeginning();',
            'subtitlesEnLayer.moveToBeginning();',
            'var bgLayer = mainComp.layers.addSolid(colorUtil.hexToRgb1(COLORS["bg"]), "BG", WIDTH, HEIGHT, PIXEL_ASPECT);',
            'bgLayer.moveToEnd();',
            '\n',
        ]
        return statements

    def eval(self, path):
        statements = ['//share_util.eval']
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
        return self._engine.execute('share_util.open_project', statements)
