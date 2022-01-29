def decode_series_length(input_text: str):
    if len(input_text) == 0:
        return ""
    elif len(input_text) == 1:
        return input_text
    result = ""
    iterator = 0
    for sign in input_text:
        if sign in "0123456789":
            iterator = int(sign)
            continue
        for _ in range(0, iterator):
            result += sign
    return result

