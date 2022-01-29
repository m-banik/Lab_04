# Funkcja pisana w pośpiechu. Zdaję sobie sprawę, że wymaga optymalizacji.
def code_series_length(input_text: str):
    if len(input_text) == 0:
        return "0"
    elif len(input_text) == 1:
        return "1" + input_text
    result = ""
    iterator = 1
    for i in range(1, len(input_text)):
        if i == len(input_text) - 1:
            if input_text[i - 1] != input_text[i]:
                result += str(iterator) + input_text[i - 1]
                iterator  = 0
            result += str(iterator + 1) + input_text[i]
            break
        elif input_text[i - 1] != input_text[i]:
            result += str(iterator) + input_text[i - 1]
            if i == len(input_text) - 1:
                result += "1" + input_text[i]
                break
            else:
              iterator = 1
        else:
          iterator += 1
    return result

