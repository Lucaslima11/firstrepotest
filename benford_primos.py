# Aplicação da Lei de Benford para os números primos
def n_primos(n):
    divisor = 2
    primalidade = True
    lista_primos = []
    while n > 1:
        while divisor <= n and primalidade:
            i = n % divisor
            if i == 0 and divisor < n:
                primalidade = False
            divisor += 1
        if primalidade:
            lista_primos.append(n)
        primalidade = True
        divisor = 2
        n -= 1
    return lista_primos


def benford_primos(n):
    lista_primos = n_primos(n)
    d1, d2, d3, d4, d5, d6, d7, d8, d9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    exp = 1
    div_esp = 100
    for primo in lista_primos:
        while primo // 10 ** exp > 10 or primo // 10 ** exp != 0:
            if 1 <= primo // 10 ** exp <= 9:
                div_esp = primo // 10 ** exp
            exp += 1
        exp = 0
        if div_esp == 1:
            d1 += 1
        if div_esp == 2:
            d2 += 1
        if div_esp == 3:
            d3 += 1
        if div_esp == 4:
            d4 += 1
        if div_esp == 5:
            d5 += 1
        if div_esp == 6:
            d6 += 1
        if div_esp == 7:
            d7 += 1
        if div_esp == 8:
            d8 += 1
        if div_esp == 9:
            d9 += 1
        div_esp = 100

    dtotal = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    d1 /= dtotal
    d2 /= dtotal
    d3 /= dtotal
    d4 /= dtotal
    d5 /= dtotal
    d6 /= dtotal
    d7 /= dtotal
    d8 /= dtotal
    d9 /= dtotal

    return [d1, d2, d3, d4, d5, d6, d7, d8, d9]


print(benford_primos(12121))
