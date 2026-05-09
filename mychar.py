
def cadena_mas_larga(lista):
    """
    Metodo que devuelve la cadena más larga de una lista de cadenas. 
    Si dos o más cadenas tienen la misma longitud, se regirá por orden alfabético
    """
    if not lista:
        return ""
    
    # recorremos cadena por cadena almacenando en max_len aquella con más caracteres
    max_len = max(len(cadena) for cadena in lista)

    # filtramos las cadenas de máxima longitud, almacenando en winners las cadenas mayor o iguales de largas
    winners = [cadena for cadena in lista if len(cadena) == max_len]

    # devolvemos la primera cadena del array por orden alfabetico
    return sorted(winners)[0]

if __name__ == "__main__":
    print("Dame 5 palaras")

    palabras = []

    for i in range(5):
        palabras.append(input(f"Palabra {i+1}:"))
    
    resultado = cadena_mas_larga(palabras)
    
    print(f"La cadena más larga es: {resultado}")