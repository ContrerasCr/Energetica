import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import Funciones


root = tk.Tk()
root.title("Proyecto energetica 2020-1")
style = ttk.Style()
style.configure("BW.TLabel", justify='LEFT')
root.geometry('660x230')

# --------------Start Code Here  'Matrices'------------------------------------------------------------

# --------------Start Function 'Graficadoras'--------------------------------------------------------------------------


def graf_recuperados(t, n, alpha, betha, p, tq, tp):

    casos_diarios = list()
    dia = list()
    for i in range(0, t+1):
        rec_nor, rec_crit = Funciones.recuperados(i, n, alpha, betha, p, tq, tp)
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


def graf_recuperados_crit(t, n, alpha, betha, p, tp):

    casos_diarios = list()
    dia = list()
    for i in range(0, t+1):
        rec_crit = Funciones.recuperados_criticos(i, n, alpha, betha, p, tp)
        casos_diarios.append(rec_crit)
        dia.append(i)

    plt.ion()
    plt.figure('Recuperados Criticos')
    plt.scatter(dia, casos_diarios)
    plt.show()


def graf_infectados_crit(t, n, alpha, betha, p):

    casos_diarios = list()
    dia = list()
    for i in range(0, t+1):
        inf_crit = Funciones.infectados_criticos(i, n, alpha, betha, p)
        casos_diarios.append(inf_crit)
        dia.append(i)

    plt.ion()
    plt.figure('Infectados Criticos')
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


def grafica_activos_por_dia(t, n, alpha, betha, p, tq, tp):

    casos_tot = list()
    dia = list()
    cont_act = 0
    for i in range(0, t+1):
        activos = Funciones.activos_diario(i, n, alpha, betha, p, tq, tp)
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
# Columna 2

dia_de_evaluacion = tk.IntVar(root, value=120)
poblacion_critica = tk.DoubleVar(root, value=0.3)
parametro_de_forma = tk.DoubleVar(root, value=1.3)
parametro_de_escala = tk.DoubleVar(root, value=60)
tiempo_r_no_critico = tk.DoubleVar(root, value=21)
tamano_de_poblacion_1 = tk.DoubleVar(root, value=49721)
tamano_de_poblacion_2 = tk.DoubleVar(root, value=51195)
ruta1 = tk.DoubleVar(root, value=152.2)
ruta2 = tk.DoubleVar(root, value=348)
ruta3 = tk.DoubleVar(root, value=349)
ventilador = tk.DoubleVar(root, value=28)

# Valores


def dia_evaluacion():
    t_ = dia_de_evaluacion.get()
    return t_


def tp():
    tp_ = ventilador.get()
    return tp_


def poblacion1():
    n1_ = tamano_de_poblacion_1.get()
    return n1_


def poblacion2():
    n2_ = tamano_de_poblacion_2.get()
    return n2_


def valor_alpha():
    alpha_ = parametro_de_forma.get()
    return alpha_


def valor_beta():
    beta_ = parametro_de_escala.get()
    return beta_


def poblc_critica():
    pob_critica_ = poblacion_critica.get()
    return pob_critica_


def tiempo_de_recuperacion_no_c():
    t_no_c = tiempo_r_no_critico.get()
    return t_no_c


def recorrido_ruta1():
    ruta1_ = ruta1.get()
    return ruta1_


def recorrido_ruta2():
    ruta2_ = ruta2.get()
    return ruta2_


def recorrido_ruta3():
    ruta3_ = ruta3.get()
    return ruta3_


def pob_total():
    tamano_pop_tot = tamano_de_poblacion_1.get() + tamano_de_poblacion_2.get()
    return tamano_pop_tot

# --------------End Code Here-----------------------------------------------

x0y4 = ttk.Label(root, text="      ", style="BW.TLabel")
x0y4.grid(sticky="W", row=0, column=3)

# ----------------------------- Block's -------------------------------------------------------------

# --------------Start Code Here  'Column 0'-------------------------------------
x0y0 = ttk.Label(root, text="   ----------------------------------", style="BW.TLabel")
x0y0.grid(sticky="W", column=0, row=0)
x0y1 = ttk.Label(root, text="Horizonte de evaluacion:", style="BW.TLabel")
x0y1.grid(sticky="W", column=0, row=1)
x0y2 = ttk.Label(root, text="Poblacion critica:", style="BW.TLabel")
x0y2.grid(sticky="W", column=0, row=2)
x0y3 = ttk.Label(root, text="Parametro de forma (alfa):", style="BW.TLabel")
x0y3.grid(sticky="W", column=0, row=3)
x0y4 = ttk.Label(root, text="Parametro de escala(beta):", style="BW.TLabel")
x0y4.grid(sticky="W", column=0, row=4)
x0y5 = ttk.Label(root, text="Tiempo de recuperacion no critico:", style="BW.TLabel")
x0y5.grid(sticky="W", column=0, row=5)
x0y6 = ttk.Label(root, text="   ---------------------------------", style="BW.TLabel")
x0y6.grid(sticky="W", column=0, row=6)
x0y7 = ttk.Label(root, text="Tamaño de la poblacion 1:", style="BW.TLabel")
x0y7.grid(sticky="W", column=0, row=7)
x0y8 = ttk.Label(root, text="Tamaño de la poblacion 2:", style="BW.TLabel")
x0y8.grid(sticky="W", column=0, row=8)


x0y14 = ttk.Label(root, text='Graficos')
x0y14.grid(column=2, row=0)


x0y15 = ttk.Button(root, text='Grafica de recuperados', state=tk.NORMAL,
                   command=lambda: graf_recuperados(dia_evaluacion(), pob_total(),
                                                    valor_alpha(), valor_beta(),
                                                    poblc_critica(), tiempo_de_recuperacion_no_c(), tp()))
x0y15.grid(sticky="W", column=2, row=1)

x0y16 = ttk.Button(root, text='Grafica de recuperados criticos', state=tk.NORMAL,
                   command=lambda: graf_recuperados_crit(dia_evaluacion(), pob_total(),
                                                         valor_alpha(), valor_beta(),
                                                         poblc_critica(), tp()))
x0y16.grid(sticky="W", column=2, row=2)

x0y17 = ttk.Button(root, text='Grafica de infectados', state=tk.NORMAL,
                   command=lambda: graf_infectados(dia_evaluacion(), pob_total(),
                                                   valor_alpha(), valor_beta(),
                                                   poblc_critica()))
x0y17.grid(sticky="W", column=2, row=3)

x0y18 = ttk.Button(root, text='Grafica de infectados criticos', state=tk.NORMAL,
                   command=lambda: graf_infectados_crit(dia_evaluacion(), pob_total(),
                                                        valor_alpha(), valor_beta(),
                                                        poblc_critica()))
x0y18.grid(sticky="W", column=2, row=4)
x0y19 = ttk.Button(root, text='Casos totales', state=tk.NORMAL,
                   command=lambda: grafica_casos_totales(dia_evaluacion(), pob_total(),
                                                         valor_alpha(), valor_beta(),
                                                         poblc_critica()))
x0y19.grid(sticky="W", column=2, row=5)
x0y20 = ttk.Button(root, text='Casos activos', state=tk.NORMAL,
                   command=lambda: grafica_activos_por_dia(dia_evaluacion(), pob_total(),
                                                           valor_alpha(), valor_beta(),
                                                           poblc_critica(), tiempo_de_recuperacion_no_c(), tp()))
x0y20.grid(sticky="W", column=2, row=6)


# --------------End Code Here-----------------------------------------------

# --------------Start Code Here  'Column 1'--------------------------------

x1y0 = ttk.Label(text="----------------------------", style="BW.TLabel")
x1y0.grid(sticky="W",  column=1, row=0)
x1y1 = ttk.Entry(root, textvariable=dia_de_evaluacion)
x1y1.grid(column=1, row=1)
x1y2 = ttk.Entry(root, textvariable=poblacion_critica)
x1y2.grid(column=1, row=2)
x1y3 = ttk.Entry(root, textvariable=parametro_de_forma)
x1y3.grid(column=1, row=3)
x1y4 = ttk.Entry(root, textvariable=parametro_de_escala)
x1y4.grid(column=1, row=4)
x1y5 = ttk.Entry(root, textvariable=tiempo_r_no_critico)
x1y5.grid(column=1, row=5)
x1y6 = ttk.Label(root, text="-----------------------------", style="BW.TLabel")
x1y6.grid(sticky="W", column=1, row=6)
x1y7 = ttk.Entry(root, textvariable=tamano_de_poblacion_1)
x1y7.grid(column=1, row=7)
x1y8 = ttk.Entry(root, textvariable=tamano_de_poblacion_2)
x1y8.grid(column=1, row=8)



x1y14 = ttk.Label(root, text='Ventiladores')
x1y14.grid(column=3, row=0)
x1y15 = ttk.Radiobutton(root, text="INFINITY W4R", variable=ventilador, value=28)
x1y15.grid(sticky="W", column=3, row=1)
x1y16 = ttk.Radiobutton(root, text="Hamiltone", variable=ventilador, value=42)
x1y16.grid(sticky="W", column=3, row=2)
x1y17 = ttk.Radiobutton(root, text="GTX1060", variable=ventilador, value=56)
x1y17.grid(sticky="W", column=3, row=3)

# --------------End Code Here-----------------------------------------------


x3y19 = ttk.Label(root, text='By Volk', style="BW.TLabel")
x3y19.grid(sticky="E", column=4, row=18)

# --------------End Code Here-----------------------------------------------


root.mainloop()

# End File
