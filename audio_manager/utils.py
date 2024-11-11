from pydub import AudioSegment
from pydub.playback import play
from resources.audio_info import AudioInfo
import json

CONFIG_FILE_NAME = "resources/test/audio_config.json"

def fetch_audio_info(id: int) -> AudioInfo:
    # 读取 JSON 文件
    try:
        with open(CONFIG_FILE_NAME, 'r') as file:
            audio_data = json.load(file)
        # 输出 JSON 数据的内容
        for audio in audio_data:
            if audio["id"] == id:
                return AudioInfo(id, audio["file_name"], audio["breakpoints"])
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

def play_audio_segment(audio_media, start=0, end=10):
    if audio_media is None:
        return
    # 裁剪音频文件
    segment = audio_media[start*1000:end*1000]

    # 播放音频片段
    play(segment)