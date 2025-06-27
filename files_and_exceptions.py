def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas = {}
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read().strip()
            pares = contenido.split(";")

            for par in pares:
                if par:
                    try:
                        producto, valor = par.split(":")
                        valor = float(valor)

                        if producto not in ventas:
                            ventas[producto] = []
                        ventas[producto].append(valor)
                    except ValueError:
                        print(f"Error en el par: '{par}', se ignora.")
    except FileNotFoundError:
        print(f"'{nombre_archivo}' no fue encontrado.")
        raise  # Importante capturarlo
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        return None


    return ventas
    


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto, montos in ventas.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")


# Ejemplo si se ejecuta como principal
if __name__ == "__main__":
    archivo = "datos.txt"
    try:
        ventas = read_file_to_dict(archivo)
        if ventas:
            process_dict(ventas)
    except FileNotFoundError:
        pass  #imprimió el mensaje en la función
