import math


def funcion_costos(Cf, Cm, CVt, ruta1, ruta2, ruta3, combust, semana):

    pc = combust    # Precio diesel en pesos

    value = vueltas_totales(Cf, Cm, CVt, semana, pc, ruta1, ruta2, ruta3)
    # value = (costo total, costo arriendo, costo combustible, vueltas, Cf, Cm, CVt, semana)
    # Value es la mejor opcion de esa curva de nivel
    #print(value)
    if not value:
        return False

    else:
        return value


def vueltas_totales(Cf, Cm, CVt, semana, pre_com, ruta1, ruta2, ruta3):

    arr_f = 37000  # Costo Arriendo Force
    arr_m = 42000  # Costo Arriendo Mercedez
    # pre_com   # Precio combustible
    eff_f = 13.4  # Eficiencia de Ford
    eff_m = 14.1  # Eficiencia de Mercedez
    d1 = ruta1  # Ruta 1 [km]
    d2 = ruta2  # Ruta 2 [km]
    d3 = ruta3  # Ruta 3 [km]

    alpha = 15
    betha = 8

    maximo = math.ceil(math.ceil((CVt/betha)) + math.ceil((CVt/betha))*1.2)
    Cf_max = math.ceil((CVt/alpha)*1.2)
    Cm_max = math.ceil((CVt / betha)*1.2)

    try:
        kkf = math.ceil((CVt/(alpha*Cf)))
    except ZeroDivisionError:
        kkf = 0

    try:
        kkm = math.ceil((CVt/(betha*Cm)))
    except ZeroDivisionError:
        kkm = 0

    if (Cf+Cm > maximo) or (Cm > Cm_max) or (Cf > Cf_max) or (Cf == 0 and Cm == 0):
        return False

    else:
        vector = [0, 0, 0, 0, kkf, kkm]

    vl0 = list((range(vector[0]+1)))
    vl1 = list((range(vector[1]+1)))
    vl2 = list((range(vector[2]+1)))
    vl3 = list((range(vector[3]+1)))

    vl4 = list((range(vector[4]+1)))
    vl5 = list((range(vector[5]+1)))

    # valores_vueltas_o1 = [(nf, nm, mf, mm) for nf in vl0 for nm in vl1 for mf in vl2 for mm in vl3]
    valores_vueltas_o2 = [(kf, km) for kf in vl4 for km in vl5]

    soluciones = list()

    for i in valores_vueltas_o2:

        e, f = i
        updt = ((int(CVt / 15)) * 15) + 15
        verificador = list(range(CVt, int(updt * 1.25)))

        control = [a1 * 15 + a2 * 8 for a1 in range(int(math.ceil((CVt / 15) * 1.5)) + 1) for a2 in
                   range(int(math.ceil((CVt / 8) * 1.5)) + 1) if (a1 * 15 + a2 * 8) in verificador]

        control.sort()
        cond2 = alpha * Cf * e + betha * Cm * f

        if cond2 in control:

            # print(a, b, c, d, e, f, '|', condicional, control, '|', Cf, Cm, '|', CVt, 'semana: ', semana)
            # print(condicional, control, '|', str('**********************************'), semana)

            val = [0, 0, 0, 0, e, f]
            val = tuple(val)
            costo_arriendo = (arr_f * Cf + arr_m * Cm)

            costo_combustible = int((pre_com * (Cf * d3 * e) / eff_f) + (pre_com * (d3 * f * Cm) / eff_m))

            costo_total = costo_arriendo + costo_combustible

            tupack_bb = (costo_combustible, costo_arriendo, costo_total, val, Cf, Cm, CVt, semana)

            soluciones.append(tupack_bb)

    if len(soluciones) == 0:
        return False
    else:
        best_pack = min(soluciones)
        a1,a2,a3,a4,a5,a6,a7,a8 = best_pack
        best_pack = (a3,a2,a1,a4,a5,a6,a7,a8)

        return best_pack

# End Document
