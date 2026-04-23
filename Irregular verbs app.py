import tkinter as tk
from tkinter import messagebox

# ─────────────────────────────────────────────
#  BASE DE DATOS DE VERBOS IRREGULARES
# ─────────────────────────────────────────────
irregular_verbs = {
    "be":      {"past": "was / were",  "participle": "been",     "spanish": "ser / estar"},
    "beat":    {"past": "beat",        "participle": "beaten",   "spanish": "golpear"},
    "become":  {"past": "became",      "participle": "become",   "spanish": "convertirse"},
    "begin":   {"past": "began",       "participle": "begun",    "spanish": "comenzar"},
    "bite":    {"past": "bit",         "participle": "bitten",   "spanish": "morder"},
    "blow":    {"past": "blew",        "participle": "blown",    "spanish": "soplar"},
    "break":   {"past": "broke",       "participle": "broken",   "spanish": "romper"},
    "bring":   {"past": "brought",     "participle": "brought",  "spanish": "traer"},
    "build":   {"past": "built",       "participle": "built",    "spanish": "construir"},
    "buy":     {"past": "bought",      "participle": "bought",   "spanish": "comprar"},
    "catch":   {"past": "caught",      "participle": "caught",   "spanish": "atrapar"},
    "choose":  {"past": "chose",       "participle": "chosen",   "spanish": "elegir"},
    "come":    {"past": "came",        "participle": "come",     "spanish": "venir"},
    "cost":    {"past": "cost",        "participle": "cost",     "spanish": "costar"},
    "cut":     {"past": "cut",         "participle": "cut",      "spanish": "cortar"},
    "do":      {"past": "did",         "participle": "done",     "spanish": "hacer"},
    "draw":    {"past": "drew",        "participle": "drawn",    "spanish": "dibujar"},
    "drink":   {"past": "drank",       "participle": "drunk",    "spanish": "beber"},
    "drive":   {"past": "drove",       "participle": "driven",   "spanish": "manejar"},
    "eat":     {"past": "ate",         "participle": "eaten",    "spanish": "comer"},
    "fall":    {"past": "fell",        "participle": "fallen",   "spanish": "caer"},
    "feel":    {"past": "felt",        "participle": "felt",     "spanish": "sentir"},
    "fight":   {"past": "fought",      "participle": "fought",   "spanish": "pelear"},
    "find":    {"past": "found",       "participle": "found",    "spanish": "encontrar"},
    "fly":     {"past": "flew",        "participle": "flown",    "spanish": "volar"},
    "forget":  {"past": "forgot",      "participle": "forgotten","spanish": "olvidar"},
    "get":     {"past": "got",         "participle": "gotten",   "spanish": "obtener"},
    "give":    {"past": "gave",        "participle": "given",    "spanish": "dar"},
    "go":      {"past": "went",        "participle": "gone",     "spanish": "ir"},
    "grow":    {"past": "grew",        "participle": "grown",    "spanish": "crecer"},
    "have":    {"past": "had",         "participle": "had",      "spanish": "tener"},
    "hear":    {"past": "heard",       "participle": "heard",    "spanish": "oír"},
    "hide":    {"past": "hid",         "participle": "hidden",   "spanish": "esconder"},
    "hit":     {"past": "hit",         "participle": "hit",      "spanish": "golpear"},
    "hold":    {"past": "held",        "participle": "held",     "spanish": "sostener"},
    "hurt":    {"past": "hurt",        "participle": "hurt",     "spanish": "herir"},
    "keep":    {"past": "kept",        "participle": "kept",     "spanish": "mantener"},
    "know":    {"past": "knew",        "participle": "known",    "spanish": "saber / conocer"},
    "lay":     {"past": "laid",        "participle": "laid",     "spanish": "poner (algo)"},
    "lead":    {"past": "led",         "participle": "led",      "spanish": "liderar"},
    "leave":   {"past": "left",        "participle": "left",     "spanish": "salir / dejar"},
    "lend":    {"past": "lent",        "participle": "lent",     "spanish": "prestar"},
    "let":     {"past": "let",         "participle": "let",      "spanish": "dejar / permitir"},
    "lie":     {"past": "lay",         "participle": "lain",     "spanish": "yacer / acostarse"},
    "lose":    {"past": "lost",        "participle": "lost",     "spanish": "perder"},
    "make":    {"past": "made",        "participle": "made",     "spanish": "hacer"},
    "mean":    {"past": "meant",       "participle": "meant",    "spanish": "significar"},
    "meet":    {"past": "met",         "participle": "met",      "spanish": "conocer / reunirse"},
    "pay":     {"past": "paid",        "participle": "paid",     "spanish": "pagar"},
    "put":     {"past": "put",         "participle": "put",      "spanish": "poner"},
    "read":    {"past": "read",        "participle": "read",     "spanish": "leer"},
    "ride":    {"past": "rode",        "participle": "ridden",   "spanish": "montar"},
    "ring":    {"past": "rang",        "participle": "rung",     "spanish": "sonar / llamar"},
    "rise":    {"past": "rose",        "participle": "risen",    "spanish": "levantarse"},
    "run":     {"past": "ran",         "participle": "run",      "spanish": "correr"},
    "say":     {"past": "said",        "participle": "said",     "spanish": "decir"},
    "see":     {"past": "saw",         "participle": "seen",     "spanish": "ver"},
    "sell":    {"past": "sold",        "participle": "sold",     "spanish": "vender"},
    "send":    {"past": "sent",        "participle": "sent",     "spanish": "enviar"},
    "set":     {"past": "set",         "participle": "set",      "spanish": "establecer"},
    "shake":   {"past": "shook",       "participle": "shaken",   "spanish": "sacudir"},
    "shine":   {"past": "shone",       "participle": "shone",    "spanish": "brillar"},
    "shoot":   {"past": "shot",        "participle": "shot",     "spanish": "disparar"},
    "show":    {"past": "showed",      "participle": "shown",    "spanish": "mostrar"},
    "shut":    {"past": "shut",        "participle": "shut",     "spanish": "cerrar"},
    "sing":    {"past": "sang",        "participle": "sung",     "spanish": "cantar"},
    "sink":    {"past": "sank",        "participle": "sunk",     "spanish": "hundir"},
    "sit":     {"past": "sat",         "participle": "sat",      "spanish": "sentarse"},
    "sleep":   {"past": "slept",       "participle": "slept",    "spanish": "dormir"},
    "speak":   {"past": "spoke",       "participle": "spoken",   "spanish": "hablar"},
    "spend":   {"past": "spent",       "participle": "spent",    "spanish": "gastar"},
    "stand":   {"past": "stood",       "participle": "stood",    "spanish": "pararse"},
    "steal":   {"past": "stole",       "participle": "stolen",   "spanish": "robar"},
    "stick":   {"past": "stuck",       "participle": "stuck",    "spanish": "pegar"},
    "swim":    {"past": "swam",        "participle": "swum",     "spanish": "nadar"},
    "swing":   {"past": "swung",       "participle": "swung",    "spanish": "balancear"},
    "take":    {"past": "took",        "participle": "taken",    "spanish": "tomar"},
    "teach":   {"past": "taught",      "participle": "taught",   "spanish": "enseñar"},
    "tell":    {"past": "told",        "participle": "told",     "spanish": "decir / contar"},
    "think":   {"past": "thought",     "participle": "thought",  "spanish": "pensar"},
    "throw":   {"past": "threw",       "participle": "thrown",   "spanish": "lanzar"},
    "understand":{"past":"understood", "participle":"understood","spanish": "entender"},
    "wake":    {"past": "woke",        "participle": "woken",    "spanish": "despertar"},
    "wear":    {"past": "wore",        "participle": "worn",     "spanish": "usar / llevar"},
    "win":     {"past": "won",         "participle": "won",      "spanish": "ganar"},
    "write":   {"past": "wrote",       "participle": "written",  "spanish": "escribir"},
}

# Verbos regulares comunes para detectar el error
regular_verbs = [
    "walk", "play", "love", "listen", "talk", "work", "watch", "help",
    "start", "stop", "finish", "open", "close", "call", "ask", "answer",
    "live", "move", "clean", "cook", "dance", "jump", "laugh", "learn",
    "like", "look", "need", "push", "pull", "rain", "smile", "study",
    "travel", "turn", "use", "visit", "wait", "want", "wash", "wish",
]

# ─────────────────────────────────────────────
#  LÓGICA PRINCIPAL
# ─────────────────────────────────────────────
def transform_verb():
    verb = entry_infinitive.get().lower().strip()

    # Limpiar campos de salida
    for field in (entry_past, entry_participle, entry_spanish):
        field.config(state="normal")
        field.delete(0, tk.END)

    if verb == "":
        messagebox.showwarning("⚠️ Empty field", "Please enter a verb before clicking TRANSFORM.")
    elif verb in irregular_verbs:
        entry_past.insert(0, irregular_verbs[verb]["past"])
        entry_participle.insert(0, irregular_verbs[verb]["participle"])
        entry_spanish.insert(0, irregular_verbs[verb]["spanish"])
    elif verb in regular_verbs:
        messagebox.showinfo("ℹ️ Regular Verb",
                            f'"{verb}" is a REGULAR verb.\n'
                            f'Past Simple: {verb}ed\n'
                            f'Past Participle: {verb}ed')
    else:
        messagebox.showerror("❌ Not found",
                             f'"{verb}" was not found in the database.\n'
                             "Check the spelling and try again.")

    for field in (entry_past, entry_participle, entry_spanish):
        field.config(state="readonly")

def clear_all():
    entry_infinitive.delete(0, tk.END)
    for field in (entry_past, entry_participle, entry_spanish):
        field.config(state="normal")
        field.delete(0, tk.END)
        field.config(state="readonly")
    entry_infinitive.focus()

def on_enter(event):
    transform_verb()

# ─────────────────────────────────────────────
#  INTERFAZ GRÁFICA
# ─────────────────────────────────────────────
root = tk.Tk()
root.title("Irregular Verbs Transformer")
root.geometry("400x500")
root.resizable(False, False)
root.config(bg="#1e1e2e", padx=30, pady=25)

# Colores
BG       = "#1e1e2e"
CARD     = "#2a2a3e"
ACCENT   = "#7c6af7"
GREEN    = "#4ade80"
TEXT     = "#e2e0ff"
SUBTEXT  = "#a0a0c0"
ENTRY_BG = "#13131f"

# ── Título ──
tk.Label(root, text="Irregular Verbs", font=("Georgia", 20, "bold"),
         bg=BG, fg=TEXT).pack(pady=(0, 2))
tk.Label(root, text="Transformer", font=("Georgia", 13, "italic"),
         bg=BG, fg=ACCENT).pack(pady=(0, 18))

# ── Frame central ──
frame = tk.Frame(root, bg=CARD, padx=20, pady=20, relief="flat")
frame.pack(fill="x")

# Entrada
tk.Label(frame, text="Verb (Infinitive)", font=("Helvetica", 9, "bold"),
         bg=CARD, fg=SUBTEXT).pack(anchor="w")
entry_infinitive = tk.Entry(frame, font=("Helvetica", 13), justify="center",
                            bg=ENTRY_BG, fg=TEXT, insertbackground=TEXT,
                            relief="flat", bd=6)
entry_infinitive.pack(fill="x", pady=(3, 12))
entry_infinitive.bind("<Return>", on_enter)
entry_infinitive.focus()

# Botones
btn_frame = tk.Frame(frame, bg=CARD)
btn_frame.pack(fill="x", pady=(0, 14))

btn_transform = tk.Button(btn_frame, text="▶  TRANSFORM", command=transform_verb,
                          bg=ACCENT, fg="white", font=("Helvetica", 10, "bold"),
                          relief="flat", cursor="hand2", padx=12, pady=7)
btn_transform.pack(side="left", expand=True, fill="x", padx=(0, 6))

btn_clear = tk.Button(btn_frame, text="✕  CLEAR", command=clear_all,
                      bg="#3a3a50", fg=SUBTEXT, font=("Helvetica", 10),
                      relief="flat", cursor="hand2", padx=12, pady=7)
btn_clear.pack(side="left", expand=True, fill="x")

# Separador visual
tk.Frame(frame, bg=ACCENT, height=1).pack(fill="x", pady=(0, 14))

# Función para crear campos de salida
def make_output(label_text, color):
    tk.Label(frame, text=label_text, font=("Helvetica", 9, "bold"),
             bg=CARD, fg=color).pack(anchor="w")
    e = tk.Entry(frame, font=("Helvetica", 12), justify="center",
                 bg=ENTRY_BG, fg=color, state="readonly",
                 readonlybackground=ENTRY_BG, relief="flat", bd=6)
    e.pack(fill="x", pady=(3, 10))
    return e

entry_past        = make_output("Past Simple",      "#60a5fa")
entry_participle  = make_output("Past Participle",  "#f472b6")
entry_spanish     = make_output("Spanish",          GREEN)

# ── Pie de página ──
tk.Label(root, text="Press Enter or click TRANSFORM  •  Database: 85 verbs",
         font=("Helvetica", 8), bg=BG, fg="#555570").pack(pady=(14, 0))

root.mainloop()