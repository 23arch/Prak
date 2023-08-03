import paramiko
import subprocess


def establish_vnc_connection(host, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, password=password)

        _, stdout, _ = ssh.exec_command('vncserver -geometry 1280x800')
        vnc_port = 5900

        return ssh, vnc_port
    except Exception as e:
        print("Fehler bei der Verbindung:", str(e))
        return None, None


def copy_file_via_vnc(ssh, vnc_port, source_file, dest_file):
    try:
        subprocess.run(
            ["vncviewer", f"{ssh.get_transport().getpeername()[0]}::{vnc_port}", "-password", "your_vnc_password",
             "-send", source_file])

        subprocess.run(
            ["vncviewer", f"{ssh.get_transport().getpeername()[0]}::{vnc_port}", "-password", "your_vnc_password",
             "-get", dest_file])

        print("Datei erfolgreich kopiert!")
    except Exception as e:
        print("Fehler beim Kopieren der Datei:", str(e))


if __name__ == "__main__":
    remote_host = input("Remote Host: ")
    remote_password = input("Remote Password: ")
    source_file = input("Pfad zur Quelldatei auf Ihrem Computer: ")
    dest_file = input("Pfad zur Zieldatei auf dem Remote-Computer: ")


    #center
    #C:\Users\Documents\VTG_Export.xlsx
    #C:\Users\MDT\Downloads

    ssh, vnc_port = establish_vnc_connection(remote_host, remote_password)

    if ssh and vnc_port:
        copy_file_via_vnc(ssh, vnc_port, source_file, dest_file)
        ssh.exec_command(f'vncserver -kill :{vnc_port}')
        ssh.close()


