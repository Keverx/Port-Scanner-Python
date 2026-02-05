from datetime import datetime
import socket
import threading

#se usa una lista para almacenar los hallazgos y evitar conflictos al ordenar.
puertos_abiertos = []

# Funcion la cual es utilizada para la conexión con los puertos indicados. 
# si tiene exito se guarda en la lista principal.
def escaneando(ip, puerto):
    # se crea el socket (IPv4, TCP)
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # timeout de 1 segundo
    cliente.settimeout(1)
    
    try:
        # se intenta la conexión, si es exitoso devulve 0.
        resultado = cliente.connect_ex((ip, puerto))
        if resultado == 0:
            # Si está abierto, lo guardamos en la lista
            puertos_abiertos.append(puerto)
            cliente.close() 
        else:
            # si está cerrado, solo cerramos el socket
            cliente.close()
    except:
        pass # ignoramos errores de conexión para no detener el hilo.

def main():
    # Menu principal
    print("-" * 50)
    print(" ESCÁNER DE PUERTOS EN PYTHON (Modo Turbo)")
    print("-" * 50)

    # Entrada de datos del usuario
    mi_objetivo = input("Ingresa la IP o dominio: ")

    # Pedimos el rango de puertos (convertimos a entero con int())
    # se utiliza manejo de errores para que ingresen enteros en el rango de puertos
    try: 
        p_inicio = int(input("Puerto inicial (ej: 1): "))
        p_fin = int(input("Puerto final (ej: 100): "))
    except ValueError:
        print("ERROR: Debes ingresar numeros enteros para los puertos.")
        return 

    print(f"\n[*] Escaneando {mi_objetivo} desde el puerto {p_inicio} al {p_fin}...")
    print(f"Hora de inicio: {datetime.now()}")

    # Gestion de hilos
    hilos = []

    #se crea un hilo por cada puerto a escanear.
    for p in range(p_inicio, p_fin + 1): 
        hilo = threading.Thread(target=escaneando, args=(mi_objetivo, p))
        hilos.append(hilo)
        hilo.start()

    # 3. ESPERAMOS
    for hilo in hilos:
        hilo.join()

    # 4. REPORTE
    if puertos_abiertos:
        puertos_abiertos.sort()
        print(f"\n--- REPORTE FINAL ---")
        print(f"Puertos abiertos encontrados: {puertos_abiertos}")
        
        # Guardamos
        # El nombre del archivo cambia según la IP
        nombre_archivo = f"reporte_{mi_objetivo}.txt" 
        with open(nombre_archivo, "w") as archivo:
            archivo.write(f"Reporte de escaneo para: {mi_objetivo}\n")
            archivo.write(f"Fecha: {datetime.now()}\n")
            for p in puertos_abiertos:
                if p == 80:
                    archivo.write(f"Puerto {p}: ABIERTO - POSIBLE SERVIDOR WEB \n" )
                elif p == 443:
                    archivo.write(f"Puerto {p}: ABIERTO - POSIBLE SERVIDOR WEB \n")
                else:
                    archivo.write(f"Puerto {p}: ABIERTO\n")
        
        print(f"\n Reporte guardado en '{nombre_archivo}'")
    else: 
        print("\n No se encontraron puertos abiertos en ese rango.")

# "Si este archivo es el principal, ejecuta main()"
if __name__ == "__main__":
    main()
    input("\nPresiona ENTER para salir...")