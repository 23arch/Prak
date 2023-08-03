import paramiko

def establish_ssh_connection(host, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=5900, username='', password=password)
        return ssh
    except paramiko.AuthenticationException:
        print("Fehler: Authentifizierung fehlgeschlagen. Stellen Sie sicher, dass das Passwort korrekt ist.")
    except paramiko.SSHException as e:
        print(f"Fehler bei der SSH-Verbindung: {str(e)}")
    except Exception as e:
        print("Fehler bei der Verbindung:", str(e))
    return None

if __name__ == "__main__":
    remote_host = input("Remote Host: ")
    remote_password = "center"

    ssh = establish_ssh_connection(remote_host, remote_password)

    if ssh:
        # Your code for copying the file via SSH here
        ssh.close()
