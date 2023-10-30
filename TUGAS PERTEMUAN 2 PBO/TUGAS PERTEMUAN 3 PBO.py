import tkinter as tkinter
from tkinter import frame,label,entry,button,END,w

def hitung_luas():
    Pj = float (txpanjang.get())
    Ib = float txlebar.get())

    L =Pj P*Ib

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

    def hitung keliling():
        Pj = float(txtpanjang.get())
        Ib = float txtlebar.get())

        k = 2 * (pj + Ib)

        txtkeliling.delete(0,END)
        txtkeliling.insert(EN,k)

def hitung():
    hitung_luas()
    hitung_luas()

    # create tkinter object
    app = tk.TK()

    # Tambahan Judul
    app.title ("Kalkulator Luas dan Keliling Persegi Panjang ")

    # windows
    frame = frame(app)
    frame.pack(padx=20,pady=20)

    # Label panjang
    panjang=Label(frame,text="panjang:")
    panjang.grid(row=0, column=0, sticky=w, pady=5, pady=5)

    # Label Lebar
    Lebar = label(frame,text="Lebar:")
    Lebar.grid(row=1, column=0, sticky=w, padx=5, pady=5)
    
    # Text panjang
    txtpanjang = Entry(frame)
    textpanjang.grid(row=0, column=1)
     
     # Textbok Lebar
     textlebar = Entry(frame)
     textlebar.grid(row=1, column=1)

     # Botton
     hitung_button = Button(frame,text="Hitung", command=hitung)
     hitung_button.grid(row=2, column=1,sticky=w,padx=5,pady=5)
     