import subprocess
import os
import re


def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')


def mostrar_menu():
    print("\n🕸️ EvilLimiter - Menú interactivo")
    print("1 - Escanear red (scan)")
    print("2 - Listar dispositivos detectados (list + tipo)")
    print("3 - Bloquear dispositivo (block)")
    print("4 - Limitar ancho de banda (limit)")
    print("5 - Liberar dispositivo (free)")
    print("6 - Salir")


def ejecutar_evillimiter(comando):
    full_cmd = f"sudo evillimiter -c \"{comando}\""
    subprocess.run(full_cmd, shell=True)


def obtener_lista_dispositivos():
    print("\n📋 Obteniendo lista de dispositivos...\n")
    resultado = subprocess.run(
        "sudo evillimiter -c \"list\"", shell=True, capture_output=True, text=True)
    salida = resultado.stdout
    print(salida)

    # Analizar y sugerir tipo de dispositivo
    lineas = salida.splitlines()
    for linea in lineas:
        match = re.match(r"(\d+)\s+([\d\.]+)\s+([0-9A-Fa-f:]+)", linea)
        if match:
            id_disp, ip, mac = match.groups()
            tipo = identificar_dispositivo(ip, mac)
            print(f"🧠 ID {id_disp} → {ip} → Posible {tipo}")


def identificar_dispositivo(ip, mac):
    mac = mac.upper()
    if ip.endswith(".1"):
        return "Router"
    elif mac.startswith("FC:FB:FB") or mac.startswith("00:15:5D"):
        return "Windows"
    elif mac.startswith("00:1A:79") or "ANDROID" in ip.upper():
        return "Android"
    elif mac.startswith("C0:3F:D5") or mac.startswith("F4:F2:6D"):
        return "TP-Link Router"
    else:
        return "Dispositivo desconocido"


def main():
    limpiar_pantalla()
    print("🛡️ EvilLimiter Automático con detección de dispositivos 🛡️")

    while True:
        mostrar_menu()
        opcion = input("👉 Elegí una opción (1-6): ")

        if opcion == '1':
            ejecutar_evillimiter("scan")

        elif opcion == '2':
            obtener_lista_dispositivos()

        elif opcion == '3':
            id_disp = input("🔒 Ingresá el ID del dispositivo a bloquear: ")
            ejecutar_evillimiter(f"block {id_disp}")

        elif opcion == '4':
            id_disp = input("📉 Ingresá el ID del dispositivo a limitar: ")
            rate = input("📏 Ingresá el límite de velocidad (ej: 100kbit): ")
            ejecutar_evillimiter(f"limit {id_disp} {rate}")

        elif opcion == '5':
            id_disp = input("🔓 Ingresá el ID del dispositivo a liberar: ")
            ejecutar_evillimiter(f"free {id_disp}")

        elif opcion == '6':
            print("👋 Cerrando EvilLimiter Automático. ¡Hasta luego!")
            break

        else:
            print("❌ Opción inválida. Elegí un número del 1 al 6.")


if __name__ == "__main__":
    main()
