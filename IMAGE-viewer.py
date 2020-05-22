from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Pratima-Image-Viewer')
my_img1 = ImageTk.PhotoImage(Image.open('image/1_ITTsaiYVay6EyAwbL7wFeQ.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('image/Make-every-possible-effort-to-reach.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('image/images (1).jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('image/unnamed.jpg'))


img_list = [my_img1, my_img2, my_img3, my_img4]

status= Label(root, text='Image 1 of ' + str(len(img_list)),bd=1,  anchor=E, relief=SUNKEN)

my_label = Label(image = my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_num):
    global button_forward
    global my_label
    global button_back
    my_label.grid_forget()
    my_label=Label(image=img_list[image_num-1])
    my_label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text='Image '+str(image_num)+ 'of ' + str(len(img_list)), bd=1, anchor=E, relief=SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    button_forward = Button(root, text='>>', command= lambda: forward(image_num+1))
    button_back= Button(root, text='<<', command= lambda: back(image_num-1))
    if image_num==4:
        button_forward=Button(root, text='>>', state=DISABLED)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)




def back(image_num):
    global button_forward
    global my_label
    global button_back
    my_label.grid_forget()
    my_label = Label(image=img_list[image_num-1])
    my_label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text='Image '+str(image_num)+ 'of ' + str(len(img_list)), bd=1, anchor=E, relief=SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    button_forward = Button(root, text='>>', command=lambda: forward(image_num + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_num - 1))
    if image_num == 1:
        button_back=Button(root, text='<<', state=DISABLED)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)



button_quit = Button(root, text='Exit', command= root.quit)
button_back= Button(root, text='<<', command= back)     #noargument to back bcoz it needs to be disabled
button_forward= Button(root, text='>>', command= lambda: forward(2))        #argument is passed tp forward to go to the next button

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1, pady=20)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()