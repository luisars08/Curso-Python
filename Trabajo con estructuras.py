import queue

miCola = queue.PriorityQueue()

miCola.put((3,"Madrid"))
miCola.put((1,"Bogotá"))
miCola.put((2,"México DF"))

print(miCola.get())

print("A continicaión se imprimen los elementos restantes en la cola")

for elemento in miCola.queue:

    print(elemento)