from pygame import mixer
from pathlib import Path

def play_sound(audio_track,generic_label):
        
        #mixer via pygame
        mixer.init()
        audio = mixer.Sound(audio_track)
        mixer.music.load(audio_track)
        mixer.music.play()
        generic_label.configure(text=("playing " + Path(audio_track).stem))

def build_audio_list(list_file=None):
        if list_file is None:
            list_file = "default_audio.txt"

        tracks= []
        with open(list_file,'r') as tracks_file:
                tracks = tracks_file.readlines()
        return tracks
