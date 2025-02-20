print("Buenos días, ¿cuánto pága usted de rente?")

renta = float( input("¿Cuánto pagas de renta? ") )

if renta<12000:
    impuesto = "7%"
elif renta>12000 and renta<18000:
    impuesto="15%"
elif renta>18000 and renta<35000:
    impuesto="21%"
elif renta>35000 and renta<70000:
    impuesto="35%"
elif renta>70000:
    impuesto="45%"
else:
    impuesto="Ocurrio un error"

print( "“A la renta " + str(renta) + " le corresponde un " + str(impuesto) + " de tipo impositivo" )