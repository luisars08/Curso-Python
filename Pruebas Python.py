def filtro_lista(lista):
   
   return [x for x in lista if isinstance(x, int)]

   

lista = [1,2,'a','b']

lista2 = [1,2,'aasf','1','123',123]

print(filtro_lista(lista2))