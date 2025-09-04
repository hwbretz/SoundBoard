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


    button_1 = Button(root,image=spkr_img,command=lambda:functions.play_sound(tracks[0],bottom_lbl))
    button_1.grid(column=0,row=1,sticky=NW)
    button_2 = Button(root,image=spkr_img)
    button_2.grid(column=1,row=1,sticky=N)
    button_3 = Button(root,image=spkr_img)
    button_3.grid(column=2,row=1,sticky=NE)
    button_4 = Button(root,image=spkr_img)
    button_4.grid(column=0,row=2,sticky=W)
    button_5 = Button(root,image=spkr_img)
    button_5.grid(column=1,row=2)
    button_6 = Button(root,image=spkr_img)
    button_6.grid(column=2,row=2,sticky=E)
    button_7 = Button(root,image=spkr_img)
    button_7.grid(column=0,row=3,sticky=W)
    button_8 = Button(root,image=spkr_img)
    button_8.grid(column=1,row=3)
    button_9 = Button(root,image=spkr_img)
    button_9.grid(column=2,row=3,sticky=E)

    #bottom label
    bottom_lbl = Label(root,text="waiting to play...")
    bottom_lbl.grid(row=4,column=1)

    #start up gui
    root.mainloop()
    

if __name__ == "__main__":
    main()