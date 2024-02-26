import socket
import sys

def check_asterisk_status(hostname, port):
    try:
        # Intenta crear un socket y conectarse al servidor Asterisk
        with socket.create_connection((hostname, port), timeout=5) as s:
            print(f"Asterisk en {hostname}:{port} está funcionando correctamente.")
    except socket.error as e:
        print(f"No se pudo conectar a Asterisk en {hostname}:{port}. Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Especifica la dirección IP o el nombre de host y el puerto de tu servidor Asterisk
    asterisk_host = "127.0.0.1"  # Cambia esto a tu dirección IP o nombre de host
    asterisk_port = 5038  # Cambia esto al puerto que estés utilizando para la interfaz de administración de Asterisk

    check_asterisk_status(asterisk_host, asterisk_port)
