from pygame import mixer
from pathlib import Path
import os
from track_obj import track_object
from tkinter import filedialog

#for audio board button commands
def play_sound(audio_track,generic_label):      
        #mixer via pygame
        mixer.init()
        mixer.music.stop()
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
def modify_button(btn_idx,btn_dict, library_text,img_text,sfx_box,img_box,btn_arr):
       # look for track in audio library
       
       if sfx_box.curselection() :
              sfx = sfx_box.get(sfx_box.curselection())
              library = [line.rstrip() for line in open(library_text)]
              found = False
              trk_idx = 0
              while not found and trk_idx < len(library):
                     cur_track =  Path(f'{library[trk_idx]}').stem
                     if cur_track == sfx:
                            found = True
                     else:       
                            trk_idx += 1
              #assign track to button dictionary              
              if found:
                     btn_dict[btn_idx[0]].set_audio_path(library[trk_idx])

       
       #update button img
       if img_box.curselection():
              img = img_box.get(img_box.curselection())
              images = [line.rstrip() for line in open(img_text)]
              found = False
              img_idx = 0
              while not found and trk_idx < len(images):
                     cur_img =  Path(f'{images[img_idx]}').stem
                     if cur_img == img:
                            found = True
                     else:       
                            img_idx += 1
              #assign track to button dictionary              
              if found:
                     #btn_dict[btn_idx[0]].set_image_path(images[img_idx])
                     btn_dict[btn_idx[0]].set_new_image(images[img_idx])
                     btn_arr[btn_idx[0]].config(image=btn_dict[btn_idx[0]].get_image())
                     #btn_arr[btn_idx[0]].photo1 = btn_dict[btn_idx[0]].get_image()

def add_to_library(type):
    if(type == "audio"):
       filename = filedialog.askopenfilename(title="Select sound effect",filetypes=[("Audio",('*.mp3','*.wav','*.ogg','*.xm'))])
       #audio_types = ["mp3","wav","ogg","xm"]
       #if filename not in audio_types:
           #return
       aud_lib = open("audio_library.txt","a")
       aud_lib.write('\n' + filename)
       aud_lib.close()
       return
    
    filename = filedialog.askopenfilename(title="Select image",filetypes=[("Image",('*.jpeg','*.jpg','*.png','*.gif'))])
    #img_types = ["png","jpeg","jpg","gif"]
    #if filename not in img_types:
       #return
    img_lib = open("img_library.txt","a")
    img_lib.write('\n' + filename)
    img_lib.close()
    return

def save_configuration(btn_dict):
       output_text =''
       for idx in range(0,len(btn_dict)):
              output_text += btn_dict[idx].get_audio_path() + '\n'
              output_text += btn_dict[idx].get_image_path() + '\n'
       
       file = open("custom_buttons.txt",'w')
       file.write(output_text)
       file.close()

                     

       