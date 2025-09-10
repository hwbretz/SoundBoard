from tkinter import *
from PIL import Image, ImageTk
import functions


def main():
    #set up main window
    root = Tk()
    root.title("Sound Board")
    root.geometry('400x600')
    root.columnconfigure(0,weight = 1)
    root.columnconfigure(1,weight = 1)
    root.columnconfigure(2,weight = 1)
    root.rowconfigure(0, weight = 1)
    root.rowconfigure(1, weight = 2)
    root.rowconfigure(2, weight = 2)
    root.rowconfigure(3, weight = 2)
    root.rowconfigure(4, weight = 1)

    top_lbl=Label(root,text="Click a button!")
    top_lbl.grid(column=1,row=0,padx=3,pady=1)
    #startup audio service
    #mixer.init()

    #basic icon
    spkr_icon = Image.open('./img/speaker.png')
    spkr_icon = spkr_icon.resize((125,125))
    spkr_img = ImageTk.PhotoImage(spkr_icon)

    #buttons and auto placement with .pack()
    #row_1 = Frame(root)
    #row_1.pack(fill = BOTH,expand=True)

    #get audio tracks
    tracks = functions.build_audio_list()
    #for track in tracks:
               #print(track)

    btn_dict = {0:tracks[0],1:tracks[1],2:tracks[2],3:tracks[3],4:tracks[4],5:tracks[5],6:tracks[6],7:tracks[7],8:tracks[8]}
    
    button_0 = Button(root,image=spkr_img,command=lambda:functions.play_sound(btn_dict[0],bottom_lbl))
    button_0.grid(column=0,row=1,sticky=NW)
    button_1 = Button(root,image=spkr_img,command=lambda:functions.play_sound(btn_dict[1],bottom_lbl))
    button_1.grid(column=1,row=1,sticky=N)
    button_2 = Button(root,image=spkr_img,command=lambda:functions.play_sound(btn_dict[2],bottom_lbl))
    button_2.grid(column=2,row=1,sticky=NE)
    button_3 = Button(root,image=spkr_img,command=lambda:functions.play_sound(btn_dict[3],bottom_lbl))
    button_3.grid(column=0,row=2,sticky=W)
    button_4 = Button(root,image=spkr_img,command=lambda:functions.play_sound(btn_dict[4],bottom_lbl))
    button_4.grid(column=1,row=2)
    button_5 = Button(root,image=spkr_img,command=lambda:functions.play_sound(btn_dict[5],bottom_lbl))
    button_5.grid(column=2,row=2,sticky=E)
    button_6 = Button(root,image=spkr_img,command=lambda:functions.play_sound(btn_dict[6],bottom_lbl))
    button_6.grid(column=0,row=3,sticky=W)
    button_7 = Button(root,image=spkr_img,command=lambda:functions.play_sound(btn_dict[7],bottom_lbl))
    button_7.grid(column=1,row=3)
    button_8 = Button(root,image=spkr_img,command=lambda:functions.play_sound(btn_dict[8],bottom_lbl))
    button_8.grid(column=2,row=3,sticky=E)
    

    #bottom label
    bottom_lbl = Label(root,text="waiting to play...")
    bottom_lbl.grid(row=4,column=1)

    

    test_btn = Button(root,text="modify board",command=lambda:modify_board(root,tracks,btn_dict))
    test_btn.grid(row=4,column=2)
    #start up gui
    root.mainloop()

#2nd window to modify sound board    
def modify_board(root,tracks,btn_dict):
    modify_window = Toplevel(root)
    modify_window.title("Modify Sound Board")
    modify_window.geometry("400x300")
    modify_window.columnconfigure(0,weight=1)
    modify_window.columnconfigure(1,weight=1)
    modify_window.rowconfigure(0,weight=5)
    modify_window.rowconfigure(1,weight=1)
    #make window modal; cant interact with main window till this one is closed
    modify_window.grab_set()
    lbl=Label(modify_window,text="main window inactive till this window closed.")
    #lbl.pack()
    #listbox for audio library
    sfx_box = Listbox(modify_window, bg="white",activestyle="dotbox",fg="black",selectmode=SINGLE, exportselection=0) #height=200,width=150,
    sfx_box.grid(row=0,column=1)
    #fill right listbox with audio options
    functions.populate_listbox_txt(sfx_box,"audio_library.txt")
    #listbox for buttons
    btn_box = Listbox(modify_window, bg="white",activestyle="dotbox",fg="black",selectmode=SINGLE,exportselection=0)
    btn_box.grid(row=0,column=0)
    btn_box.insert(0,"Top Left")
    btn_box.insert(1,"Top Mid")
    btn_box.insert(2,"Top Right")
    btn_box.insert(3,"Center Left")
    btn_box.insert(4,"Center Mid")
    btn_box.insert(5,"Center Right")
    btn_box.insert(6,"Bottom Left")
    btn_box.insert(7,"Bottom Mid")
    btn_box.insert(8,"Bottom Right")

    modify = Button(modify_window,text="Assign selected audio to selected button",command=lambda:functions.modify_button(btn_box.curselection(),sfx_box.get(sfx_box.curselection()),btn_dict))
                    #tracks,btn_box.get(btn_box.curselection()),sfx_box.get(0,END),sfx_box.get(sfx_box.curselection())
    modify.grid(row=1,column=0)
    modify_window.protocol("WM_DELETE_WINDOW",lambda: close_window(modify_window))

# close child window
def close_window(window):
    window.grab_release()
    window.destroy()

if __name__ == "__main__":
    main()


# make window to change soundboard
##open file path
##assign to button
####build a play function into 2nd window
##build array of tracks
##make sure not array of old tracks
##assign tracks to buttons
####modify images
####save soundboard layout
####auto load newest saved soundboard