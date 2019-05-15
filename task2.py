from collections import Counter
a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
#2.3 task
print("--------------------------task 2.3-------------------------------")
c=(a,b)
print(c)
d={}
for Dict in c:
    for key in Dict:
        try:
            d[key]+=Dict[key]
        except:
            d[key]=Dict[key]
print(d)
#2.1 task
print("----------------------------task 2.1-------------------------------")
list_for_a=[]
list_for_b=[]
for key in a:
    list_for_a.append(key)
print(list_for_a)
for key in b:
    list_for_b.append(key)
print(list_for_b)
for item in list_for_b:
    list_for_a.append(item)
print(list_for_a)
list_for_a.sort()
for item in range(0,len(list_for_a)-1):
    if list_for_a[item]==list_for_a[item+1]:
        print ("'"+ str(list_for_a[item]) +"'"+' are in both dict')
#task 2.2
print("----------------------task 2.2-------------------------")
list_for_a=[]
list_for_b=[]
for key in a:
    list_for_a.append(key)
print(list_for_a)
for key in b:
    list_for_b.append(key)
print(list_for_b)
list_for_b.sort()
list_for_a.sort()
list_for_origin=[]
for item in range(0,len(list_for_b)):
    count1 = 0
    for jtem in range(0,len(list_for_a)):
        if list_for_b[item] == list_for_a[jtem]:
            count1=+1
    if count1==0:
        print("'" + str(list_for_b[item]) + "'" + 'origin')

