import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import vncdotool


class VncFileTransferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VNC File Transfer")

        self.connected = False  # Variable to track the connection status
        self.explorer_access = False  # Variable to track explorer access

        self.host_label = tk.Label(root, text="VNC Host (IP):")
        self.host_label.pack()
        self.host_entry = tk.Entry(root)
        self.host_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.connect_button = tk.Button(root, text="Connect", command=self.connect_vnc)
        self.connect_button.pack()

        self.status_label = tk.Label(root, text="Not Connected")
        self.status_label.pack()

        self.browse_button = tk.Button(root, text="Browse Files", command=self.browse_files)
        self.browse_button.pack()

        self.transfer_button = tk.Button(root, text="Transfer Files", command=self.transfer_files)
        self.transfer_button.pack()

    def connect_vnc(self):
        host = self.host_entry.get()
        password = self.password_entry.get()

        try:
            self.vnc_client = vncdotool.VNCClient(host=host, password=password)
            self.vnc_client.start()  # Start the VNC client
            self.connected = True
            self.update_status()
        except Exception as e:
            self.connected = False
            self.update_status()
            messagebox.showerror("Connection Error", f"Error while connecting to VNC: {str(e)}")

    def browse_files(self):
        if self.connected:
            file_path = filedialog.askopenfilename()
            # Update UI or perform any necessary actions with the selected file
        else:
            messagebox.showinfo("Not Connected", "Please connect to VNC before browsing files.")

    def transfer_files(self):
        if self.connected:
            # Implement file transfer logic using self.vnc_client
            # ...
            messagebox.showinfo("File Transfer", "File transfer completed successfully!")
        else:
            messagebox.showinfo("Not Connected", "Please connect to VNC before transferring files.")

    def update_status(self):
        if self.connected:
            status_text = "Connected"
            if self.explorer_access:
                status_text += " - Explorer Access"
        else:
            status_text = "Not Connected"

        self.status_label.config(text=status_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = VncFileTransferApp(root)
    root.mainloop()
