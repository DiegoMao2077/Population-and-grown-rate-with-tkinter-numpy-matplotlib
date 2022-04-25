import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
lista_Po = []
lista_n = []

def Start():
    # ----------------------------------------------------------------# Interface Desing: "Variable"
    lamda = float(LambdaEntry.get())
    Po=float(PopulationEntry.get())
    n=int(TimeEntry.get())
    lista_Po.append(Po)
    lista_n.append(n)
    # ----------------------------------------------------------------# Interface Desing: "Variable"
    #----------------------------------------------------------------# Exercise
    for i in range(n):
        if i == 0:
            Pn = lamda * (Po) * (1 - (Po))
            lista_Po.append(Pn)
        else:
            Pn = lamda * (lista_Po[i] * (1 - (lista_Po[i])))
            lista_Po.append(round(Pn, 4))
        lista_n.append(i)
    # ----------------------------------------------------------------# Exercise
    # ----------------------------------------------------------------# Plot
    x = np.array(range(n + 1))
    y = np.zeros(len(x))
    for i in range(len(lista_Po)):
        y[i] = lista_Po[i]
    print(x, y)
    plt.plot(x, y, 'o')
    plt.plot(x, y, 'o-')
    plt.title('Function: P(t)')
    plt.xlabel('t')
    plt.ylabel('P')
    plt.show()
    # ----------------------------------------------------------------# Plot

# ----------------------------------------------------------------# Interface Desing
root = Tk()
root.title("Population and Grown Rate")
root.geometry("500x300")

Lambda = Label(root,text="Lambda (λ)",font="arial 15")
Lambda.pack()
Population = Label(root,text="Population (Po)", font="arial 15")
Population.pack()
Time = Label(root,text="Time (n)", font="arial 15")
Time.pack()

Lambda.place(x=50,y=20)
Population.place(x=50,y=90)
Time.place(x=50,y=160)

LambdaValue=StringVar()
PopulationValue=StringVar()
TimeValue=StringVar()

LambdaEntry = Entry(root,textvariable=LambdaValue,font="arial 20",width=8)
LambdaEntry.pack()
PopulationEntry = Entry(root,textvariable=PopulationValue,font="arial 20",width=8)
PopulationEntry.pack()
TimeEntry = Entry(root,textvariable=TimeValue,font="arial 20",width=8)
TimeEntry.pack()

LambdaEntry.place(x=200,y=20)
PopulationEntry.place(x=200,y=90)
TimeEntry.place(x=200,y=160)

Button(text="Start",font="arial 15",command=Start).place(x=350,y=20)
Button(text="Exit",command=lambda:exit(),font="arial 15",width=8).place(x=350,y=90)

root.mainloop()
# ----------------------------------------------------------------# Interface Desing