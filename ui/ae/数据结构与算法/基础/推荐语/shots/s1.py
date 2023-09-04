from .consts import ASSETS_DIR
# from .transcript_cn import subtitles as all_subtitles_cn
# from .transcript_en import subtitles as all_subtitles_en
from utils.py.audio import audios_subtitles

sn = 1
s_name = f's{sn}'


def build_conf(start_time):
    # all_subtitles = list(map(list, zip(all_subtitles_cn[sn], all_subtitles_en[sn])))
    # audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles, start_time)
    end_time = 30
    duration = end_time - start_time
    start_time_ds = 0
    start_time_basic_ds = 1
    start_time_array = 2
    start_time_queue = 3
    start_time_stack = 4
    start_time_ll = 5
    start_time_tree = 6
    start_time_graph = 7

    shot = [
        {
            'layerName': '数据结构', 'startTime': start_time_ds,
        },
        {
            'layerName': '基本数据结构', 'startTime': start_time_basic_ds
        },
        {
            'layerName': '基本数据结构.音效', 'startTime': start_time_basic_ds, 'Anchor Point': None,
        },
        {
            'layerName': '数组', 'startTime': start_time_array
        },
        {
            'layerName': '数组/素材.ai', 'startTime': start_time_array
        },
        {
            'layerName': '数组.音效', 'startTime': start_time_array, 'Anchor Point': None,
        },
        {
            'layerName': '队列', 'startTime': start_time_queue
        },
        {
            'layerName': '队列/素材.ai', 'startTime': start_time_queue
        },
        {
            'layerName': '队列.音效', 'startTime': start_time_queue, 'Anchor Point': None,
        },
        {
            'layerName': '栈', 'startTime': start_time_stack
        },
        {
            'layerName': '栈/素材.ai', 'startTime': start_time_stack
        },
        {
            'layerName': '栈.音效', 'startTime': start_time_stack, 'Anchor Point': None,
        },
        {
            'layerName': '链表', 'startTime': start_time_ll
        },
        {
            'layerName': '链表/素材.ai', 'startTime': start_time_ll
        },
        {
            'layerName': '链表.音效', 'startTime': start_time_ll, 'Anchor Point': None,
        },
        {
            'layerName': '树', 'startTime': start_time_tree
        },
        {
            'layerName': '树/素材.ai', 'startTime': start_time_tree
        },
        {
            'layerName': '树.音效', 'startTime': start_time_tree, 'Anchor Point': None,
        },
        {
            'layerName': '图', 'startTime': start_time_graph
        },
        {
            'layerName': '图/素材.ai', 'startTime': start_time_graph
        },
        {
            'layerName': '图.音效', 'startTime': start_time_graph, 'Anchor Point': None,
        },
    ]
    for layer in shot:
        layer['sourceName'] = s_name
        layer['parentFolderName'] = s_name
        layer['duration'] = duration
    return sn, shot, end_time


def build(start_time):
    return build_conf(start_time)
