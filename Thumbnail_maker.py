import os
from tkinter import *
import tkinter.messagebox as tkMessageBox
import webbrowser
import sys
from PIL import Image
from functools import partial


build = "0.2"

path = os.getcwd()

data = path + r"\Thumbnailmaker\data\\"

path_self = path + r"\Thumbnail_maker.py"
path_tm = path + r"\Thumbnailmaker"
path_res = path_tm + r"\Resources"
path_tn = path_tm + r"\Thumbnails"


#Variables

tutorial_url = "https://www.youtube.com/user/KoraktorXV"

#Funktions for Commands

def infobox(a):
   tkMessageBox.showinfo("INFO", a)

def add_f_1():
    global tk_from_num
    global tk_to_num
    if tk_from_num.get() + 1 < tk_to_num.get():
        tk_from_num.set(tk_from_num.get() + 1)

def add_f_10():
    global tk_from_num
    global tk_to_num
    if tk_from_num.get() + 10 < tk_to_num.get():
        tk_from_num.set(tk_from_num.get() + 10)

def add_f_100():
    global tk_from_num
    global tk_to_num
    if tk_from_num.get() + 100 < tk_to_num.get():
        tk_from_num.set(tk_from_num.get() + 100)

def sub_f_1():
    global tk_from_num
    if tk_from_num.get() >= 0 and tk_from_num.get()-1 >= 0:
        tk_from_num.set(tk_from_num.get() - 1)

def sub_f_10():
    global tk_from_num
    if tk_from_num.get() >= 0 and tk_from_num.get()-10 >= 0:
        tk_from_num.set(tk_from_num.get() - 10)

def sub_f_100():
    global tk_from_num
    if tk_from_num.get() >= 0 and tk_from_num.get()-100 >= 0:
        tk_from_num.set(tk_from_num.get() - 100)



def add_t_1():
    global tk_to_num
    tk_to_num.set(tk_to_num.get() + 1)

def add_t_10():
    global tk_to_num
    tk_to_num.set(tk_to_num.get() + 10)

def add_t_100():
    global tk_to_num
    tk_to_num.set(tk_to_num.get() + 100)

def sub_t_1():
    global tk_to_num
    if tk_to_num.get() >= 0 and tk_to_num.get()-1 > 0:
        tk_to_num.set(tk_to_num.get() - 1)

def sub_t_10():
    global tk_to_num
    if tk_to_num.get() >= 0 and tk_to_num.get()-10 > 0:
        tk_to_num.set(tk_to_num.get() - 10)

def sub_t_100():
    global tk_to_num
    if tk_to_num.get() >= 0 and tk_to_num.get()-100 > 0:
        tk_to_num.set(tk_to_num.get() - 100)


def tut():
    webbrowser.open("https://www.youtube.com/user/KoraktorXV")

def tnm():

    start = tk_from_num.get()
    end = tk_to_num.get()
    name = entry_dataname.get()

    global path
    zero = path + r"\Thumbnailmaker\Resources\Numbers\0.png"
    one = path + r"\Thumbnailmaker\Resources\Numbers\1.png"
    two = path + r"\Thumbnailmaker\Resources\Numbers\2.png"
    three = path + r"\Thumbnailmaker\Resources\Numbers\3.png"
    four = path + r"\Thumbnailmaker\Resources\Numbers\4.png"
    five = path + r"\Thumbnailmaker\Resources\Numbers\5.png"
    six = path + r"\Thumbnailmaker\Resources\Numbers\6.png"
    seven = path + r"\Thumbnailmaker\Resources\Numbers\7.png"
    eight = path + r"\Thumbnailmaker\Resources\Numbers\8.png"
    nine = path + r"\Thumbnailmaker\Resources\Numbers\9.png"
    part = path + r"\Thumbnailmaker\Resources\Part\Part.png"
    backgrund = path + r"\Thumbnailmaker\Resources\Background\Background.png"

    try:
        num_size = Image.open(zero).size
        part_size = Image.open(part).size
        bg_size = Image.open(backgrund).size
        part_pos = (0, bg_size[1] - part_size[1])

        img_0 = Image.open(zero)
        img_1 = Image.open(one)
        img_2 = Image.open(two)
        img_3 = Image.open(three)
        img_4 = Image.open(four)
        img_5 = Image.open(five)
        img_6 = Image.open(six)
        img_7 = Image.open(seven)
        img_8 = Image.open(eight)
        img_9 = Image.open(nine)
        img_part = Image.open(part)
        img_bg = Image.open(backgrund)

    except FileNotFoundError:
        infobox("A image could not been found \n posible reasons: \n wrong name \n wrong format (use PNG) \n wrong location")
        sys.exit("A image could not been found \n posible reasons: \n wrong name \n wrong format (use PNG) \n wrong location")
        root.destroy()

    cur_img_num = start

    while end >= cur_img_num:

        img_part.load()

        cur_img = Image.new("RGBA", bg_size, "black")
        cur_img.paste(img_bg, (0, 0))
        cur_img.paste(img_part, part_pos, mask=img_part.split()[3])

        num_num = 1
        for x in str(cur_img_num):
            nums = [img_0, img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8, img_9]
            cur_num = int(x)

            num = nums[cur_num]
            num.load()

            cur_img.paste(num, (part_size[0] + img_0.size[0]*num_num, bg_size[1] - num.size[1]), mask=num.split()[3])

            num_num += 1

        cur_img.save(path + "\Thumbnailmaker\Thumbnails" + "\\" + name + " "+ str(cur_img_num) + ".jpg")
        cur_img_num += 1



if os.path.isdir(path + r"\Thumbnailmaker") == False:
    #---Folder creation---
    os.makedirs(path_tm + r"\Resources")
    os.makedirs(path_res + r"\Background")
    os.makedirs(path_res + r"\Numbers")
    os.makedirs(path_res + r"\Part")
    os.makedirs(path_tm + r"\Thumbnails")


elif os.path.isdir(path + r"\Thumbnailmaker") == True:

    root = Tk()

    root.wm_title("Thumbnailmaker Version " + build)
    #root.iconbitmap(data + "icon.ico")

    tk_from_num = IntVar()
    tk_to_num = IntVar()
    tk_to_num.set(1)

    #Widgets
    #Label
    label_dataname = Label(root, text="Thumbnail name")
    label_from = Label(root, text="from")
    label_to = Label(root, text="to")
    label_from_num = Label(root, textvariable=tk_from_num)
    label_to_num = Label(root, textvariable=tk_to_num)

    #Entrys
    entry_dataname = Entry(root)

    #Buttons
    button_create = Button(text="Create", command=tnm)
    button_tutorial = Button(text="Tutorial", command=tut)

    f_p1= Button(text="+1", command=add_f_1)
    f_p10= Button(text="+10", command=add_f_10)
    f_p100= Button(text="+100", command=add_f_100)
    f_m1= Button(text="-1", command=sub_f_1)
    f_m10= Button(text="-10", command=sub_f_10)
    f_m100= Button(text="-100", command=sub_f_100)

    t_p1= Button(text="+1", command=add_t_1)
    t_p10= Button(text="+10", command=add_t_10)
    t_p100= Button(text="+100", command=add_t_100)
    t_m1= Button(text="-1", command=sub_t_1)
    t_m10= Button(text="-10", command=sub_t_10)
    t_m100= Button(text="-100", command=sub_t_100)

    #griding
    label_dataname.grid(row=0)
    entry_dataname.grid(row=0, column=1, columnspan=7, ipadx=88, sticky=E)

    label_from.grid(row=1, column=0)
    f_p1.grid(row=1, column=1)
    f_p10.grid(row=1, column=2)
    f_p100.grid(row=1, column=3)
    f_m1.grid(row=1, column=4)
    f_m10.grid(row=1, column=5)
    f_m100.grid(row=1, column=6)
    label_from_num.grid(row=1, column=7)

    label_to.grid(row=2, column=0)
    t_p1.grid(row=2, column=1)
    t_p10.grid(row=2, column=2)
    t_p100.grid(row=2, column=3)
    t_m1.grid(row=2, column=4)
    t_m10.grid(row=2, column=5)
    t_m100.grid(row=2, column=6)
    label_to_num.grid(row=2, column=7)

    button_tutorial.grid(row=3, column=7)
    button_create.grid(row=3)

    root.update_idletasks()

    root.mainloop()
