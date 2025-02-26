import queue

miCola = queue.Queue(4)

miCola.put("Madrid")
miCola.put("Bogotá")
miCola.put("México DF")
#miCola.put("Lima")

while not miCola.empty():
    
    print(miCola.get())