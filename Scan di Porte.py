import socket

def scan_servizi(indirizzo_ip, porta_iniziale, porta_finale):
    porte_aperte = []
    porte_chiuse = 0
    for porta in range(porta_iniziale, porta_finale + 1):
        try:
            # Creazione di un oggetto socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Impostazione del timeout per la connessione
            sock.settimeout(1)
            # Tentativo di connessione al servizio sulla porta specificata
            risultato = sock.connect_ex((indirizzo_ip, porta))
            # Controllo se la porta è aperta
            if risultato == 0:
                print(f"Porta {porta}: Aperta")
                porte_aperte.append(porta)
            else:
                print(f"Porta {porta}: Chiusa")
                porte_chiuse += 1
            # Chiusura del socket
            sock.close()
        except KeyboardInterrupt:
            print("\nScansione interrotta.")
            return
        except socket.error:
            print("Impossibile connettersi al server.")
            return

    # Report finale
    print("\n--- Report finale ---")
    print(f"Porte aperte: {len(porte_aperte)}")
    print(f"Porte chiuse: {porte_chiuse}")
    if porte_aperte:
        print("Porte aperte trovate:")
        print(porte_aperte)

# Esempio di utilizzo
if __name__ == "__main__":
    indirizzo_ip = input("Inserisci l'indirizzo IP del target: ")
    porta_iniziale = int(input("Inserisci la porta iniziale: "))
    porta_finale = int(input("Inserisci la porta finale: "))
    print(f"Scansione delle porte da {porta_iniziale} a {porta_finale} su {indirizzo_ip}...")
    scan_servizi(indirizzo_ip, porta_iniziale, porta_finale)