import sqlite3

miConexion = sqlite3.connect("Trabajo BBDD/miBBDD")

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('Camiseta',25,'Moda')")

muchosProductos = [

    ("Patin",100,"Deportes"),
    ("Cenicero",20,"Cerámicas"),
    ("Pantalón",80,"Moda")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",muchosProductos)

miConexion.commit()

miCursor.close()


miConexion.close()