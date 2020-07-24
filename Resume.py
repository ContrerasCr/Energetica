import Funciones
import costos_transp
import fun_vehi
import fun_vent


def retorno_final(t, gamma, n1, n2, alpha, beta, pob_critica):

    n = n1+n2

    # Tupla (compra, almacenamiento)
    costo_ventiladores = fun_vent.costo_total_ventiladores(gamma, alpha, beta, t, n, pob_critica)

    # Lista de ventiladores por semana
    ventiladores_por_semana = fun_vent.vent_nece_x_semana(gamma, alpha, beta, t, n, pob_critica)

    transporte_semanal = list()
    for semana in range(len(ventiladores_por_semana)):

        value = fun_vehi.costo_vehiculo(gamma, beta, t, n1, n2, pob_critica, semana)
        transporte_semanal.append(value)

    costo_arriendo = 0
    costo_combustible = 0

    for a, b, _, _, _ in transporte_semanal:
        costo_arriendo += a
        costo_combustible += b

    datos_vehiculos_x_semana = list()
    for semana in range(len(ventiladores_por_semana)):
        # Tupla (arriendo, combustible, Cantidad Cf, Cm, Vueltas)
        costo_transporte = fun_vehi.costo_vehiculo(gamma, beta, t, n1, n2, pob_critica, semana)
        datos_vehiculos_x_semana.append(costo_transporte)

    vent_neces_transp, _ = fun_vent.vent_necesarios(t, n, alpha, beta, pob_critica)
    print(vent_neces_transp)

    ret = (costo_arriendo, costo_combustible, costo_ventiladores,
           ventiladores_por_semana, vent_neces_transp, datos_vehiculos_x_semana)
    print(ret)
    return None

# End Document
