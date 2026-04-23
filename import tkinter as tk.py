import tkinter as tk
from tkinter import messagebox

# 1. Base de datos (Deberás completarla con tu guía de verbos)
irregular_verbs = {
    "eat": {"past": "ate", "participle": "eaten", "spanish": "comer"},
    "go": {"past": "went", "participle": "gone", "spanish": "ir"},
    "write": {"past": "wrote", "participle": "written", "spanish": "escribir"},
    "break": {"past": "broke", "participle": "broken", "spanish": "romper"},
    "furry":{"past": "rule 34", "participle":"a camilo le gustan las guatonas", "spanish": "67"},

}

# Lista de ejemplo para detectar verbos regulares
regular_verbs = ["walk", "play", "love", "listen"]

def transform_verb():
    verb = entry_infinitive.get().lower().strip()
    
    # Limpiar campos de salida antes de mostrar nuevos resultados
    entry_past.config(state="normal")
    entry_participle.config(state="normal")
    entry_spanish.config(state="normal")
    
    entry_past.delete(0, tk.END)
    entry_participle.delete(0, tk.END)
    entry_spanish.delete(0, tk.END)

    if verb in irregular_verbs:
        # Si es irregular, llenamos los cuadros
        entry_past.insert(0, irregular_verbs[verb]["past"])
        entry_participle.insert(0, irregular_verbs[verb]["participle"])
        entry_spanish.insert(0, irregular_verbs[verb]["spanish"])
    elif verb in regular_verbs:
        messagebox.showwarning("Error", "this verb is a REGULAR verb")
    elif verb == "":
        messagebox.showwarning("Error", "Please enter a word")
    else:
        messagebox.showerror("Error", "this word isn't a verb")

    # Volver a poner los campos en modo SOLO LECTURA (Read Only)
    entry_past.config(state="readonly")
    entry_participle.config(state="readonly")
    entry_spanish.config(state="readonly")

# 2. Configuración de la Ventana Principal
root = tk.Tk()
root.title("Irregular Verbs Transformer")
root.geometry("350x450")
root.config(padx=20, pady=20)

# --- Elementos de la Interfaz ---

# Entrada: Verbo Infinitivo
tk.Label(root, text="Verb (Infinitive)", font=("Arial", 10, "bold")).pack()
entry_infinitive = tk.Entry(root, justify="center")
entry_infinitive.pack(pady=5)

# Botón: Transform
btn_transform = tk.Button(root, text="TRANSFORM VERB", bg="#4CAF50", fg="white", 
                          font=("Arial", 10, "bold"), command=transform_verb)
btn_transform.pack(pady=20)

# Salida: Past Simple
tk.Label(root, text="Past Simple").pack()
entry_past = tk.Entry(root, justify="center", state="readonly")
entry_past.pack(pady=5)

# Salida: Past Participle
tk.Label(root, text="Past Participle").pack()
entry_participle = tk.Entry(root, justify="center", state="readonly")
entry_participle.pack(pady=5)

# Salida: Spanish
tk.Label(root, text="Spanish").pack()
entry_spanish = tk.Entry(root, justify="center", state="readonly")
entry_spanish.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()