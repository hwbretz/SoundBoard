from pygame import mixer
from pathlib import Path
import os
from track_obj import track_object

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
        
        #file_dir = os.path.dirname(os.path.realpath('__file__'))
        
        tracks= [line.rstrip() for line in open(list_file)]
        #with open(list_file,'r') as tracks_file:
                #tracks = tracks_file.readlines()
        track_objs = []
        for track in tracks:
               track = os.path.abspath(track)
               track_objs.append(track_object(track))
               #track = os.path.join(file_dir,track)
        return track_objs

#for populating, listboxes
def populate_listbox_txt(listbox,list_file):
       list = build_audio_list(list_file)
       for idx in range(0,len(list)):
              listbox.insert(idx,Path(list[idx]).stem)

#updated above to array track objects
def populate_listbox_obj_arr(listbox,arr):
       for idx in range(0,len(arr)):
              listbox.insert(idx,arr[idx])

# reasign button through updating button dictionary
def modify_button(btn_idx,sfx,btn_dict, library):
       # look for track in audio library
       found = False
       trk_idx = 0
       while not found and trk_idx < len(library):
              cur_track =  f'{library[trk_idx]}'
              if cur_track == sfx:
                     found = True
              else:       
                     trk_idx += 1
       #assign track to button dictionary              
       if found:
              btn_dict[btn_idx[0]] = library[trk_idx]
      