import shunting_yard
import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Algorithme Shunting Yard ")

tk.Label(fenetre, text="Entrez une expression mathématique :").pack()

champ_expression = tk.Entry(fenetre, width=40)
champ_expression.pack()

def conversion():
    expression = champ_expression.get()
    try:
        tokens = shunting_yard.tokenize(expression)
        postfix = shunting_yard.infix_to_postfix(tokens)
        resultat = shunting_yard.evaluate_postfix(postfix)
        label_postfix.config(text=f"Notation postfixée : {' '.join(postfix)}")
        label_resultat.config(text=f"Résultat : {resultat}")
    except ValueError as e:
        label_resultat.config(text=f"Erreur : {e}")

bouton_convertir = tk.Button(fenetre, text="Convertir et évaluer", command=conversion)
bouton_convertir.pack()
label_postfix = tk.Label(fenetre, text="Notation postfixée : ")
label_postfix.pack()
label_resultat = tk.Label(fenetre, text="Résultat : ")
label_resultat.pack()

fenetre.mainloop()