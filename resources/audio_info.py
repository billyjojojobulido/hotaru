from dataclasses import dataclass

@dataclass
class AudioInfo:
    id: int
    file_name: str
    breakpoints: list