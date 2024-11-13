from pydub import AudioSegment
from pydub.playback import play


class AudioSegmentNode:
    def __init__(self, audio_seg: AudioSegment, order, next=None):
        self._audio_seg = audio_seg
        self._ord = order
        self._next = next

    def link(self, next_node):
        self._next = next_node
