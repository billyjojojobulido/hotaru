from pydub import AudioSegment
from pydub.playback import play

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