from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Image Viewer')
root.iconbitmap('icon/icon.ico')

img1 = ImageTk.PhotoImage(Image.open("images_for_try/1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images_for_try/2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images_for_try/3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images_for_try/4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images_for_try/5.jpg"))


image_List = [img1, img2, img3, img4, img5]
current_img = image_List[0]


img_label = Label(root, image=current_img)
img_label.grid(row=0, column=0, columnspan=3)


def forward(img_number):
    global img_label
    global next_button
    global prev_button

    img_label.grid_forget()
    img_label = Label(image=image_List[img_number-1])
    next_button = Button(
        root, text=">>", command=lambda: forward(img_number+1))
    prev_button = Button(
        root, text="<<", command=lambda: back(img_number-1))

    if img_number == 5:
        next_button = Button(root, text=">>", state=DISABLED)
    next_button.grid(row=1, column=1)
    prev_button.grid(row=1, column=0)
    img_label.grid(row=0, column=0, columnspan=3)
    status = Label(root, text="Image " + str(img_number) +
                   " of " + str(len(image_List)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(img_number):
    global img_label
    global next_button
    global prev_button

    img_label.grid_forget()
    img_label = Label(image=image_List[img_number-1])
    next_button = Button(
        root, text=">>", command=lambda: forward(img_number+1))
    prev_button = Button(
        root, text="<<", command=lambda: back(img_number-1))

    if img_number == 0:
        prev_button = Button(root, text="<<", state=DISABLED)

    next_button.grid(row=1, column=1)
    prev_button.grid(row=1, column=0)
    img_label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text="Image " + str(img_number) +
                   " of " + str(len(image_List)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


next_button = Button(root, text=">>", command=lambda: forward(2))
prev_button = Button(root, text="<<", command=back, state=DISABLED)
quit_button = Button(root, text="Quit", command=root.quit)

status = Label(root, text="Image 1 of " +
               str(len(image_List)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

next_button.grid(row=1, column=1)
prev_button.grid(row=1, column=0)
quit_button.grid(row=1, column=2)


root.mainloop()
