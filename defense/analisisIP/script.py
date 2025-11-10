import webbrowser
import time
from colorama import Fore, Style

# Leer direcciones IP desde archivo
with open('direcciones_ip.txt', 'r') as documento:
    lista_ips = [ip.strip() for ip in documento if ip.strip()]

# Menú de herramientas (VirusTotal ahora es la opción 1)
eleccion = input(
    Fore.GREEN + 'Escribe el nombre de la herramienta que querés utilizar para analizar las direcciones IP ' +
    Fore.YELLOW + '\n1 - VirusTotal\n2 - AbuseIP\n3 - Symantec\n' +
    Style.RESET_ALL + '¿Cuál es tu elección? --> '
)

if eleccion == '1':
    for ip in lista_ips:
        url = f'https://www.virustotal.com/gui/ip-address/{ip}'
        print(Fore.CYAN +
              f'Analizando {ip} en VirusTotal...' + Style.RESET_ALL)
        webbrowser.open_new(url)
        time.sleep(5)

elif eleccion == '2':
    for ip in lista_ips:
        url = f'https://www.abuseipdb.com/check/{ip}'
        print(Fore.CYAN + f'Analizando {ip} en AbuseIPDB...' + Style.RESET_ALL)
        webbrowser.open_new(url)
        time.sleep(5)

elif eleccion == '3':
    for ip in lista_ips:
        url = f'https://sitereview.bluecoat.com/#/lookup-result/{ip}'
        print(Fore.CYAN + f'Analizando {ip} en Symantec...' + Style.RESET_ALL)
        webbrowser.open_new(url)
        time.sleep(5)

else:
    print(Fore.RED + '❌ ERROR: tenés que insertar un número del 1 al 3' + Style.RESET_ALL)
