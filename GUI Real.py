import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import Funciones
import Resume

root = tk.Tk()
root.title("Proyecto energetica 2020")
style = ttk.Style()
style.configure("BW.TLabel", justify='LEFT')

# --------------Start Code Here  'Matrices'------------------------------------------------------------

# --------------Start Function 'Graficadoras'--------------------------------------------------------------------------


def graf_recuperados(t, n, alpha, betha, p, tp):

    casos_diarios = list()
    dia = list()
    for i in range(0, t+1):
        rec_nor, rec_crit = Funciones.recuperados(i, n, alpha, betha, p, tp)
        rec_total = rec_nor+rec_crit
        casos_diarios.append(rec_total)
        dia.append(i)

    plt.ion()
    plt.figure('Recuperados')
    plt.scatter(dia, casos_diarios)
    plt.show()


def graf_infectados(t, n, alpha, betha, p):

    casos_diarios = list()
    dia = list()
    for i in range(0, t+1):
        inf_nor, inf_crit = Funciones.infectados(i, n, alpha, betha, p)
        inf_total = inf_nor + inf_crit
        casos_diarios.append(inf_total)
        dia.append(i)

    plt.ion()
    plt.figure('Infectados')
    plt.scatter(dia, casos_diarios)
    plt.show()


def grafica_casos_totales(t, n, alpha, betha, p):

    casos_tot = list()
    cont_casos_totales = 0
    dia = list()
    for i in range(0, t+1):
        inf_nor, inf_crit = Funciones.infectados(i, n, alpha, betha, p)
        inf_total = inf_nor + inf_crit
        cont_casos_totales += inf_total
        casos_tot.append(cont_casos_totales)
        dia.append(i)
    plt.ion()
    plt.figure('Casos totales')
    plt.scatter(dia, casos_tot)
    plt.show()


def grafica_activos_por_dia(t, n, alpha, betha, p, tp):

    casos_tot = list()
    dia = list()
    cont_act = 0
    for i in range(0, t+1):
        activos = Funciones.activos_diario(i, n, alpha, betha, p, tp)
        sum_casos_diarios = activos[0] - activos[1]
        cont_act += sum_casos_diarios
        casos_tot.append(cont_act)
        dia.append(i)

    plt.ion()
    plt.figure('Activos')
    plt.scatter(dia, casos_tot)
    plt.show()


# --------------End Function 'Graficadoras'-----------------------------------------


# --------------End Code Here------------------------------------------------------------------------------------------


# --------------Start Code Here  'Variables'---------------------------------
# (1,1)

dia_de_evaluacion = tk.IntVar(root, value=120)
poblacion_critica = tk.DoubleVar(root, value=0.3)
parametro_de_forma = tk.DoubleVar(root, value=1.3)
parametro_de_escala = tk.DoubleVar(root, value=60)
tiempo_r_no_critico = tk.DoubleVar(root, value=21)

# (2,1)
tamano_de_poblacion_1 = tk.DoubleVar(root, value=49721)
tamano_de_poblacion_2 = tk.DoubleVar(root, value=51195)
ventilador = tk.DoubleVar(value=1)

t_ = dia_de_evaluacion.get()
gamma_ = 6
n1_ = tamano_de_poblacion_1.get()
n2_ = tamano_de_poblacion_2
alpha_ = parametro_de_forma.get()
beta_ = parametro_de_escala.get()
pob_critica_ = 0.3


# Extras

#ca, cc, cv, vxs, vxstot, dat_viajes = Resume.retorno_final(t_, gamma_, n1_, n2_, alpha_, beta_, pob_critica_)

#cv, av = cv

#c_tot = ca+cc+cv+av

# --------------End Code Here-----------------------------------------------

x0y4 = ttk.Label(text="      ", style="BW.TLabel")
x0y4.grid(sticky="W", row=0, column=3)

# ----------------------------- Block's -------------------------------------------------------------

# --------------Start Code Here  'Column 0'-------------------------------------
x0y0 = ttk.Label(text="   ----------------------------------", style="BW.TLabel")
x0y0.grid(sticky="W", column=0, row=0)
x0y1 = ttk.Label(text="Dia de evaluacion:", style="BW.TLabel")
x0y1.grid(sticky="W", column=0, row=1)
x0y2 = ttk.Label(text="Poblacion critica:", style="BW.TLabel")
x0y2.grid(sticky="W", column=0, row=2)
x0y3 = ttk.Label(text="Parametro de forma (alfa):", style="BW.TLabel")
x0y3.grid(sticky="W", column=0, row=3)
x0y4 = ttk.Label(text="Parametro de escala(beta):", style="BW.TLabel")
x0y4.grid(sticky="W", column=0, row=4)
x0y5 = ttk.Label(text="Tiempo de recuperacion no critico:", style="BW.TLabel")
x0y5.grid(sticky="W", column=0, row=5)
x0y6 = ttk.Label(text="   ---------------------------------", style="BW.TLabel")
x0y6.grid(sticky="W", column=0, row=6)
x0y7 = ttk.Label(text="Tamaño de la poblacion 1:", style="BW.TLabel")
x0y7.grid(sticky="W", column=0, row=7)
x0y8 = ttk.Label(text="Tamaño de la poblacion 2:", style="BW.TLabel")
x0y8.grid(sticky="W", column=0, row=8)

x0y10 = ttk.Label(text="   ----------------------------------", style="BW.TLabel")
x0y10.grid(sticky="W", column=0, row=10)


# --------------End Code Here-----------------------------------------------

# --------------Start Code Here  'Column 1'--------------------------------

x1y0 = ttk.Label(text="----------------------------", style="BW.TLabel")
x1y0.grid(sticky="W",  column=1, row=0)
x1y1 = ttk.Entry(textvariable=dia_de_evaluacion)
x1y1.grid(column=1, row=1)
x1y2 = ttk.Entry(textvariable=poblacion_critica)
x1y2.grid(column=1, row=2)
x1y3 = ttk.Entry(textvariable=parametro_de_forma)
x1y3.grid(column=1, row=3)
x1y4 = ttk.Entry(textvariable=parametro_de_escala)
x1y4.grid(column=1, row=4)
x1y5 = ttk.Entry(textvariable=tiempo_r_no_critico)
x1y5.grid(column=1, row=5)
x1y6 = ttk.Label(text="-----------------------------", style="BW.TLabel")
x1y6.grid(sticky="W", column=1, row=6)
x1y7 = ttk.Entry(textvariable=tamano_de_poblacion_1)
x1y7.grid(column=1, row=7)
x1y8 = ttk.Entry(textvariable=tamano_de_poblacion_2)
x1y8.grid(column=1, row=8)

x1y10 = ttk.Label(text="-----------------------------", style="BW.TLabel")
x1y10.grid(column=1, row=10)
x1y11 = ttk.Label(text='Ventiladores')
x1y11.grid(column=1, row=11)
x1y12 = ttk.Radiobutton(root, text="INFINITY W4R", variable=ventilador, value=1)
x1y12.grid(sticky="W", column=1, row=12)
x1y13 = ttk.Radiobutton(root, text="Hamiltone", variable=ventilador, value=2)
x1y13.grid(sticky="W", column=1, row=13)
x1y14 = ttk.Radiobutton(root, text="GTX1060", variable=ventilador, value=3)
x1y14.grid(sticky="W", column=1, row=14)

# --------------End Code Here-----------------------------------------------

# --------------Start Code Here  'Column 2'-------------------------------------
x2y0 = ttk.Label(text="--------------------------", style="BW.TLabel")
x2y0.grid(sticky="W", column=2, row=0)
x2y1 = ttk.Label(text="Costos Totales:", style="BW.TLabel")
x2y1.grid(sticky="W", column=2, row=1)
x2y2 = ttk.Label(text="Costo Ventiladores:", style="BW.TLabel")
x2y2.grid(sticky="W", column=2, row=2)
x2y3 = ttk.Label(text="Costo Arriendo Vehiculo:", style="BW.TLabel")
x2y3.grid(sticky="W", column=2, row=3)
x2y4 = ttk.Label(text="Costo Combustible:", style="BW.TLabel")
x2y4.grid(sticky="W", column=2, row=4)
x2y5 = ttk.Label(text="Total de ventiladores:", style="BW.TLabel")
x2y5.grid(sticky="W", column=2, row=5)
x2y6 = ttk.Label(text="-------------------------", style="BW.TLabel")
x2y6.grid(sticky="W", column=2, row=6)
x2y10 = ttk.Label(text="------------------------", style="BW.TLabel")
x2y10.grid(sticky="W", column=2, row=10)

# --------------End Code Here-----------------------------------------------

# --------------Start Code Here  'Column 2'-------------------------------------
x3y0 = ttk.Label(text="--------------------------", style="BW.TLabel")
x3y0.grid(sticky="W", column=3, row=0)
x3y1 = ttk.Label(text="#Costos Totales: ", style="BW.TLabel")
x3y1.grid(sticky="W", column=3, row=1)
x3y2 = ttk.Label(text="#Costo Ventiladores:", style="BW.TLabel")
x3y2.grid(sticky="W", column=3, row=2)
x3y3 = ttk.Label(text="#Costo Arriendo Vehiculo:", style="BW.TLabel")
x3y3.grid(sticky="W", column=3, row=3)
x3y4 = ttk.Label(text="#Costo Combustible:", style="BW.TLabel")
x3y4.grid(sticky="W", column=3, row=4)
x3y5 = ttk.Label(text="#Total de ventiladores:", style="BW.TLabel")
x3y5.grid(sticky="W", column=3, row=5)
x3y6 = ttk.Label(text="-------------------------", style="BW.TLabel")
x3y6.grid(sticky="W", column=3, row=6)
x3y10 = ttk.Label(text="------------------------", style="BW.TLabel")
x3y10.grid(sticky="W", column=3, row=10)

# --------------End Code Here-----------------------------------------------

# --------------Start Code Here  'Block 4,1'-------------------------------------

x0y10 = ttk.Label(text='Graficos')
x0y10.grid(column=0, row=11)

tamano_pop_tot = tamano_de_poblacion_1.get() + tamano_de_poblacion_2.get()

calcular_NT = ttk.Button(root, text='Grafica de recuperados', state=tk.NORMAL,
                         command=lambda: graf_recuperados(dia_de_evaluacion.get(), tamano_pop_tot,
                                                          parametro_de_forma.get(), parametro_de_escala.get(),
                                                          poblacion_critica.get(), tiempo_r_no_critico.get()))
calcular_NT.grid(row=12, column=0)
calcular_NN = ttk.Button(root, text='Grafica de infectados', state=tk.NORMAL,
                         command=lambda: graf_infectados(dia_de_evaluacion.get(), tamano_pop_tot,
                                                         parametro_de_forma.get(), parametro_de_escala.get(),
                                                         poblacion_critica.get()))
calcular_NN.grid(row=13, column=0)
calcular_NO = ttk.Button(root, text='Casos totales', state=tk.NORMAL,
                         command=lambda: grafica_casos_totales(dia_de_evaluacion.get(), tamano_pop_tot,
                                                               parametro_de_forma.get(), parametro_de_escala.get(),
                                                               poblacion_critica.get()))
calcular_NO.grid(row=14, column=0)
calcular_UU = ttk.Button(root, text='Casos activos', state=tk.NORMAL,
                         command=lambda: grafica_activos_por_dia(dia_de_evaluacion.get(), tamano_pop_tot,
                                                                 parametro_de_forma.get(), parametro_de_escala.get(),
                                                                 poblacion_critica.get(), tiempo_r_no_critico.get()))
calcular_UU.grid(row=15, column=0)

extraaaa = ttk.Label(text='  ', style="BW.TLabel")
extraaaa.grid(row=16, column=0)
# --------------End Code Here-----------------------------------------------

root.mainloop()

# End File
