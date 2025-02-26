sistema_solar = "Mercurio,Venus,Tierra,Marte,Júpiter,Saturno,Urano,Neptuno,Plutón"

planetas = set()

for planeta in sistema_solar.split(","):
    planetas.add(planeta)

print(planetas)
print(len(planetas))