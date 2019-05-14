def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        d = 3
        while d * d <= number:
            if number % 3 == 0:
                return False
            d += 2

    return True


print(is_prime(234))
