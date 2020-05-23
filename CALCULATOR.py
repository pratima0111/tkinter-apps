from tkinter import *
import parser
root=Tk()
root.title('CALCULATOR')

#get the user input and place it in the input feild
i=0
def get_var(num):
    global i
    display.insert(i, num)
    i+=1
def calculate():
    try:
        entire_string = display.get()
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert('Error')

i=0
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length

def clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string)>0:
        new_sting = entire_string[ :-1]
        clear_all()
        display.insert(0, new_sting)
    else:
        clear_all()
        display.insert(0, 'Error')



#adding the input feild
display = Entry(root, bg='White', fg='Red')
display.grid(row=0, columnspan=6, sticky = W+E)

#adding buttons to the calculator
Button(root, text='1',padx=30, pady=30, bg='White', fg='Red', command=lambda: get_var(1)).grid(row=2, column=0)
Button(root, text='2',padx=30, pady=30,bg='White', fg='Red', command=lambda: get_var(2)).grid(row=2, column=1)
Button(root, text='3',padx=30, pady=30, bg='White', fg='Red', command=lambda: get_var(3)).grid(row=2, column=2)

Button(root, text='4', padx=30, pady=30, bg='White', fg='Red',command=lambda: get_var(4)).grid(row=3, column=0)
Button(root, text='5',padx=30, pady=30, bg='White', fg='Red', command=lambda: get_var(5)).grid(row=3, column=1)
Button(root, text='6', padx=30, pady=30, bg='White', fg='Red',command=lambda: get_var(6)).grid(row=3, column=2)

Button(root, text='7',padx=30, pady=30, bg='White', fg='Red', command=lambda: get_var(7)).grid(row=4, column=0)
Button(root, text='8',padx=30, pady=30, bg='White', fg='Red', command=lambda: get_var(8)).grid(row=4, column=1)
Button(root, text='9',padx=30, pady=30, bg='White', fg='Red', command=lambda: get_var(9)).grid(row=4, column=2)

Button(root, text='AC',padx=25, pady=30, bg='White', fg='Red', command=clear_all).grid(row=5, column=0)
Button(root, text='0',padx=30, pady=30, bg='White', fg='Red',command=lambda: get_var(0)).grid(row=5, column=1)
Button(root, text='=',padx=30, pady=30, bg='White', fg='Red', command = calculate).grid(row=5, column=2)

Button(root, text='+', padx=32, pady=30, bg='White', fg='Red',command =lambda: get_operation('+')).grid(row=2, column=3)
Button(root, text='*',padx=34, pady=30, bg='White', fg='Red', command =lambda :get_operation('*')).grid(row=3, column=3)
Button(root, text='/',padx=34, pady=30, bg='White', fg='Red',  command =lambda :get_operation('/')).grid(row=4, column=3)
Button(root, text='-', padx=32, pady=30, bg='White', fg='Red', command =lambda :get_operation('-')).grid(row=5, column=3)


Button(root, text='pi',padx=30, pady=30,  bg='White', fg='Red', command =lambda :get_operation('3.14')).grid(row=2, column=4)
Button(root, text='%', padx=30, pady=30, bg='White', fg='Red', command =lambda :get_operation('%')).grid(row=3, column=4)
Button(root, text=' ( ',padx=30, pady=30,  bg='White', fg='Red', command =lambda: get_operation('(')).grid(row=4, column=4)
Button(root, text='exp',padx=30, pady=30,  bg='White', fg='Red', command =lambda :get_operation('**')).grid(row=5, column=4)


Button(root, text='<-', padx=30, pady=30,  bg='White', fg='Red',command= undo).grid(row=2, column=4)
Button(root, text='x!', padx=33, pady=30, bg='White', fg='Red',command=lambda:get_operation('!')).grid(row=3, column=4)
Button(root, text=' )',padx=33, pady=30, bg='White', fg='Red', command =lambda :get_operation(')')).grid(row=4, column=4)
Button(root, text='^2', padx=25, pady=30, bg='White', fg='Red', command =lambda :get_operation('**2')).grid(row=5, column=4)



root.mainloop()