def parse_integer_to_another_number_system(integer: int, k: int):
    if k < 2 or k > 36:
        print("Podano nieprawdiłową wartość! Obsługiwany przedział to 2-36.")
        return
    is_number_negative = integer < 0
    if is_number_negative is True:
        integer *= -1
    rests = ""
    while True:
        if integer >= 1:
            rest = integer % k
            # Ponieważ mamy pracować algorytmicznie, poniżej parsuję
            # część całkowitą liczby trochę "łopatologicznie"...
            if rest >= 10:
                whole_number = ""
                for sign in str(rest):
                    if sign == ".":
                        break
                    whole_number += sign
                rests += chr(65 + int(whole_number) - 10)
            else:
                rests += str(rest)[0]
            integer = integer / k
            continue
        break
    result = ""
    for i in range(len(rests) -1, -1, -1):
        result += rests[i]
    if is_number_negative is True:
        result = "-" + result
    # Jako string, bo niektóre systemy zawierają też litery.
    return result

