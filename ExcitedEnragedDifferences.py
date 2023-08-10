import paramiko
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class RemoteFileCopyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Remote File Copy")
        
        self.source_host_label = tk.Label(root, text="Source Host:")
        self.source_host_label.pack()
        self.source_host_entry = tk.Entry(root)
        self.source_host_entry.pack()
        
        self.source_username_label = tk.Label(root, text="Source Username:")
        self.source_username_label.pack()
        self.source_username_entry = tk.Entry(root)
        self.source_username_entry.pack()
        
        self.source_password_label = tk.Label(root, text="Source Password:")
        self.source_password_label.pack()
        self.source_password_entry = tk.Entry(root, show="*")
        self.source_password_entry.pack()
        
        self.source_path_label = tk.Label(root, text="Source File Path:")
        self.source_path_label.pack()
        self.source_path_entry = tk.Entry(root)
        self.source_path_entry.pack()
        
        self.dest_host_label = tk.Label(root, text="Destination Host:")
        self.dest_host_label.pack()
        self.dest_host_entry = tk.Entry(root)
        self.dest_host_entry.pack()
        
        self.dest_username_label = tk.Label(root, text="Destination Username:")
        self.dest_username_label.pack()
        self.dest_username_entry = tk.Entry(root)
        self.dest_username_entry.pack()
        
        self.dest_password_label = tk.Label(root, text="Destination Password:")
        self.dest_password_label.pack()
        self.dest_password_entry = tk.Entry(root, show="*")
        self.dest_password_entry.pack()
        
        self.dest_path_label = tk.Label(root, text="Destination File Path:")
        self.dest_path_label.pack()
        self.dest_path_entry = tk.Entry(root)
        self.dest_path_entry.pack()
        
        self.copy_button = tk.Button(root, text="Copy File", command=self.copy_file)
        self.copy_button.pack()

    def copy_file(self):
        source_host = self.source_host_entry.get()
        source_username = self.source_username_entry.get()
        source_password = self.source_password_entry.get()
        source_path = self.source_path_entry.get()
        
        dest_host = self.dest_host_entry.get()
        dest_username = self.dest_username_entry.get()
        dest_password = self.dest_password_entry.get()
        dest_path = self.dest_path_entry.get()
        
        try:
            source_client = paramiko.SSHClient()
            source_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            source_client.connect(source_host, username=source_username, password=source_password)
          
            dest_client = paramiko.SSHClient()
            dest_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            dest_client.connect(dest_host, username=dest_username, password=dest_password)
            

            sftp_source = source_client.open_sftp()
            sftp_dest = dest_client.open_sftp()
            sftp_dest.put(source_path, dest_path)
            

            sftp_source.close()
            sftp_dest.close()
            source_client.close()
            dest_client.close()
            
            messagebox.showinfo("Success", "File successfully copied!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = RemoteFileCopyApp(root)
    root.mainloop()
