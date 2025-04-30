import sqlite3

miConexion = sqlite3.connect("Trabajo BBDD/miBBDD")

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('Camiseta',25,'Moda')")

miCursor.execute("SELECT * FROM PRODUCTOS")

muchosProductos = miCursor.fetchall()

for p in muchosProductos:

    print("Nombre: " , p[0] , " Precio: " , p[1] , " Categoría: " , p[2])

#miConexion.commit()

miCursor.close()


miConexion.close()