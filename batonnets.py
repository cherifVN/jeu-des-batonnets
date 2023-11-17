batonnets = 21
player = 1
print("Jeu des batonnets: le but est de retirer des batonnets (il y en a 21) et celui qui retire le dernier a perdu")
print(f"Tour du joueur {player}")
def main():
    global batonnets    
    retirer = input("Combien voulez-vous enlever de bâtonnets (1, 2 ou 3): ")
    try:
        retirer = int(retirer)
    except ValueError:
        print("Vous n'avez pas saisi un nombre valide.")
        main()
        return

    if retirer > 3 or retirer < 1:    
        print("Veuillez retirer soit 1, 2 ou 3 bâtonnets.")
        main()
        return

    elif retirer > batonnets :
            print(f"Il n'y a pas assez de bâtonnets pour en retirer {retirer}")
            main()
            return
    else:
        batonnets -= retirer
        print(f"Il reste {batonnets} bâtonnets.")
        
        if batonnets == 0:
            global player
            print(f"Le joueur {player} a perdu, son adversaire a donc gagné. BRAVO!")
        else:
            switch_player()

def switch_player():
    global player
    if player == 1:
        player = 2
    elif player == 2:
        player = 1 
    print(f"Tour du joueur {player}")
    main()

main()