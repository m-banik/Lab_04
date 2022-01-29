from utils.encrypt_by_caesar import encrypt_by_caesar
from utils.decrypt_by_caesar import decrypt_by_caesar
from utils.parse_integer_to_another_number_system import parse_integer_to_another_number_system
from utils.parse_integer_to_decimal_system import parse_integer_to_decimal_system
from utils.code_series_length import code_series_length
from utils.decode_series_length import decode_series_length


print()
print("Zadanie 1")
print()

# Poniżej testy. Zachęcam też to własnych prób walidacji tych funkcji.
test_texts = ["WARSZAWA", "Wrocław", "Gdańsk", "PoznaŃ", "Zakopane", "xYzQ*%"]
first_test_endoced_texts = ["UYPQXYUY", "Upmałyu", "Ebyńqi", "NmxlyŃ", "Xyimnylc", "vWxO*%"]
second_test_endoced_texts = ["YCTUBCYC", "Ytqełcy", "Ifcńum", "RqbpcŃ", "Bcmqrcpg", "zAbS*%"]
test_keys = [-2, 2]

for key in test_keys:
    for i in range(0, len(test_texts)):
        print("Dla klucza " + str(key) + " tekst " + test_texts[i] + ":")
        encoded = encrypt_by_caesar(test_texts[i], key)
        print("Zakodowany:", encoded)
        decoded = decrypt_by_caesar(encoded, key)
        print("Odkodowany:", decoded)
        try:
            if key == test_keys[0]:
                assert encoded == first_test_endoced_texts[i]
            else:
                assert encoded == second_test_endoced_texts[i]
            assert decoded == test_texts[i]
            print("Kodowanie w obie strony zadziałało prawidłowo.")
        except AssertionError:
            print("Kodowanie w obie strony się nie powiodło!")
        print()


print()
print("Zadanie 2")
print()

# Przy tym zadaniu nie jestem pewien prawidłowości działania dla liczb szczególnie
# małych(np. 25 w systemie o podstawie 26). Nie udało mi się zebrać więcej danych, 
# ale wydaje się, że w takich wypadkach powinno się podawać wartość po przecinku. 
# W niniejszym zadaniu takie przypadki pozostały nieobsłużone.
while True:
    try:
        # Np. 46532(liczba znaleziona w prezentacji z wykładu.)
        number_to_be_converted = int(input("Proszę podać liczbę do konwersji: "))
        break
    except ValueError:
        print("Podano nieprawidłową liczbę całkowitą!")

print("Testowa liczba " + str(number_to_be_converted) + " w kolejnych systemach liczbowych:")

numbers_in_given_number_system: list[int] = []
for i in range(2, 37):
    number_in_given_number_system = parse_integer_to_another_number_system(number_to_be_converted, i)
    numbers_in_given_number_system.append(number_in_given_number_system)
    print(i, number_in_given_number_system)


print()
print("Zadanie 3")
print()

print("Trwają testy porównawcze z " + str(number_to_be_converted) + "...")

try:
    for i in range(0, len(numbers_in_given_number_system)):
        number_as_decimal = parse_integer_to_decimal_system(numbers_in_given_number_system[i], i + 2)
        assert number_as_decimal == number_to_be_converted
    print("Liczby we wszystkich systemach zostały zamienione na system dziesiętny prawidłowo.")
except AssertionError:
    print("Testy dekodowania na system dziesiętny nie przeszły pomyślnie!")


print()
print("Zadanie 4 i 5")
print()

encoded_text = code_series_length("AAAAAABBBAAABBA")
print(encoded_text)
decoded_text = decode_series_length(encoded_text)
print(decoded_text)
print()

encoded_text = code_series_length(" aBc|")
print(encoded_text)
decoded_text = decode_series_length(encoded_text)
print(decoded_text)
print()

encoded_text = code_series_length("abcdefgh ")
print(encoded_text)
decoded_text = decode_series_length(encoded_text)
print(decoded_text)
print()

encoded_text = code_series_length("AbbCCCddddEEEEE...")
print(encoded_text)
decoded_text = decode_series_length(encoded_text)
print(decoded_text)
print()

encoded_text = code_series_length("//AbbCCCddddEEEEE-+--")
print(encoded_text)
decoded_text = decode_series_length(encoded_text)
print(decoded_text)