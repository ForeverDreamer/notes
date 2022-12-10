from ae.constants.share import PIXEL_ASPECT, FRAME_RATE
from ae.utils.py.color import hex_to_rgb1


class PrecompUtil:

    def __init__(self, engine):
        self._engine = engine

    def _stack(self, conf):
        name = '栈.' + conf["name"]
        width = conf['width']
        height = conf['height']
        duration = conf['duration']
        elems = conf['elems']
        effects = conf.get('effects')
        keyframes = conf.get('keyframes')
        statements = [
            f'var queueComp = project.items.addComp("{name}", {width}, {height}, {PIXEL_ASPECT}, {duration}, {FRAME_RATE});']
        statements.append('var props = {};')
        elem_height = 50
        for i, elem in enumerate(elems):
            statements.append(f'props["pos"] = [{width/2}, {height-elem_height/2} - {elem_height} * {i}, 0]; props["Size"] = [{width}, {elem_height}]')
            statements.append(f'var shapeLayer = shapeUtil.add(queueComp, "Shape"+"{elem}", props)')
            statements.append(f'props["text"] = "{elem}"; props["font"] = "Arial-BoldItalicMT"; props["fontSize"] = 40;')
            statements.append(
                f'props["pos"] = null; var textLayer = textUtil.overlay(queueComp, shapeLayer, "Text"+"{elem}", props)')
            if keyframes:
                for key_chain, values in keyframes.items():
                    key = ''.join([f'("{k}")' for k in key_chain.split('.')])
                    if 'Color' in key_chain:
                        for idx, value in enumerate(values[i][1]):
                            values[i][1][idx] = hex_to_rgb1(value)
                    statements.append(f'shapeLayer{key}.setValuesAtTimes({values[i][0]}, {values[i][1]});')
                    for keyIndex in range(1, len(values[i][0]) + 1):
                        statements.append(
                            f'shapeLayer{key}.setInterpolationTypeAtKey({keyIndex}, KeyframeInterpolationType.HOLD, KeyframeInterpolationType.HOLD);')
                    if 'Opacity' in key_chain:
                        statements.append(f'textLayer{key}.setValuesAtTimes({values[i][0]}, {values[i][1]});')
                        for keyIndex in range(1, len(values[i][0]) + 1):
                            statements.append(
                                f'textLayer{key}.setInterpolationTypeAtKey({keyIndex}, KeyframeInterpolationType.HOLD, KeyframeInterpolationType.HOLD);')
        statements.append('var queueLayer = mainComp.layers.add(queueComp);')
        statements.append('var left = queueLayer.sourceRectAtTime(0, false).left;')
        statements.append('var anchorPointProp = queueLayer("Transform")("Anchor Point");')
        statements.append('var value = anchorPointProp.value;')
        statements.append('anchorPointProp.setValue([left, value[1], value[2]]);')
        statements.append(
            'effectsUtil.add(queueLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 30, "Opacity": 255});')
        statements.append(f'queueLayer("Transform")("Position").setValue({conf["pos"]});')

        return statements

    def _queue(self, conf):
        name = '队列.' + conf["name"]
        width = conf['width']
        height = conf['height']
        duration = conf['duration']
        elems = conf['elems']
        effects = conf.get('effects')
        keyframes = conf.get('keyframes')
        statements = [f'var queueComp = project.items.addComp("{name}", {width}, {height}, {PIXEL_ASPECT}, {duration}, {FRAME_RATE});']
        statements.append('var props = {};')
        elem_width = 50
        for i, elem in enumerate(elems):
            statements.append(f'props["pos"] = [{elem_width/2} + {elem_width} * {i}, {height/2}, 0]; props["Size"] = [{elem_width}, {height}]')
            statements.append(f'var shapeLayer = shapeUtil.add(queueComp, "Shape"+"{elem}", props)')
            statements.append(f'props["text"] = "{elem}"; props["font"] = "Arial-BoldItalicMT"; props["fontSize"] = 40;')
            statements.append(f'props["pos"] = null; var textLayer = textUtil.overlay(queueComp, shapeLayer, "Text"+"{elem}", props)')
            if keyframes:
                for key_chain, values in keyframes.items():
                    key = ''.join([f'("{k}")' for k in key_chain.split('.')])
                    if 'Color' in key_chain:
                        for idx, value in enumerate(values[i][1]):
                            values[i][1][idx] = hex_to_rgb1(value)
                    statements.append(f'shapeLayer{key}.setValuesAtTimes({values[i][0]}, {values[i][1]});')
                    for keyIndex in range(1, len(values[i][0]) + 1):
                        statements.append(f'shapeLayer{key}.setInterpolationTypeAtKey({keyIndex}, KeyframeInterpolationType.HOLD, KeyframeInterpolationType.HOLD);')
                    if 'Opacity' in key_chain:
                        statements.append(f'textLayer{key}.setValuesAtTimes({values[i][0]}, {values[i][1]});')
                        for keyIndex in range(1, len(values[i][0]) + 1):
                            statements.append(
                                f'textLayer{key}.setInterpolationTypeAtKey({keyIndex}, KeyframeInterpolationType.HOLD, KeyframeInterpolationType.HOLD);')
        statements.append('var queueLayer = mainComp.layers.add(queueComp);')
        statements.append('var left = queueLayer.sourceRectAtTime(0, false).left;')
        statements.append('var anchorPointProp = queueLayer("Transform")("Anchor Point");')
        statements.append('var value = anchorPointProp.value;')
        statements.append('anchorPointProp.setValue([left, value[1], value[2]]);')
        statements.append('effectsUtil.add(queueLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 30, "Opacity": 255});')
        statements.append(f'queueLayer("Transform")("Position").setValue({conf["pos"]});')

        return statements

    def create_many(self, precomps):
        statements = ['//precompUtil.create_many']
        for conf in precomps:
            # conf['elems'] = list(map(js_null, conf['elems']))
            if conf['type'] == 'STACK':
                statements += self._stack(conf)
            elif conf['type'] == 'QUEUE':
                statements += self._queue(conf)
            elif conf['type'] == 'LINKED_LIST':
                pass
            elif conf['type'] == 'BINARY_TREE':
                statements.append(f'animationUtil.buildBinaryTree(project.items, mainComp, {conf});')
            elif conf['type'] == 'GRAPH':
                pass
            elif conf['type'] == 'CODE':
                statements += self._code(conf)
        # return self._engine.execute('ShareUtil.create_precomps', statements)
        statements.append('\n')
        return statements

    def binary_tree(self, conf):
        name = conf['name']
        width = conf['width']
        height = conf['height']
        duration = conf['duration']

        statements = [
            'var items = project.items;',
            f'var comp = items.addComp("二叉树" + {name}, {width}, {height}, {PIXEL_ASPECT}, {duration}, {FRAME_RATE});',
            'var layers = comp.layers;',
        ]

        node = conf['node']
        edge = conf['edge']
        elems = conf['elems']
        scale = node["scale"][0] / 100
        edgeOffset = 40 * scale
        horizontalDist = 160 * scale
        verticalDist = 240 * scale
        textPos = [65, 75, 0]
        NODE_PREFIX = 'Node'
        EDGE_PREFIX = 'Edge'

        node["pos"] = [225 * scale, 65 * scale, 0]
        node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[0]
        statements.append(f'var nodeLayer = shareUtil.addLayer(items, layers, {node});')

        script = '\n'.join(statements)
        self._engine.execute(script)

    def _code(self, conf):
        name = '代码.' + conf['name']
        width = conf['width']
        height = conf['height']
        duration = conf['duration']
        pairs = conf["pairs"]

        statements = [f'var codeComp = project.items.addComp("{name}", {width}, {height}, {PIXEL_ASPECT}, {duration}, {FRAME_RATE});']
        start_x = 0
        start_y = 30
        pos_y = start_y
        for i, pair in enumerate(pairs):
            for j, line in enumerate(pair):
                if line != ['', 0]:
                    pos_x = start_x + line[1] * 80
                    pos = [pos_x, pos_y, 0]
                    statements.append('var props = {};')
                    statements.append(f'props["text"] = "{line[0]}", props["Anchor Point"] = "{conf["Anchor Point"]}", props["pos"] = {pos}, props["fontSize"] = 30;')
                    statements.append(f'var textLayer = textUtil.add(codeComp, "code" + {i} + "." + {j}, props);')
                    pos_y += 43
        statements.append('var codeLayer = mainComp.layers.add(codeComp);')
        statements.append('var conf =  {};')
        statements.append('conf["name"] = "Arrow Shape/Elements.ai"; shareUtil.addLayer(project. items, mainComp.layers, conf);')

        return statements
