
musicos = ["Paul McCartney","Bruce Springsteen", "Tina Turner", "Justin Bieber", "Elton Jhon"]

#def ordena_musicos(m):
    #return m.split()[1]

musicos.sort(key=lambda m:m.split()[1])

print(musicos)