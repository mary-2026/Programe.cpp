import tkinter as tk


def calculeaza():
    n = int(caseta.get())

    suma = 0

    while n != 0:
        cifra = n % 10
        suma = suma + cifra
        n = n // 10

    rezultat.config(text="Suma cifrelor este: " + str(suma))


fereastra = tk.Tk()
fereastra.title("Suma cifrelor")
fereastra.geometry("500x300")


mesaj = tk.Label(
    fereastra,
    text="Introdu numărul:"
)
mesaj.pack()


caseta = tk.Entry(fereastra)
caseta.pack()


buton = tk.Button(
    fereastra,
    text="Calculează",
    command=calculeaza
)
buton.pack()


rezultat = tk.Label(
    fereastra,
    text=""
)
rezultat.pack()


fereastra.mainloop()
