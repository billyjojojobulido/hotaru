from pydub import AudioSegment
from pydub.playback import play
from models.audio_info import AudioInfo
from models.audio_node import AudioSegmentNode
import json

CONFIG_FILE_NAME = "resources/audio_config.json"

def fetch_audio_info(id: int) -> AudioInfo:
    # 读取 JSON 文件
    try:
        with open(CONFIG_FILE_NAME, 'r') as file:
            audio_data = json.load(file)
        # 输出 JSON 数据的内容
        for audio in audio_data:
            if audio["id"] == id:
                return AudioInfo(id, audio["file_name"], audio["file_path"], audio["breakpoints"])
    except FileNotFoundError:
        print("Config File: {} not found".format(CONFIG_FILE_NAME))
        return None
    except Exception as e:
        print("Error occurs during configuration".format(e))
        return None

def get_audio_media(audio_file):
    # 获取音频对象
    try:
        audio = AudioSegment.from_file(audio_file)
        return audio
    except FileNotFoundError:
        print("Audio File: {} not found".format(audio_file))
        return None
    except Exception as e:
        print("Error occurs when loading audio media".format(e))

def get_audio_segment(audio_media, start, end):
    if audio_media is None:
        return None 
    # 裁剪音频文件
    segment = audio_media[start*1000:end*1000] if end > 0 else audio_media[start*1000:]

    return segment


# 获取最终的循环列表
def construct_audio_loop(id):
    audio_info = fetch_audio_info(id)
    dummy_head: AudioSegmentNode = AudioSegmentNode(None, -1)
    ptr:AudioSegmentNode = dummy_head
    if audio_info is None:
        print("No such file, please check.")
        return None

    else:
        audio_media = get_audio_media(audio_info.file_path)
        start = 0
        end = audio_info.breakpoints[0]

        for i in range(len(audio_info.breakpoints)):
            if i > 0:
                start = audio_info.breakpoints[i-1]
                end = audio_info.breakpoints[i]

            audio_seg = get_audio_segment(audio_media, start, end)

            new_node = AudioSegmentNode(audio_seg, i, None)
            ptr.link(new_node)

            ptr = new_node

    # 成环
    ptr.link(dummy_head.next())
    return dummy_head

def _test_audio_loop(id):
    loop_head = construct_audio_loop(id)
    ptr: AudioSegmentNode = loop_head.next()
    visited = False
    while True:
        if ptr.is_head():
            if not visited:            
                visited = True
            else:
                break
        print(ptr._ord)
        ptr = ptr.next()
