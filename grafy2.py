# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:23:15 2019

@author: martin412
"""

from tkinter import *
from tkinter import filedialog
import pylab 


class App():
    
    def __init__(self,master):
        self.frame=Frame(master)
        self.frame.grid()
        
        
        
        
        self.selected=IntVar()
        self.selectedmax=StringVar()
        self.selectedmin=StringVar()
        
        
        
        #okno manuální výběru
        self.manualFrame = LabelFrame(master, text="Manuální vytvoření grafu")
        self.manualFrame.grid(column=0,row=0)
        
        
        
        
        #výběr operace
        Radiobutton(self.manualFrame,text="sin",variable=self.selected, value=0).grid(column=0,row=0)
        Radiobutton(self.manualFrame,text="log",variable=self.selected, value=1).grid(column=0,row=1)
        Radiobutton(self.manualFrame,text="exp",variable=self.selected, value=2).grid(column=0,row=2)
        
        
        
        
        
        #popisky před zadávacím polem
        Label(self.manualFrame, text="Od").grid(column=1,row=0)
        Entry(self.manualFrame, textvariable=self.selectedmin,width=5).grid(column=2,row=0)
        
        Label(self.manualFrame, text="Do").grid(column=1,row=1)
        Entry(self.manualFrame, textvariable=self.selectedmax,width=5).grid(column=2,row=1)
        #vytvoření grafu z manuálně vložených hodnot
        Button(self.manualFrame, text="Vytvořit",command=self.Graf).grid(column=1,row=3)
      
        
        
        
        
        
        
        
        #vytvoření podokna pro grafy ze souboru
        self.selectedFile=StringVar()
        self.fileFrame = LabelFrame(master,text = "Graf ze souboru",padx=5,pady=5)
        self.fileFrame.grid(column=0,row=1)
        #výběr souboru
        Label(self.fileFrame,text="Vložte trasu k souboru")
        Entry(self.fileFrame, textvariable=self.selectedFile).grid(sticky=W)
        Button(self.fileFrame, text="Vyberte soubor",command=self.pickfile).grid(column=0,row=1)
        
        Button(self.fileFrame, text="Vytvořit",command=self.SouborGraf).grid(column=0,row=2)
      
        
        
        
        #okno popisků os
        self.axisFrame=LabelFrame(master, text="Popis os",padx=5,pady=5,width=10)
        self.axisFrame.grid(column=0,row=2)
        
        Label(self.axisFrame,text="Osa X").grid()
        Label(self.axisFrame,text="Osa Y").grid()
        
        #jména os
        self.Xaxis=StringVar()
        self.Yaxis=StringVar()
        
        Entry(self.axisFrame, textvariable=self.Xaxis,width=15).grid(column=1,row=0)
        Entry(self.axisFrame, textvariable=self.Yaxis,width=15).grid(column=1,row=1)
        
        #vykreslování grafu z manuálních parametrů
  
    
    def Graf(self):
        #vykreslovací pole
        x = pylab.linspace(float(self.selectedmin.get()),float(self.selectedmax.get()) ,1000)
        #výběr funkce uživatelem
        if self.selected.get()==0:
            y=pylab.sin(x)
        elif self.selected.get()==1:
            y=pylab.log10(x)
        elif self.selected.get()==2:
            y=pylab.exp(x)
            
        #samotné vykreslení
        pylab.figure()
        pylab.plot(x,y)
        pylab.xlabel(self.Xaxis.get())
        pylab.ylabel(self.Yaxis.get())
        pylab.grid(True)
        pylab.show()
        
        
        #výběr souboru pro import
    def pickfile(self):
        self.path=filedialog.askopenfilename(title="Vyberte soubor")
        self.selectedFile.set(self.path)
        
        #graf ze souboru
    def SouborGraf(self):
        #přečtení souboru
        self.f = open(self.path,"r")
        #prázdné seznamy
        self.x=[]
        self.y=[]
        
        
        
        #čte řádek po řádku
        while True:
            self.line=self.f.readline()
            if self.line=="":
                break
            self.numbers=self.line.split()
            self.x.append(float(self.numbers[0]))
            self.y.append(float(self.numbers[1]))
            
        self.f.close()
        pylab.figure()
        pylab.plot(self.x,self.y)
        pylab.xlabel(self.Xaxis.get())
        pylab.ylabel(self.Yaxis.get())
        pylab.grid(True)
        pylab.show()
        
        
root = Tk()
app = App(root)
root.mainloop()