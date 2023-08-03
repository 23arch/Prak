from pyRDP.client import RDPClient

def get_rdp_information(host, password):
    try:
        with RDPClient(host, password) as client:
            client.connect()
            system_information = client.system_information()
            return system_information
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    remote_host = input("Remote Host: ")
    remote_password = input("center")

    rdp_info = get_rdp_information(remote_host, remote_password)
    print("RDP System Information:")
    print(rdp_info)
