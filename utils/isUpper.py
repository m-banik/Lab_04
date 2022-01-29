def isUpper(char: str):
    sign_as_ascii = ord(char)
    if (sign_as_ascii >= 65 and sign_as_ascii <= 90):
      return True
    return False

