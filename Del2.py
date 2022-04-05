#2A
def alfa(text: str, num: float) -> str:
    if num <= 0:
        return min(text)
    else:
        return max(text)


#2B
def ant_land(geografi) -> int:
    return len(geografi.keys())


#2C
def sjekktall(tall) -> str:
    if tall-int(tall) != 0:
        return "des"
    else:
        if tall%2 == 0:
            return "par"
        elif tall%2 != 0:
            return "odde"

#2DEF

list1 = [1,4,4,3,5,5,5,3,2]

#2G
def fjern_dup(liste) -> None:
    list1 = []

    for index, element in enumerate(liste):
        if element != liste[index-1] or index == 0:
            list1.append(element)

    liste[:] = list1

fjern_dup(list1)
print(list1)

#2H


def list_str(s:str) -> list:
    return_this = []
    for index, element in enumerate(s):
        if element.lower() == "a" and len(s) > index+8:
            if s[index+7] == "a":
                return_this.append(s[index-1])
    return return_this

print(list_str("abcdefSabcdefOabcdefSabcdef"))

#2I
def sjekk_to(streng:str) -> int:
    flag = 0
    if int(streng[0:2]) <= 25 and int(streng[2:4]) <= 18 and int(streng[4:6]) <= 56:
        flag = 1

    elif int(streng[0:2]) > 25 and int(streng[2:4]) <= 18 and int(streng[4:6]) <= 56:
        flag = 2
    elif int(streng[0:2]) <= 25 and int(streng[2:4]) > 18 and int(streng[4:6]) <= 56:
        flag = 3
    elif int(streng[0:2]) <= 25 and int(streng[2:4]) <= 18 and int(streng[4:6]) > 56:
        flag = 5

    elif int(streng[0:2]) > 25 and int(streng[2:4]) > 18 and int(streng[4:6]) <= 56:
        flag = 6
    elif int(streng[0:2]) > 25 and int(streng[2:4]) <= 18 and int(streng[4:6]) > 56:
        flag = 10
    elif int(streng[0:2]) > 25 and int(streng[2:4]) > 18 and int(streng[4:6]) > 56:
        flag = 30
    return flag

