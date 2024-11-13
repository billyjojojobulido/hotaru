from pydub import AudioSegment
from pydub.playback import play
from audio_manager.utils import _test_audio_loop, construct_audio_loop
from models.audio_node import AudioSegmentNode

TEST_ID = 70090

if __name__ == "__main__":
    # 加载音频文件
    # play_audio_segment(TEST_AUDIO_FILE_NAME)
    # _test_audio_loop(70090)

        
    loop_head = construct_audio_loop(TEST_ID)

    ptr: AudioSegmentNode = loop_head.next()
    visited = False
    while True:
        if ptr.is_head():
            if not visited:            
                visited = True
            else:
                break
        print(ptr._ord)
        ptr.play_audio()
        input("Press <Enter> To Play Next Segment >>> ")
        ptr = ptr.next()