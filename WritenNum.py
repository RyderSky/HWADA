def convertir(numero):
    unidades = {
        0: 'cero', 1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco', 6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve'
    }
    excepciones = {
        10: 'diez', 11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce', 15: 'quince', 20: 'veinte', 30: 'treinta', 40: 'cuarenta', 50: 'cincuenta', 60: 'sesenta', 70: 'setenta', 80: 'ochenta', 90: 'noventa'
    }
    decenas = {
        2: 'veinti', 3: 'treinta y ', 4: 'cuarenta y ', 5: 'cincuenta y ', 6: 'sesenta y ', 7: 'setenta y ', 8: 'ochenta y ', 9: 'noventa y '
    }
    centenas = {
        1: 'ciento ', 2: 'doscientos ', 3: 'trescientos ', 4: 'cuatrocientos ', 5: 'quinientos ', 6: 'seiscientos ', 7: 'setecientos ', 8: 'ochocientos ', 9: 'novecientos '
    }
    miles = {
        1: 'mil', 1000: 'mil'
    }
    millones = {
        1: 'millón', 1000000: 'millones'
    }
    billones = {
        1: 'billones', 1000000000: 'billones'
    }
    trillones = {
        1: 'trillones', 1000000000000: 'trillones'
    }

    if numero < 10:
        return unidades[numero]
    elif numero < 16:
        return excepciones[numero]
    elif numero < 20:
        return excepciones[numero - 10] + 'i'
    elif numero < 100:
        decena = numero // 10
        unidad = numero % 10
        if unidad == 0:
            return decenas[decena]
        else:
            return decenas[decena] + unidades[unidad]
    elif numero < 1000:
        centena = numero // 100
        sobrante = numero % 100
        if sobrante == 0:
            if centena == 1:
                return 'cien'
            else:
                return centenas[centena]
        else:
            return centenas[centena] + convertir(sobrante)
    elif numero < 1000000:
        millar = numero // 1000
        sobrante = numero % 1000
        if sobrante == 0:
            return convertir(millar) + ' ' + miles[1000]
        elif sobrante < 100:
            return convertir(millar) + ' ' + miles[1000] + ' ' + convertir(sobrante)
        else:
            return convertir(millar) + ' ' + miles[1000] + ', ' + convertir(sobrante)
    elif numero < 1000000000:
        millon = numero // 1000000
        sobrante = numero % 1000000
        if sobrante == 0:
            return convertir(millon) + ' ' + millones[1000000]
        elif sobrante < 1000:
            return convertir(millon) + ' ' + millones[1000000] + ' ' + convertir(sobrante)
        else:
            return convertir(millon) + ' ' + millones[1000000] + ', ' + convertir(sobrante)
    elif numero < 1000000000000:
        billon = numero // 1000000000
        sobrante = numero % 1000000000
        if sobrante == 0:
            return convertir(billon) + ' ' + billones[1000000000]
        elif sobrante < 1000000:
            return convertir(billon) + ' ' + billones[1000000000] + ' ' + convertir(sobrante)
        else:
            return convertir(billon) + ' ' + billones[1000000000] + ', ' + convertir(sobrante)
    elif numero < 1000000000000000:
        trillon = numero // 1000000000000
        sobrante = numero % 1000000000000
        if sobrante == 0:
            return convertir(trillon) + ' ' + trillones[1000000000000]
        elif sobrante < 1000000000:
            return convertir(trillon) + ' ' + trillones[1000000000000] + ' ' + convertir(sobrante)
        else:
            return convertir(trillon) + ' ' + trillones[1000000000000] + ', ' + convertir(sobrante)


numero = eval(input("Ingrese un valor numérico entre 0 y 1 trillón: "))
print(convertir(numero))