from tkinter import *
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

def solver(a,b,c):
    D= b * b - 4 * a * c
    if D>=0:
        x1=(-b+sqrt(D))/(2*a)
        x2=(-b-sqrt(D))/(2*a)
        text="D =%s \n x1=%s \n x2=%s\n" %(D, x1, x2)
    elif D==0:
        x=-b/(2*a)  
        text="D=%s\nx=%s\n" %(D,x)
    else:
        text='D=%s\n Võrrandil pole juuri' % D
    return text


def inserter(value):
    output.delete("0.0",END)
    output.insert("0.0", value)

def plot_graph(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Ruutvõrrandi graafik: {}x^2 + {}x + {}'.format(a, b, c))
    plt.grid(True)
    plt.show()

def handler():
    try:
        a_val=float(a.get())
        b_val=float(b.get())
        c_val=float(c.get())
        plot_graph(a_val,b_val,c_val)
        inserter(solver(a_val, b_val, c_val))

    except ValueError:
        inserter("Sisestage kindlasti 3 numbrit.")




def prillid():
    x1 = np.arange(-9,-0.5,0.5)
    y1 = (-1/16)*(x1+5)**2 + 2
    x2 = np.arange(1,9.5,0.5)
    y2 = (-1/16)*(x2-5)**2 + 2
    x3 = np.arange(-9,-0.5,0.5)
    y3 = (1/4)*(x3+5)**2 - 3
    x4 = np.arange(1,9.5,0.5)
    y4 = (1/4)*(x4-5)**2 - 3
    x5 = np.arange(-9,-5.5,0.5)
    y5 = -(x5+7)**2 + 5
    x6 = np.arange(6,9.5,0.5)
    y6 = -(x6-7)**2 + 5
    x7 = np.arange(-1,1.5,0.5)
    y7 = -0.5*x7**2 + 1.5
    plt.figure()
    plt.plot(x1, y1,color='black') 
    plt.plot(x2, y2,color='black') 
    plt.plot(x3, y3,color='red') 
    plt.plot(x4, y4,color='red') 
    plt.plot(x5, y5,color='black') 
    plt.plot(x6, y6,color='black') 
    plt.plot(x7, y7,color='blue') 
    plt.title("Prillid")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()


def vaal():
    x1 = np.arange(0, 9.5, 0.5)
    y1 = (2/27) * x1 * x1 - 3
    x2 = np.arange(-10, 0, 0.5)
    y2 = 0.04 * x2 * x2 - 3
    x3 = np.arange(-9, -2.5, 0.5)
    y3 = (2/9) * (x3 + 6) ** 2 + 1
    x4 = np.arange(-3, 9.5, 0.5)
    y4 = (-1/12) * (x4 - 3) ** 2 + 6
    x5 = np.arange(5, 9, 0.5)
    y5 = (1/9) * (x5 - 5) ** 2 + 2
    x6 = np.arange(5, 8.5, 0.5)
    y6 = (1/8) * (x6 - 7) ** 2 + 1.5
    x7 = np.arange(-13, -8.5, 0.5)
    y7 = (-0.75) * (x7 + 11) ** 2 + 6
    x8 = np.arange(-15, -12.5, 0.5)
    y8 = (-0.5) * (x8 + 13) ** 2 + 3
    x9 = np.arange(-15, -10, 0.5)
    y9 = [1] * len(x9)
    x10 = np.arange(3, 4, 0.5)
    y10 = [3] * len(x10)
    plt.figure()
    plt.plot(x1, y1,color='blue') 
    plt.plot(x2, y2,color='blue') 
    plt.plot(x3, y3,color='black') 
    plt.plot(x4, y4,color='black') 
    plt.plot(x5, y5,color='red') 
    plt.plot(x6, y6,color='red') 
    plt.plot(x7, y7,color='yellow') 
    plt.plot(x8, y8,color='yellow') 
    plt.plot(x9, y9,color='yellow') 
    plt.plot(x10, y10)
    plt.title("Vaal")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
    

def vihmavari():
    x1 = np.arange(-12,12.5,0.5)
    y1 = (-1/18)*x1**2 + 12
    x2 = np.arange(-4,4.5,0.5)
    y2 = (-1/8)*x2**2 + 6
    x3 = np.arange(-12,-3.5,0.5)
    y3 = (-1/8)*(x3+8)**2 + 6
    x4 = np.arange(4,12.5,0.5)
    y4 = (-1/8)*(x4-8)**2 + 6
    x5 = np.arange(-4,0.2,0.5)
    y5 = 2*(x5+3)**2 - 9
    x6 = np.arange(-4,0.7,0.5)
    y6 = 1.5*(x6+3)**2 - 10
    plt.figure()
    plt.plot(x1, y1,color='cyan') 
    plt.plot(x2, y2,color='green') 
    plt.plot(x3, y3,color='red') 
    plt.plot(x4, y4,color='blue') 
    plt.plot(x5, y5,color='black') 
    plt.plot(x6, y6,color='black') 
    plt.title("Vihmavari")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()


aken=Tk()  
aken.geometry('1000x200')    
aken.iconbitmap('pild.ico')  
aken.title('Ruutvõrrandid')
aken.resizable(width=False,height=False)
frame_top=Frame(aken)
frame_bot=Frame(aken)
frame_top.pack()
frame_bot.pack()
pealkiri=Label(frame_top,bg="#fede94",fg="#ae955b",font="Arial 20",text="Ruutvõrrandi lahendamine")
pealkiri.pack(side=TOP,pady=3,padx=3)

a=Entry(frame_top,width=5,bg="#7dd8bf",fg="#407d6c",font="Arial 20")
a.pack(side=LEFT,pady=10,padx=10)
a_label=Label(frame_top,bg="#7dd8bf",fg="#407d6c",font="Arial 20",text="x**2+").pack(side=LEFT,pady=10)

b=Entry(frame_top,width=5,bg="#7dd8bf",fg="#407d6c",font="Arial 20")
b.pack(side=LEFT,pady=10)
b_label=Label(frame_top,bg="#7dd8bf",fg="#407d6c",font="Arial 20",text="2x+").pack(side=LEFT,pady=10)


c=Entry(frame_top,width=3,bg="#7dd8bf",fg="#407d6c",font="Arial 20")
c.pack(side=LEFT,pady=10,padx=10)
c_label=Label(frame_top,bg="#7dd8bf",fg="#407d6c",font="Arial 20",text="=0").pack(side=LEFT,pady=10)

nupp=Button(frame_top,text="Otsustama",command=handler,bg="#7dd8bf",fg="#407d6c",font="Arial 20").pack(side=LEFT,pady=10,padx=10)

output=Text(frame_bot,bg="#fede94",fg="#ae955b",font="Arial 20")
output.pack(expand=1,fill=BOTH,side=LEFT)

plot_button = Button(frame_top, text="Koostage graafik", command=lambda: plot_graph(float(a.get()), float(b.get()), float(c.get())), bg="#7dd8bf", fg="#407d6c", font="Arial 20")
plot_button.pack(side=LEFT, pady=10, padx=10)

vihma_radio = Button(frame_top,bg="#7dd8bf",fg="#407d6c",font="Arial 16", text="vihmavari", command=vihmavari)
vihma_radio.pack(anchor=W)

vaal_radio = Button(frame_top,bg="#7dd8bf",fg="#407d6c",font="Arial 16", text="vaal",command=vaal)
vaal_radio.pack(anchor=W)

prillid_radio = Button(frame_top,bg="#7dd8bf",fg="#407d6c",font="Arial 16", text="prillid", command=prillid)
prillid_radio.pack(anchor=W)

aken.mainloop()
