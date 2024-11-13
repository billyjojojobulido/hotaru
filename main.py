from pydub import AudioSegment
from pydub.playback import play
from audio_manager.utils import play_audio_segment, fetch_audio_info, get_audio_media



if __name__ == "__main__":
    # 加载音频文件
    # play_audio_segment(TEST_AUDIO_FILE_NAME)
    audio = fetch_audio_info(70090)

    ## UNIT TESTING
    # audio_media = get_audio_media(audio.file_path)
    # play_audio_segment(audio_media, 0, 29)


    if audio is None:
        print("No such file, please check.")
        
    else:
        audio_media = get_audio_media(audio.file_path)
        cnt = 0
        start = 0
        end = audio.breakpoints[0]
        while True:
            i = input("Press Enter to play the next one")
            if cnt > len(audio.breakpoints):
                break
            print("Briefing: from {}s to {}s".format(cnt, start, end) if cnt == 0 else "Section: {} from {}s to {}s".format(cnt, start, end))
            play_audio_segment(audio_media, start, end)
            cnt += 1
            start = audio.breakpoints[cnt - 1]
            end = audio.breakpoints[cnt] if cnt < len(audio.breakpoints) else -1
