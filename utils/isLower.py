def isLower(char: str):
    sign_as_ascii = ord(char)
    if (sign_as_ascii >= 97 and sign_as_ascii <= 122):
      return True
    return False

