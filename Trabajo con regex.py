import re

codigo1 = "asdsadsdadad255"

codigo2 = "asddasd133asdasdasd"

codigo3 = "asdasd255asdasdasdasdsadddsaasd"

if re.search("255",codigo1):
    
    print("Código encontrado")

else:

    print("No se encontró el código")