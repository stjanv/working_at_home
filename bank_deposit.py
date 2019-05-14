def deposit(count_of_money, years):
    i = 1
    while i <= years:
        count_of_money = count_of_money+(count_of_money*0.1)
        i += 1
    return count_of_money


print(deposit(1000, 2))
