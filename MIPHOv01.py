from scapy.all import ARP, Ether, srp
import socket

rango_ip = "192.168.1.1/24"
arp = ARP(pdst=rango_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
paquete = ether / arp
resultado = srp(paquete, timeout=3, verbose=0)[0]  # Almacena el paquete enviado/recibido a nivel 2

def scaneared():
    # Lista de clientes inicializada, en ciclo for se llena con datos
    clientes = []
    # Creacion del paquete ARP
    for enviados, recibidos in resultado:
        clientes.append({'IP': recibidos.psrc, 'MAC': recibidos.hwsrc})
        # Para cada respuesta, ingresa valores de IP y MAC en la lista 'Clientes'
    # Imprimir Clientes
    print("Dispositivos conectados en la Red:")
    print("IP" + " " * 18 + "MAC")
    for cliente in clientes:
        print("{:16}   {}".format(cliente['IP'], cliente['MAC']))

def hostname():

    input01 = input("Ingrese ip a consultar: ").upper()
    output = socket.gethostbyaddr(str(input01))
    output_processed = str(output).split("'")[1::2]
    print(f"Their hostname is: {output_processed[0]}\n")
    print("""
            Que quieres hacer ahora?
            1) Volver al menu principal
            2) Salir.
            """)
    elije = input("-Ingresa la eleccion: ")
    if elije == "1":
        menu()
    elif elije == "2":
        print("Adios!")
        print(quit())

def menu():
    print("""
    1) Escaneo de IP's y MAC de mi Red Local
    2) Obtener Hostname de una IP
    """)
    opcion = input("-Selecciona tu Opción: ")
    if opcion == "1":
        scaneared()
        print("""
        Quieres saber el hostname de algun equipo?
        1) Si
        2) No, Salir.
        """)
        elije = input("-Ingresa la eleccion: ")
        if elije == "1":
            hostname()
        elif elije == "2":
            print("Adios!")
            print(quit())

    elif opcion == "2":
        hostname()
    else:
        print("Opcion fuera de rango!")

def inicio():
    print("""
    :::'##::::'##:'####:'########::'##::::'##::'#######:::::
    ::: ###::'###:. ##:: ##.... ##: ##:::: ##:'##.... ##::::
    ::: ####'####:: ##:: ##:::: ##: ##:::: ##: ##:::: ##::::
    ::: ## ### ##:: ##:: ########:: #########: ##:::: ##::::
    ::: ##. #: ##:: ##:: ##.....::: ##.... ##: ##:::: ##::::
    ::: ##:.:: ##:: ##:: ##:::::::: ##:::: ##: ##:::: ##::::
    ::: ##:::: ##:'####: ##:::::::: ##:::: ##:. #######:::::
    :::..:::::..::....::..:::::::::..:::::..:::.......::::::
    ::::::'##::::'##:::::::::::'#####:::::::::::'##:::::::::
    :::::: ##:::: ##::::::::::'##.. ##::::::::'####:::::::::
    :::::: ##:::: ##:::::::::'##:::: ##:::::::.. ##:::::::::
    :::::: ##:::: ##::::::::: ##:::: ##::::::::: ##:::::::::
    ::::::. ##:: ##:::::::::: ##:::: ##::::::::: ##:::::::::
    :::::::. ## ##:::'###::::. ##:: ##::'###:::: ##:::::::::
    ::::::::. ###:::: ###:::::. #####::: ###::'######:::::::
    :::::::::...:::::...:::::::.....::::...:::......::::::::

      , __  _                , __      ,__ __    ___        
     /|/  \(_|   |          /|/  \|  |/|  |  |  /   \       
      | __/  |   |           |___/|__|_|  |  |    __/       
      |   \  |   |   -----   | \     | |  |  |      \  -----
      |(__/   \_/|/          |  \_/  | |  |  |_/\___/       
                /|                                          
                \|                                          

    """)

inicio()
menu()





