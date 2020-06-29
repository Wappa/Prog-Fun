from tkinter import*

# Construction de la fenetre principale «root»
root = Tk()
root.title('Password Manager')

root.geometry('300x300')
# Construction d'un simple bouton
qb = Button(root, text='Quitter', command=root.quit)

# Placement du bouton dans «root»
qb.pack()

# Lancement de la «boucle principale»
root.mainloop()