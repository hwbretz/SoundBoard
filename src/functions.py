from pygame import mixer
from pathlib import Path
import os

#for audio board button commands
def play_sound(audio_track,generic_label):      
        #mixer via pygame
        mixer.init()
        audio = mixer.Sound(audio_track)
        mixer.music.load(audio_track)
        mixer.music.play()
        generic_label.configure(text=("playing " + Path(audio_track).stem))

#read txt file and convert to sfx list
def build_audio_list(list_file=None):
        if list_file is None:
            list_file = "default_audio.txt"
        
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        tracks= [line.rstrip() for line in open(list_file)]
        #with open(list_file,'r') as tracks_file:
                #tracks = tracks_file.readlines()
       
        for track in tracks:    
               track = os.path.join(file_dir,track)
        return tracks

#for populating, listboxes
def populate_listbox_txt(listbox,list_file):
       list = build_audio_list(list_file)
       for idx in range(0,len(list)):
              listbox.insert(idx,Path(list[idx]).stem)


def modify_button(btn_idx,sfx,btn_dict):
       file_dir = os.path.dirname(os.path.realpath('__file__'))
       audio_file = os.path.join(file_dir,"audio/",(sfx + ".mp3"))
       #print(audio_file)
       btn_dict[btn_idx[0]] = audio_file
       #print(btn_idx)