import Resume
infinity = (0.5469, 6, 28)


# --------------End Code Here  'Functions select'---------------------------------------

# t: Dia de evaluacion
# n: Tamaño de la poblacion
# alpha: Parametro de forma
# betha: Parametro de escala
# p = poblacion critica
# tp = tiempo de recuperacion critico

# --------------Start Function 'Infectados'----------------------------------------------

def infectados_criticos(t, n, alpha, betha, p):

    infectados_crit = round((10 ** -5) * p * n * pow(t, alpha) * pow(2.71828, (-t / betha)), 0)

    return infectados_crit


def infectados_normales(t, n, alpha, betha, p):

    infectados_norm = round((10 ** -5) * (1 - p) * n * pow(t, alpha) * pow(2.71828, (-t / betha)), 0)

    return infectados_norm


def infectados(t, n, alpha, betha, p):

    infect = (infectados_normales(t, n, alpha, betha, p), infectados_criticos(t, n, alpha, betha, p))

    return infect

# --------------End Function 'Infectados'-------------------------------------------------------------------------------


# --------------Start Function 'Recuperados'----------------------------------------------------------------------------

def recuperados_criticos(t, n, alpha, betha, p):

    _, _, tp = infinity

    if t >= tp:
        recuperados_norm = round(pow(10, -5) * p * n * pow((t-tp), alpha) * pow(2.71828, (-(t-tp) / betha)), 0)
    else:
        recuperados_norm = 0

    return recuperados_norm


def recuperados_normales(t, n, alpha, betha, p, tq):

    if t >= tq:
        recuperados_crit = round(pow(10, -5) * (1-p) * n * pow((t-tq), alpha) * pow(2.71828, (-(t-tq) / betha)), 0)
    else:
        recuperados_crit = 0

    return recuperados_crit


def recuperados(t, n, alpha, betha, p, tq):

    recup = (recuperados_normales(t, n, alpha, betha, p, tq), recuperados_criticos(t, n, alpha, betha, p))

    return recup


# --------------End Function 'Recuperados'------------------------------------------------------------------------------

def activos_diario(t, n, alpha, betha, p, tp):

    inf_nor, inf_crit = infectados(t, n, alpha, betha, p)
    rec_nor, rec_crit = recuperados(t, n, alpha, betha, p, tp)

    inf_tot = inf_nor + inf_crit
    rec_tot = rec_nor + rec_crit

    active = [inf_tot, rec_tot]

    return active


def activos_criticos_acumulados(t, n, alpha, betha, p, tp):

    _, inf_crit = infectados(t, n, alpha, betha, p)
    _, rec_crit = recuperados(t, n, alpha, betha, p, tp)
    activos_dia_t = 0

    for i in range(t+1):
        activos_diarios = inf_crit - rec_crit
        activos_dia_t += activos_diarios

    return activos_dia_t


def poner_punto_de_miles(value):

    value = str(value)
    lis = list(value)

    lis.reverse()
    grups = list()
    for i in range(0, len(lis), 3):
        try:
            grups.append(str(lis[i])+str(lis[i+1])+str(lis[i+2]))
        except IndexError:
            try:
                grups.append(str(lis[i]) + str(lis[i + 1]))
            except IndexError:
                grups.append(str(lis[i]))

    grups = '.'.join(grups)
    val = list(grups)
    val.reverse()
    ret = ''.join(val)
    ret = '$' + ret

    return ret


def contaminacion_total(cc, pre_comb):

    litros_totales = cc/pre_comb

    co2_producido = int(litros_totales*2.68)

    return co2_producido


def activos_diarios_acumulados(t, n, alpha, betha, p, tp):

    activos_dia_t = 0
    for i in range(t+1):
        value = activos_diario(i, n, alpha, betha, p, tp)
        inf = value[0]
        rec = value[1]
        activos_diarios = inf - rec

        if activos_diarios <0:
            activos_diarios = 0
        activos_dia_t += activos_diarios

    return activos_dia_t


# End Document
