from ae.constants.share import PIXEL_ASPECT, FRAME_RATE


class PrecompUtil:

    def __init__(self, engine):
        self._engine = engine

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
