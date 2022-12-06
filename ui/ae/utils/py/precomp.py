from ae.constants.share import PIXEL_ASPECT, FRAME_RATE


class PrecompUtil:

    def __init__(self, engine):
        self._engine = engine

    def _queue(self, conf):
        name = '队列' + conf["name"]
        elems = conf['elems']
        effects = conf['effects']
        keyframes = conf['keyframes']
        statements = [f'var queueComp = project.items.addComp("{name}", 250, 50, 1, 10, 30);']
        statements.append('var props = {};')
        for i, num in enumerate(elems):
            statements.append(f'props["pos"] = [25 + 50 * {i}, 25, 0]')
            statements.append(f'var shapeLayer = shapeUtil.add(queueComp, "Shape"+{num}, props)')
            statements.append(f'props["text"] = {num}; props["font"] = "Arial-BoldItalicMT"; props["fontSize"] = 40;')
            statements.append(f'var textLayer = textUtil.overlay(queueComp, shapeLayer, "Text"+{num}, props)')
        statements.append('var queueLayer = mainComp.layers.add(queueComp);')
        statements.append('var left = queueLayer.sourceRectAtTime(0, false).left;')
        statements.append('var anchorPointProp = queueLayer("Transform")("Anchor Point");')
        statements.append('var value = anchorPointProp.value;')
        statements.append('anchorPointProp.setValue([left, value[1], value[2]]);')
        statements.append('effectsUtil.add(queueLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 30, "Opacity": 255});')
        statements.append(f'queueLayer("Transform")("Position").setValue({conf["pos"]});')

        return statements

    def create_many(self, precomps):
        statements = []
        for conf in precomps:
            # conf['elems'] = list(map(js_null, conf['elems']))
            if conf['type'] == 'STACK':
                pass
            elif conf['type'] == 'QUEUE':
                statements += self._queue(conf)
            elif conf['type'] == 'LINKED_LIST':
                pass
            elif conf['type'] == 'BINARY_TREE':
                statements.append(f'animationUtil.buildBinaryTree(project.items, mainComp, {conf});')
            elif conf['type'] == 'GRAPH':
                pass
        return self._engine.execute('ShareUtil.create_precomps', statements)

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
