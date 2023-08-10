import vncdotool.api

def establish_vnc_connection(host, password):
    try:
        vnc = vncdotool.api.connect(server=host, password=password)
        return vnc
    except Exception as e:
        print("Fehler bei der Verbindung:", str(e))
    return None

if __name__ == "__main__":
    remote_host = "172.31.247.65"
    remote_password = "center" # Replace with your actual VNC password

    vnc_client = establish_vnc_connection(remote_host, remote_password)

    if vnc_client:
        try:
            # Type the string "Hallo" using individual key presses
            vnc_client.keyPress('H')
            vnc_client.keyPress('a')
            vnc_client.keyPress('l')
            vnc_client.keyPress('l')
            vnc_client.keyPress('o')
        except Exception as e:
            print("Error while interacting with VNC:", str(e))
        finally:
            vnc_client.disconnect()
