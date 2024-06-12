import os
import psutil
import ping3
import socket
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuração do logger
logging.basicConfig(filename='network_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_network_info():
    network_info = psutil.net_if_addrs()
    for interface, addresses in network_info.items():
        logging.info(f"Interface: {interface}")
        for address in addresses:
            if address.family == socket.AF_INET:
                logging.info(f"  IP Address: {address.address}")
                logging.info(f"  Netmask: {address.netmask}")
                logging.info(f"  Broadcast IP: {address.broadcast}")

def ping_device(ip):
    response = ping3.ping(ip)
    if response is not None:
        logging.info(f"Device {ip} is reachable")
        return True
    else:
        logging.warning(f"Device {ip} is not reachable")
        return False

def send_email(subject, body, to_email):
    from_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    if not from_email or not password:
        logging.error("Email user or password not set in environment variables")
        raise ValueError("Email user or password not set in environment variables")

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        logging.info(f"Email sent to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def main():
    logging.info("Starting network monitoring")
    get_network_info()

    # Example IP addresses of printers
    printer_ips = ["192.168.1.100", "192.168.1.101"]

    logging.info("Checking Printer Connections")
    for ip in printer_ips:
        if not ping_device(ip):
            send_email(
                subject="Printer Offline",
                body=f"Printer with IP {ip} is offline",
                to_email="admin@example.com"  # Alterar para o email do administrador
            )
    logging.info("Finished network monitoring")

if __name__ == "__main__":
    main()
