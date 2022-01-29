def isAlpha(char: str):
    sign_as_ascii = ord(char)
    if (sign_as_ascii >= 97 and sign_as_ascii <= 122) or (sign_as_ascii >= 65 and sign_as_ascii <= 90):
      return True
    return False

