
def Unique_in_order(sequence):
    if not sequence:
        return []
    
    # Inicializamos la lista con el primer elemento
    unique_list = [sequence[0]]
    
    # Recorremos desde el segundo elemento
    for i in range(1, len(sequence)):
        # Si el elemento actual es diferente al anterior, lo agregamos
        if sequence[i] != sequence[i-1]:
            unique_list.append(sequence[i])
    
    return unique_list

print(Unique_in_order('AAAABBBCCDAABBB'))
print(Unique_in_order([1, 2, 2, 3, 3]))
print(Unique_in_order('ABBCcAD'))
print(Unique_in_order([]))
print(Unique_in_order('A'))     