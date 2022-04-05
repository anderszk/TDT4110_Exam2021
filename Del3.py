beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 1}

matvarer = [['laks', 59, 'middag'], ['kjøttdeig', 25, 'middag'],

            ['ris', 15, 'middag'], ['ost', 99, 'frokost'], ['bønner', 7, 'middag'],

            ['soyasaus', 33, 'middag'],['banan', 4, 'mellommåltid']]

tekst = "Jeg liker laks og ris asdasdjn banan"

#3.1
def finn_pris(matvarer:list ,let_etter:str) -> int:
    for i in matvarer:
        if i[0] == let_etter:
            return i[1]
        else:
            return 0


#3.2
def oppdater_matvare(beholdning:dict, matvare:str,antall:int) -> dict:
    old = int(beholdning[matvare])
    beholdning.update({str(matvare):(old+antall)})
    return beholdning

#3.3
def oppdater_beholdning(beholdning:dict, endringer:list) -> dict:
    for element in endringer:
        oppdater_matvare(beholdning, element, element[1])
    return beholdning


#3.4
def vis_priser(beholdning:dict, matvarer, tekst) -> list:
    return_this = []
    gyldig = tekst.split(" ")
    for i in gyldig:
        for s in matvarer:
            if i == s[0]:
                for k in beholdning:
                    if k == i:
                        return_this.append(tuple([k, beholdning.get(k)]))
    return return_this

#3.5
#Antar at sum og tuple skal returneres i en og samme string
def salg(matvarer:list, beholdning:dict, handleliste: list):
    unique = []
    total = 0
    for i in handleliste:
        print(str(vis_priser(beholdning, matvarer, i)))
        oppdater_beholdning(beholdning, [i,-1])
        total += vis_priser(beholdning,matvarer,i)
        if i not in unique:
            unique.append(i)
    return total, tuple(unique)

print(salg(matvarer,beholdning,['banan', 'ris', 'ost']))

