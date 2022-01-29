from utils.isUpper import isUpper


def parse_integer_to_decimal_system(integer: str, k: int):
    if k < 2 or k > 36:
          print("Podano nieprawdiłową wartość! Obsługiwany przedział to 2-36.")
          return
    is_number_negative = integer[0] == "-"
    if is_number_negative is True:
        integer_copy = ""
        for i in range(1, len(integer)):
            integer_copy += integer[i]
        integer = integer_copy
    result = 0
    integer_as_string = str(integer)
    index = len(integer_as_string) - 1
    for i in integer_as_string:
        power = 1
        for _ in range(0, index):
          power *= k
        if isUpper(i):
            result += (10 + ord(i) - 65) * power
        else:
            result += int(i)*power
        index -= 1
    if is_number_negative is True:
        result *= -1
    return result

