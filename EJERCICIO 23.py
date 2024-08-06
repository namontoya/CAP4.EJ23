#Capitulo 4. Ejercicio propuesto 23

import tkinter as tk
from tkinter import messagebox
import math

def resolver_ecuacion_segundo_grado(A, B, C):
    discriminante = B ** 2 - 4 * A * C
    
    if discriminante > 0:
        s1 = (-B - math.sqrt(discriminante)) / (2 * A)
        s2 = (-B + math.sqrt(discriminante)) / (2 * A)
        return f"Soluciones reales: {s1:.2f} y {s2:.2f}"
    elif discriminante == 0:
        sln = -B / (2 * A)
        return f"Solución doble: {sln:.2f}"
    else:
        real = -B / (2 * A)
        imag = math.sqrt(-discriminante) / (2 * A)
        return (f"Soluciones complejas: {real:.2f} + {imag:.2f}i y "
                f"{real:.2f} - {imag:.2f}i")

def calcular_soluciones():
    try:
        A = float(entry_a.get())
        B = float(entry_b.get())
        C = float(entry_c.get())
        resultado = resolver_ecuacion_segundo_grado(A, B, C)
        messagebox.showinfo("Resultados", resultado)
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "El coeficiente 'A' no puede ser cero.")

root = tk.Tk()
root.title("Ecuación Cuadrática")

for i, text in enumerate(["Coeficiente A:", "Coeficiente B:", "Coeficiente C:"]):
    tk.Label(root, text=text).grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    if i == 0:
        entry_a = entry
    elif i == 1:
        entry_b = entry
    else:
        entry_c = entry

tk.Button(root, text="Calcular", command=calcular_soluciones).grid(row=3, columnspan=2)

root.mainloop()
