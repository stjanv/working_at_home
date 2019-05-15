# 1.1 task
print("--------------------------------------1.2 task-------------------------------------")
list1 = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
l = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
print(l)
print(max(l))
print(l.index(max(l)))
print(min(l))
print(l.index(min(l)))
# 1.2 task
print("--------------------------------------1.2 task------------------------------------")
list1 = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
def count(seaquence):
    listSorted = set(list1)
    most_coming = None
    qty_most_coming = 0
    print(listSorted)
    for item in listSorted:
        qty = list1.count(item)
        if qty > qty_most_coming:
            qty_most_coming = qty
            most_coming = item
    print(most_coming)
    print(list1)
    for item in list1:
        if item==most_coming:
            list1.remove(item)
    print(list1)
    return most_coming
j=1
while j<4:
    count(list1)
    j+=1
# 1.3.1 task
print("--------------------------1.3.1 task---------------------------------")
list1 = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
listSorted=list(set(list1))
print(list1)
print(listSorted)
# 1.3.2 task
print("---------------------------1.3.2 task-----------------------------------")
seen = {}
new_list = [seen.setdefault(x, x) for x in list1 if x not in seen]
print(new_list)