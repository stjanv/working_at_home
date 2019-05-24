list1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]


def swap(list1):
    list1_index_x = 2
    list1_index_y = 3
    list1[list1_index_x], list1[list1_index_y] = list1[list1_index_y], list1[list1_index_x]
    return list1


print(swap(list1))


def mutka(list3):
    list3 = []
    for i in range(len(list1)):
        list3.append(bin(i))
    return list3


def mutka2(list2):
    list3 = []
    for i in list2:
        calk = 0
        for j in i:
            if j == '1':
                calk += 1
        if calk >= 2 and calk % 2 == 0:
            list3.append(i)

    return list3


def mutka3(list1, list2):
    calk = 0
    calk2 = 0
    for i in range(len(list1)):
        if bin(i) == list2[calk]:
            calk2 += list1[i]
            calk += 1
    return calk2


list2 = mutka(list1)
print(list2)
print(mutka2(list2))
print(mutka3(list1, list2)*(list1[len(list2)-2]))

a=input()

def check_for_registry(a):
    for i in a:
        if i.istitle():
            break
            return False
    return True

def check_for_
def check(a:str):
    if len(a)>4 and check_for_registry(a) and
