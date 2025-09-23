import os
from pathlib import Path
from PIL import Image, ImageTk

class track_object():
    def __init__(self,track_path,img_path=None):
        self.track_path = os.path.abspath(track_path)

        if img_path is None or img_path == "default":
            img_path = './img/speaker.png'
        self.img_path = os.path.abspath(img_path)
        self.icon = self.make_img_icon(self.img_path)
        
    def make_img_icon(self,img_path):
        spkr_icon = Image.open(img_path)
        spkr_icon = spkr_icon.resize((125,125))
        return ImageTk.PhotoImage(spkr_icon)
    def __str__(self):
        return Path(self.track_path).stem + ".mp3"
    def get_audio_path(self):
        return self.track_path
    def set_audio_path(self,new_path):
        self.track_path = os.path.abspath(new_path)
    def get_image_path(self):
        return self.img_path
    def set_image_path(self,new_path):
        self.img_path = os.path.abspath(new_path)
    def set_new_image(self,new_path):
        self.set_image_path(new_path)
        self.icon = self.make_img_icon(new_path)
    def get_image(self):
        return self.icon