import re

def DezimalZuBinaer():
    """Funktion, mit der man Dezimal zu Binärzahl umzuwandeln kann."""
    while True:
        number = input("Bitte geben Sie eine Integer: ")
        try:
            n = int(number)
            break
        except ValueError:
            print("Falsche Eingabe. Bitte geben Sie eine Integer.")

    if n == 0:
        return 0
    else:
        binaer = []
        while n != 0:
            rest = n % 2
            binaer.append(str(rest))
            n = n // 2
        binaer.reverse()
        text = ''.join(binaer)
        return text

def DezimalZuHexadezimal():
    """Funktion, mit der man Dezimal zu Hexadezimal umwandeln kann"""
    while True:
        number = input("Bitte geben Sie eine Integer: ")
        try:
            n = int(number)
            break
        except ValueError:
            print("Falsche Eingabe. Bitte geben Sie eine Integer.")

    if n == 0:
        return 0
    else:
        hex = []
        while n != 0:
            rest = n % 16
            match rest:
                case 10:
                    hex.append('A')
                case 11:
                    hex.append('B')
                case 12:
                    hex.append('C')
                case 13:
                    hex.append('D')
                case 14:
                    hex.append('E')
                case 15:
                    hex.append('F')
                case 1|2|3|4|5|6|7|8|9:
                    hex.append(str(rest))
            n = n // 16
        hex.reverse()
        text = ''.join(hex)
        return text

def DezimalZuOktal():
    """Funktion, mit der man von Dezimal zu Oktal umwandeln kann."""
    while True:
        number = input("Bitte geben Sie eine Integer: ")
        try:
            n = int(number)
            break
        except ValueError:
            print("Falsche Eingabe. Bitte geben Sie eine Integer.")

    if n == 0:
        return 0
    else:
        okt = []
        while n != 0:
            rest = n % 8
            okt.append(str(rest))
            n = n // 8
        okt.reverse()
        text = ''.join(okt)
        return text

def BinaerZuDezimal():
    """Funktion, mit der man Binär in Dezimal umwandeln kann."""
    while True:
        n = input("Bitte geben Sie eine Binäre Zahl ein: ")
        if re.fullmatch(r'[01]+', n):
            print("Gültige Eingabe:", n)
            break
        else:
            print("Ungültige Eingabe! Bitte nur 0 oder 1 eingeben.")

    if n == 0:
        return 0
    else:
        bits = [int(x) for x in str(n)]
        bits.reverse()
        ergibnis = 0
        listIndex = 0
        for i in bits:
            sumNow = i * 2**listIndex
            listIndex += 1
            ergibnis += sumNow
        return ergibnis

def HexZuDezimal():
    "Funktion, mit der man Hexadezimal in Dezimal umwandeln kann."
    while True:
        n = input("Bitte geben Sie eine Hexadezimalzahl ein: ")
        if re.fullmatch(r'[0-9A-F]+', n):
            print("Gültige Eingabe:", n)
            break
        else:
            print("Ungültige Eingabe! Bitte nur 0-9 und A-F eingeben.")

    if n == 0:
        return 0
    else:
        hexsStrList = [x for x in str(n)]
        newHexList = []
        for i in hexsStrList:
            match i:
                case 'A':
                    newHexList.append(10)
                case 'B':
                    newHexList.append(11)
                case 'C':
                    newHexList.append(12)
                case 'D':
                    newHexList.append(13)
                case 'E':
                    newHexList.append(14)
                case 'F':
                    newHexList.append(15)
                case '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
                    newHexList.append(int(i))
        newHexList.reverse()
        ergibnis = 0
        listIndex = 0
        for j in newHexList:
            sumNow = j * 16**listIndex
            listIndex += 1
            ergibnis += sumNow
        return ergibnis

def OktalZuDezimal():
    "Funktion, mit der man Oktal in Dezimal umwandeln kann."
    while True:
        n = input("Bitte geben Sie eine Oktaldarstellung ein: ")
        if re.fullmatch(r'[0-7]+', n):
            print("Gültige Eingabe:", n)
            break
        else:
            print("Ungültige Eingabe! Bitte nur 0-7 eingeben.")

    if n == 0:
        return 0
    else:
        oktal = [int(x) for x in str(n)]
        oktal.reverse()
        ergibnis = 0
        listIndex = 0
        for i in oktal:
            sumNow = i * 8 ** listIndex
            listIndex += 1
            ergibnis += sumNow
        return ergibnis

if __name__ == "__main__":
    print("Taschenrechner startet.")
    print("------------------------------------------------------------")
    print("1: Dezimal zu Binär\n" 
          "2: Dezimal zu Hexadezimal\n" 
          "3: Dezimal zu Oktal\n"
          "4: Binär zu Dezimal\n"
          "5: Hexadezimal zu Dezimal\n"
          "6: Oktal zu Dezimal\n")
    while True:
        n = int(input("Bitte geben Sie an, welche modul SIe anwenden wollen:"))
        if n == 1:
            print(DezimalZuBinaer())
            break
        elif n == 2:
            print(DezimalZuHexadezimal())
            break
        elif n == 3:
            print(DezimalZuOktal())
            break
        elif n == 4:
            print(BinaerZuDezimal())
            break
        elif n == 5:
            print(HexZuDezimal())
            break
        elif n == 6:
            print(OktalZuDezimal())
            break
        else:
            print("Ungültige Eingabe! Bitte nur 1-6 eingeben.")