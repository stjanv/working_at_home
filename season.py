def season(number_of_month):
    if number_of_month > 0 and number_of_month <= 2 and number_of_month == 12:
        return 'Winter'
    elif number_of_month > 2 and number_of_month <= 5:
        return 'spring'
    elif number_of_month > 5 and number_of_month <= 8:
        return 'summer'
    elif number_of_month > 8 and number_of_month <= 11:
        return 'autumn'
    else:
        return 'Out of range'


print(season(13))
