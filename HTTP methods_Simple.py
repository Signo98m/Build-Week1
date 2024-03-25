import requests 

def enumerazione_metodi_http(indirizzo_ip):
    url = f"http://{indirizzo_ip}:80"
    metodi_abilitati = []

    try:
        response = requests.options(url)
        if response.status_code == 200:
            headers = response.headers
            if 'allow' in headers:
                metodi_abilitati = headers['allow'].split(',')
                print("Metodi HTTP abilitati sul servizio HTTP sulla porta 80:")
                for metodo in metodi_abilitati:
                    print(metodo.strip())
            else:
                print("Nessun metodo HTTP abilitato trovato.")
        else:
            print(f"Errore durante la richiesta: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la connessione al server: {e}")

# Esempio di utilizzo
if __name__ == "__main__":
    indirizzo_ip = input("Inserisci l'indirizzo IP del servizio HTTP: ")
    print(f"Esecuzione dell'enumerazione dei metodi HTTP su {indirizzo_ip}...")
    enumerazione_metodi_http(indirizzo_ip)
