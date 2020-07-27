import fun_vent
import costos_transp
import math


def costo_vehiculo(gamma, alpha, beta, t, n1, n2, pob_critica, semana, ruta1, ruta2, ruta3, pre_comb):

    betha = 8
    n_tot = n1+n2

    cvt = fun_vent.vent_nece_x_semana(gamma, alpha, beta, t, n_tot, pob_critica)  # ventiladores necesarios totales
    cvt = cvt[semana]
    cf_max = math.ceil((cvt / betha))
    cm_max = math.ceil((cvt / betha))

    costs = [costos_transp.funcion_costos(cf, cm, cvt, ruta1, ruta2, ruta3, pre_comb, semana)
             for cf in range(cf_max+1)
             for cm in range(cm_max+1)
             if costos_transp.funcion_costos(cf, cm, cvt, ruta1, ruta2, ruta3, pre_comb, semana) != False]

    if len(costs) != 0:
        lowest_value = min(costs)
    else:
        lowest_value = (0, 0, 0, (0, 0, 0, 0, 0, 0), 0, 0, 0, semana)

    return lowest_value

# End Document
