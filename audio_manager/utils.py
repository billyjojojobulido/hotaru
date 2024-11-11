from pydub import AudioSegment
from pydub.playback import play
from resources.audio_info import AudioInfo
import json

CONFIG_FILE_NAME = "resources/test/audio_config.json"

def fetch_audio_info(id: int) -> AudioInfo:
    # 读取 JSON 文件
    with open(CONFIG_FILE_NAME, 'r') as file:
        audio_data = json.load(file)

    # 输出 JSON 数据的内容
    for audio in audio_data:
        if audio["id"] == id:
            return AudioInfo(id, audio["file_name"], audio["breakpoints"])
        
    return None




def play_audio_segment(audio_file):
    # 获取音频对象
    audio = AudioSegment.from_file(audio_file)

    # 定义开始和结束时间（以毫秒为单位）
    start_time = 0
    end_time = 15 * 1000

    # 裁剪音频文件
    # segment = audio[start_time:]

    # 播放音频片段
    # play(segment)
    play(audio)