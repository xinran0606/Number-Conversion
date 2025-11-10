def DezimalZuBinaer(n):
    """Funktion, mit der man Dezimal zu Binärzahl umzuwandeln kann."""
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

def DezimalZuHexadezimal(n):
    """Funktion, mit der man Dezimal zu Hexadezimal umwandeln kann"""
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

def DezimalZuOktal(n):
    """Funktion, mit der man von Dezimal zu Oktal umwandeln kann."""
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

def BinaerZuDezimal(n):
    """Funktion, mit der man Binär in Dezimal umwandeln kann."""
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

def HexZuDezimal(n):
    "Funktion, mit der man Hexadezimal in Dezimal umwandeln kann."
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
                case '1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
                    newHexList.append(int(i))
        newHexList.reverse()
        ergibnis = 0
        listIndex = 0
        for j in newHexList:
            sumNow = j * 16**listIndex
            listIndex += 1
            ergibnis += sumNow
        return ergibnis

def OktalZuDezimal(n):
    "Funktion, mit der man Oktal in Dezimal umwandeln kann."
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

