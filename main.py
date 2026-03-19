# =====================Entête=================================
# Nom du project : Jeu 2048 5x5
# Auteur : Lilibeth Zerda
# Date de debut : 05.02.2026
# Date final :
# ======================================================

#1er sprint final: 12.02.2026, correction: 26.02.2026
#2eme sprint final : 05.03.2026, correction: 13.03.2026
#3éme sprint final : 12.03.2026, correction:

# ================= IMPORT ============================
import tkinter as tk
import random
# =================Paramètres de la grille=================================
GRID_SIZE = 5  # Grille 5x5
CELL_SIZE = 120  # Taille d'une cellule agrandie
FONT = ("Arial Rounded MT Bold", 18)  # Police agrandie
BACKGROUND_COLOR = "#FDEAF2"
########################################################################################################################
#variables globales pour game over
game_over = False
game_over_label = None
retry_button = None

#variables globales pour gagne
win_label = None
continue_button = None
win_displayed = False
win_state = False
########################################################################################################################

# ================Couleurs des tuiles (dictionaire)=========================
COLORS = {
    0: "#CCCCCC", #case vide
    2: "#FFD6FF",
    4: "#F3CEFF",
    8: "#E7C6FF",
    16: "#D8BEFF",
    32: "#C8B6FF",
    64: "#B8C0FF",
    128: "#B79CED",
    256: "#A68EEE",
    512: "#9275E7",
    1024: "#8463E8",
    2048: "#6D48DB",
    4096: "#6853A8",
    8192:"#4D3691"
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
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

game = game_mid

# = Liste qui va contenir les labels de chaque case de la grille=
cells = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

# ================= Fonctions =================
def display_game():
    """Met à jour l'affichage de la grille logique"""
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = game[i][j]

            if value == 0:
                cells[i][j].config(
                    text="",
                    bg=COLORS[0],
                    fg="black"
                )
            else:
                cells[i][j].config(
                    text=str(value),
                    bg=COLORS[value],
                    fg="black"
                )

def pack5_ligne(ligne):
    """
    Reçoit une liste de 5 valeurs.
    Retourne :
    la ligne tassée vers la gauche, le nombre de mouvements effectués
    """
    #5 valeurs de la ligne
    a, b, c, d, e = ligne
    nmove = 0 #pour compte de mouvements

    # ===== Déplacement vers la gauche =====

    if d == 0 and e != 0:
        d, e = e, 0
        nmove += 1

    if c == 0 and d != 0:
        c, d, e = d, e, 0
        nmove += 1

    if b == 0 and c != 0:
        b, c, d, e = c, d, e, 0
        nmove += 1

    if a == 0 and b != 0:
        a, b, c, d, e = b, c, d, e, 0
        nmove += 1

    #si deux cases voisines sont égales, on les fusionne

    if a == b and a != 0:
        a *= 2
        b, c, d, e = c, d, e, 0
        nmove += 1

    if b == c and b != 0:
        b *= 2
        c, d, e = d, e, 0
        nmove += 1

    if c == d and c != 0:
        c *= 2
        d, e = e, 0
        nmove += 1

    if d == e and d != 0:
        d *= 2
        e = 0
        nmove += 1

    return [a, b, c, d, e], nmove

#tests
print(pack5_ligne([0, 0, 0, 0, 2]))
print(pack5_ligne([0, 0, 2, 2, 0]))
print(pack5_ligne([2, 0, 2, 2, 2]))
print(pack5_ligne([2, 2, 2, 2, 2]))
print(pack5_ligne([2, 2, 4, 0, 4]))
#######################################################################################################################
#######################################################################################################################
# Function pour recommencer une nouvelle partie
def restart_game():
    global game, game_over, game_over_label, retry_button,win_displayed, win_state

    hide_win()
    win_displayed = False
    win_state = False

    game_over = False

    #pour supprimer le message Game over
    if game_over_label is not None:
        game_over_label.destroy()
        game_over_label = None

    if retry_button is not None:
        retry_button.destroy()
        retry_button = None

    # grille vide
    game = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

    # ajouter les 2 premières tuiles aletoire
    add_random_tile()
    add_random_tile()

    # réaffiche la grille
    display_game()
    print("Nouvelle partie")

#######################################################################################################################
#######################################################################################################################
#Function pour déplacer la grille vers la gauche
def move_left():
    global game
    tot_move = 0

    ligne, nmove = pack5_ligne(game[0])
    game[0][0], game[0][1], game[0][2], game[0][3], game[0][4] = ligne
    tot_move += nmove

    ligne, nmove = pack5_ligne(game[1])
    game[1][0], game[1][1], game[1][2], game[1][3], game[1][4] = ligne
    tot_move += nmove

    ligne, nmove = pack5_ligne(game[2])
    game[2][0], game[2][1], game[2][2], game[2][3], game[2][4] = ligne
    tot_move += nmove

    ligne, nmove = pack5_ligne(game[3])
    game[3][0], game[3][1], game[3][2], game[3][3], game[3][4] = ligne
    tot_move += nmove

    ligne, nmove = pack5_ligne(game[4])
    game[4][0], game[4][1], game[4][2], game[4][3], game[4][4] = ligne
    tot_move += nmove

    if tot_move > 0:
        add_random_tile()
        display_game()

        if check_win() and not win_displayed:
            show_win()

        if check_lose():
            print("PERDU !")
            show_game_over()
    return tot_move

########################################################################################################################
########################################################################################################################
#function pour déplacer la grille vers la droite
def move_right():
    global game
    tot_move = 0

    # Ligne 0
    ligne, nmove = pack5_ligne([game[0][4], game[0][3], game[0][2], game[0][1], game[0][0]])
    ligne = list(reversed(ligne))
    game[0][0], game[0][1], game[0][2], game[0][3], game[0][4] = ligne
    tot_move += nmove

    # Ligne 1
    ligne, nmove = pack5_ligne([game[1][4], game[1][3], game[1][2], game[1][1], game[1][0]])
    ligne = list(reversed(ligne))
    game[1][0], game[1][1], game[1][2], game[1][3], game[1][4] = ligne
    tot_move += nmove

    # Ligne 2
    ligne, nmove = pack5_ligne([game[2][4], game[2][3], game[2][2], game[2][1], game[2][0]])
    ligne = list(reversed(ligne))
    game[2][0], game[2][1], game[2][2], game[2][3], game[2][4] = ligne
    tot_move += nmove

    # Ligne 3
    ligne, nmove = pack5_ligne([game[3][4], game[3][3], game[3][2], game[3][1], game[3][0]])
    ligne = list(reversed(ligne))
    game[3][0], game[3][1], game[3][2], game[3][3], game[3][4] = ligne
    tot_move += nmove

    # Ligne 4
    ligne, nmove = pack5_ligne([game[4][4], game[4][3], game[4][2], game[4][1], game[4][0]])
    ligne = list(reversed(ligne))
    game[4][0], game[4][1], game[4][2], game[4][3], game[4][4] = ligne
    tot_move += nmove

    if tot_move > 0:
        add_random_tile()
        display_game()


        if check_win() and not win_displayed:
            show_win()

        if check_lose():
            print("PERDU !")
            show_game_over()
    return tot_move
########################################################################################################################

########################################################################################################################
#function pour déplacer la grille vers le haut
def move_up():
    global game
    tot_move = 0

    # Colonne 0
    ligne, nmove = pack5_ligne([game[0][0], game[1][0], game[2][0], game[3][0], game[4][0]])
    game[0][0], game[1][0], game[2][0], game[3][0], game[4][0] = ligne
    tot_move += nmove

    # Colonne 1
    ligne, nmove = pack5_ligne([game[0][1], game[1][1], game[2][1], game[3][1], game[4][1]])
    game[0][1], game[1][1], game[2][1], game[3][1], game[4][1] = ligne
    tot_move += nmove

    # Colonne 2
    ligne, nmove = pack5_ligne([game[0][2], game[1][2], game[2][2], game[3][2], game[4][2]])
    game[0][2], game[1][2], game[2][2], game[3][2], game[4][2] = ligne
    tot_move += nmove

    # Colonne 3
    ligne, nmove = pack5_ligne([game[0][3], game[1][3], game[2][3], game[3][3], game[4][3]])
    game[0][3], game[1][3], game[2][3], game[3][3], game[4][3] = ligne
    tot_move += nmove

    # Colonne 4
    ligne, nmove = pack5_ligne([game[0][4], game[1][4], game[2][4], game[3][4], game[4][4]])
    game[0][4], game[1][4], game[2][4], game[3][4], game[4][4] = ligne
    tot_move += nmove

    if tot_move > 0:
        add_random_tile()
        display_game()

        if check_win() and not win_displayed:
            show_win()

        if check_lose():
            print("PERDU !")
            show_game_over()
    return tot_move
########################################################################################################################

########################################################################################################################
#function pour déplacer la grille vers le bas
def move_down():
    global game
    tot_move = 0

    ligne, nmove = pack5_ligne([game[4][0], game[3][0], game[2][0], game[1][0], game[0][0]])
    ligne = list(reversed(ligne))
    game[0][0], game[1][0], game[2][0], game[3][0], game[4][0] = ligne
    tot_move += nmove

    ligne, nmove = pack5_ligne([game[4][1], game[3][1], game[2][1], game[1][1], game[0][1]])
    ligne = list(reversed(ligne))
    game[0][1], game[1][1], game[2][1], game[3][1], game[4][1] = ligne
    tot_move += nmove

    ligne, nmove = pack5_ligne([game[4][2], game[3][2], game[2][2], game[1][2], game[0][2]])
    ligne = list(reversed(ligne))
    game[0][2], game[1][2], game[2][2], game[3][2], game[4][2] = ligne
    tot_move += nmove

    ligne, nmove = pack5_ligne([game[4][3], game[3][3], game[2][3], game[1][3], game[0][3]])
    ligne = list(reversed(ligne))
    game[0][3], game[1][3], game[2][3], game[3][3], game[4][3] = ligne
    tot_move += nmove

    ligne, nmove = pack5_ligne([game[4][4], game[3][4], game[2][4], game[1][4], game[0][4]])
    ligne = list(reversed(ligne))
    game[0][4], game[1][4], game[2][4], game[3][4], game[4][4] = ligne
    tot_move += nmove

    if tot_move > 0:
        add_random_tile()
        display_game()

        if check_win() and not win_displayed:
            show_win()

        if check_lose():
            print("PERDU !")
            show_game_over()
    return tot_move
########################################################################################################################

########################################################################################################################
#function pour tasser quand une touche est pressée (a,d,w,s/A,D,W,S).
# La touche q/Q pour quitter le jeu.
def key_pressed(event):
    global game_over, win_state

    # bloque le jeu si gagné ou perdu
    if game_over: #perdu
        return
    if game_over or win_state: #gagné
        return

    touche = event.keysym #nom de la touche pressée

    if (touche=="Left" or touche=="a" or touche=="A"): #Déplacement vers la gauche
        print("move LEFT")
        if move_left() > 0:
            display_game()

    if (touche=="Right" or touche=="d" or touche=="D"): #Déplacement vers la droite
        print("move RIGHT")
        if move_right() > 0:
            display_game()

    if (touche=="Up" or touche=="w" or touche=="W"): #Déplacement vers la haut
        print("move UP")
        if move_up() > 0:
            display_game()

    if (touche=="Down" or touche=="s" or touche=="S"): #Déplacement ver le bas
        print("move DOWN")
        if move_down() > 0:
            display_game()

    if (touche=="q" or touche=="Q"): #toucher "q" pour quitter le jeu 2048
        print("touche quit")
        exit()

    if (touche=="r" or touche=="R"): #touche pour recommencer le jeu
        print("recomence")
        restart_game()

########################################################################################################################

########################################################################################################################
#function pour ajouter 2 ou 4 dans une casse vide
def add_random_tile():
    #list de casse vides disponibles
    empty_cells = []

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if game[i][j] == 0: # garde seulment les cases vides
                empty_cells.append((i, j))

    # s'il n'y a plus de case vide on fait rien
    if len(empty_cells) == 0:
        return

    # choisir une case vide au hasard
    i, j = random.choice(empty_cells)

    # On va ajouter le 80% de chance d'avoir 2, 20% d'avoir 4
    if random.random() < 0.8:
        game[i][j] = 2
    else:
        game[i][j] = 4
########################################################################################################################
########################################################################################################################
def check_win(): #function pour verifier si le joueur a gagné
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if game[i][j] == 2048:
                return True
    return False
########################################################################################################################
########################################################################################################################
def check_lose(): #Fonction qui vérifie si le joueur a perdu (plus aucun mouvement possible)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if game[i][j] == 0:
                return False

    for i in range(GRID_SIZE): #verifier horizontal
        for j in range(GRID_SIZE -1):
            if game[i][j] == game[i][j+1]:
                return False

    for j in range(GRID_SIZE): #verifier vertical
        for i in range(GRID_SIZE -1):
            if game[i][j] == game[i+1][j]:
                return False
    return True
########################################################################################################################
########################################################################################################################
def show_game_over(): # Affiche l’écran "Game Over" avec un bouton pour recommencer
    global game_over, game_over_label, retry_button

    game_over = True

    game_over_label = tk.Label(
        frame,
        text="Game Over !",
        font=("Arial", 40, "bold"),
        bg="#FFFFFF",
        fg="#555555"
    )
    game_over_label.place(relx=0.5, rely=0.4, anchor="center")

    retry_button = tk.Button(
        frame,
        text="Réessayer",
        command=restart_game,
        font=("Arial", 12, "bold"),
        bg="#8C7B6B",
        fg="white"
    )
    retry_button.place(relx=0.5, rely=0.55, anchor="center")

    if game_over:
        return
    game_over = True
########################################################################################################################
########################################################################################################################
def show_win(): #function
    global win_label, continue_button, retry_button, win_displayed, win_state

    if win_displayed:
        return

    win_displayed = True
    win_state = True  # pour bloquée le jeu

    win_label = tk.Label(
        frame,
        text="Gagné ! 🎉",
        font=("Arial", 40, "bold"),
        bg="#FFFFFF",
        fg="#4CAF50"
    )
    win_label.place(relx=0.5, rely=0.35, anchor="center")

    continue_button = tk.Button(
        frame,
        text="Continuer",
        command=continue_game,
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white"
    )
    continue_button.place(relx=0.4, rely=0.55, anchor="center")

    retry_button = tk.Button(
        frame,
        text="Recommencer",
        command=restart_game,
        font=("Arial", 12, "bold"),
        bg="#8C7B6B",
        fg="white"
    )
    retry_button.place(relx=0.6, rely=0.55, anchor="center")
########################################################################################################################
########################################################################################################################
def hide_win(): #function pour enlever le message "gagné"

    global win_label, continue_button, retry_button

    if win_label is not None:
        win_label.destroy()
        win_label = None

    if continue_button is not None:
        continue_button.destroy()
        continue_button = None

    if retry_button is not None:
        retry_button.destroy()
        retry_button = None
########################################################################################################################
########################################################################################################################
def continue_game(): #function pour continuer le jeu
    global win_state

    win_state = False
    hide_win()
#================= INTERFACE GRAPHIQUE =================

# Création de la fenêtre principale
window = tk.Tk()
window.title("2048 - Lilibeth")
window.geometry("630x680")  # Taille de la fenêtre agrandie


########################################################################################
# === Cadre supérieur pour le score et les boutons ===
top_frame = tk.Frame(window)
top_frame.pack(pady=(10, 10), ipadx=39)  # Espacement avec la grille

########################################################################################
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
                            height=1, width=12, relief="solid", bd=2,command=restart_game)
new_game_button.pack(side="right",padx=(100,0))
#######################################################################################

#######################################################################################
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

# Création des tuiles graphiques
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        label = tk.Label(
            frame,
            text="",
            font=FONT,
            width=6,
            height=3,
            bg=COLORS[0],
            fg="black",
            relief="solid",
            bd=0.4,
            highlightbackground="black",
            highlightthickness=2
        )
        label.grid(row=i, column=j, padx=10, pady=10)
        cells[i][j] = label

window.bind('<Key>', key_pressed) #appelle key_pressed quand une touche est pressée

# apparition des 2 premières tuiles aletoire au début du jeu
add_random_tile()
add_random_tile()

display_game()
window.mainloop()
