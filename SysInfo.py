import winrm

def get_rdp_information(host, password):
    try:
        session = winrm.Session(host, auth=(password))
        ps_script = """
        $sysInfo = Get-CimInstance -ClassName Win32_OperatingSystem
        $sysInfo | Select-Object CSName, Caption, Version, BuildNumber, OSArchitecture
        """
        result = session.run_ps(ps_script)
        return result.std_out.decode("utf-8")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    remote_host = input("Remote Host: ")
    remote_password = input("center")

    rdp_info = get_rdp_information(remote_host, remote_password)
    print("RDP System Information:")
    print(rdp_info)
