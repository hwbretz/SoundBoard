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
def build_audio_list(audio_list=None):
        if audio_list is None:
            audio_list = "default_audio.txt"
        
        #file_dir = os.path.dirname(os.path.realpath('__file__'))
        
        tracks= [line.rstrip() for line in open(audio_list)]
        #with open(list_file,'r') as tracks_file:
                #tracks = tracks_file.readlines()
        track_objs = []

        for idx in range(0,len(tracks),2):
               track_path = os.path.abspath(tracks[idx])
               if tracks[idx + 1] is not "default":
                     img_path = os.path.abspath(tracks[idx + 1])
               else:
                     img_path = "default"
               track_objs.append(track_object(track_path,img_path))
               #track = os.path.join(file_dir,track)
        return track_objs

#for populating, listboxes
def populate_listbox_txt(listbox,list_file):
       list = [line.rstrip() for line in open(list_file)]
       for idx in range(0,len(list)):
              listbox.insert(idx,Path(list[idx]).stem)

#updated above to array track objects
def populate_listbox_obj_arr(listbox,arr):
       for idx in range(0,len(arr)):
              listbox.insert(idx,arr[idx])

# reasign button through by button dictionary
def modify_button(btn_idx,sfx,btn_dict, library_text):
       # look for track in audio library
       library = [line.rstrip() for line in open(library_text)]
       found = False
       trk_idx = 0
       print(f"SFX:{sfx}")
       while not found and trk_idx < len(library):
              cur_track =  Path(f'{library[trk_idx]}').stem
              print(f"CURTRACK:{cur_track}")
              if cur_track == sfx:
                     found = True
              else:       
                     trk_idx += 1
       #assign track to button dictionary              
       if found:
              btn_dict[btn_idx[0]].set_audio_path(library[trk_idx])
      