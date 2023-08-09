from Ae.constants.share import *
from .transcript import scenes


name = 's0'


def shot_0(start_time):
    sn = 0
    prefix = f'{name}.{sn}'
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]+SUBTITLES_INTERVAL
    # duration = end_time - start_time
    duration = 100
    # QUE_UNIT['RC'] = {'Radius': 10}

    elems = [
        {'key': 21, 'oper': 'I'}, {'key': 17, 'oper': 'I'}, {'key': 19, 'oper': 'I'},
        {'key': 1, 'oper': 'I'}, {'key': 20, 'oper': 'I'}, {'key': 9, 'oper': 'I'},
        {'key': 16, 'oper': 'I'}, {'key': 2, 'oper': 'I'}, {'key': 6, 'oper': 'I'},
        {'key': 12, 'oper': 'I'}, {'key': 18, 'oper': 'I'}, {'key': 5, 'oper': 'I'},
        {'key': 7, 'oper': 'I'}, {'key': 18, 'oper': 'S'}, {'key': 1, 'oper': 'D'},
    ]

    texts = []
    text_start_time = 0
    for i, elem in enumerate(elems):
        conf_text = {
            'name': f'{prefix}.操作指令', 'Position': [400, 50],
            'font': FONTS['subtitle'], 'fillColor': COLORS['subtitle'], 'fontSize': 40,
            'keyframes': {
                'Transform.Opacity': [
                    [text_start_time, text_start_time+i+1, text_start_time+i+2],
                    [0, 100, 0],
                    {'spatial': SPATIAL_HOLD*3}
                ]
            }
        }
        oper = '插入'
        if elem['oper'] == 'S':
            oper = '搜索'
        elif elem['oper'] == 'D':
            oper = '删除'
        conf_text['text'] = oper + ' ' + str(elem['key'])
        texts.append(conf_text)

    conf = {
        'layerName': prefix, 'startTime': start_time, 'duration': duration,
        # 'presets': [
        #     {
        #         'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Transitions - Movement/Slide - drop.ffx',
        #         'keyframes': {
        #             'Slide Master Control.Transition Completion': [
        #                 [0, 1],
        #                 [0, 100],
        #                 {"temporal": [[[0, 0.1], [200, 50]], [[0, 30], [0, 0.1]]]},
        #                 True
        #             ]
        #         }
        #     }
        # ],
        'texts': [
            {
                'name': 'expression_test', 'text': 'expression_test', 'Position': [500, 500],
                'font': FONTS['subtitle'], 'fillColor': COLORS['subtitle'], 'fontSize': 100,
                'expression': [
                    'var layerNames = [];',
                    'var myComp = comp(thisComp.layer(2).name);',
                    'for (var i = 1; i <= myComp.numLayers; i ++) {',
                    '    layerNames.push(myComp.layer(i).name)',
                    '}',
                    'layerNames;',
                ]
            }
        ],
        'misc': {
            'layerName': 'B-Tree合成', 'width': 1920, 'height': 1080, 'startTime': start_time, 'duration': duration,
            'texts': texts,
            'vectors': [
                {
                    'name': 'Indicator/Elements.ai', 'layerName': 'Indicator',
                    'Scale': [100, 100, 100], 'Opacity': 0, 'Position': [960, 900],
                    # 'Anchor Point': 'TOP', 'Position': [400, 200],
                }
            ],
            'precomps': [
                {
                    'layerName': 'B-Tree', 'type': 'B-TREE', 'width': 1920, 'height': 1080,
                    'Position': [960, 540],
                    'startTime': start_time, 'duration': duration,
                    'animation': True,
                    'elems': elems,
                    # 'elems': [
                    #     {'key': 21}, {'key': 17}, {'key': 19}, {'key': 1}, {'key': 20}, {'key': 9}, {'key': 16}, {'key': 2},
                    #     {'key': 6}, {'key': 12}, {'key': 18}, {'key': 5}, {'key': 7}
                    # ],
                    'unit': QUE_UNIT,
                    'layersRoot': 'misc'
                },
            ],
        },
        'subtitles': subtitles,
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
