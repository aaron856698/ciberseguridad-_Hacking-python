import os
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)
alertas_detectadas = []


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_banner():
    print(Fore.RED + Style.BRIGHT + """
   .--.             █████████████████████████████████████████
  |o_o |            ███ DEFENSA ACTIVA - CIBERSEGURIDAD ████
  |:_/ |            █████████████████████████████████████████
 //   \ \           🛡️ Herramienta de protección y detección
(|     | )          👨‍💻 Desarrollado por Aaron G - Estudiante
/'\_   _/`\          🔍 Monitoreo de red, procesos y accesos
\___)=(___/
""")


def mostrar_menu():
    while True:
        print("\n📋 MENÚ PRINCIPAL:")
        print("1. Ver procesos sospechosos")
        print("2. Conexiones de red activas")
        print("3. Intentos de acceso fallidos")
        print("4. Escaneo de puertos")
        print("5. Verificar integridad de archivo")
        print("6. Últimos logs del sistema")
        print("7. Usuarios conectados")
        print("8. Servicios activos")
        print("9. Archivos ocultos en /home")
        print("10. Tráfico de red (iftop)")
        print("11. Cambios recientes en /etc")
        print("12. Permisos inseguros en /var/www")
        print("13. Uso de disco")
        print("14. Uso de CPU y RAM")
        print("15. Escaneo antivirus (ClamAV)")
        print("16. Escaneo rootkits (chkrootkit + rkhunter)")
        print("17. Detectar y bloquear intrusos en la red")
        print("18. Desbloquear IP manualmente")
        print("19. Ver resumen de seguridad")
        print("0. Salir")

        opcion = input("\nElegí una opción: ")

        acciones = {
            "1": ver_procesos,
            "2": ver_conexiones,
            "3": ver_accesos_fallidos,
            "4": escanear_puertos,
            "5": verificar_archivo,
            "6": ver_logs,
            "7": ver_usuarios,
            "8": ver_servicios,
            "9": buscar_archivos_ocultos,
            "10": analizar_trafico,
            "11": cambios_en_etc,
            "12": revisar_permisos,
            "13": uso_disco,
            "14": uso_cpu_ram,
            "15": escaneo_clamav,
            "16": escaneo_rootkits,
            "17": detectar_intrusos,
            "18": desbloquear_ip,
            "19": mostrar_resumen
        }

        if opcion == "0":
            print("\n👋 Cerrando herramienta. ¡Hasta la próxima!")
            break
        elif opcion in acciones:
            acciones[opcion]()
        else:
            print("❌ Opción inválida. Probá de nuevo.")


def ver_procesos():
    print("\n🔍 Procesos con alto consumo:")
    salida = subprocess.getoutput("ps aux --sort=-%cpu | head -n 10")
    print(salida)
    if "minerd" in salida or "crypto" in salida:
        alertas_detectadas.append(
            "⚠️ Proceso sospechoso detectado (minería o malware)")


def ver_conexiones():
    print("\n🌐 Conexiones activas:")
    print(subprocess.getoutput("ss -tunap | grep ESTAB"))


def ver_accesos_fallidos():
    print("\n🚫 Últimos intentos fallidos de login:")
    salida = subprocess.getoutput(
        "sudo grep 'Failed password' /var/log/auth.log | tail -n 10")
    print(salida)
    if salida:
        alertas_detectadas.append(
            "⚠️ Se detectaron intentos de acceso fallidos")


def escanear_puertos():
    objetivo = input("🔎 IP o dominio a escanear: ")
    os.system(f"nmap -sS -Pn {objetivo}")


def verificar_archivo():
    ruta = input("📁 Ruta del archivo: ")
    print("🔐 Hash SHA256:")
    print(subprocess.getoutput(f"sha256sum {ruta}"))


def ver_logs():
    print("\n📜 Últimos eventos del sistema:")
    print(subprocess.getoutput("sudo journalctl -xe | tail -n 20"))


def ver_usuarios():
    print("\n👥 Usuarios conectados:")
    print(subprocess.getoutput("who"))


def ver_servicios():
    print("\n🔧 Servicios activos:")
    salida = subprocess.getoutput(
        "systemctl list-units --type=service --state=running")
    print(salida)
    if "telnet" in salida or "ftp" in salida:
        alertas_detectadas.append(
            "⚠️ Servicio inseguro detectado (telnet o ftp)")


def buscar_archivos_ocultos():
    print("\n🕵️ Archivos ocultos en /home:")
    print(subprocess.getoutput("find /home -name '.*' -type f"))


def analizar_trafico():
    print("\n📡 Ejecutando iftop por 10 segundos...")
    os.system("sudo timeout 10 iftop")


def cambios_en_etc():
    print("\n📁 Archivos modificados en /etc en las últimas 24h:")
    print(subprocess.getoutput("sudo find /etc -type f -mtime -1"))


def revisar_permisos():
    print("\n🔒 Archivos con permisos inseguros en /var/www:")
    print(subprocess.getoutput("find /var/www -type f -perm -o+w"))


def uso_disco():
    print("\n💽 Uso de disco:")
    print(subprocess.getoutput("df -h"))


def uso_cpu_ram():
    print("\n📊 Uso de CPU y RAM:")
    print(subprocess.getoutput("top -b -n 1 | head -n 10"))


def escaneo_clamav():
    print("\n🛡️ Escaneando con ClamAV...")
    salida = subprocess.getoutput("clamscan -r /home")
    print(salida)
    if "Infected files: 0" not in salida:
        alertas_detectadas.append("⚠️ ClamAV detectó archivos infectados")


def escaneo_rootkits():
    print("\n🧪 chkrootkit:")
    salida_chk = subprocess.getoutput("sudo chkrootkit")
    print(salida_chk)
    if "INFECTED" in salida_chk:
        alertas_detectadas.append("🚨 chkrootkit detectó posible rootkit")

    print("\n🧪 rkhunter:")
    salida_rkh = subprocess.getoutput("sudo rkhunter --check --sk")
    print(salida_rkh)
    if "Warning" in salida_rkh or "Suspicious" in salida_rkh:
        alertas_detectadas.append("🚨 rkhunter detectó actividad sospechosa")


def detectar_intrusos():
    print("\n🕵️ Conexiones activas en el sistema:")
    conexiones = subprocess.getoutput("ss -tunap | grep ESTAB")
    print(conexiones)

    ip = input(
        "\n🔎 Ingresá la IP que querés bloquear (o enter para cancelar): ").strip()
    if ip:
        confirmacion = input(
            f"⚠️ ¿Seguro que querés bloquear la IP {ip}? (s/n): ").lower()
        if confirmacion == "s":
            subprocess.getoutput(f"sudo iptables -A INPUT -s {ip} -j DROP")
            print(f"🚫 IP {ip} bloqueada con iptables.")
            alertas_detectadas.append(f"⚠️ Se bloqueó la IP sospechosa: {ip}")
        else:
            print("🔄 Acción cancelada.")
    else:
        print("🔄 No se ingresó ninguna IP.")


def desbloquear_ip():
    ip = input("\n🔓 Ingresá la IP que querés desbloquear: ").strip()
    if ip:
        subprocess.getoutput(f"sudo iptables -D INPUT -s {ip} -j DROP")
        print(f"✅ IP {ip} desbloqueada.")
    else:
        print("❌ No se ingresó ninguna IP.")


def mostrar_resumen():
    print("\n📊 RESUMEN DE SEGURIDAD:")
    if alertas_detectadas:
        print("🚨 Se detectaron las siguientes alertas:")
        for alerta in alertas_detectadas:
            print(alerta)
        print("\n🛠️ Recomendaciones:")
        print("- Revisá los procesos y servicios sospechosos.")
        print("- Considerá bloquear accesos no autorizados.")
        print("- Usá herramientas como fail2ban, auditd o AppArmor.")
    else:
        print("✅ Todo limpio. No se detectaron amenazas.")


if __name__ == "__main__":
    limpiar_pantalla()
    mostrar_banner()
    mostrar_menu()
