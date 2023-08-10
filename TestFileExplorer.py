import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class SimpleFileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple File Explorer")

        self.current_directory = tk.StringVar()
        self.current_directory.set("C:\\")

        self.label = tk.Label(root, text="Current Directory:")
        self.label.pack()

        self.entry = tk.Entry(root, textvariable=self.current_directory, width=50)
        self.entry.pack()

        self.tree = ttk.Treeview(root, columns=("Name", "Type"))
        self.tree.heading("#0", text="Name")
        self.tree.heading("Type", text="Type")
        self.tree.pack()

        self.navigate_button = tk.Button(root, text="Navigate", command=self.navigate)
        self.navigate_button.pack()

        self.navigate_up_button = tk.Button(root, text="Navigate Up", command=self.navigate_up)
        self.navigate_up_button.pack()

        self.tree.bind("<Double-1>", self.open_selected)

    def navigate(self):
        directory = self.current_directory.get()
        if os.path.isdir(directory):
            self.update_tree(directory)
        else:
            messagebox.showinfo("Invalid Directory", "Please enter a valid directory.")

    def navigate_up(self):
        current_path = self.current_directory.get()
        parent_path = os.path.dirname(current_path)
        if parent_path:
            self.current_directory.set(parent_path)
            self.update_tree(parent_path)
        else:
            messagebox.showinfo("Root Directory", "Already at the root directory.")

    def update_tree(self, directory):
        self.current_directory.set(directory)
        self.tree.delete(*self.tree.get_children())
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            item_type = "Directory" if os.path.isdir(item_path) else "File"
            self.tree.insert("", "end", text=item, values=(item_type,))

    def open_selected(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_text = self.tree.item(selected_item, "text")
            item_path = os.path.join(self.current_directory.get(), item_text)
            if os.path.isdir(item_path):
                self.update_tree(item_path)
            else:
                os.startfile(item_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleFileExplorer(root)
    root.mainloop()
