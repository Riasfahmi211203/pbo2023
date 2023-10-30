import tkinter as tk
from tkinter import frame,label,Entry,Button,END,w

# Creat tkinter object
app = tk.TK()
app.geometry("450x450")
# Tambahkan judul
app.title("kalkulator Luas dan keliling persegi panjang")

# windows 
frame = frame(app)
frame.pack(padx=20, pady=20)

app.mainloop()
