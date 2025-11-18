# 📦 Dependencias para Kali Linux (G.A.BruteForce)

Este README lista únicamente las librerías y paquetes seguros que necesitas instalar en Kali Linux para ejecutar `script.py`.

## Requisitos
- `Python 3` (incluido en Kali)
- `pip` (gestor de paquetes de Python)

## Paquetes del sistema (APT)
Instala estos paquetes del sistema para soporte completo:

```bash
sudo apt update
sudo apt install -y python3-pip unrar
```

- `unrar`: necesario para manejar archivos `.rar` protegidos.

## Librerías de Python (pip)
Actualiza `pip` e instala las librerías necesarias:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install \
  colorama \
  paramiko \
  requests \
  PyPDF2 \
  msoffcrypto-tool \
  mysql-connector-python \
  rarfile
```

## Opcionales seguros (según módulos que uses)
- Escaneo de red (módulo de red):
```bash
sudo apt install -y nmap
```
- Módulos Android (ADB):
```bash
sudo apt install -y android-tools-adb
```

## Verificación rápida
Comprueba que las librerías están instaladas correctamente:

```bash
python3 -c "import colorama, paramiko, requests, PyPDF2, msoffcrypto, mysql.connector, rarfile; print('Dependencias OK')"
```

---
Uso únicamente en entornos controlados y con autorización. Seguridad antes que todo.

## Comando único (copiar y pegar)
Instala todo lo necesario de una sola vez en Kali:

```bash
sudo apt update && \
sudo apt install -y python3-pip unrar && \
python3 -m pip install --upgrade pip && \
python3 -m pip install colorama paramiko requests PyPDF2 msoffcrypto-tool mysql-connector-python rarfile
```

Opcionales seguros (si usarás esos módulos):

```bash
# Escaneo de red
sudo apt install -y nmap

# Android por USB (ADB)
sudo apt install -y android-tools-adb
```