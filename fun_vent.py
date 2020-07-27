import Funciones

# Datos


def activos_criticos(t, n, alpha, beta, pob_critica):

    casos_totales = list()
    dia = list()
    cont_act = 0

    for i in range(t+1):
        inf_crit = Funciones.infectados_criticos(i, n, alpha, beta, pob_critica)
        rec_crit = Funciones.recuperados_criticos(i, n, alpha, beta, pob_critica)
        casos_activos = inf_crit-rec_crit
        cont_act += casos_activos
        casos_totales.append(cont_act)
        dia.append(i)

    ret = casos_totales

    return ret


def vent_necesarios(t, n, alpha, beta, pob_critica):

    # Se necesitan semanalmente
    inf_diarios = activos_criticos(t, n, alpha, beta, pob_critica)
    infectados_semanales = []
    dat_diarios_separados_por_semana = list()

    if t % 7 != 0:
        t = (int(t/7)+1)*7

    for i in range(0, t+1, 7):
        try:
            inf_semanales = [inf_diarios[i],
                             inf_diarios[i+1],
                             inf_diarios[i+2],
                             inf_diarios[i+3],
                             inf_diarios[i+4],
                             inf_diarios[i+5],
                             inf_diarios[i+6],
                             ]
            semana = int(i/7)

            datos_semanales = (semana, inf_semanales)
            infectados_semanales.append(max(inf_semanales))
            dat_diarios_separados_por_semana.append(datos_semanales)

        except IndexError:
            pass

    ret = (infectados_semanales, dat_diarios_separados_por_semana)

    return ret


def costo_compra_ventilador(gamma, alpha, beta, t, n, pob_critica):

    ventiladores_compra_semanal= vent_nece_x_semana(gamma, alpha, beta, t, n, pob_critica)

    costo_ventiladores = 0

    for i in range(len(ventiladores_compra_semanal)):
        h = i*7
        costo_ventiladores += ventiladores_compra_semanal[i] * round((1/gamma)*(1/alpha)*pow(2.71828, (beta*h)/2790), 3)
    return costo_ventiladores


def costo_almacenamiento_ventilador(gamma, alpha, beta, t, n, pob_critica):

    ven_semenales, vent_por_semana = vent_necesarios(t, n, alpha, beta, pob_critica)

    cva = 0  # cantidad de ventiladores en el local actuales
    lis_vent_alm_x_dia = list()

    for i in range(len(ven_semenales)):
        if cva <= ven_semenales[i]:
            cva = ven_semenales[i]
        dia, vs = vent_por_semana[i]  # Ventiladores en uso por dia esa semana

        lis_vent_alm_x_dia.append(cva-vs[0])
        lis_vent_alm_x_dia.append(cva-vs[1])
        lis_vent_alm_x_dia.append(cva-vs[2])
        lis_vent_alm_x_dia.append(cva-vs[3])
        lis_vent_alm_x_dia.append(cva-vs[4])
        lis_vent_alm_x_dia.append(cva-vs[5])
        lis_vent_alm_x_dia.append(cva-vs[6])

    costos_almacenamieto = 0

    for tm in range(t-1):
        try:
            costos_almacenamieto += lis_vent_alm_x_dia[tm] * round((gamma*alpha * pow(2.71828, (-beta * tm) / 2790)), 4)
        except IndexError:
            costos_almacenamieto += 0

    costos_almacenamieto = round(costos_almacenamieto, 0)

    return costos_almacenamieto


def costo_total_ventiladores(gamma, alpha, beta, t, n, pob_critica):

    cost_compra = costo_compra_ventilador(gamma, alpha, beta, t, n, pob_critica)
    costo_almacenamiento = costo_almacenamiento_ventilador(gamma, alpha, beta, t, n, pob_critica)

    ret = (int(cost_compra), int(costo_almacenamiento))

    return ret


def vent_nece_x_semana(gamma, alpha, beta, t, n, pob_critica):

    vent_nece, _ = vent_necesarios(t, n, alpha, beta, pob_critica)
    vent_actuales = 0
    vent_nece_transp = list()   # Ventiladores necesarios para ser transportados por semana

    for i in range(len(vent_nece)):
        value = int(vent_nece[i] - vent_actuales)
        if value < 0:
            value = 0
        vent_nece_transp.append(value)
        vent_actuales = vent_nece[i]

    return vent_nece_transp


# End File
