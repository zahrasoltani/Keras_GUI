import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pandas as pd
import numpy as np

import warnings
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from tkinter import filedialog as fd

import pandas as pd
import numpy as np
import csv

import sklearn
from sklearn.model_selection import train_test_split

model = Sequential()

def get_file_name(file_entry):
    global file_name # inform function to assign it to external/global variable
    file_name = fd.askopenfilename(title="Select file", filetypes=(("CSV Files","*.csv"),))
    print(file_name)
    file_entry.delete(0, 'end')
    file_entry.insert(0, file_name)

def run_and_close(event=None):
    df = pd.read_csv(file_name)
    df.head()
    X = df.iloc[:,:-1]
    y = df.iloc[: , -1]
    global X_train
    global X_test
    global y_train
    global y_test
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    #msg = messagebox.showinfo("warning", "Data loaded successfully!")
    
    global show_csv
    show_csv = Toplevel(window)
    show_csv.title("your csv file")
    show_csv.geometry("950x470")
    
    col_names = ()
    for i, col_name in enumerate(col_names, start=1):
        tk.Label(show_csv, text=col_name).grid(row=3, column=i, padx=40)
    
    with open(file_name , "r", newline="") as passfile:
        reader = csv.reader(passfile)
        data = list(reader)
    
    entrieslist = []
    for i, row in enumerate(data, start=4):
        entrieslist.append(row[0])
        for col in range(1, 8):
            tk.Label(show_csv, text=row[col]).grid(row=i, column=col)

def blah():
    print(txt_train.get())
    
def ok():
    layer_name = cmb_lay.get()
    global file 
    file = open ("keras_code.txt", "a+")
    if layer_name == "Conv2D":
        filters_hp = int(filterss.get())
        strides_hp = list(stridess.get())
        kernel_size_hp = list(kernel_sizee.get())
        padding_hp = paddingg.get()
        activation_hp = activationn.get()
        file.write(f"model.add(Conv2D({filters_hp}, (int({kernel_size_hp[1]}), int({kernel_size_hp[3]})),strides=(int({strides_hp[1]}), int({strides_hp[3]})), padding= {padding_hp}, activation = {activation_hp}))\n")
        file.close()
        tree.insert('', 'end',text="1",values=("Conv2D",filters_hp, "-", padding_hp, activation_hp,kernel_size_hp,strides_hp))
        
        warning = Label(window, text="Conv2D added")
        warning.place(x=250, y=450)
    elif layer_name == "maxpool2D":
        pool_size_hp = list(pool_sizee.get())
        strides_hp = list(stridess.get())
        padding_hp = paddingg.get()
        file.write(f"model.add(MaxPooling2D((int({pool_size_hp[1]}), int({pool_size_hp[3]})), strides=(int({strides_hp[1]}), int({strides_hp[3]})), padding= {padding_hp}))\n")
        file.close()
        tree.insert('', 'end',text="2",values=("Maxpool2D","-", pool_size_hp , padding_hp, "-","-",strides_hp))
        warning = Label(window, text="maxpool2D added")
        warning.place(x=250, y=470)
    elif layer_name == "Dense":
        activation_hp = activationn.get()
        file.write(f"model.add(Dense(10,activation = {activation_hp}))\n")
        file.close()
        model.add(Dense(10,activation = activation_hp))
        warning = Label(window, text="Dense added")
        warning.place(x=250, y=490)
        tree.insert('', 'end',text="3",values=("Dense","-", "-" , "-", activation_hp ,"-", "-"))
        
    elif layer_name == "Flatten":
        model.add(Flatten())
        file.write(f"model.add(Flatten())\n")
        file.close()
        warning = Label(window, text="Flatten added")
        warning.place(x=250, y=510)
        tree.insert('', 'end',text="3",values=("Flatten","-", "-" , "-", "-" ,"-", "-"))
    


def add_layer():
    global new_layer
    new_layer = Toplevel(window)
    new_layer.title("add new layer")
    new_layer.geometry("950x470")
    
    choose_model = Label(new_layer, text="Choose your model:")
    choose_model.place(x=70, y=30)
    
    global cmb_lay
    cmb_lay =Combobox(new_layer)
    cmb_lay["values"] = ["Conv2D","maxpool2D", "Dense","Flatten"]
    cmb_lay["state"]="readonly"
    cmb_lay.current(0)
    cmb_lay.place(x=70, y= 55)
    
    global pool_sizee
    lbl = Label(new_layer, text="pool size:")
    lbl.place(x=70  , y=100)
    pool_sizee =Combobox(new_layer)
    pool_sizee["values"] = ["(1,1)","(2,2)", "(3,3)"]
    pool_sizee["state"]="readonly"
    pool_sizee.current(0)
    pool_sizee.place(x=70  , y=120 )
    
    global stridess
    lbl = Label(new_layer, text="strides:")
    lbl.place(x=70  , y=150)
    stridess =Combobox(new_layer)
    stridess["values"] = ["(1,1)","(2,2)", "(3,3)"]
    stridess["state"]="readonly"
    stridess.current(0)
    stridess.place(x=70  , y=170 )
    
    global paddingg
    lbl = Label(new_layer, text="paddings:")
    lbl.place(x=70  , y=200)
    paddingg =Combobox(new_layer)
    paddingg["values"] = ["Valid","Same"]
    paddingg["state"]="readonly"
    paddingg.current(0)
    paddingg.place(x=70  , y=220 )
    
    global activationn
    lbl = Label(new_layer, text="activation function:")
    lbl.place(x=70  , y=250)
    activationn =Combobox(new_layer)
    activationn["values"] = ["relu","sigmoid", "tanh"]
    activationn["state"]="readonly"
    activationn.current(0)
    activationn.place(x=70  , y=270 )
    
    global kernel_sizee
    lbl = Label(new_layer, text="kernel size:")
    lbl.place(x=70  , y=300)
    kernel_sizee =Combobox(new_layer)
    kernel_sizee["values"] = ["(1,1)","(2,2)", "(3,3)"]
    kernel_sizee["state"]="readonly"
    kernel_sizee.current(0)
    kernel_sizee.place(x=70  , y=320 )
    
    global filterss
    lbl = Label(new_layer, text="filters:")
    lbl.place(x=70  , y=350)
    filterss =Combobox(new_layer)
    filterss["values"] = ["32", "64"]
    filterss["state"]="readonly"
    filterss.current(0)
    filterss.place(x=70  , y=370 )
    
    btn = Button(new_layer, text="OK", command = ok)
    btn.place(x=100, y =410)
    
    
    # Add a Treeview widget
    global tree
    tree=ttk.Treeview(new_layer, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings', height=8)
    tree.place(x= 300, y = 120)
    tree.column("# 1",anchor=CENTER, stretch=NO, width=80)
    tree.heading("# 1", text="layer")
    tree.column("# 2",anchor=CENTER, stretch=NO, width=80)
    tree.heading("# 2", text="filter")
    tree.column("# 3", anchor=CENTER, stretch=NO, width=80)
    tree.heading("# 3", text="pool size")
    tree.column("# 4",anchor=CENTER, stretch=NO, width=80)
    tree.heading("# 4", text="padding")
    tree.column("# 5", anchor=CENTER, stretch=NO, width=80)
    tree.heading("# 5", text="activation")
    tree.column("# 6",anchor=CENTER, stretch=NO, width=80)
    tree.heading("# 6", text="kernel size")
    tree.column("# 7", anchor=CENTER, stretch=NO, width=80)
    tree.heading("# 7", text="stride")
    

def fit():
    file = open ("keras_code.txt", "a+")
    file.write(f"model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])\n")
    file.write(f"model.fit(X_train, y_train, epochs=10, verbose=1)\n")
    file.close()
    
def save():
    file = open ("keras_code.txt", "a+")
    file.write(f"model.save('model_saved.h5')\n")
    file.close()
    #model.save('model_saved.h5')
    
def summeryy():
    pass
    #print(model.summary())
    
def showcode():
    file.close()
    osCommandString = "keras_code.txt"
    os.system(osCommandString)
    

def execute():
    global window
    window = Tk()
    window.title("My App")
    window.geometry("680x650")
    
    entry_csv = tk.Entry(window, text="", width=50)
    entry_csv.grid(row=5, column=6, sticky='w', padx=5)
    entry_csv.place(x=170,y=100)
    
    
    label = Label(window, text="Load Data")
    label.place(x=100,y=100)
    btn = Button(window, text="Browse...", width=10, command=lambda:get_file_name(entry_csv))
    btn.place(x=485,y=99)
    
    btn = Button(window, text="Ok",     command=run_and_close, width=10)
    btn.place(x=485,y=130)
    
    
    choose_model = Label(window, text="Choose your model:")
    choose_model.place(x=110, y=220)
    
    
    cmb =Combobox(window)
    cmb["values"] = ["CNN"]
    cmb["state"]="readonly"
    cmb.current(0)
    cmb.place(x=110, y= 250)
    
    btn = Button(window, text="add layer...", command = add_layer)
    btn.place(x=110, y =320)
    
    btn = Button(window, text="Build Model", command = fit)
    btn.place(x=110, y =450)
    
    btn = Button(window, text="Save Model", command = save)
    btn.place(x=110, y =500)
    
    btn = Button(window, text="Show Code", command = showcode)
    btn.place(x=110, y =550)
    
    window.mainloop()
    



