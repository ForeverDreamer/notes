from ae.constants.share import PIXEL_ASPECT, FRAME_RATE
from ae.utils.py.color import hex_to_rgb1
from ae.utils.py.share import ShareUtil


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
        layer = 'stackLayer'
        statements.append(f'var {layer} = mainComp.layers.add(queueComp);')
        start_time = conf.get('startTime')
        if start_time:
            statements.append(f'{layer}.startTime = {start_time};')
        statements.append(f'var left = {layer}.sourceRectAtTime(0, false).left;')
        statements.append(f'var anchorPointProp = {layer}("Transform")("Anchor Point");')
        statements.append('var value = anchorPointProp.value;')
        statements.append('anchorPointProp.setValue([left, value[1], value[2]]);')
        statements.append('var props = {"Distance": 10, "Softness": 30, "Opacity": 255}')
        statements.append(f'effectsUtil.add({layer}, "ADBE Drop Shadow", props);')
        statements.append(f'{layer}("Transform")("Position").setValue({conf["pos"]});')

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
        layer = 'queueLayer'
        statements.append(f'var {layer} = mainComp.layers.add(queueComp);')
        start_time = conf.get('startTime')
        if start_time:
            statements.append(f'{layer}.startTime = {start_time};')
        statements.append(f'var left = {layer}.sourceRectAtTime(0, false).left;')
        statements.append(f'var anchorPointProp = {layer}("Transform")("Anchor Point");')
        statements.append('var value = anchorPointProp.value;')
        statements.append('anchorPointProp.setValue([left, value[1], value[2]]);')
        statements.append('var props = {"Distance": 10, "Softness": 30, "Opacity": 255}')
        statements.append(f'effectsUtil.add({layer}, "ADBE Drop Shadow", props);')
        statements.append(f'{layer}("Transform")("Position").setValue({conf["pos"]});')

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
            f'var comp = project.items.addComp("二叉树" + {name}, {width}, {height}, {PIXEL_ASPECT}, {duration}, {FRAME_RATE});',
        ]

        tracker = conf['tracker']
        node = conf['node']
        edge = conf['edge']
        elems = conf['elems']
        scale = node['scale'][0]/100
        edge_offset = 40*scale
        horizontal_dist = 160*scale
        vertical_dist = 240*scale
        text_pos = [65, 75, 0]
        node_prefix = 'Node'
        edge_prefix = 'Edge'

        node['pos'] = [225 * scale, 65 * scale, 0]
        node['layerName'] = f'{node_prefix}.Shape.{elems[0]}'
        layer = 'nodeLayer'
        statements.append(f'var {layer} = comp.layers.add(shareUtil.findItemByName(project.items, "{node["name"]}"));')
        statements += ShareUtil(None).configLayer(layer, node)

        return statements

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
