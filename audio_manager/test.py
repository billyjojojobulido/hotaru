from pydub import AudioSegment
from pydub.playback import play
from audio_manager.utils import play_audio_segment

TEST_AUDIO_FILE_NAME = "test_audio_sample.mp3"

if __name__ == "__main__":
    # 加载音频文件
    play_audio_segment(TEST_AUDIO_FILE_NAME)
    
