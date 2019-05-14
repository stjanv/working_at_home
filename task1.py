# 1.1 task
list1 = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
l = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
print(l)
print(max(l))
print(l.index(max(l)))
print(min(l))
print(l.index(min(l)))
# 1.2 task
print("new")
listSorted = set(list1)
most_coming = None
qty_most_coming = 0

for item in listSorted:
    qty = list1.count(item)
    if qty > qty_most_coming:
        qty_most_coming = qty
        most_coming = item
print(most_coming)
# 1.3.1 task
print("new")
listSorted=set(list1)
print(list1)
print(listSorted)