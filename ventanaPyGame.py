import tkinter as tk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Datos personales")
ventana.geometry("500x300")

# Nombre completo
nombre = tk.Label(
    ventana,
    text="Keinner Jesús Durán Pineda",
    font=("Times New Roman", 25, "bold")
)
nombre.pack(pady=40)

# Centro educativo
centro = tk.Label(
    ventana,
    text="I.E.S. UNICARIBE",
    font=("Times New Roman", 20)
)
centro.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
