🛡️ Herramienta de Defensa Cibernética
📌 ¿Qué es esto?
Este script en Python es una herramienta defensiva pensada para proteger sistemas Linux. Te permite detectar procesos raros, conexiones sospechosas, accesos no autorizados, rootkits, archivos infectados y mucho más. Ideal para estudiantes de ciberseguridad que quieren auditar su entorno como profesionales.

🧰 ¿Qué funciones incluye?
Desde un menú interactivo podés ejecutar 19 módulos:

Ver procesos sospechosos

Monitorear conexiones de red

Ver intentos de acceso fallidos

Escanear puertos abiertos

Verificar integridad de archivos

Auditar logs del sistema

Ver usuarios conectados

Ver servicios activos y sospechosos

Buscar archivos ocultos

Analizar tráfico de red (iftop)

Ver cambios recientes en /etc

Revisar permisos inseguros en /var/www

Ver uso de disco

Ver uso de CPU y RAM

Escanear con ClamAV

Detectar rootkits con chkrootkit y rkhunter

Detectar y bloquear intrusos en la red

Desbloquear IPs manualmente

Ver resumen de seguridad con alertas

🖥️ Requisitos
Sistema operativo: Linux (Kali, Ubuntu, Debian, etc.)

Python 3 instalado

Acceso a terminal con permisos de sudo

🔧 Instalación de herramientas necesarias
Antes de usar el script, instalá estas herramientas:

bash
sudo apt update
sudo apt install nmap chkrootkit rkhunter clamav clamav-daemon iftop
sudo freshclam  # Actualiza la base de datos de ClamAV
🚀 Cómo usarlo
Guardá el archivo como defensa.py

Abrí la terminal y ejecutá:

bash
python3 defensa.py
Navegá por el menú y elegí lo que querés analizar.

⚠️ Notas importantes
Algunas funciones requieren permisos de administrador (sudo)

El escaneo con ClamAV puede tardar unos minutos

El script no modifica nada en tu sistema, solo analiza y reporta

Podés bloquear IPs sospechosas y desbloquearlas manualmente

📊 ¿Qué pasa al final?
Después de usar varios módulos, podés ver un resumen de seguridad. Si se detectó algo raro, te lo muestra con alertas y sugerencias para actuar.

👨‍💻 Autor
Aaron G. Estudiante de Licenciatura en Ciberseguridad Apasionado por la defensa digital y la automatización en Python