import tkinter as tk   #tkinter este biblioteca Python pentru realizarea interfeței grafice.

def afiseaza():
    nume = caseta.get()
    rezultat.config(text="Salut, " + nume + "!")
    
fereastra = tk.Tk()#Tk() creează fereastra

fereastra.title("Prima mea aplicație")
fereastra.geometry("500x300")#stabilim dimens

eticheta = tk.Label(   #creează obiectul.-Punem primul text în fereastră: Label
    fereastra,
    text="Introdu numele tău:"
)
eticheta.pack()#îl așază în fereastră;Fără pack(), Label există, dar nu va fi afișat.

caseta = tk.Entry(fereastra) #Adăugăm o casetă pentru introducerea datelor- entry
caseta.pack()




buton = tk.Button(  #Adăugăm un buton
    fereastra,
    text="Afișează",
    command=afiseaza
)

buton.pack()

rezultat = tk.Label(
    fereastra,
    text=""
)
rezultat.pack()


fereastra.mainloop()#mainloop() o menține deschisă și permite interacțiunea cu ea.
