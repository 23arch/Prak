import paramiko
import subprocess

def establish_ssh_connection(host, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.get_transport().set_banner("SSH")
        ssh.connect(host, port=5900, password=password)
        return ssh
    except paramiko.AuthenticationException:
        print("Fehler: Authentifizierung fehlgeschlagen. Stellen Sie sicher, dass das Passwort korrekt ist.")
    except paramiko.SSHException as e:
        print(f"Fehler bei der SSH-Verbindung: {str(e)}")
    except Exception as e:
        print("Fehler bei der Verbindung:", str(e))
    return None

def copy_file_via_ssh(ssh, source_file, dest_file):
    try:
        sftp = ssh.open_sftp()
        sftp.put(source_file, dest_file)
        sftp.close()
        print("Datei erfolgreich kopiert!")
    except IOError as e:
        print(f"Fehler beim Kopieren der Datei: {str(e)}")
    except Exception as e:
        print("Allgemeiner Fehler:", str(e))

if __name__ == "__main__":
    remote_host = input("Remote Host: ")
    remote_password = "center"  # Set the password here
    source_file = input("Pfad zur Quelldatei auf Ihrem Computer: ")
    dest_file = input("Pfad zur Zieldatei auf dem Remote-Computer: ")

    ssh = establish_ssh_connection(remote_host, remote_password)

    if ssh:
        copy_file_via_ssh(ssh, source_file, dest_file)
        ssh.close()

