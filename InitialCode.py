import paramiko
import subprocess
import vncdotool


def establish_vnc_connection(host, password):
    def establish_vnc_connection(host, password):
        try:
            vnc = vncdotool.api.connect(server=host, password=password)
            return vnc
        except Exception as e:
            print("Fehler bei der Verbindung:", str(e))
        return None


def copy_file_via_vnc(vnc, vnc_port, source_file, dest_file):
    try:
        subprocess.run(
            ["vncviewer", f"{vnc.get_transport().getpeername()[0]}::{vnc_port}", "-password", "your_vnc_password",
             "-send", source_file])

        subprocess.run(
            ["vncviewer", f"{vnc.get_transport().getpeername()[0]}::{vnc_port}", "-password", "your_vnc_password",
             "-get", dest_file])

        print("Datei erfolgreich kopiert!")
    except Exception as e:
        print("Fehler beim Kopieren der Datei:", str(e))


if __name__ == "__main__":
    remote_host = "172.31.247.65"
    remote_password = "center"
    source_file = "C:\\Users\\talha.yuecel\\Documents\\VTG_Export.xlsx"
    dest_file = "C:\\Users\\MDT\\Downloads\\"


    #center
    #C:\Users\Documents\VTG_Export.xlsx
    #C:\Users\MDT\Downloads

    vnc_port = establish_vnc_connection(remote_host, remote_password)




