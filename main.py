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
        start = 0
        end = audio.breakpoints[0]

        for i in range(len(audio.breakpoints)):
            input("Press <Enter> to play the next audio segment.")
            if i == 0:
                start = 0
                end = audio.breakpoints[0]
                print("Briefing: from {}s to {}s".format(start, end))

            else:
                start = audio.breakpoints[i-1]
                end = audio.breakpoints[i]
                print( "Section: {} from {}s to {}s".format(i, start, end))

            play_audio_segment(audio_media, start, end)
        
