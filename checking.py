def count(list1, item) :
    qty =0
    index = 0
    for item in list1:
        if list1[index]==item:
            qty+=1
        index +=1
    return qty
    list2=[1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 2,7, 43, 54, 13]
    print(count(list2,1))