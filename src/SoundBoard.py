from tkinter import *
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

    #get audio tracks for buttons
    tracks = functions.build_audio_list()
    
    #dictionary to hold tracks assigned to buttons
    btn_dict = {0:tracks[0],1:tracks[1],2:tracks[2],3:tracks[3],4:tracks[4],5:tracks[5],6:tracks[6],7:tracks[7],8:tracks[8]}

    #sound effect buttons
    btn_arr = [
        Button(root,image=btn_dict[0].get_image(),command=lambda:functions.play_sound(btn_dict[0].get_audio_path(),bottom_lbl)),
        Button(root,image=btn_dict[1].get_image(),command=lambda:functions.play_sound(btn_dict[1].get_audio_path(),bottom_lbl)),
        Button(root,image=btn_dict[2].get_image(),command=lambda:functions.play_sound(btn_dict[2].get_audio_path(),bottom_lbl)),
        Button(root,image=btn_dict[3].get_image(),command=lambda:functions.play_sound(btn_dict[3].get_audio_path(),bottom_lbl)),
        Button(root,image=btn_dict[4].get_image(),command=lambda:functions.play_sound(btn_dict[4].get_audio_path(),bottom_lbl)),
        Button(root,image=btn_dict[5].get_image(),command=lambda:functions.play_sound(btn_dict[5].get_audio_path(),bottom_lbl)),
        Button(root,image=btn_dict[6].get_image(),command=lambda:functions.play_sound(btn_dict[6].get_audio_path(),bottom_lbl)),
        Button(root,image=btn_dict[7].get_image(),command=lambda:functions.play_sound(btn_dict[7].get_audio_path(),bottom_lbl)),
        Button(root,image=btn_dict[8].get_image(),command=lambda:functions.play_sound(btn_dict[8].get_audio_path(),bottom_lbl))
    ]
    btn_arr[0].grid(column=0,row=1,sticky=NW)
    btn_arr[1].grid(column=1,row=1,sticky=N)
    btn_arr[2].grid(column=2,row=1,sticky=NE)
    btn_arr[3].grid(column=0,row=2,sticky=W)
    btn_arr[4].grid(column=1,row=2)
    btn_arr[5].grid(column=2,row=2,sticky=E)
    btn_arr[6].grid(column=0,row=3,sticky=W)
    btn_arr[7].grid(column=1,row=3)
    btn_arr[8].grid(column=2,row=3,sticky=E)

    #menu bar
    menubar = Menu(root)
    #menu heading
    menu = Menu(menubar,tearoff=0)
    #subheadings
    menu.add_command(label="Add to audio library",command=lambda:functions.add_to_library("audio"))
    menu.add_command(label="Add to image library",command=lambda:functions.add_to_library("img"))
    menu.add_command(label="Save configuration",command=lambda:functions.save_configuration(btn_dict))
    menu.add_command(label="Revert to default",command=lambda:functions.load_default(btn_dict,btn_arr,True))
    menubar.add_cascade(label="File",menu=menu)
    root.config(menu = menubar)

    #bottom label
    bottom_lbl = Label(root,text="waiting to play...")
    bottom_lbl.grid(row=4,column=1)

    # button to modify board
    mod_btn = Button(root,text="modify board",command=lambda:modify_board(root,"audio_library.txt",btn_dict,btn_arr))
    mod_btn.grid(row=4,column=2)
    
    #start up gui
    root.mainloop()



#2nd window to modify sound board    
def modify_board(root,library,btn_dict,btn_arr):
    modify_window = Toplevel(root)
    modify_window.title("Modify Sound Board")
    modify_window.geometry("460x300")
    modify_window.columnconfigure(0,weight=1)
    modify_window.columnconfigure(1,weight=1)
    modify_window.columnconfigure(2,weight=1)
    modify_window.rowconfigure(0,weight=5)
    modify_window.rowconfigure(1,weight=1)
    #make window modal; cant interact with main window till this one is closed
    modify_window.grab_set()
    lbl=Label(modify_window,text="main window inactive till this window closed.")

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

    #listbox for audio library
    sfx_box = Listbox(modify_window, bg="white",activestyle="dotbox",fg="black",selectmode=SINGLE, exportselection=0)
    sfx_box.grid(row=0,column=1)
    #fill right listbox with audio options
    functions.populate_listbox_txt(sfx_box, library)

    #listbox for image library
    img_box = Listbox(modify_window, bg="white",activestyle="dotbox",fg="black",selectmode=SINGLE, exportselection=0)
    img_box.grid(row=0,column=2)
    functions.populate_listbox_txt(img_box,"img_library.txt")

    modify = Button(modify_window,text="Update selected button",command=lambda:functions.modify_button(btn_box.curselection(),btn_dict,library,"img_library.txt",sfx_box,img_box,btn_arr))
    modify.grid(row=1,column=0)

    modify_window.protocol("WM_DELETE_WINDOW",lambda: close_window(modify_window))

# close child window
def close_window(window):
    window.grab_release()
    window.destroy()




if __name__ == "__main__":
    main()



##open file path
####build a play function into 2nd window
##build array of tracks
##make sure not array of old tracks
##assign tracks to buttons
####modify images
####save soundboard layout
####auto load newest saved soundboard