import fun_vent
import costos_transp
import math

t = 120
n = 100916
alpha = 1.3
beta = 60
t_critico = 21
pob_critica = 0.3  # p
gamma = 6


def costo_vehiculo(gamma, beta, t, n1, n2, pob_critica, semana):

    Tvhf = 8.6
    Tvhm = 4.6
    Tvt  = 0.5469

    betha = 8
    n_tot = n1+n2

    CVt1 = fun_vent.vent_nece_x_semana(gamma, alpha, beta, t, n1, pob_critica)  # ventiladores necesarios ruta 1
    CVt2 = fun_vent.vent_nece_x_semana(gamma, alpha, beta, t, n2, pob_critica)  # ventiladores necesarios ruta 1
    CVt = fun_vent.vent_nece_x_semana(gamma, alpha, beta, t, n_tot, pob_critica)  # ventiladores necesarios totales

    CVt1 = CVt1[semana]
    CVt2 = CVt2[semana]
    CVt =  CVt[semana]

    Cf_max = math.ceil((CVt / betha))
    Cm_max = math.ceil((CVt / betha))

    costs = list()

    for cf in range(Cf_max+1):
        for cm in range(Cm_max+1):

            costos = costos_transp.funcion_costos(cf, cm, CVt1, CVt2)

            if costos != False:
                arr, comb, vueltas = costos

                if comb != 0:
                    costos = (arr, comb, cf, cm, vueltas)
                    costs.append(costos)

    cost_tot = list()
    for i in range(len(costs)):

        arr, combust, _, _, _ = costs[i]

        total = arr + combust
        cost_tot.append(total)
    try:
        low_value = min(cost_tot)
        position = cost_tot.index(low_value)
        lowest_values = costs[position]
    except ValueError:
        lowest_values = (0, 0, 0, 0, (0, 0, 0, 0, 0, 0))

    return lowest_values


costo_vehiculo(gamma, beta, t, 49721, 51195, pob_critica, 4)

# End Document
