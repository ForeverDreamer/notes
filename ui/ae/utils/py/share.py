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
        camera = {
            'Transform.Position': [960, 540, -800], 'Transform.Point of Interest': [960, 540, 0],
            'Camera Options.Zoom': 800, 'Camera Options.Focus Distance': 800, 'Camera Options.Aperture': 7.6,
        }
        # subtitles_bg = {
        #                    'layerName': '字幕背景',
        #                    'Position': [960, 1025],
        #                    'pathGroup': {'type': 'Rect', 'Size': [1000, 40]},
        #                    'Gradient Fill': {'Start Point': [-500, 0], 'End Point': [500, 0], 'Opacity': 70},
        # }

        statements = [
            '//share_util.body',
            'app.purge(PurgeTarget.ALL_CACHES);',
            'var project = app.project;',
            'var mainComp = shareUtil.findItemByName("Main");',
            'if (!mainComp) {',
            '    mainComp = project.items.addComp("Main", WIDTH, HEIGHT, PIXEL_ASPECT, DURATION, FRAME_RATE)',
            '}',
            'mainComp.openInViewer()',
            'mainComp.resolutionFactor = RESOLUTION_FACTOR;',
            'var subtitlesCnLayer = textUtil.addOne({"layerName": "字幕cn", "text": "Write the code, change the world!", "Position": [960, 1017], "font": FONTS["cn"], "fontSize": 40, "fillColor": COLORS["subtitle"]}, mainComp);',
            'var subtitlesEnLayer = textUtil.addOne({"layerName": "字幕en", "text": "Write the code, change the world!", "Position": [960, 1052], "font": FONTS["en"], "fontSize": 30, "fillColor": COLORS["subtitle"]}, mainComp);',
            'var effects = {"ADBE Drop Shadow": {"props": {"Distance": 2.5, "Softness": 10}}}',
            'effectsUtil.add(subtitlesCnLayer, effects)',
            'effectsUtil.add(subtitlesEnLayer, effects)',
            f'var cameraLayer = cameraUtil.add("MainCamera", [960, 540], {camera})',
            'cameraLayer.moveToEnd();',
            'shareUtil.importFiles(conf["files"], project);',
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
