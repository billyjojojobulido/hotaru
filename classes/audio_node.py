from pydub import AudioSegment
from pydub.playback import play

HEAD_ID = 0

class AudioSegmentNode:
    def __init__(self, audio_seg: AudioSegment, order, next=None):
        self._audio_seg = audio_seg
        self._ord = order
        self._next = next

    def link(self, next_node):
        self._next = next_node


    def next(self):
        return self._next

    def is_head(self):
        return self._ord == HEAD_ID
    
    def get_audio_length(self):
        return len(self._audio_seg) / 1000.0