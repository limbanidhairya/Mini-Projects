import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk, Image

def resetAll(root, frame1):
    # Uncomment if reset logic is implemented in dframe
    # df.count_reset()
    # df.reset_voter_list()
    # df.reset_cand_list()
    Label(frame1, text="").grid(row=10, column=0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row=11, column=0, columnspan=5)

def showVotes(root, frame1):
    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row=0, column=1, rowspan=1)
    Label(frame1, text="").grid(row=1, column=0)

    vote = StringVar(frame1, "-1")

    bjpLogo = ImageTk.PhotoImage(Image.open("img/bjp.png").resize((35, 35), Image.Resampling.LANCZOS))
    congLogo = ImageTk.PhotoImage(Image.open("img/cong.jpg").resize((25, 38), Image.Resampling.LANCZOS))
    aapLogo = ImageTk.PhotoImage(Image.open("img/aap.png").resize((45, 30), Image.Resampling.LANCZOS))
    ssLogo = ImageTk.PhotoImage(Image.open("img/ss.png").resize((40, 35), Image.Resampling.LANCZOS))
    notaLogo = ImageTk.PhotoImage(Image.open("img/nota.jpg").resize((35, 25), Image.Resampling.LANCZOS))

    Label(frame1, image=bjpLogo).grid(row=2, column=0)
    Label(frame1, image=congLogo).grid(row=3, column=0)
    Label(frame1, image=aapLogo).grid(row=4, column=0)
    Label(frame1, image=ssLogo).grid(row=5, column=0)
    Label(frame1, image=notaLogo).grid(row=6, column=0)

    Label(frame1, text="BJP           : ", font=('Helvetica', 12, 'bold')).grid(row=2, column=1)
    Label(frame1, text=result['bjp'], font=('Helvetica', 12, 'bold')).grid(row=2, column=2)

    Label(frame1, text="Cong         : ", font=('Helvetica', 12, 'bold')).grid(row=3, column=1)
    Label(frame1, text=result['cong'], font=('Helvetica', 12, 'bold')).grid(row=3, column=2)

    Label(frame1, text="AAP          : ", font=('Helvetica', 12, 'bold')).grid(row=4, column=1)
    Label(frame1, text=result['aap'], font=('Helvetica', 12, 'bold')).grid(row=4, column=2)

    Label(frame1, text="Shiv Sena    : ", font=('Helvetica', 12, 'bold')).grid(row=5, column=1)
    Label(frame1, text=result['ss'], font=('Helvetica', 12, 'bold')).grid(row=5, column=2)

    Label(frame1, text="NOTA         : ", font=('Helvetica', 12, 'bold')).grid(row=6, column=1)
    Label(frame1, text=result['nota'], font=('Helvetica', 12, 'bold')).grid(row=6, column=2)

    # Keep a reference to avoid garbage collection of images
    frame1.image_refs = [bjpLogo, congLogo, aapLogo, ssLogo, notaLogo]

    frame1.pack()
    root.mainloop()
