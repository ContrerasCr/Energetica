import fun_vehi
import fun_vent


def retorno_final(t, gamma, n1, n2, alpha, beta, pob_critica, ruta1, ruta2, ruta3, pre_comb):

    n = n1+n2

    # Tupla (compra, almacenamiento)
    costo_ventiladores = fun_vent.costo_total_ventiladores(gamma, alpha, beta, t, n, pob_critica)

    # Lista de ventiladores por semana
    ventiladores_por_semana = fun_vent.vent_nece_x_semana(gamma, alpha, beta, t, n, pob_critica)

    costo_arriendo = 0
    costo_combustible = 0

    datos_vehiculos_x_semana = list()
    for semana in range(len(ventiladores_por_semana)):
        # costo_vehiculo = (costo total, costo arriendo, costo combustible, vueltas, Cf, Cm, CVt, semana)
        costo_transporte = fun_vehi.costo_vehiculo(gamma, alpha, beta, t, n1, n2, pob_critica,
                                                   semana, ruta1, ruta2, ruta3, pre_comb)
        _, a, b, _, _, _, _, _ = costo_transporte
        costo_arriendo += a
        costo_combustible += b
        datos_vehiculos_x_semana.append(costo_transporte)

    vent_neces_transp, _ = fun_vent.vent_necesarios(t, n, alpha, beta, pob_critica)

    ret = (costo_arriendo, costo_combustible, costo_ventiladores,
           ventiladores_por_semana, vent_neces_transp, datos_vehiculos_x_semana)
    # ret indica los datos totales del proyecto

    return ret

# End File

# End Document
