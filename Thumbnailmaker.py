import os
from tkinter import *
import tkinter.messagebox as tkMessageBox
import webbrowser
import sys
from PIL import Image

build = "0.4.0"

path = os.getcwd()

data = path + r"\Thumbnailmaker\data\\"

#path_self = path + r"\Thumbnailmaker.py"
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

    global path_tn
    global path_res
    global align_var
    zero = path_res + r"\Numbers\0.png"
    one = path_res + r"\Numbers\1.png"
    two = path_res + r"\Numbers\2.png"
    three = path_res + r"\Numbers\3.png"
    four = path_res + r"\Numbers\4.png"
    five = path_res + r"\Numbers\5.png"
    six = path_res + r"\Numbers\6.png"
    seven = path_res + r"\Numbers\7.png"
    eight = path_res + r"\Numbers\8.png"
    nine = path_res + r"\Numbers\9.png"
    part = path_res + r"\Part\Part.png"
    backgrund = path_res + r"\Background\Background.png"

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
    print(cur_img_num, end)

    while end >= cur_img_num:

        img_part.load()
        nums = [img_0, img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8, img_9]
        cur_img = Image.new("RGBA", bg_size, "black")
        cur_img.paste(img_bg, (0, 0))

        #---align left---

        if align_var.get() == 0:
            cur_img.paste(img_part, part_pos, mask=img_part.split()[3])

            num_num = 0
            for x in str(cur_img_num):

                cur_num = int(x)
                num = nums[cur_num]
                #memo at me: DONT DELITE THAT LINE BELOW!
                num.load()

                cur_img.paste(num, (part_size[0] + img_0.size[0]*num_num + 30, bg_size[1] - num.size[1]), mask=num.split()[3])

                num_num += 1
        #---Center---

        if align_var.get() == 1:

            totl_len = part_size[0] + img_0.size[0]*len(str(cur_img_num)) + 30
            half_len = int(totl_len*0.5)
            half_bg_len = int(img_bg.size[0]*0.5)

            cur_img.paste(img_part, (half_bg_len - half_len, bg_size[1] - part_size[1]), mask=img_part.split()[3])

            num_num = 0
            for y in str(cur_img_num):

                cur_num = int(y)
                num = nums[cur_num]
                #memo at me: DONT DELITE THAT LINE BELOW!
                num.load()

                cur_img.paste(num, (half_bg_len - half_len + part_size[0] + 30 + img_0.size[0]*num_num, bg_size[1] - num.size[1]), mask=num.split()[3])
                num_num += 1

            print("mitte")


        #---align right---

        if align_var.get() == 2:

            totl_r_len = part_size[0] + img_0.size[0]*len(str(cur_img_num)) + 30

            cur_img.paste(img_part, (bg_size[0] - totl_r_len, bg_size[1] - part_size[1]), mask=img_part.split()[3])

            num_num = 0
            for x in str(cur_img_num):

                cur_num = int(x)
                num = nums[cur_num]
                #memo at me: DONT DELITE THAT LINE BELOW!
                num.load()

                cur_img.paste(num, (bg_size[0] - totl_r_len + part_size[0] + 30 + img_0.size[0]*num_num, bg_size[1] - num.size[1]), mask=num.split()[3])

                num_num += 1
            print("rechts")

        cur_img.save(path + "\Thumbnailmaker\Thumbnails\\" + name + " "+ str(cur_img_num) + ".jpg")
        cur_img_num += 1

    infobox("Thumbnails has been created" + "\n The Thumbnails are in: \n" + str(path_tn))


#---
#--- Start of the Programm ---
#---

if os.path.isdir(path + r"\Thumbnailmaker") == False:

    #---Folder creation---
    os.makedirs(path_res)
    os.makedirs(path_res + r"\Background")

    #---Background creation---
    HD = (1920, 1080)
    Image.new("RGBA", HD, "black").save(path_res + "\Background\Background.png")

    #---Number creation---
    os.makedirs(path_res + r"\Numbers")
    num_res = (120, 250)
    for num in range(10):
        Image.new("RGBA", num_res, "red").save(path_res + r"\Numbers\\"+ str(num) + r".png")

    #---Part creation---
    os.makedirs(path_res + r"\Part")
    part_res = (450, 250)
    Image.new("RGBA", part_res, "blue").save(path_res + "\Part\Part.png")

    #---Thumbnail folder---
    os.makedirs(path_tm + r"\Thumbnails")

    #---Finisch Info---
    infobox("Folder struktur has been creatied")


elif os.path.isdir(path + r"\Thumbnailmaker") == True:

    root = Tk()

    root.wm_title("Thumbnailgenerator Version " + build)
    #root.iconbitmap(data + "icon.ico")

    tk_from_num = IntVar()
    tk_from_num.set(1)
    tk_to_num = IntVar()
    tk_to_num.set(2)

    align_var = IntVar()
    #align_var.set(1)

    #Widgets
    #Label
    label_dataname = Label(root, text="Thumbnail name")
    label_from = Label(root, text="set start")
    label_to = Label(root, text="set end")
    label_from_num = Label(root, textvariable=tk_from_num)
    label_to_num = Label(root, textvariable=tk_to_num)

    #Entrys
    entry_dataname = Entry(root)

    #Buttons
    button_create = Button(text="Create Thumbnails", command=tnm)
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

    #radiobutton

    index = IntVar(0)

    align_left = Radiobutton(root, text="align left", value = 1, variable= index, command= lambda: align_var.set(0))
    align_center = Radiobutton(root, text="center", value = 2, variable= index, command= lambda: align_var.set(1))
    align_right = Radiobutton(root, text="align right", value = 3, variable= index, command= lambda: align_var.set(2))

    #griding
    label_dataname.grid(row=0)
    entry_dataname.grid(row=0, column=1, columnspan=7, ipadx=88, sticky=E)

    to_row = 1

    label_to.grid(row=to_row, column=0)
    t_p1.grid(row=to_row, column=1)
    t_p10.grid(row=to_row, column=2)
    t_p100.grid(row=to_row, column=3)
    t_m1.grid(row=to_row, column=4)
    t_m10.grid(row=to_row, column=5)
    t_m100.grid(row=to_row, column=6)
    label_to_num.grid(row=to_row, column=7)

    from_row = 2

    label_from.grid(row=from_row, column=0)
    f_p1.grid(row=from_row, column=1)
    f_p10.grid(row=from_row, column=2)
    f_p100.grid(row=from_row, column=3)
    f_m1.grid(row=from_row, column=4)
    f_m10.grid(row=from_row, column=5)
    f_m100.grid(row=from_row, column=6)
    label_from_num.grid(row=from_row, column=7)

    align_row = 3

    align_left.grid(row=align_row, column= 0)
    align_center.grid(row=align_row, column= 1)
    align_right.grid(row=align_row, column= 2)

    create_row = 4

    button_tutorial.grid(row=create_row, column=7)
    button_create.grid(row=create_row)

    #root.update_idletasks()

    root.mainloop()
