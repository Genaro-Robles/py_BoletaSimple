import tkinter as tk
from tkinter import ttk as ttk
from tkinter import messagebox as mb

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Inicio")
        self.label1=ttk.Label(self.ventana1, text="Cantidad de Producto:")
        self.label1.grid(column=0, row=0, pady=6)
        self.variable1 = tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, textvariable=self.variable1)
        self.entry1.grid(column=1, row=0, pady=6, padx=4)
        self.boton = ttk.Button(self.ventana1, text="Ingresar",command=self.mostrar)
        self.boton.grid(column=0,row=1)

        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Producto 1")
        self.labelframe1.grid(column=0, row=2, padx=5, pady=10)
        self.labelframe2=ttk.LabelFrame(self.ventana1, text="Producto 2")
        self.labelframe2.grid(column=0, row=3, padx=5, pady=10)
        self.labelframe3=ttk.LabelFrame(self.ventana1, text="Producto 3")
        self.labelframe3.grid(column=0, row=4, padx=5, pady=10)
        self.labelframe4=ttk.LabelFrame(self.ventana1, text="Producto 4")
        self.labelframe4.grid(column=0, row=5, padx=5, pady=10)
        self.labelframe5=ttk.LabelFrame(self.ventana1, text="Producto 5")
        self.labelframe5.grid(column=0, row=6, padx=5, pady=10)
        self.labelframe6=ttk.LabelFrame(self.ventana1, text="Producto 6")
        self.labelframe6.grid(column=1, row=2, padx=5, pady=10)
        self.labelframe7=ttk.LabelFrame(self.ventana1, text="Producto 7")
        self.labelframe7.grid(column=1, row=3, padx=5, pady=10)
        self.labelframe8=ttk.LabelFrame(self.ventana1, text="Producto 8")
        self.labelframe8.grid(column=1, row=4, padx=5, pady=10)
        self.labelframe9=ttk.LabelFrame(self.ventana1, text="Producto 9")
        self.labelframe9.grid(column=1, row=5, padx=5, pady=10)
        self.labelframe10=ttk.LabelFrame(self.ventana1, text="Producto 10")
        self.labelframe10.grid(column=1, row=6, padx=5, pady=10)

        

        self.ventana1.mainloop()

    def P1(self):
        self.label1=ttk.Label(self.labelframe1, text="Nombre del Producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.var1= tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1,textvariable=self.var1)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.var2 = tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe1, textvariable=self.var2)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe1, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.var3 = tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe1, textvariable=self.var3)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)

    def P2(self):
        self.label1=ttk.Label(self.labelframe2, text="Nombre del Producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.var4= tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe2,textvariable=self.var4)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Cantidad:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.var5 = tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe2, textvariable=self.var5)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.var6 = tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe2, textvariable=self.var6)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)

    def P3(self):
        self.label1=ttk.Label(self.labelframe3, text="Nombre del Producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.var7= tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe3,textvariable=self.var7)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe3, text="Cantidad:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.var8 = tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe3, textvariable=self.var8)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe3, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.var9 = tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe3, textvariable=self.var9)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)

    def P4(self):
        self.label1=ttk.Label(self.labelframe4, text="Nombre del Producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.var10= tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe4,textvariable=self.var10)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe4, text="Cantidad:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.var11 = tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe4, textvariable=self.var11)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe4, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.var12 = tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe4, textvariable=self.var12)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)

    def P5(self):
        self.label1=ttk.Label(self.labelframe5, text="Nombre del Producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.var13= tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe5,textvariable=self.var13)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe5, text="Cantidad:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.var14 = tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe5, textvariable=self.var14)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe5, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.var15 = tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe5, textvariable=self.var15)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)

    def P6(self):
        self.label1=ttk.Label(self.labelframe6, text="Nombre del Producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.var16= tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe6,textvariable=self.var16)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe6, text="Cantidad:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.var17 = tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe6, textvariable=self.var17)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe6, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.var18 = tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe6, textvariable=self.var18)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)

    def P7(self):
        self.label1=ttk.Label(self.labelframe7, text="Nombre del Producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.var19= tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe7,textvariable=self.var19)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe7, text="Cantidad:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.var20 = tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe7, textvariable=self.var20)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe7, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.var21 = tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe7, textvariable=self.var21)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)

    def P8(self):
        self.label1=ttk.Label(self.labelframe8, text="Nombre del Producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.var22= tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe8,textvariable=self.var22)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe8, text="Cantidad:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.var23 = tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe8, textvariable=self.var23)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe8, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.var24 = tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe8, textvariable=self.var24)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)

    def P9(self):
        self.label1=ttk.Label(self.labelframe9, text="Nombre del Producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.var25= tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe9,textvariable=self.var25)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe9, text="Cantidad:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.var26 = tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe9, textvariable=self.var26)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe9, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.var27 = tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe9, textvariable=self.var27)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)

    def P10(self):
        self.label1=ttk.Label(self.labelframe10, text="Nombre del Producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.var28= tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe10,textvariable=self.var28)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe10, text="Cantidad:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.var29 = tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe10, textvariable=self.var29)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe10, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.var30 = tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe10, textvariable=self.var30)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)

    def mostrar(self):
        self.label1.destroy()
        self.entry1.destroy()
        self.boton.destroy() 
        
        self.botonR = ttk.Button(self.ventana1, text="Regresar", command=self.volver)
        self.botonR.grid(column=0,row=13)
        
        self.botonC = ttk.Button(self.ventana1, text="Calcular", command=self.calcular)
        self.botonC.grid(column=0,row=12)
               
        if int(self.variable1.get()) == 1:
            self.P1()
        elif int(self.variable1.get()) == 2:
            self.P1()
            self.P2()
        elif int(self.variable1.get()) == 3:
            self.P1()
            self.P2()
            self.P3()
        elif int(self.variable1.get()) == 4:
            self.P1()
            self.P2()
            self.P3()
            self.P4()
        elif int(self.variable1.get()) == 5:
            self.P1()
            self.P2()
            self.P3()
            self.P4()
            self.P5()
        elif int(self.variable1.get()) == 6:
            self.P1()
            self.P2()
            self.P3()
            self.P4()
            self.P5()
            self.P6()
        elif int(self.variable1.get()) == 7:
            self.P1()
            self.P2()
            self.P3()
            self.P4()
            self.P5()
            self.P6()
            self.P7()
        elif int(self.variable1.get()) == 8:
            self.P1()
            self.P2()
            self.P3()
            self.P4()
            self.P5()
            self.P6()
            self.P7()
            self.P8()
        elif int(self.variable1.get()) == 9:
            self.P1()
            self.P2()
            self.P3()
            self.P4()
            self.P5()
            self.P6()
            self.P7()
            self.P8()
            self.P9()
        elif int(self.variable1.get()) == 10:
            self.P1()
            self.P2()
            self.P3()
            self.P4()
            self.P5()
            self.P6()
            self.P7()
            self.P8()
            self.P9()
            self.P10()
        else:
            mb.showerror("Cuidado","La cantidad de productos ingresada no puede ser mayor a 10\n ni menor a 0. Selecciona REGRESAR para reiniciar el programa")
            self.botonC.destroy()

    def Rec1(self):
       pr1 = self.var1.get()
       cant1 = int(self.var2.get())
       pre1 = float(self.var3.get())
       subT1 = cant1*pre1
       self.igvT += subT1

       self.label1=ttk.Label(self.labelframe1, text="Nombre del Producto:")
       self.label1.grid(column=0, row=0, padx=4, pady=4)
       self.label2=ttk.Label(self.labelframe1, text=pr1)
       self.label2.grid(column=1, row=0, padx=4, pady=4)
       self.label3=ttk.Label(self.labelframe1, text="Costo:")
       self.label3.grid(column=0, row=1, padx=4, pady=4)
       self.label4=ttk.Label(self.labelframe1, text=subT1)
       self.label4.grid(column=1, row=1, padx=4, pady=4)

    def Rec2(self):
          pr2 = self.var4.get()
          cant2 = int(self.var5.get())
          pre2 = float(self.var6.get())
          subT2 = cant2*pre2
          self.igvT += subT2
          
          self.label1=ttk.Label(self.labelframe2, text="Nombre del Producto:")
          self.label1.grid(column=0, row=0, padx=4, pady=4)
          self.label2=ttk.Label(self.labelframe2, text=pr2)
          self.label2.grid(column=1, row=0, padx=4, pady=4)
          self.label3=ttk.Label(self.labelframe2, text="Costo:")
          self.label3.grid(column=0, row=1, padx=4, pady=4)
          self.label4=ttk.Label(self.labelframe2, text=subT2)
          self.label4.grid(column=1, row=1, padx=4, pady=4)

    def Rec3(self):
          pr3 = self.var7.get()
          cant3 = int(self.var8.get())
          pre3 = float(self.var9.get())
          subT3 = cant3*pre3
          self.igvT += subT3
          
          self.label1=ttk.Label(self.labelframe3, text="Nombre del Producto:")
          self.label1.grid(column=0, row=0, padx=4, pady=4)
          self.label2=ttk.Label(self.labelframe3, text=pr3)
          self.label2.grid(column=1, row=0, padx=4, pady=4)
          self.label3=ttk.Label(self.labelframe3, text="Costo:")
          self.label3.grid(column=0, row=1, padx=4, pady=4)
          self.label4=ttk.Label(self.labelframe3, text=subT3)
          self.label4.grid(column=1, row=1, padx=4, pady=4)

    def Rec4(self):
          pr4 = self.var10.get()
          cant4 = int(self.var11.get())
          pre4 = float(self.var12.get())
          subT4 = cant4*pre4
          self.igvT += subT4
          
          self.label1=ttk.Label(self.labelframe4, text="Nombre del Producto:")
          self.label1.grid(column=0, row=0, padx=4, pady=4)
          self.label2=ttk.Label(self.labelframe4, text=pr4)
          self.label2.grid(column=1, row=0, padx=4, pady=4)
          self.label3=ttk.Label(self.labelframe4, text="Costo:")
          self.label3.grid(column=0, row=1, padx=4, pady=4)
          self.label4=ttk.Label(self.labelframe4, text=subT4)
          self.label4.grid(column=1, row=1, padx=4, pady=4)

    def Rec5(self):
          pr5 = self.var13.get()
          cant5 = int(self.var14.get())
          pre5 = float(self.var15.get())
          subT5 = cant5*pre5
          self.igvT += subT5
          
          self.label1=ttk.Label(self.labelframe5, text="Nombre del Producto:")
          self.label1.grid(column=0, row=0, padx=4, pady=4)
          self.label2=ttk.Label(self.labelframe5, text=pr5)
          self.label2.grid(column=1, row=0, padx=4, pady=4)
          self.label3=ttk.Label(self.labelframe5, text="Costo:")
          self.label3.grid(column=0, row=1, padx=4, pady=4)
          self.label4=ttk.Label(self.labelframe5, text=subT5)
          self.label4.grid(column=1, row=1, padx=4, pady=4)

    def Rec6(self):
          pr6 = self.var16.get()
          cant6 = int(self.var17.get())
          pre6 = float(self.var18.get())
          subT6 = cant6*pre6
          self.igvT += subT6
          
          self.label1=ttk.Label(self.labelframe6, text="Nombre del Producto:")
          self.label1.grid(column=0, row=0, padx=4, pady=4)
          self.label2=ttk.Label(self.labelframe6, text=pr6)
          self.label2.grid(column=1, row=0, padx=4, pady=4)
          self.label3=ttk.Label(self.labelframe6, text="Costo:")
          self.label3.grid(column=0, row=1, padx=4, pady=4)
          self.label4=ttk.Label(self.labelframe6, text=subT6)
          self.label4.grid(column=1, row=1, padx=4, pady=4)

    def Rec7(self):
          pr7 = self.var19.get()
          cant7 = int(self.var20.get())
          pre7 = float(self.var21.get())
          subT7 = cant7*pre7
          self.igvT += subT7
          
          self.label1=ttk.Label(self.labelframe7, text="Nombre del Producto:")
          self.label1.grid(column=0, row=0, padx=4, pady=4)
          self.label2=ttk.Label(self.labelframe7, text=pr7)
          self.label2.grid(column=1, row=0, padx=4, pady=4)
          self.label3=ttk.Label(self.labelframe7, text="Costo:")
          self.label3.grid(column=0, row=1, padx=4, pady=4)
          self.label4=ttk.Label(self.labelframe7, text=subT7)
          self.label4.grid(column=1, row=1, padx=4, pady=4)

    def Rec8(self):
          pr8 = self.var22.get()
          cant8 = int(self.var23.get())
          pre8 = float(self.var24.get())
          subT8 = cant8*pre8
          self.igvT += subT8
          
          self.label1=ttk.Label(self.labelframe8, text="Nombre del Producto:")
          self.label1.grid(column=0, row=0, padx=4, pady=4)
          self.label2=ttk.Label(self.labelframe8, text=pr8)
          self.label2.grid(column=1, row=0, padx=4, pady=4)
          self.label3=ttk.Label(self.labelframe8, text="Costo:")
          self.label3.grid(column=0, row=1, padx=4, pady=4)
          self.label4=ttk.Label(self.labelframe8, text=subT8)
          self.label4.grid(column=1, row=1, padx=4, pady=4)

    def Rec9(self):
          pr9 = self.var25.get()
          cant9 = int(self.var26.get())
          pre9 = float(self.var27.get())
          subT9 = cant9*pre9
          self.igvT += subT9
          
          self.label1=ttk.Label(self.labelframe9, text="Nombre del Producto:")
          self.label1.grid(column=0, row=0, padx=4, pady=4)
          self.label2=ttk.Label(self.labelframe9, text=pr9)
          self.label2.grid(column=1, row=0, padx=4, pady=4)
          self.label3=ttk.Label(self.labelframe9, text="Costo:")
          self.label3.grid(column=0, row=1, padx=4, pady=4)
          self.label4=ttk.Label(self.labelframe9, text=subT9)
          self.label4.grid(column=1, row=1, padx=4, pady=4)

    def Rec10(self):
          pr10 = self.var28.get()
          cant10 = int(self.var29.get())
          pre10 = float(self.var30.get())
          subT10 = cant10*pre10
          self.igvT += subT10
          
          self.label1=ttk.Label(self.labelframe10, text="Nombre del Producto:")
          self.label1.grid(column=0, row=0, padx=4, pady=4)
          self.label2=ttk.Label(self.labelframe10, text=pr10)
          self.label2.grid(column=1, row=0, padx=4, pady=4)
          self.label3=ttk.Label(self.labelframe10, text="Costo:")
          self.label3.grid(column=0, row=1, padx=4, pady=4)
          self.label4=ttk.Label(self.labelframe10, text=subT10)
          self.label4.grid(column=1, row=1, padx=4, pady=4)


    def calcular(self):

        self.ventana2 = tk.Tk()
        self.ventana2.title("Boleta")
        self.igvT=0
        self.labelframe1=ttk.LabelFrame(self.ventana2, text="Producto 1")
        self.labelframe1.grid(column=0, row=2, padx=5, pady=10)
        self.labelframe2=ttk.LabelFrame(self.ventana2, text="Producto 2")
        self.labelframe2.grid(column=0, row=3, padx=5, pady=10)
        self.labelframe3=ttk.LabelFrame(self.ventana2, text="Producto 3")
        self.labelframe3.grid(column=0, row=4, padx=5, pady=10)
        self.labelframe4=ttk.LabelFrame(self.ventana2, text="Producto 4")
        self.labelframe4.grid(column=0, row=5, padx=5, pady=10)
        self.labelframe5=ttk.LabelFrame(self.ventana2, text="Producto 5")
        self.labelframe5.grid(column=0, row=6, padx=5, pady=10)
        self.labelframe6=ttk.LabelFrame(self.ventana2, text="Producto 6")
        self.labelframe6.grid(column=1, row=2, padx=5, pady=10)
        self.labelframe7=ttk.LabelFrame(self.ventana2, text="Producto 7")
        self.labelframe7.grid(column=1, row=3, padx=5, pady=10)
        self.labelframe8=ttk.LabelFrame(self.ventana2, text="Producto 8")
        self.labelframe8.grid(column=1, row=4, padx=5, pady=10)
        self.labelframe9=ttk.LabelFrame(self.ventana2, text="Producto 9")
        self.labelframe9.grid(column=1, row=5, padx=5, pady=10)
        self.labelframe10=ttk.LabelFrame(self.ventana2, text="Producto 10")
        self.labelframe10.grid(column=1, row=6, padx=5, pady=10)
        self.labelframe11=ttk.LabelFrame(self.ventana2, text="TOTAL")
        self.labelframe11.grid(column=0, row=7, padx=5, pady=10)
        
        self.botonR2 = ttk.Button(self.ventana2, text="Regresar", command=self.volver2)
        self.botonR2.grid(column=0,row=13)

        if int(self.variable1.get()) == 1:
            self.Rec1()
        elif int(self.variable1.get()) == 2:
            self.Rec1()
            self.Rec2()
        elif int(self.variable1.get()) == 3:
            self.Rec1()
            self.Rec2()
            self.Rec3()
        elif int(self.variable1.get()) == 4:
            self.Rec1()
            self.Rec2()
            self.Rec3()
            self.Rec4()
        elif int(self.variable1.get()) == 5:
            self.Rec1()
            self.Rec2()
            self.Rec3()
            self.Rec4()
            self.Rec5()
        elif int(self.variable1.get()) == 6:
            self.Rec1()
            self.Rec2()
            self.Rec3()
            self.Rec4()
            self.Rec5()
            self.Rec6()
        elif int(self.variable1.get()) == 7:
            self.Rec1()
            self.Rec2()
            self.Rec3()
            self.Rec4()
            self.Rec5()
            self.Rec6()
            self.Rec7()
        elif int(self.variable1.get()) == 8:
            self.Rec1()
            self.Rec2()
            self.Rec3()
            self.Rec4()
            self.Rec5()
            self.Rec6()
            self.Rec7()
            self.Rec8() 
        elif int(self.variable1.get()) == 9:
            self.Rec1()
            self.Rec2()
            self.Rec3()
            self.Rec4()
            self.Rec5()
            self.Rec6()
            self.Rec7()
            self.Rec8()
            self.Rec9()
        elif int(self.variable1.get()) == 10:
            self.Rec1()
            self.Rec2()
            self.Rec3()
            self.Rec4()
            self.Rec5()
            self.Rec6()
            self.Rec7()
            self.Rec8()
            self.Rec9()
            self.Rec10()
        
                        
        self.label1=ttk.Label(self.labelframe11, text="Total:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe11, text=self.igvT)
        self.label2.grid(column=1, row=0, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe11, text="TOTAL + IGV:")
        self.label3.grid(column=0, row=1, padx=4, pady=4)
        self.label4=ttk.Label(self.labelframe11, text=self.igvT*0.18+self.igvT)
        self.label4.grid(column=1, row=1, padx=4, pady=4)

        self.ventana1.destroy()
        self.ventana2.mainloop()

    def volver(self):
        self.ventana1.destroy()
        self.__init__()

    def volver2(self):
        self.ventana2.destroy()
        self.__init__()

aplicacion1=Aplicacion()