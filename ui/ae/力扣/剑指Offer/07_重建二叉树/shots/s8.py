from constants.share import (
    FONTS, QUE_UNIT, COLORS, SPATIAL_HOLD, STROKE_ADD, PATH_STROKE, PATH_COLOR, PATH_EFFECTS, SUBTITLES_INTERVAL
)
from .consts import ASSETS_DIR
from .transcript import subtitles as all_subtitles
from utils_v0.py.audio import audios_subtitles
from utils_v0.py.color import hex_to_rgb1

sn = 8
prefix = f's{sn}'


def build_conf(start_time):
    audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles[sn], start_time)
    duration = end_time - start_time

    QUE_ELEM_WIDTH = 80
    QUE_ELEM_HEIGHT = 80
    QUE_UNIT['pathGroup']['Size'] = [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT]
    QUE_UNIT['fontSize'] = None

    conf = {
        'layerName': prefix, 'startTime': start_time, 'duration': duration,
        'subtitles': subtitles,
        'files': [
            {
                'folder': 'audios',
                'files': audios,
            },
        ],
        'texts': [
            {
                'layerName': f'{prefix}.前序.注解', 'text': '前序遍历按照【根节点->左子树->右子树】的顺序进行\n第一个元素就是树的根节点\n只但无法确定左子树和右子树的分布区域',
                'Anchor Point': 'LEFT_TOP', 'Position': [220.6, 227.8],
                'font': FONTS['cn'], 'fontSize': 40, 'justification': 'LEFT_JUSTIFY',
            },
            {
                'layerName': f'{prefix}.前序0.左', 'text': '左',
                'Anchor Point': 'LEFT_DOWN', 'Position': [1372.4, 405.8],
                'font': FONTS['cn'],
                'keyframes': {
                    "Opacity": [
                        [l_times[4], l_times[4]+SUBTITLES_INTERVAL],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.前序0.根', 'text': '根',
                'Anchor Point': 'LEFT_DOWN', 'Position': [1290.4, 403.9],
                'font': FONTS['cn'],
                'keyframes': {
                    "Opacity": [
                        [l_times[1]-SUBTITLES_INTERVAL, l_times[1]],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.前序0.右', 'text': '右',
                'Anchor Point': 'LEFT_DOWN', 'Position': [1530.4, 403.7],
                'font': FONTS['cn'],
                'keyframes': {
                    "Opacity": [
                        [l_times[5], l_times[5]+SUBTITLES_INTERVAL],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.中序0.注解', 'text': '中序遍历按照【左子树->根节点->右子树】的顺序进行\n只要定位出根节点\n就能确定左子树和右子树的分布区域',
                'Anchor Point': 'LEFT_TOP', 'Position': [220.6, 656],
                'font': FONTS['cn'], 'fontSize': 40, 'justification': 'LEFT_JUSTIFY',
            },
            {
                'layerName': f'{prefix}.中序0.左', 'text': '左',
                'Anchor Point': 'LEFT_DOWN', 'Position': [1292.3, 841.4],
                'font': FONTS['cn'],
                'keyframes': {
                    "Opacity": [
                        [l_times[2], l_times[2] + SUBTITLES_INTERVAL],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.中序0.根', 'text': '根',
                'Anchor Point': 'LEFT_DOWN', 'Position': [1374.3, 843.4],
                'font': FONTS['cn'],
                'keyframes': {
                    "Opacity": [
                        [4.5, 5],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.中序0.右', 'text': '右',
                'Anchor Point': 'LEFT_DOWN', 'Position': [1547.8, 841.3],
                'font': FONTS['cn'],
                'keyframes': {
                    "Transform.Opacity": [
                        [9, 9.5],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
        ],
        'vectors': [
            {
                'layerName': f'{prefix}.前序v0.左',
                'sourceName': 'Tree Length Left Down/Elements.ai',
                'Scale': [75, 75], 'Position': [1398.7, 339.8],
                'keyframes': {
                    "Opacity": [
                        [l_times[4], l_times[4]+SUBTITLES_INTERVAL],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.前序v0.根',
                'sourceName': 'Tree Length Root Down/Elements.ai',
                'Scale': [75, 75], 'Position': [1316.7, 339.8],
                'keyframes': {
                    "Opacity": [
                        [l_times[1]-SUBTITLES_INTERVAL, l_times[1]],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.前序v0.右',
                'sourceName': 'Tree Length Right Down 3x/Elements.ai',
                'Scale': [75, 75], 'Position': [1556.7, 339.8],
                'keyframes': {
                    "Opacity": [
                        [l_times[5], l_times[5]+SUBTITLES_INTERVAL],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.中序v0.左',
                'sourceName': 'Tree Length Left Down/Elements.ai',
                'Scale': [75, 75], 'Position': [1316.9, 780.8],
                'keyframes': {
                    "Opacity": [
                        [l_times[2], l_times[2]+SUBTITLES_INTERVAL],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.中序v0.根',
                'sourceName': 'Tree Length Root Down/Elements.ai',
                'Scale': [75, 75], 'Position': [1398.3, 780.8],
                'keyframes': {
                    "Opacity": [
                        [4.5, 5],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.中序v0.右',
                'sourceName': 'Tree Length Right Down 3x/Elements.ai',
                'Scale': [75, 75], 'Position': [1558.4, 780.8],
                'keyframes': {
                    "Transform.Opacity": [
                        [9, 9.5],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
        ],
        'dsa': [
            {
                'layerName': f'{prefix}.前序队列', 'type': 'QUEUE', 'duration': duration,
                'Anchor Point': 'LEFT_TOP', 'Position': [1276.4, 236],
                # 'elems': [[3, '#0573E1'], [9, '#FADED8'], [20, '#CEF2ED'], [15, '#CEF2ED'], [7, '#CEF2ED']],
                'elems': [
                    {
                        'key': 3,
                        'keyframes': {
                            "Contents.Group 1.Contents.Fill 1.Color": [
                                [l_times[1] - SUBTITLES_INTERVAL, l_times[1]],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["root"])
                                ],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 9,
                        'keyframes': {
                            "Contents.Group 1.Contents.Fill 1.Color": [
                                [l_times[4], l_times[4]+SUBTITLES_INTERVAL],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["left"])
                                ],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 20,
                        'keyframes': {
                            "Contents.Group 1.Contents.Fill 1.Color": [
                                [l_times[5], l_times[5]+SUBTITLES_INTERVAL],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["right"])
                                ],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 15,
                        'keyframes': {
                            "Contents.Group 1.Contents.Fill 1.Color": [
                                [l_times[5], l_times[5]+SUBTITLES_INTERVAL],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["right"])
                                ],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 7,
                        'keyframes': {
                            "Contents.Group 1.Contents.Fill 1.Color": [
                                [l_times[5], l_times[5]+SUBTITLES_INTERVAL],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["right"])
                                ],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    }
                ],
                'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5 + STROKE_ADD, 'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                'unit': QUE_UNIT,
                # 'effects': {'ADBE Drop Shadow': {}},
            },
            {
                'layerName': f'{prefix}.中序队列', 'type': 'QUEUE', 'duration': duration,
                'Anchor Point': 'LEFT_TOP', 'Position': [1276.4, 673.5],
                # 'elems': [[3, '#0573E1'], [9, '#FADED8'], [20, '#CEF2ED'], [15, '#CEF2ED'], [7, '#CEF2ED']],
                'elems': [
                    {
                        'key': 9,
                        'keyframes': {
                            "Contents.Group 1.Contents.Fill 1.Color": [
                                [l_times[2], l_times[2]+SUBTITLES_INTERVAL],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["left"])
                                ],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 3,
                        'keyframes': {
                            "Contents.Group 1.Contents.Fill 1.Color": [
                                [4.5, 5],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["root"])
                                ],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 15,
                        'keyframes': {
                            "Contents.Group 1.Contents.Fill 1.Color": [
                                [9, 9.5],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["right"])
                                ],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 20,
                        'keyframes': {
                            "Contents.Group 1.Contents.Fill 1.Color": [
                                [9, 9.5],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["right"])
                                ],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 7,
                        'keyframes': {
                            "Contents.Group 1.Contents.Fill 1.Color": [
                                [9, 9.5],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["right"])
                                ],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    }
                ],
                'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5 + STROKE_ADD,
                'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                'unit': QUE_UNIT,
                # 'effects': {'ADBE Drop Shadow': {}},
            },
        ],
        'shapes': [
            {
                'layerName': f'{prefix}.前序注解选中框',
                'Position': [718, 243], 'Opacity': 50,
                'pathGroup': {'type': 'Rect', 'Size': [480, 47]},
                'Fill': {'Color': hex_to_rgb1(COLORS['markBox'])},
                'Stroke': {'Stroke Width': 3, 'Color': hex_to_rgb1(COLORS['markBox'])},
                'effects': {
                    "ADBE Glo2": {}
                }
            },
            {
                'layerName': f'{prefix}.中序注解选中框',
                'Position': [718, 672], 'Opacity': 50,
                'pathGroup': {'type': 'Rect', 'Size': [480, 47]},
                'Fill': {'Color': hex_to_rgb1(COLORS['markBox'])},
                'Stroke': {'Stroke Width': 3, 'Color': hex_to_rgb1(COLORS['markBox'])},
                'effects': {
                    "ADBE Glo2": {}
                }
            },
        ],
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf = build_conf(start_time)
    return sn, conf, conf['end_time']
