def EinerKomplement_8bits():
    n = int(input("Bitte geben Sie eine Zahl zwischen 0 bis 127"))
    print("Okay, hier sind die Ergebnisse von Zahl " + str(n))
    binaer = []
    while n != 0:
        rest = n % 2
        binaer.append(str(rest))
        n = n // 2
    binaer.reverse()
    actualStelle = 8 - len(binaer)
    while actualStelle > 0:
        binaer.insert(0, '0')  # vorne auffüllen, nicht hinten!
        actualStelle -= 1
    toStr = ''.join(binaer)
    print("Hier ist binäre Darstellung: \n" + str(toStr))

    einerKom = []
    for i in binaer:
        if i == "0":
            einerKom.append(str(1))
        else:
            einerKom.append(str(0))
    text = ''.join(einerKom)
    print("Hier ist Einerkomplementsdarstellung: ")
    return text

print(EinerKomplement_8bits())