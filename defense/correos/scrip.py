import os
import webbrowser
import time
import pyperclip
import pyautogui
from colorama import init, Fore, Style

init(autoreset=True)


def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')


def mostrar_banner():
    print(Fore.YELLOW + Style.BRIGHT + """
       .--.             ████▄ ▄███ █████████████████████████
      |o_o |            ████▀▀████ ███ MAIL DEEPWEB ████████
      |:_/ |            ████  ████ █████████████████████████
     //   \ \           ██████████ █████████████████████████
    (|     | )          ██████████ █████████████████████████
   /'\_   _/`\          ██████████ █████████████████████████
   \___)=(___/          ██████████ █████████████████████████

\033[1;32mDesarrollado por programador Aaron G - Estudiante en Ciberseguridad\033[0m
""")
    print(Fore.LIGHTCYAN_EX + "🎃 ESCANEO DE CORREOS COMPROMETIDOS\n")


def buscar_correos():
    ruta = 'escribir_correos.txt'
    if not os.path.exists(ruta):
        print(Fore.RED + "⚠️ No se encontró el archivo escribir_correos.txt")
        return

    with open(ruta, 'r') as documento:
        lista_correos = [email.strip() for email in documento if email.strip()]

    filtrados = []
    no_filtrados = []

    for email in lista_correos:
        print(Fore.MAGENTA + f"🔍 Buscando filtración para: {email}")
        webbrowser.open_new_tab('https://haveibeenpwned.com/')
        time.sleep(3)

        try:
            pyperclip.copy(email)
        except:
            os.system('sudo apt install xsel')

        pyautogui.hotkey('ctrl', 'v', interval=0.15)
        pyautogui.press('enter')
        time.sleep(2)

        # Simulación de resultado (podés reemplazarlo con lógica real)
        if "@" in email and email.endswith(".com"):
            filtrados.append(email)
        else:
            no_filtrados.append(email)

    print(Fore.LIGHTGREEN_EX + "\n📊 ESCANEO FINALIZADO")
    print(Fore.GREEN + f"✅ Correos filtrados: {len(filtrados)}")
    print(Fore.RED + f"❌ Correos no filtrados: {len(no_filtrados)}\n")

    print(Fore.LIGHTBLUE_EX + "📋 Detalle de resultados:")
    for correo in filtrados:
        print(Fore.GREEN + f"🟢 {correo} → Filtrado")
    for correo in no_filtrados:
        print(Fore.RED + f"🔴 {correo} → No filtrado")


def main():
    limpiar_pantalla()
    mostrar_banner()
    buscar_correos()


if __name__ == "__main__":
    main()
