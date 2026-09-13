import csv

def leer_datos(ruta_archivo):
    """Lee un archivo CSV y lo convierte en una lista de diccionarios."""
    datos = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append(dict(fila))
    except FileNotFoundError:
        print(f"No se encontró el archivo en la ruta: {ruta_archivo}")
    return datos

def mostrar_resumen(datos):
    """Muestra la cantidad total de registros y tres estadísticas básicas."""
    total_registros = len(datos)
    print(f"Cantidad total de registros: {total_registros}")
    
    if total_registros == 0:
        print("El conjunto de datos está vacío.")
        return

        columna_ejemplo = 'valor' 
    
    try:
        valores = [float(fila[columna_ejemplo]) for fila in datos if fila[columna_ejemplo] != '']
        if valores:
            promedio = sum(valores) / len(valores)
            maximo = max(valores)
            minimo = min(valores)
            print(f"Estadísticas para '{columna_ejemplo}':")
            print(f" - Promedio: {promedio:.2f}")
            print(f" - Máximo: {maximo}")
            print(f" - Mínimo: {minimo}")
    except KeyError:
        print(f"La columna '{columna_ejemplo}' no existe en el archivo CSV.")

if __name__ == "__main__":
    # Ajusta la ruta al archivo CSV que guardaste en tu carpeta 'data/'
    ruta = "data/tus_datos.csv"
    print(f"Leyendo datos desde {ruta}...")
    registros = leer_datos(ruta)
    mostrar_resumen(registros)

