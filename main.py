from pydub import AudioSegment
from pydub.playback import play
from audio_manager.utils import play_audio_segment, fetch_audio_info, get_audio_media


if __name__ == "__main__":
    # 加载音频文件
    # play_audio_segment(TEST_AUDIO_FILE_NAME)
    audio = fetch_audio_info(1)
    if audio is None:
        print("No such file, please check.")
        
    else:
        audio_media = get_audio_media(audio.file_name)
        play_audio_segment(audio_media)

