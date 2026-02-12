# =====================Entête=================================
# Nom du project : 2048
# Auteur : Lilibeth Zerda
# Date de debut : 12.02.2026
# Date final :
# ======================================================

# ================= IMPORT ============================
import tkinter as tk

# =================Paramètres de la grille=================================
GRID_SIZE = 5  # Grille 5x5
CELL_SIZE = 120  # Taille d'une cellule agrandie
FONT = ("Arial Rounded MT Bold", 18)  # Police agrandie
BACKGROUND_COLOR = "#FDEAF2"

# ================Couleurs des tuiles (dictionaire)=========================
COLORS = {
    0: ("#CCCCCC", "#000000"), #case vide
    2: ("#FFD6FF", "#000000"),
    4: ("#F3CEFF", "#000000"),
    8: ("#E7C6FF", "#000000"),
    16: ("#D8BEFF", "#000000"),
    32: ("#C8B6FF", "#000000"),
    64: ("#B8C0FF", "#000000"),
    128: ("#B79CED", "#000000"),
    256: ("#A68EEE", "#000000"),
    512: ("#9275E7", "#000000"),
    1024: ("#8463E8", "#000000"),
    2048: ("#6D48DB", "#000000"),
    4096: ("#6853A8","#000000"),
    8192:("#4D3691","#000000")
}

# ===============Valeurs pour la grille (tableaux memoire)====================
game = [
    [0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

game_mid = [
    [2,4,8,16,32],
    [64,128,256,512,1024],
    [2048,4096,8192,4,0],
    [64,32,16,0,4],
    [128,128,256,512,0]
]

game = game_mid

# ================= Liste des labels =================
cells = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

# ================= Fonction =================
def display_game():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = game[i][j]

            if value == 0:
                cells[i][j].config(
                    text="",
                    bg=COLORS[0][0],
                    fg=COLORS[0][1]
                )
            else:
                cells[i][j].config(
                    text=str(value),
                    bg=COLORS[value][0],
                    fg=COLORS[value][1]
                )

# ================= PROGRAMME PRINCIPAL =================

# Création de la fenêtre principale
window = tk.Tk()
window.title("2048 - Lilibeth")
window.geometry("630x680")  # Taille de la fenêtre agrandie


########################################################################################################################
# === Cadre supérieur pour le score et les boutons ===
top_frame = tk.Frame(window)
top_frame.pack(pady=(10, 10), ipadx=39)  # Espacement avec la grille

########################################################################################################################
# frame meilleur score et nouvelle partie
frame1 = tk.Frame(top_frame)
frame1.pack(pady=10, fill="x")

# Meilleur score
best_score_label = tk.Label(frame1, text="Meilleur score : ", font=("Arial", 10, "bold"), fg="#000000")
best_score_label.pack(side="left")

best_score_value = tk.Label(frame1, text="0", font=("Arial", 10, "bold"), bg="#FFD1EF", width=5, relief="solid", bd=2)
best_score_value.pack(side="left")

# Bouton "Nouvelle Partie"
new_game_button = tk.Button(frame1, text="Nouvelle Partie", font=("Arial", 10, "bold"), bg="#FFD1EF", fg="#000000",
                            height=1, width=12, relief="solid", bd=2)
new_game_button.pack(side="right",padx=(100,0))
########################################################################################################################

########################################################################################################################
# frame score et quitter
frame2 = tk.Frame(top_frame)
frame2.pack(fill="x")

# Score actuel
score_label = tk.Label(frame2, text="Score :", font=("Arial", 10, "bold"), fg="#000000")
score_label.pack(side="left")

score_value = tk.Label(frame2, text="0", font=("Arial", 10, "bold"), bg="#FFD1EF", width=5, relief="solid", bd=2)
score_value.pack(side="left")

# Bouton "Quitter"
quit_button = tk.Button(frame2, text="Quitter", font=("Arial", 10, "bold"), bg="#FFD1EF", fg="#000000", height=1,
                        width=12, command=window.quit, relief="solid", bd=2)
quit_button.pack(side="right",padx=(100,0))
########################################################################################################################

# === Cadre principal pour la grille ===
frame = tk.Frame(window, bg=BACKGROUND_COLOR, relief="solid", bd=2)
frame.pack(padx=10, pady=10)  # Ajout d'un peu d'espace autour du cadre de la grille

# Création des lables
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        label = tk.Label(
            frame,
            text="",
            font=FONT,
            width=6,
            height=3,
            bg=COLORS[0][0],
            fg=COLORS[0][1],
            relief="solid",
            bd=0.4,
            highlightbackground="black",
            highlightthickness=2
        )
        label.grid(row=i, column=j, padx=10, pady=10)
        cells[i][j] = label


display_game()
window.mainloop()
