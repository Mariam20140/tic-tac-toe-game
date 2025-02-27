from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Tic Tac Toe')
click=True
count=0

def select(b):
    global click,count
    if b['text']==" " and click==True:
        b['text']='X'
        click=False
        count+=1
        checkwon()
    elif b['text']==" " and click==False:
        b['text']='O'
        click=True
        count+=1
        checkwon()
    else:
        messagebox.showerror('Error','Please Try Again')
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    b1=Button(root,text=" ",width=6,height=3,bg='SystemButtonFace',font=('Liter',24),command=lambda:select(b1))
    b2=Button(root,text=" ",width=6,height=3,bg='SystemButtonFace',font=('Liter',24),command=lambda:select(b2))
    b3=Button(root,text=" ",width=6,height=3,bg='SystemButtonFace',font=('Liter',24),command=lambda:select(b3))

    b4=Button(root,text=" ",width=6,height=3,bg='SystemButtonFace',font=('Liter',24),command=lambda:select(b4))
    b5=Button(root,text=" ",width=6,height=3,bg='SystemButtonFace',font=('Liter',24),command=lambda:select(b5))
    b6=Button(root,text=" ",width=6,height=3,bg='SystemButtonFace',font=('Liter',24),command=lambda:select(b6))

    b7=Button(root,text=" ",width=6,height=3,bg='SystemButtonFace',font=('Liter',24),command=lambda:select(b7))
    b8=Button(root,text=" ",width=6,height=3,bg='SystemButtonFace',font=('Liter',24),command=lambda:select(b8))
    b9=Button(root,text=" ",width=6,height=3,bg='SystemButtonFace',font=('Liter',24),command=lambda:select(b9))

    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

def stop():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkwon():
    global winner
    winner=False
    if b1['text']=="X" and b2['text']=="X" and b3['text']=="X":
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        messagebox.showinfo('Game Over','X is the winner')
        winner=True
        stop()

    elif b4['text']=="X" and b5['text']=="X" and b6['text']=="X":
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        messagebox.showinfo('Game Over','X is the winner')
        winner=True
        stop()

    elif b7['text']=="X" and b8['text']=="X" and b9['text']=="X":
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        messagebox.showinfo('Game Over','X is the winner')
        winner=True
        stop()

    elif b1['text']=="X" and b4['text']=="X" and b7['text']=="X":
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        messagebox.showinfo('Game Over','X is the winner')
        winner=True
        stop()

    elif b2['text']=="X" and b5['text']=="X" and b8['text']=="X":
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        messagebox.showinfo('Game Over','X is the winner')
        winner=True
        stop()

    elif b3['text']=="X" and b6['text']=="X" and b9['text']=="X":
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        messagebox.showinfo('Game Over','X is the winner')
        winner=True
        stop()

    elif b1['text']=="X" and b5['text']=="X" and b9['text']=="X":
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        messagebox.showinfo('Game Over','X is the winner')
        winner=True
        stop()

    elif b3['text']=="X" and b5['text']=="X" and b7['text']=="X":
        b3.config(bg='red')
        b5.config(bg='red')
        b7.config(bg='red')
        messagebox.showinfo('Game Over','X is the winner')
        winner=True
        stop()

    # check for o
    if b1['text']=="O" and b2['text']=="O" and b3['text']=="O":
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        messagebox.showinfo('Game Over','O is the winner')
        winner=True
        stop()

    elif b4['text']=="O" and b5['text']=="O" and b6['text']=="O":
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        messagebox.showinfo('Game Over','O is the winner')
        winner=True
        stop()

    elif b7['text']=="O" and b8['text']=="O" and b9['text']=="O":
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        messagebox.showinfo('Game Over','O is the winner')
        winner=True
        stop()

    elif b1['text']=="O" and b4['text']=="O" and b7['text']=="O":
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        messagebox.showinfo('Game Over','O is the winner')
        winner=True
        stop()

    elif b2['text']=="O" and b5['text']=="O" and b8['text']=="O":
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        messagebox.showinfo('Game Over','O is the winner')
        winner=True
        stop()
    
    elif b3['text']=="O" and b6['text']=="O" and b9['text']=="O":
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        messagebox.showinfo('Game Over','O is the winner')
        winner=True
        stop()

    elif b3['text']=="O" and b5['text']=="O" and b7['text']=="O":
        b3.config(bg='red')
        b5.config(bg='red')
        b7.config(bg='red')
        messagebox.showinfo('Game Over','O is the winner')
        winner=True
        stop()
 
    elif b1['text']=="O" and b5['text']=="O" and b9['text']=="O":
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        messagebox.showinfo('Game Over','O is the winner')
        winner=True
        stop()

    elif b3['text']=="O" and b5['text']=="O" and b7['text']=="O":
        b3.config(bg='red')
        b5.config(bg='red')
        b7.config(bg='red')
        messagebox.showinfo('Game Over','O is the winner')
        winner=True
        stop()
    
    elif count==9 and winner==False:
        messagebox.showinfo('Game Over','It is a Tie')
reset()
menu1=Menu(root)
root.config(menu=menu1)
options=Menu(menu1,tearoff=False)
menu1.add_cascade(label='Options',menu=options)
options.add_command(label='Reset Game',command=reset)
root.mainloop()