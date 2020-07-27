import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import Funciones
import Resume


root = tk.Tk()
root.title("Proyecto energetica 2020-1")
style = ttk.Style()
style.configure("BW.TLabel", justify='LEFT')
root.geometry('730x430')

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


def graf_recuperados_crit(t, n, alpha, betha, p):

    casos_diarios = list()
    dia = list()
    for i in range(0, t+1):
        rec_crit = Funciones.recuperados_criticos(i, n, alpha, betha, p)
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
ventilador = tk.DoubleVar(root, value=1)
costo_combustible = tk.IntVar(root, value=550)


# Valores
def dia_evaluacion():
    t_ = dia_de_evaluacion.get()
    return t_


def gamma():
    gamma_ = 6
    return gamma_


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


def valor_combustible():
    costo_comb = costo_combustible.get()
    return costo_comb


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

x0y9 = ttk.Label(root, text="   ----------------------------------", style="BW.TLabel")
x0y9.grid(sticky="W", column=0, row=9)
# x0y10 = ttk.Label(root, text="Ruta 1:", style="BW.TLabel")
# x0y10.grid(sticky="W", column=0, row=10)
# x0y11 = ttk.Label(root, text="Ruta 2:", style="BW.TLabel")
# x0y11.grid(sticky="W", column=0, row=11)
x0y12 = ttk.Label(root, text="Ruta[km]:", style="BW.TLabel")
x0y12.grid(sticky="W", column=0, row=10)
x0y13 = ttk.Label(root, text="Costo Combustible:", style="BW.TLabel")
x0y13.grid(sticky="W", column=0, row=11)

x0y14 = ttk.Label(root, text='Graficos')
x0y14.grid(column=0, row=12)


x0y15 = ttk.Button(root, text='Grafica de recuperados', state=tk.NORMAL,
                   command=lambda: graf_recuperados(dia_evaluacion(), pob_total(),
                                                    valor_alpha(), valor_beta(),
                                                    poblc_critica(), tiempo_de_recuperacion_no_c()))
x0y15.grid(column=0, row=13)

x0y16 = ttk.Button(root, text='Grafica de recuperados criticos', state=tk.NORMAL,
                   command=lambda: graf_recuperados_crit(dia_evaluacion(), pob_total(),
                                                         valor_alpha(), valor_beta(),
                                                         poblc_critica()))
x0y16.grid(column=0, row=14)

x0y17 = ttk.Button(root, text='Grafica de infectados', state=tk.NORMAL,
                   command=lambda: graf_infectados(dia_evaluacion(), pob_total(),
                                                   valor_alpha(), valor_beta(),
                                                   poblc_critica()))
x0y17.grid(column=0, row=15)

x0y18 = ttk.Button(root, text='Grafica de infectados criticos', state=tk.NORMAL,
                   command=lambda: graf_infectados_crit(dia_evaluacion(), pob_total(),
                                                        valor_alpha(), valor_beta(),
                                                        poblc_critica()))
x0y18.grid(column=0, row=16)
x0y19 = ttk.Button(root, text='Casos totales', state=tk.NORMAL,
                   command=lambda: grafica_casos_totales(dia_evaluacion(), pob_total(),
                                                         valor_alpha(), valor_beta(),
                                                         poblc_critica()))
x0y19.grid(column=0, row=17)
x0y20 = ttk.Button(root, text='Casos activos', state=tk.NORMAL,
                   command=lambda: grafica_activos_por_dia(dia_evaluacion(), pob_total(),
                                                           valor_alpha(), valor_beta(),
                                                           poblc_critica(), tiempo_de_recuperacion_no_c()))
x0y20.grid(column=0, row=18)


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
x1y9 = ttk.Label(root, text="-----------------------------", style="BW.TLabel")
x1y9.grid(column=1, row=9)
# x1y10 = ttk.Entry(root, textvariable=ruta1)
# x1y10.grid(column=1, row=10)
# x1y11 = ttk.Entry(root, textvariable=ruta2)
# x1y11.grid(column=1, row=11)
x1y12 = ttk.Entry(root, textvariable=ruta3)
x1y12.grid(column=1, row=10)
x1y13 = ttk.Entry(root, textvariable=costo_combustible)
x1y13.grid(column=1, row=11)
x1y14 = ttk.Label(root, text='Ventiladores')
x1y14.grid(column=1, row=12)
x1y15 = ttk.Radiobutton(root, text="INFINITY W4R", variable=ventilador, value=1)
x1y15.grid(sticky="W", column=1, row=13)
# x1y16 = ttk.Radiobutton(root, text="Hamiltone", variable=ventilador, value=2)
# x1y16.grid(sticky="W", column=1, row=16)
# x1y17 = ttk.Radiobutton(root, text="GTX1060", variable=ventilador, value=3)
# x1y17.grid(sticky="W", column=1, row=17)

# --------------End Code Here-----------------------------------------------


# --------------Start Code Here  'Column 2'-------------------------------------
x2y0 = ttk.Label(root, text="--------------------------", style="BW.TLabel")
x2y0.grid(sticky="W", column=2, row=0)
x2y2 = ttk.Label(root, text="Costos Totales:", style="BW.TLabel")
x2y2.grid(sticky="W", column=2, row=2)
x2y3 = ttk.Label(root, text="Costo Compra Ventiladores:", style="BW.TLabel")
x2y3.grid(sticky="W", column=2, row=3)
x2y4 = ttk.Label(root, text="Costo Almacenamiento Ventiladores:", style="BW.TLabel")
x2y4.grid(sticky="W", column=2, row=4)
x2y5 = ttk.Label(root, text="Costo Arriendo Vehiculo:", style="BW.TLabel")
x2y5.grid(sticky="W", column=2, row=5)
x2y6 = ttk.Label(root, text="Costo Combustible:", style="BW.TLabel")
x2y6.grid(sticky="W", column=2, row=6)
x2y7 = ttk.Label(root, text="Total de ventiladores Necesarios:", style="BW.TLabel")
x2y7.grid(sticky="W", column=2, row=7)
x2y8 = ttk.Label(root, text="Cantidad de [kg] de CO2 producido: ", style="BW.TLabel")
x2y8.grid(sticky="W", column=2, row=8)
x2y9 = ttk.Label(root, text="------------------------", style="BW.TLabel")
x2y9.grid(sticky="W", column=2, row=9)

# --------------End Code Here-----------------------------------------------


# --------------Start Code Here  'Column 3'-------------------------------------
x3y0 = ttk.Label(root, text="--------------------------", style="BW.TLabel")
x3y0.grid(sticky="W", column=3, row=0)
x3y1 = ttk.Button(root, text='Calcular Datos', state=tk.NORMAL,
                  command=lambda: show_data(dia_evaluacion(), gamma(), poblacion1(), poblacion2(),
                                            valor_alpha(), valor_beta(), poblc_critica(), recorrido_ruta1(),
                                            recorrido_ruta2(), recorrido_ruta3(), valor_combustible()))
x3y1.grid(column=3, row=1)
x3y2 = ttk.Label(root, text="                    ", style="BW.TLabel")
x3y2.grid(sticky="W", column=3, row=2)
x3y3 = ttk.Label(root, text="                    ", style="BW.TLabel")
x3y3.grid(sticky="W", column=3, row=3)
x3y4 = ttk.Label(root, text="                    ", style="BW.TLabel")
x3y4.grid(sticky="W", column=3, row=4)
x3y5 = ttk.Label(root, text="                    ", style="BW.TLabel")
x3y5.grid(sticky="W", column=3, row=5)
x3y6 = ttk.Label(root, text="                    ", style="BW.TLabel")
x3y6.grid(sticky="W", column=3, row=6)
x3y7 = ttk.Label(root, text="                    ", style="BW.TLabel")
x3y7.grid(sticky="W", column=3, row=7)
x3y9 = ttk.Label(root, text='', style="BW.TLabel")
x3y9.grid(sticky="W", column=3, row=9)
x3y15 = ttk.Label(root, text='Generar archivo .txt con datos', style="BW.TLabel")
x3y15.grid(sticky="W", column=3, row=15)
x3y16 = ttk.Label(root, text='detallados del proyecto', style="BW.TLabel")
x3y16.grid(sticky="W", column=3, row=16)
x3y17 = ttk.Button(root, text='Generar archivo', state=tk.NORMAL,
                   command=lambda: generar_txt(dia_evaluacion(), gamma(), poblacion1(), poblacion2(),
                                               valor_alpha(), valor_beta(), poblc_critica(), recorrido_ruta1(),
                                               recorrido_ruta2(), recorrido_ruta3(), valor_combustible()))
x3y17.grid(column=3, row=17)
x3y19 = ttk.Label(root, text='By Volk', style="BW.TLabel")
x3y19.grid(sticky="E", column=3, row=18)

# --------------End Code Here-----------------------------------------------

# Funcion puesta en pantalla
# Posicion: Columna 3


def show_data(t, gamm, n1, n2, alpha, beta, pob_critica, rut1, rut2, rut3, pre_comb):

    value = Resume.retorno_final(t, gamm, n1, n2, alpha, beta, pob_critica, rut1, rut2, rut3, pre_comb)
    ca, cc, cv, vxs, vxstot, dat_viajes = value
    ccv, cav = cv
    c_tot = ca+cc+ccv+cav
    vent_totales = sum(vxs)
    co2_prod = Funciones.contaminacion_total(cc, pre_comb)

    ca = Funciones.poner_punto_de_miles(ca)
    cc = Funciones.poner_punto_de_miles(cc)
    ccv = Funciones.poner_punto_de_miles(ccv)
    cav = Funciones.poner_punto_de_miles(cav)
    c_tot = Funciones.poner_punto_de_miles(c_tot)

    # Datos en STR

    costo_arriendo_vehiculo = str(ca + '     ')
    costo_combustible = str(cc + '     ')
    costo_compra_ventiladores = str(ccv + '     ')
    costo_almacenamiento_ventiladores = str(cav + '     ')
    costo_total = str(c_tot + '     ')
    ventiladores_totales = str(vent_totales) + '     '
    co2_total = str(co2_prod) + '[kg]'

    y2 = ttk.Label(root, text=costo_total, style="BW.TLabel")
    y2.grid(sticky="W", column=3, row=2)
    y3 = ttk.Label(root, text=costo_compra_ventiladores, style="BW.TLabel")
    y3.grid(sticky="W", column=3, row=3)
    y4 = ttk.Label(root, text=costo_almacenamiento_ventiladores, style="BW.TLabel")
    y4.grid(sticky="W", column=3, row=4)
    y5 = ttk.Label(root, text=costo_arriendo_vehiculo, style="BW.TLabel")
    y5.grid(sticky="W", column=3, row=5)
    y6 = ttk.Label(root, text=costo_combustible, style="BW.TLabel")
    y6.grid(sticky="W", column=3, row=6)
    y7 = ttk.Label(root, text=ventiladores_totales, style="BW.TLabel")
    y7.grid(sticky="W", column=3, row=7)
    y8 = ttk.Label(root, text=co2_total, style="BW.TLabel")
    y8.grid(sticky="W", column=3, row=8)
    y9 = ttk.Label(root, text="-------------------------", style="BW.TLabel")
    y9.grid(sticky="W", column=3, row=9)

    return None


def generar_txt(t, gamm, n1, n2, alpha, beta, pob_critica, rut1, rut2, rut3, pre_comb):

    # value = (costo total, costo arriendo, costo combustible, vueltas, Cf, Cm, CVt, semana)
    value = Resume.retorno_final(t, gamm, n1, n2, alpha, beta, pob_critica, rut1, rut2, rut3, pre_comb)

    ca, cc, cv, vxs, vxstot, dat_veh_x_sem = value
    ccv, cav = cv
    c_tot = ca+cc+ccv+cav
    vent_totales = sum(vxs)
    rec_no_c = tiempo_de_recuperacion_no_c()

    ca = Funciones.poner_punto_de_miles(ca)
    cc = Funciones.poner_punto_de_miles(cc)
    ccv = Funciones.poner_punto_de_miles(ccv)
    cav = Funciones.poner_punto_de_miles(cav)
    c_tot = Funciones.poner_punto_de_miles(c_tot)

    # Datos del modelo

    nombre_archivo = 'Datos del modelo, horizonte ' + str(t) + ' dias' + '.txt'
    pob_1 = 'Personas en la localidad 1: ' + str(int(n1))
    pob_2 = 'Personas en la localidad 2: ' + str(int(n2))
    # rec_ruta1 = 'Recorrido de la ruta 1 [km]: ' + str(rut1) + '[km]'
    # rec_ruta2 = 'Recorrido de la ruta 2 [km]: ' + str(rut2) + '[km]'
    rec_ruta3 = 'Recorrido de la ruta 3 [km]: ' + str(rut3) + '[km]'
    poblacion_crit = 'Porcentaje de poblacion critica: ' + str(poblc_critica()) + '%'
    t_rec_nocritico = 'Tiempo de recuperacion de pacientes no criticos: ' + str(rec_no_c)
    parametros_alpha = 'Parametro de forma: ' + str(alpha)
    parametro_beta = 'Parametro de escala: ' + str(beta)

    # Costos del modelo
    costo_total = 'Gasto total del proyecto: ' + str(c_tot)
    costo_ventiladores = 'Gasto total en compra de ventiladores: ' + str(ccv)
    costo_almacenamiento = 'Gasto total en almacenamiento de ventiladores: ' + str(cav)
    costo_arriendo = 'Gasto total en arriendo de vehiculos: ' + str(ca)
    costo_combustible = 'Gasto total en combustibles: ' + str(cc)
    ventiladores_totales = 'Cantidad de ventiladores totales a comprar : ' + str(vent_totales)
    precio_combustible = 'Precio del combustible: ' + str(valor_combustible())

    file = open(nombre_archivo, "w")
    file.write("Datos del modelo de despacho de ventiladores" + '\n')
    file.write("    " + '\n')
    file.write("Parametros del modelo" + '\n')
    file.write(pob_1 + '\n')
    file.write(pob_2 + '\n')
    # file.write(rec_ruta1 + '\n')
    # file.write(rec_ruta2 + '\n')
    file.write(rec_ruta3 + '\n')
    file.write(poblacion_crit + '\n')
    file.write(t_rec_nocritico + '\n')
    file.write(parametros_alpha + '\n')
    file.write(parametro_beta + '\n')
    file.write("    " + '\n')
    file.write("Gastos totales del modelo" + '\n')
    file.write(costo_total + '\n')
    file.write(costo_ventiladores + '\n')
    file.write(costo_almacenamiento + '\n')
    file.write(costo_arriendo + '\n')
    file.write(costo_combustible + '\n')
    file.write(ventiladores_totales + '\n')
    file.write(precio_combustible + '\n')
    file.write("    " + '\n')
    file.write("Datos de transporte" + '\n')

    for i in range(len(vxs)):
        # value = (costo total, costo arriendo, costo combustible, vueltas, Cf, Cm, CVt, semana)
        datos_viaje = dat_veh_x_sem[i]
        cost_total, costo_arriendo, costo_combustible, recorridos, force, mercedes, ventiladores, semana = datos_viaje
        nf, nm, mf, mm, kf, km = recorridos

        arriendo = Funciones.poner_punto_de_miles(costo_arriendo)
        combustible = Funciones.poner_punto_de_miles(costo_combustible)

        file.write("    " + '\n')
        file.write('Semana ' + str(i+1) + '\n')
        file.write('Cantidad de ventiladores necesarios de transportar: ' + str(vxs[i]) + '\n')
        file.write('Gasto en arriendo de vehiculos: ' + str(Funciones.poner_punto_de_miles(costo_arriendo)) + '\n')
        file.write('Gasto en combustible: ' + str(Funciones.poner_punto_de_miles(costo_combustible)) + '\n')
        file.write('Cantidad de vehiculos Force 3500: ' + str(force) + '\n')
        file.write('Cantidad de vehiculos Mercedez: ' + str(mercedes) + '\n')
        file.write('"Vueltas"' + '\n')
        #file.write('Force ruta 1:    ' + str(nf) + '\n')
        #file.write('Mercedez ruta 1: ' + str(nm) + '\n')
        #file.write('Force ruta 2:    ' + str(mf) + '\n')
        #file.write('Mercedez ruta 2: ' + str(mm) + '\n')
        file.write('Force:    ' + str(kf) + '\n')
        file.write('Mercedez: ' + str(km) + '\n')

    file.close()

    nt_win = tk.Tk()
    nt_win.title('Ventana emergente')
    stilo = ttk.Style()
    stilo.configure("BW.TLabel", justify='CENTER')
    nt_win.geometry('220x100')
    a0b0 = ttk.Label(nt_win, text="                                    ", style="BW.TLabel")
    a0b0.grid(row=0, column=0)
    a1b0 = ttk.Label(nt_win, text="Se ha generado el archivo:", style="BW.TLabel")
    a1b0.grid(row=1, column=0)
    a2b0 = ttk.Label(nt_win, text=nombre_archivo, style="BW.TLabel")
    a2b0.grid(row=2, column=0)
    nt_win.mainloop()

    return None


root.mainloop()

# End File
