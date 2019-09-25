def rendimento(meses, juros, inv_inicial, inv_mensal) -> float:
    juro_perc = juros / 100
    if meses == 1:
        return ((1 + juro_perc) * inv_inicial)
    elif meses > 1:
        return ((rendimento((meses - 1), juros, inv_inicial, inv_mensal) + inv_mensal) * (1 + juro_perc))

def lucro(rend, meses, inv_inicial, inv_mensal):
    return rend - (inv_inicial + (meses * inv_mensal))

def lucro_perc(rend, meses, inv_inicial, inv_mensal) -> float:
    return ((lucro(rend, meses, inv_inicial, inv_mensal) / (inv_inicial + (meses * inv_mensal))) * 100)

def mostrar(rend4, rend12, lucro4, lucro12, lucroperc4, lucroperc12, meses):
    print("Entre {} euros (lucro {}E ({}%)) e {} euros (lucro {}E ({}%)) ao fim de {} mes(es)".format(rend4.__format__(".2f"), lucro4, lucroperc4, rend12.__format__(".2f"), lucro12, lucroperc12, meses))

meses = 24
inv_inicial = 100
inv_mensal = 20

rend_4 = rendimento(meses, 4, inv_inicial, inv_mensal)
rend_12 = rendimento(meses, 12, inv_inicial, inv_mensal)

lucro_4 = lucro(rend_4, meses, inv_inicial, inv_mensal).__format__(".2f")
lucro_12 = lucro(rend_12, meses, inv_inicial, inv_mensal).__format__(".2f")

lucro_perc_4 = lucro_perc(rend_4, meses, inv_inicial, inv_mensal).__format__(".2f")
lucro_perc_12 = lucro_perc(rend_12, meses, inv_inicial, inv_mensal).__format__(".2f")

mostrar(rend_4, rend_12, lucro_4, lucro_12, lucro_perc_4, lucro_perc_12, meses)
