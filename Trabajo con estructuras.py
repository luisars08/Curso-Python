import queue

miCola = queue.Queue()

miCola.put("Madrid")
miCola.put("Bogotá")
miCola.put("México DF")

print(miCola.get())

print("A continicaión se imprimen los elementos restantes en la cola")

for elemento in miCola.queue:

    print(elemento)