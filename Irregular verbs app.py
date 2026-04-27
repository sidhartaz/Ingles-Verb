import tkinter as tk
irregular = {
    "arise":      {"past": "arose",          "participle": "arisen",          "spanish": "levantarse, surgir"},
    "awake":      {"past": "awoke",          "participle": "awoken",          "spanish": "despertarse"},
    "be":         {"past": "was / were",     "participle": "been",            "spanish": "ser, estar"},
    "bear":       {"past": "bore",           "participle": "born",            "spanish": "soportar, llevar"},
    "beat":       {"past": "beat",           "participle": "beaten",          "spanish": "golpear, vencer"},
    "become":     {"past": "became",         "participle": "become",          "spanish": "llegar a ser, convertirse"},
    "begin":      {"past": "began",          "participle": "begun",           "spanish": "empezar"},
    "bend":       {"past": "bent",           "participle": "bent",            "spanish": "doblar, flexionar"},
    "bet":        {"past": "bet",            "participle": "bet",             "spanish": "apostar"},
    "bind":       {"past": "bound",          "participle": "bound",           "spanish": "vendar, encademar"},
    "bite":       {"past": "bit",            "participle": "bitten",          "spanish": "morder"},
    "bleed":      {"past": "bled",           "participle": "bled",            "spanish": "sangrar"},
    "blow":       {"past": "blew",           "participle": "blown",           "spanish": "soplar"},
    "break":      {"past": "broke",          "participle": "broken",          "spanish": "romper"},
    "bring":      {"past": "brought",        "participle": "brought",         "spanish": "traer, llevar"},
    "broadcast":  {"past": "broadcast",      "participle": "broadcast",       "spanish": "emitir"},
    "build":      {"past": "built",          "participle": "built",           "spanish": "construir"},
    "buy":        {"past": "bought",         "participle": "bought",          "spanish": "comprar"},
    "cast":       {"past": "cast",           "participle": "cast",            "spanish": "echar, arrojar"},
    "catch":      {"past": "caught",         "participle": "caught",          "spanish": "coger, atrapar"},
    "choose":     {"past": "chose",          "participle": "chosen",          "spanish": "elegir"},
    "cling":      {"past": "clung",          "participle": "clung",           "spanish": "aferrarse, agarrarse"},
    "come":       {"past": "came",           "participle": "come",            "spanish": "venir"},
    "cost":       {"past": "cost",           "participle": "cost",            "spanish": "costar"},
    "creep":      {"past": "crept",          "participle": "crept",           "spanish": "deslizarse, trepar"},
    "cut":        {"past": "cut",            "participle": "cut",             "spanish": "cortar"},
    "deal":       {"past": "dealt",          "participle": "dealt",           "spanish": "tratar"},
    "dig":        {"past": "dug",            "participle": "dug",             "spanish": "cavar, excavar"},
    "do":         {"past": "did",            "participle": "done",            "spanish": "hacer"},
    "draw":       {"past": "drew",           "participle": "drawn",           "spanish": "dibujar"},
    "dream":      {"past": "dreamt/dreamed", "participle": "dreamt/dreamed",  "spanish": "soñar"},
    "drink":      {"past": "drank",          "participle": "drunk",           "spanish": "beber"},
    "drive":      {"past": "drove",          "participle": "driven",          "spanish": "conducir"},
    "dwell":      {"past": "dwelt/dwelled",  "participle": "dwelt/dwelled",   "spanish": "morar"},
    "eat":        {"past": "ate",            "participle": "eaten",           "spanish": "comer"},
    "fall":       {"past": "fell",           "participle": "fallen",          "spanish": "caer"},
    "feed":       {"past": "fed",            "participle": "fed",             "spanish": "alimentar"},
    "feel":       {"past": "felt",           "participle": "felt",            "spanish": "sentir"},
    "fight":      {"past": "fought",         "participle": "fought",          "spanish": "luchar"},
    "find":       {"past": "found",          "participle": "found",           "spanish": "encontrar"},
    "fit":        {"past": "fit/fitted",     "participle": "fit/fitted",      "spanish": "encajar, ajustar"},
    "flee":       {"past": "fled",           "participle": "fled",            "spanish": "huir"},
    "fling":      {"past": "flung",          "participle": "flung",           "spanish": "arrojar"},
    "fly":        {"past": "flew",           "participle": "flown",           "spanish": "volar"},
    "forbid":     {"past": "forbade",        "participle": "forbidden",       "spanish": "prohibir"},
    "forecast":   {"past": "forecast",       "participle": "forecast",        "spanish": "prever, predecir"},
    "forget":     {"past": "forgot",         "participle": "forgotten",       "spanish": "olvidar"},
    "freeze":     {"past": "froze",          "participle": "frozen",          "spanish": "congelar(se)"},
    "get":        {"past": "got",            "participle": "got",             "spanish": "obtener"},
    "give":       {"past": "gave",           "participle": "given",           "spanish": "dar"},
    "go":         {"past": "went",           "participle": "gone",            "spanish": "ir"},
    "grow":       {"past": "grew",           "participle": "grown",           "spanish": "crecer, cultivar"},
    "hang":       {"past": "hung/hanged",    "participle": "hung/hanged",     "spanish": "colgar"},
    "have":       {"past": "had",            "participle": "had",             "spanish": "tener"},
    "hear":       {"past": "heard",          "participle": "heard",           "spanish": "oír"},
    "hide":       {"past": "hid",            "participle": "hidden",          "spanish": "ocultar(se)"},
    "hit":        {"past": "hit",            "participle": "hit",             "spanish": "golpear"},
    "hold":       {"past": "held",           "participle": "held",            "spanish": "sostener, coger"},
    "hurt":       {"past": "hurt",           "participle": "hurt",            "spanish": "herir"},
    "keep":       {"past": "kept",           "participle": "kept",            "spanish": "guardar, quedarse"},
    "kneel":      {"past": "knelt/kneeled",  "participle": "knelt/kneeled",   "spanish": "arrodillarse"},
    "knit":       {"past": "knit/knitted",   "participle": "knit/knitted",    "spanish": "tejer, hacer punto"},
    "know":       {"past": "knew",           "participle": "known",           "spanish": "saber, conocer"},
    "lay":        {"past": "laid",           "participle": "laid",            "spanish": "colocar, poner"},
    "lead":       {"past": "led",            "participle": "led",             "spanish": "guiar, llevar"},
    "lean":       {"past": "leant/leaned",   "participle": "leant/leaned",    "spanish": "apoyar(se)"},
    "leap":       {"past": "leapt/leaped",   "participle": "leapt/leaped",    "spanish": "saltar"},
    "learn":      {"past": "learnt/learned", "participle": "learnt/learned",  "spanish": "aprender"},
    "leave":      {"past": "left",           "participle": "left",            "spanish": "dejar, salir"},
    "lend":       {"past": "lent",           "participle": "lent",            "spanish": "prestar"},
    "let":        {"past": "let",            "participle": "let",             "spanish": "dejar, permitir"},
    "lie":        {"past": "lay",            "participle": "lain",            "spanish": "estar tumbado"},
    "light":      {"past": "lit",            "participle": "lit",             "spanish": "encender"},
    "lose":       {"past": "lost",           "participle": "lost",            "spanish": "perder"},
    "make":       {"past": "made",           "participle": "made",            "spanish": "hacer, fabricar"},
    "mean":       {"past": "meant",          "participle": "meant",           "spanish": "significar"},
    "meet":       {"past": "met",            "participle": "met",             "spanish": "encontrarse, conocer"},
    "mow":        {"past": "mowed",          "participle": "mown/mowed",      "spanish": "cortar, segar"},
    "pay":        {"past": "paid",           "participle": "paid",            "spanish": "pagar"},
    "prove":      {"past": "proved",         "participle": "proven/proved",   "spanish": "probar, demostrar"},
    "put":        {"past": "put",            "participle": "put",             "spanish": "poner"},
    "quit":       {"past": "quit",           "participle": "quit",            "spanish": "dejar"},
    "read":       {"past": "read /red/",     "participle": "read /red/",      "spanish": "leer"},
    "ride":       {"past": "rode",           "participle": "ridden",          "spanish": "montar, cabalgar"},
    "ring":       {"past": "rang",           "participle": "rung",            "spanish": "sonar, tocar timbre"},
    "rise":       {"past": "rose",           "participle": "risen",           "spanish": "levantarse"},
    "run":        {"past": "ran",            "participle": "run",             "spanish": "correr"},
    "saw":        {"past": "sawed",          "participle": "sawn/sawed",      "spanish": "serrar"},
    "say":        {"past": "said",           "participle": "said",            "spanish": "decir"},
    "see":        {"past": "saw",            "participle": "seen",            "spanish": "ver"},
    "seek":       {"past": "sought",         "participle": "sought",          "spanish": "buscar"},
    "sell":       {"past": "sold",           "participle": "sold",            "spanish": "vender"},
    "send":       {"past": "sent",           "participle": "sent",            "spanish": "enviar"},
    "set":        {"past": "set",            "participle": "set",             "spanish": "poner"},
    "sew":        {"past": "sewd",           "participle": "sewn/sewed",      "spanish": "coser"},
    "shake":      {"past": "shook",          "participle": "shaken",          "spanish": "agitar"},
    "shear":      {"past": "sheared",        "participle": "shorn/sheared",   "spanish": "esquilar"},
    "shed":       {"past": "shed",           "participle": "shed",            "spanish": "verter, derramar"},
    "shine":      {"past": "shone",          "participle": "shone",           "spanish": "brillar"},
    "shoot":      {"past": "shot",           "participle": "shot",            "spanish": "disparar, filmar"},
    "show":       {"past": "showed",         "participle": "shown",           "spanish": "mostrar"},
    "shrink":     {"past": "shrank",         "participle": "shrunk",          "spanish": "encoger(se)"},
    "shut":       {"past": "shut",           "participle": "shut",            "spanish": "cerrar"},
    "sing":       {"past": "sang",           "participle": "sung",            "spanish": "cantar"},
    "sink":       {"past": "sank",           "participle": "sunk",            "spanish": "hundir(se)"},
    "sit":        {"past": "sat",            "participle": "sat",             "spanish": "sentarse"},
    "sleep":      {"past": "slept",          "participle": "slept",           "spanish": "dormir"},
    "slide":      {"past": "slid",           "participle": "slid",            "spanish": "resbalarse"},
    "sling":      {"past": "slung",          "participle": "slung",           "spanish": "tirar, arrojar"},
    "smell":      {"past": "smelt/smelled",  "participle": "smelt/smelled",   "spanish": "oler"},
    "sow":        {"past": "sowed",          "participle": "sown/sowed",      "spanish": "sembrar"},
    "speak":      {"past": "spoke",          "participle": "spoken",          "spanish": "hablar"},
    "speed":      {"past": "sped/speeded",   "participle": "sped/speeded",    "spanish": "conducir a mucha velocidad"},
    "spell":      {"past": "spelt/spelled",  "participle": "spelt/spelled",   "spanish": "deletrear"},
    "spend":      {"past": "spent",          "participle": "spent",           "spanish": "gastar, pasar tiempo"},
    "spin":       {"past": "spun/span",      "participle": "spun",            "spanish": "girar"},
    "spit":       {"past": "spit/spat",      "participle": "spit/spat",       "spanish": "escupir"},
    "spill":      {"past": "spilt/spilled",  "participle": "spilt/spilled",   "spanish": "derramar"},
    "split":      {"past": "split",          "participle": "split",           "spanish": "dividir"},
    "spoil":      {"past": "spoilt",         "participle": "spoilt",          "spanish": "estropear"},
    "spread":     {"past": "spread",         "participle": "spread",          "spanish": "extender, untar"},
    "spring":     {"past": "sprang",         "participle": "sprung",          "spanish": "brotar, nacer"},
    "stand":      {"past": "stood",          "participle": "stood",           "spanish": "estar de pie"},
    "steal":      {"past": "stole",          "participle": "stolen",          "spanish": "robar"},
    "stick":      {"past": "stuck",          "participle": "stuck",           "spanish": "pegar, encajarse"},
    "stink":      {"past": "stank",          "participle": "stunk",           "spanish": "apestar"},
    "strike":     {"past": "struck",         "participle": "struck",          "spanish": "golpear"},
    "sting":      {"past": "stung",          "participle": "stung",           "spanish": "picar (insecto)"},
    "strive":     {"past": "strove",         "participle": "striven",         "spanish": "esforzarse, luchar"},
    "swear":      {"past": "swore",          "participle": "sworn",           "spanish": "jurar"},
    "sweep":      {"past": "swept",          "participle": "swept",           "spanish": "barrer"},
    "swell":      {"past": "swelled",        "participle": "swollen/swelled", "spanish": "hinchar(se)"},
    "swim":       {"past": "swam",           "participle": "swum",            "spanish": "nadar"},
    "swing":      {"past": "swung",          "participle": "swung",           "spanish": "balancear"},
    "take":       {"past": "took",           "participle": "taken",           "spanish": "coger"},
    "teach":      {"past": "taught",         "participle": "taught",          "spanish": "enseñar"},
    "tear":       {"past": "tore",           "participle": "torn",            "spanish": "rasgar"},
    "tell":       {"past": "told",           "participle": "told",            "spanish": "decir"},
    "think":      {"past": "thought",        "participle": "thought",         "spanish": "pensar"},
    "throw":      {"past": "threw",          "participle": "thrown",          "spanish": "lanzar"},
    "thrust":     {"past": "thrust",         "participle": "thrust",          "spanish": "empujar"},
    "tread":      {"past": "trod",           "participle": "trodden",         "spanish": "pisar"},
    "understand": {"past": "understood",     "participle": "understood",      "spanish": "comprender"},
    "wake":       {"past": "woke",           "participle": "woken",           "spanish": "despertar(se)"},
    "wear":       {"past": "wore",           "participle": "worn",            "spanish": "llevar puesto"},
    "weave":      {"past": "wove",           "participle": "woven/weaved",    "spanish": "tejer"},
    "weep":       {"past": "wept",           "participle": "wept",            "spanish": "llorar"},
    "wet":        {"past": "wet/wetted",     "participle": "wet/wetted",      "spanish": "mojar"},
    "win":        {"past": "won",            "participle": "won",             "spanish": "ganar"},
    "wind":       {"past": "wound",          "participle": "wound",           "spanish": "enrollar, dar cuerda"},
    "wring":      {"past": "wrung",          "participle": "wrung",           "spanish": "torcer, retorcer"},
    "write":      {"past": "wrote",          "participle": "written",         "spanish": "escribir"},
}

regular = [
    "walk", "play", "love", "listen", "talk", "work", "watch", "help",
    "start", "stop", "finish", "open", "close", "call", "ask", "answer",
    "live", "move", "clean", "cook", "dance", "jump", "laugh", "learn",
    "like", "look", "need", "push", "pull", "rain", "smile", "study",
    "travel", "turn", "use", "visit", "wait", "want", "wash", "wish",
]


def buscar():
    verb = entry.get().lower().strip()

    lbl_past.config(text="")
    lbl_participle.config(text="")
    lbl_spanish.config(text="")
    lbl_msg.config(text="")

    if not verb:
        lbl_msg.config(text="Please enter a verb first.", fg="gray")
        return

    if verb in irregular:
        info = irregular[verb]
        lbl_past.config(text=info["past"])
        lbl_participle.config(text=info["participle"])
        lbl_spanish.config(text=info["spanish"])
    elif verb in regular:
        lbl_msg.config(text=f'"{verb}" is a regular verb. Past: {verb}ed', fg="#2563eb")
    else:
        lbl_msg.config(text=f'"{verb}" isn\'t a verb.', fg="red")


def limpiar():
    entry.delete(0, tk.END)
    lbl_past.config(text="")
    lbl_participle.config(text="")
    lbl_spanish.config(text="")
    lbl_msg.config(text="")
    entry.focus()


root = tk.Tk()
root.title("Verbos irregulares")
root.geometry("420x360")
root.resizable(False, False)
root.config(bg="white", padx=30, pady=25)

tk.Label(root, text="Irregular Verb Transformer", font=("Arial", 14, "bold"),
         bg="white", fg="#1d4ed8").pack(pady=(0, 16))

tk.Label(root, text="Verb(Infinitive):", bg="white", fg="black").pack(anchor="w")
entry = tk.Entry(root, font=("Arial", 12), relief="solid", bd=1)
entry.pack(fill="x", pady=(4, 10))
entry.bind("<Return>", lambda e: buscar())
entry.focus()

frame_botones = tk.Frame(root, bg="white")
frame_botones.pack(fill="x", pady=(0, 16))

tk.Button(frame_botones, text="TRANSFORM VERB", command=buscar,
          bg="#2563eb", fg="white", relief="flat", padx=12, pady=5,
          cursor="hand2").pack(side="left", padx=(0, 8))

tk.Button(frame_botones, text="CLEAR", command=limpiar,
          bg="white", fg="#2563eb", relief="solid", bd=1, padx=12, pady=5,
          cursor="hand2").pack(side="left")

separador = tk.Frame(root, bg="#e5e7eb", height=1)
separador.pack(fill="x", pady=(0, 14))

def fila(etiqueta, color):
    f = tk.Frame(root, bg="white")
    f.pack(fill="x", pady=3)
    tk.Label(f, text=etiqueta, width=16, anchor="w", bg="white",
             fg="gray", font=("Arial", 10)).pack(side="left")
    lbl = tk.Label(f, text="", anchor="w", bg="white",
                   fg=color, font=("Arial", 11, "bold"))
    lbl.pack(side="left")
    return lbl

lbl_past        = fila("Past simple:",     "#1d4ed8")
lbl_participle  = fila("Past participle:", "#1d4ed8")
lbl_spanish     = fila("Español:",         "#166534")

lbl_msg = tk.Label(root, text="", bg="white", font=("Arial", 10), wraplength=360)
lbl_msg.pack(pady=(12, 0))

root.mainloop()