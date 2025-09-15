import os
from pathlib import Path

class track_object():
    def __init__(self,track_path,img_path=None):
        self.track_path = os.path.abspath(track_path)
        if img_path is None:
            img_path = './img/speaker.png'
        self.img_path = os.path.abspath(img_path)
    def __str__(self):
        return Path(self.track_path).stem
    def get_audio_path(self):
        return self.track_path