# 🔐 G.A.BruteForce - Herramienta de Testing Ético

## 📋 Descripción
G.A.BruteForce es una suite de herramientas de ciberseguridad diseñada para pruebas de penetración éticas y educativas. Incluye módulos de fuerza bruta para diferentes servicios y archivos protegidos.

## ⚠️ Advertencia de Uso Ético
**ESTA HERRAMIENTA ES EXCLUSIVAMENTE PARA PROPÓSITOS EDUCATIVOS Y TESTING ÉTICO**
- ✅ Solo usar en sistemas propios o con permiso explícito
- ✅ Para aprendizaje y mejora de la seguridad
- ❌ Uso ilegal está prohibido y puede tener consecuencias legales
- ❌ No usar en sistemas sin autorización

## 🚀 Instalación

### 1. Instalar Python 3.7+
Asegúrate de tener Python 3.7 o superior instalado.

### 2. Instalar dependencias
```bash
# Opción 1: Usar pip directamente
pip install -r requirements.txt

# Opción 2: Instalar manualmente las librerías principales
pip install colorama paramiko requests PyPDF2 msoffcrypto-tool

# Opción 3: Si tienes problemas con algunas librerías
pip install colorama
pip install paramiko
pip install requests
pip install PyPDF2
pip install msoffcrypto-tool
# Para RAR: pip install rarfile (también necesitas WinRAR instalado)
# Para MySQL: pip install mysql-connector-python
```

### Linux (Python 3)
```bash
# Usa siempre el intérprete correcto
python3 -m pip install -r requirements.txt

# Si solo falta una librería concreta
python3 -m pip install rarfile paramiko requests PyPDF2 msoffcrypto-tool mysql-connector-python

# Para manejar archivos RAR cifrados, instala además en el sistema:
# Debian/Ubuntu
sudo apt update && sudo apt install unrar
# o alternativa
sudo apt install unar

# Fedora
sudo dnf install unrar

# Arch
sudo pacman -S unrar
```

### 3. Verificar instalación
```bash
python script.py
```

## 📚 Módulos Disponibles

### 🔐 Módulos de Fuerza Bruta
1. **SSH** - Ataque a servidores SSH
2. **FTP** - Ataque a servidores FTP
3. **ZIP** - Desencriptación de archivos ZIP
4. **RAR** - Desencriptación de archivos RAR
5. **MySQL** - Ataque a bases de datos MySQL
6. **HTTP Login** - Ataque a formularios web
7. **Excel** - Desencriptación de archivos Excel protegidos
8. **PDF** - Desencriptación de archivos PDF protegidos

### 📱 Módulos Android (requiere ADB)
12. **PIN Android** - Simulación de ataque a PIN
13. **Listar Apps** - Listar aplicaciones instaladas
14. **Extraer SMS** - Extraer mensajes SMS
15. **Extraer Contactos** - Extraer lista de contactos

### 🔍 Módulos de Auditoría
17. **Wi-Fi Windows** - Ver contraseñas Wi-Fi guardadas
18. **Procesos Windows** - Ver procesos activos
19. **Servicios Linux** - Ver servicios en Linux
21. **Historial Comandos** - Ver historial de comandos
22. **USB Conectados** - Ver dispositivos USB
23. **Archivos Modificados** - Ver archivos recientemente modificados
24. **Escanear Red** - Escanear red local
25. **Logs Sudo** - Ver intentos de sudo
26. **Wi-Fi Linux** - Ver claves Wi-Fi en Linux
27. **Tareas Programadas** - Ver tareas cron/programadas
28. **Conexiones Salientes** - Ver conexiones de red
29. **Logs Grandes** - Buscar archivos log grandes
30. **Detectar Sniffers** - Ver interfaces en modo promiscuo

## 🎯 Cómo Usar

### 1. Ejecutar el script
```bash
python script.py
```

### 2. Seleccionar un módulo
El menú mostrará todas las opciones numeradas. Solo ingresa el número correspondiente.

### 3. Seguir las instrucciones
Cada módulo pedirá información específica:
- Archivos objetivo (ZIP, RAR, PDF, Excel)
- Diccionario de contraseñas
- IPs o URLs objetivo
- Credenciales conocidas (usuario)

## 📁 Archivos de Prueba

### Diccionario de contraseñas comunes
El archivo `diccionario_basico.txt` contiene contraseñas comunes para pruebas:
- password
- 123456
- admin
- root
- test
- qwerty
- abc123
- letmein

### Crear archivos protegidos de prueba
```bash
# Crear un ZIP protegido (manualmente con WinRAR/7-Zip)
# Crear un PDF protegido (con LibreOffice o similar)
# Crear un Excel protegido (con contraseña de apertura)
```

## 🔧 Solución de Problemas

### Error: "No module named 'paramiko'"
```bash
pip install paramiko
```

### Error: "No module named 'rarfile'"
```bash
pip install rarfile
# También necesitas WinRAR instalado en el sistema
```

### Error de conexión en SSH/FTP
- Verifica que el servidor esté activo
- Verifica la IP y puerto
- Verifica que el usuario exista

### Error en módulos Android
- Asegúrate de tener ADB instalado
- Activa depuración USB en el dispositivo
- El dispositivo debe estar rooteado para algunas funciones

## 🎓 Ejemplos de Uso

### Probar fuerza bruta ZIP
1. Crea un archivo ZIP con contraseña "password"
2. Selecciona opción 3 del menú
3. Ingresa ruta del ZIP
4. Ingresa ruta del diccionario
5. El script probará cada contraseña

### Probar auditoría Wi-Fi Windows
1. Selecciona opción 17
2. El script mostrará redes y contraseñas guardadas

### Probar escaneo de red
1. Selecciona opción 24
2. Ingresa tu rango de red (ej: 192.168.1.0/24)
3. El script mostrará dispositivos activos

## 📋 Notas Importantes

### Seguridad
- Los intentos de fuerza bruta pueden ser detectados
- Algunos servicios bloquean después de X intentos fallidos
- Usa timeouts apropiados para evitar bloqueos

### Rendimiento
- La fuerza bruta es lenta por naturaleza
- Usa diccionarios pequeños para pruebas
- Considera usar herramientas más especializadas para producción

### Legalidad
- Solo usar en sistemas propios o con permiso
- El uso indebido puede ser delito
- Respeta las leyes de tu país

## 🆘 Soporte
Si encuentras problemas:
1. Verifica que todas las dependencias estén instaladas
2. Lee los mensajes de error cuidadosamente
3. Asegúrate de tener permisos adecuados
4. Para Android: verifica ADB y root

## 📄 Licencia
Este proyecto es solo para fines educativos. El autor no se hace responsable del uso indebido de esta herramienta.

---
**👨‍💻 Desarrollado por Aaron G - Estudiante de Ciberseguridad**
**📚 Para aprendizaje y testing ético únicamente**