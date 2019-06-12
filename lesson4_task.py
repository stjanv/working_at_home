from operator import itemgetter
import collections

list1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]


# task1


def swap(list1):
    list1_index_x = 2
    list1_index_y = 3
    list1[list1_index_x], list1[list1_index_y] = list1[list1_index_y], list1[list1_index_x]
    return list1


print(swap(list1))


# task2


def take_bin(list1):
    list3 = [bin(i) for i in range(len(list1))]
    return list3


def take_whole_nums(list2):
    list3 = []
    for i in list2:
        calk = i.count('1')
        if calk >= 2 and calk % 2 == 0:
            list3.append(i)
    return list3


def return_res(list3, list1, list2):
    summ = 0
    for i in list3:
        for j in list2:
            if i == j:
                summ += list1[list2.index(j)]
    return summ * list1[len(list1) - 1]


list2 = take_bin(list1)
print(list2)
list3 = take_whole_nums(list2)
print(list3)
print(return_res(list3, list1, list2))


# task 3


# a = input()
def check_for_registry(a):
    g = True
    for i in a:
        if i.isupper():
            g = False
    return g


def check_for_cheet(a):
    k = 0
    n = 0
    for i in a:
        if i.isdigit():
            k += 1
        else:
            n += 1
    if k % 2 == 0 and n % 2 == 1:
        return True
    else:
        return False


def check(a: str):
    if len(a) > 4 and check_for_registry(a) and check_for_cheet(a):
        print('Pass is successful')
    else:
        print('Pass is incorrect')


# print(check_for_registry(a))
# print(check_for_cheet(a))
# check(a)

# task4
autos = [

    {"brand": "Ford", "model": "Mustang", "year": 1964, "price": 4000},

    {"brand": "Ford", "model": "Mondeo", "year": 1999, "price": None},

    {"brand": "Ford", "model": "Fiesta", "year": 2003, "price": 4200},

    {"brand": "Nissan", "model": "Primera", "year": 1997, "price": 3100},

    {"brand": "BMW", "model": "X3", "year": 2001, "price": 5000},

    {"brand": "Nissan", "model": None, "year": 1964, "price": None},

    {"brand": "VW", "model": "Passat", "year": 1996, "price": 1200},

    {"brand": "BMW", "model": "X5", "year": 2010, "price": 7500},

    {"brand": "Renault", "model": "Megane", "year": 1999, "price": 2300}

]


def by_key(autos):
    for i in range(len(autos)):
        for j in range(len(autos)-1):
            if autos[j]['price'] is None:
                continue
            if autos[i]['price'] is None:
                autos[i], autos[j] = autos[j], autos[i]

            elif autos[i]['price'] < autos[j]['price']:
                autos[i], autos[j] = autos[j], autos[i]
    return autos


autos = sorted(autos, key=lambda x: x['price'] if x['price'] else 0, reverse=True)
print(autos)

autos = by_key(autos)[::-1]
print(autos)
