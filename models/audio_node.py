from pydub import AudioSegment
from pydub.playback import play

HEAD_ID = 0

# 用于轮转调度 播放音频的数据结构 -> 循环链表
class AudioSegmentNode:
    def __init__(self, audio_seg: AudioSegment, order, next=None):
        self._audio_seg = audio_seg
        self._ord = order
        self._next = next

    def link(self, next_node):
        self._next = next_node

    def next(self):
        return self._next
    
    def is_tail(self):
        return self._next.is_head()

    def is_head(self):
        return self._ord == HEAD_ID
    
    def get_audio_length(self):
        return len(self._audio_seg) / 1000.0
    
    def play_audio(self):
        play(self._audio_seg)

    def get_section_id(self):
        return self._ord
    
    def is_valid(self):
        return self._audio_seg is not None
    