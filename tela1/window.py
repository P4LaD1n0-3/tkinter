from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("904x459")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 459,
    width = 904,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    452.0, 229.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    681.5, 246.5,
    image = entry0_img)

#Data log
entry0 = Entry(
    bd = 0,
    #f1f5ff
    bg = "#f1f5ff",
    highlightthickness = 0)

entry0.place(
    x = 525.0, y = 149,
    width = 321.0,
    height = 197)

canvas.create_text(
    559.5, 127.0,
    text = "Data Log.",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(24.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    217.5, 165.5,
    image = entry1_img)

#send to entry
entry1 = Entry(
    bd = 0,
    font="Arial 12",
    bg = "#f1f5ff",
    highlightthickness = 0)

#Send to
entry1.place(
    x = 57.0, y = 160,
    width = 321.0,
    height = 30 )


img12 = PhotoImage(file = f"img12.png")
b0 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 606, y = 366,
    width = 100,
    height = 20)


b0.place(
    x = 625, y = 372,
    
    width = 120,
    height = 40)


canvas.create_text(
    82.0, 146.0,
    text = "Send to",
    fill = "#3a7ff6",
    font = ("Roboto-Bold", int(15.0)))

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    217.5, 254.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    font="Arial 12",
    bg = "#f1f5ff",
    highlightthickness = 0)

entry2.place(
    x = 57.0, y = 250,
    width = 321.0,
    height = 30)

canvas.create_text(
    92.0, 236.6,
    text = "Recipients",
    fill = "#3a7ff6",
    font = ("Roboto-Bold", int(15.0)))

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    217.5, 354.5,
    image = entry3_img)

#entry3 = Entry(
#    bd = 0,
#    bg = "green",
#    highlightthickness = 0)

#entry3.place(
#    x = 57.0, y = 324,
#    width = 321.0,
#    height = 59)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 339, y = 344,
    width = 24,
    height = 22)

canvas.create_text(
    96.5, 339.0,
    text = "Output Path",
    fill = "#3a7ff6",
    font = ("Roboto-Bold", int(15.0)))

window.resizable(False, False)
window.mainloop()
