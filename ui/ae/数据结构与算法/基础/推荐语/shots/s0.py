from .consts import ASSETS_DIR
# from .transcript_cn import subtitles as all_subtitles_cn
# from .transcript_en import subtitles as all_subtitles_en
from utils.py.audio import audios_subtitles

sn = 0
prefix = f's{sn}'


def build_conf(start_time):
    # all_subtitles = list(map(list, zip(all_subtitles_cn[sn], all_subtitles_en[sn])))
    # audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles, start_time)
    end_time = 10
    duration = end_time - start_time

    conf = {
        'layerName': prefix, 'startTime': start_time, 'duration': duration,
        # 'subtitles': subtitles,
        # 'files': [
        #     {
        #         'folder': 'audios',
        #         'files': audios,
        #     },
        #     {
        #         'path': f'{ASSETS_DIR}/题目描述.jpg',
        #         'layers': [
        #             {
        #                 'sourceName': '题目描述.jpg',
        #                 'layerName': f'{prefix}.题目描述',
        #                 'Scale': [90, 90, 90],
        #                 'Position': [960, 540],
        #                 'startTime': start_time,
        #                 # 'span': {'inPoint': start_time, 'outPoint': end_time},
        #             }
        #         ],
        #     }
        # ],
        # 'texts': [
        #     {
        #         'name': f'{prefix}.主标题', 'text': '什么是数据结构和算法？',
        #         'Anchor Point': 'LEFT_TOP', 'Position': [100, 540],
        #     },
        #     {
        #         'name': f'{prefix}.数据结构',
        #         'text': '数据结构：\n数据结构是以有效且有组织的方式在计算机内存中组织和存储数据的方法\n它们为存储、访问和操作数据提供了基础\n数据结构的示例包括数组、链表、堆栈、队列、树和图',
        #         'fontSize': 30, 'Anchor Point': 'LEFT_TOP', 'Position': [600, 270], "justification": "LEFT_JUSTIFY",
        #     },
        #     {
        #         'name': f'{prefix}.算法', 'text': '算法：\n算法是解决特定问题所遵循的分步过程或指令\n它们是一组定义明确的规则，可将输入数据转换为所需的输出\n算法决定了解决问题的效率，并在软件开发中发挥着至关重要的作用',
        #         'fontSize': 30, 'Anchor Point': 'LEFT_TOP', 'Position': [600, 810], "justification": "LEFT_JUSTIFY",
        #     },
        #
        # ],
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf = build_conf(start_time)
    return sn, conf, conf['end_time']
