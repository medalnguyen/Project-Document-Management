from tkinter import *
from tkinter import filedialog, ttk
import pandas as pd

# create root window
root = Tk()

# root window title and dimension
root.title("Project Document Management")
root.geometry('800x500')

# Configure grid weights for dynamic resizing
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Label to display file path
file_path_label = Label(root, text="", fg="green")
file_path_label.grid(row=1, column=0, columnspan=3, sticky='w')

# Treeview widget to display Excel data
tree = None

def import_excel():
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    if file_path:
        file_path_label.config(text=file_path)
    # Không đọc và hiển thị dữ liệu

def export_excel():
    export_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    if export_path:
        # Xuất một DataFrame mẫu
        df = pd.DataFrame({
            "Column 1": [1, 2, 3],
            "Column 2": ["A", "B", "C"]
        })
        df.to_excel(export_path, index=False)

# Button to import Excel file
import_btn = Button(root, text="Import", fg="blue", command=import_excel)
import_btn.grid(column=2, row=0)

# Button to export Excel file (nằm cạnh Import)
export_btn = Button(root, text="Export", fg="blue", command=export_excel)
export_btn.grid(column=3, row=0)

# Execute Tkinter
root.mainloop()