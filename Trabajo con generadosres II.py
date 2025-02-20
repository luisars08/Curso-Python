def capitales_mundo(*ciudades):
    for capital in ciudades:
        for letra_capital in capital:
            yield letra_capital
        #yield capital


capitales_devuelta = capitales_mundo("Berlín", "Roma", "Bogotá", "Pekín", "Hanoi")

print(next(capitales_devuelta))

print(next(capitales_devuelta))

print(next(capitales_devuelta))