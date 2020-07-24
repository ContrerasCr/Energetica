import math


def funcion_costos(Cf, Cm, CVt1, CVt2):

    Af = 37000  # Arriendo diario Force 3500
    Am = 42000  # Arriendo diario Mercedez Benz
    Pc = 550    # Precio diesel en pesos
    Em = 25     # Km por litros de Mercedez Benz
    Ef = 15     # KM por litro de Force 3500
    d1 = 152.2  # Ruta 1 [km]
    d2 = 348    # Ruta 2 [km]
    d3 = 349    # Ruta 3 [km]
    Tvhf = 8.6  # Capacidad de equipaje de Force 3500
    Tvhm = 4.6  # Capacidad de equipaje de Mercedes Benz
    Tvt  = 0.5469  # Tamaño del ventilador
    CVt = CVt1 + CVt2  # Suma de las dos poblaciones
    alpha = int(Tvhf/Tvt)  # Cantidad maximas de ventiladores que puede llevar Force 3500
    betha = int(Tvhm/Tvt)  # Cantidad maximas de ventiladores que puede llevar Mercedez Benz

    value = vueltas_totales(Cf, Cm, CVt1, CVt2)

    if value == False:
        return False

    n, m, k = value

    Nf = 0
    Mf = 0
    Kf = 0
    Nm = 0
    Mm = 0
    Km = 0

    rango_max = 8
    if Cm == 0:
        rango_max = 15

    for nf in range(n+1):
        for nm in range(n+1):
            if (nf + nm == n) and (n != 0):
                if ((nf*alpha*Cf)+(nm*betha*Cm)) in list(range(CVt1, CVt1 + rango_max)):
                    Nf = nf
                    Nm = nm

    for mf in range(m+1):
        for mm in range(n+1):
            if (mf + mm == m) and (m != 0):
                if ((mf*alpha*Cf)+(mm*betha*Cm)) in list(range(CVt2, CVt2 + rango_max)):
                    Mf = mf
                    Mm = mm

    for kf in range(k+1):
        for km in range(n+1):
            if (kf + km == k) and (k != 0):
                if ((kf*alpha*Cf)+(km*betha*Cm)) in list(range(CVt, CVt + rango_max)):
                    Kf = kf
                    Km = km

    vueltas = (Nf, Nm, Mf, Mm, Kf, Km)


    costo_arriendo = (Af*Cf + Am*Cm)
    costo_combustible = int((Pc*((d1*Nm)+(d2*Mm)+(d3*Km)))/Em + (Pc*((d1*Nf)+(d2*Mf)+(d3*Kf)))/Ef)


    ret = (costo_arriendo, costo_combustible, vueltas)

    return ret





def vueltas_totales(Cf, Cm, CVt1, CVt2):

    Tvhf = 8.6
    Tvhm = 4.6
    Tvt  = 0.5469
    CVt = CVt1 + CVt2

    alpha = int(Tvhf/Tvt)
    betha = int(Tvhm/Tvt)

    maximo = math.ceil((CVt1/betha)) + math.ceil((CVt2/betha))
    Cf_max = math.ceil((CVt/betha))
    Cm_max = math.ceil((CVt / betha))
    n_max = math.ceil((CVt1 / betha))
    m_max = math.ceil((CVt2 / betha))
    k_max = math.ceil((CVt / betha))
    try:
        n = math.ceil(CVt1/((alpha*Cf)+(betha*Cm)))
    except ZeroDivisionError:
        n = 0

    try:
        m = math.ceil(CVt2/((alpha*Cf)+(betha*Cm)))
    except ZeroDivisionError:
        m = 0

    k = 0
    try:
        k = math.ceil((CVt/((alpha*Cf)+(betha*Cm))))
    except ZeroDivisionError:
        k = 0

    rango_max = 15
    if Cf == 0:
        rango_max = 8

    if (Cf+Cm>maximo)or(Cm>Cm_max)or(Cf > Cf_max)or(n > n_max)or(m > m_max)or(k > k_max)or(CVt<(Cf*15+Cm*8)-rango_max):

        return False

    else:
        ret = (n, m, k)

        return ret

# End Document
