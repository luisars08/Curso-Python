
def abbrev_name(name):
    siglas=[]
    nsigla=[]
    for i in name.split(" "):
        may = i.capitalize()
        siglas.append(may)
    for letra in siglas:
        nm = letra[0]
        nsigla.append(nm)
    return nsigla[0] + "." + nsigla[1]


def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

name = "luis rosado"

print(abbrev_name(name))
print(abbrevName(name))