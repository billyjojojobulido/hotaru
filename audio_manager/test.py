from pydub import AudioSegment
from pydub.playback import play

TEST_AUDIO_FILE_NAME = "test_audio_sample.mp3"

if __name__ == "__main__":
    # 加载音频文件
    audio = AudioSegment.from_file(TEST_AUDIO_FILE_NAME)

    # 定义开始和结束时间（以毫秒为单位）
    start_time = 0
    end_time = 15 * 1000

    # 裁剪音频文件
    segment = audio[start_time:]

    # 播放音频片段
    play(segment)
