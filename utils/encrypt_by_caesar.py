from common.variables import key
from utils.isAlpha import isAlpha
from utils.isLower import isLower
from utils.isUpper import isUpper


def encrypt_by_caesar(text:str, used_key: int = key):
    encrypted = ""
    for i in range(0, len(text)):
        if isAlpha(text[i]) is True:
            as_ascii = ord(text[i])
            if isLower(text[i]) is True:
                if as_ascii + used_key > 122:
                    if used_key > 0:
                        encrypted +=  chr(96 + used_key - 122 + as_ascii)
                    else:
                        encrypted +=  chr(96 + 122 - as_ascii + used_key)
                elif as_ascii + used_key < 97:
                    if used_key > 0:
                        encrypted +=  chr(122 - used_key)
                    else:
                        encrypted +=  chr(122 - 96 + as_ascii + used_key)
                else:
                    encrypted +=  chr(as_ascii + used_key)
            elif isUpper(text[i]) is True:
                if as_ascii + used_key > 90:
                    if used_key > 0:
                        encrypted +=  chr(64 + used_key - 90 + as_ascii)
                    else:
                        encrypted +=  chr(64 + 90 - as_ascii + used_key)
                elif as_ascii + used_key < 65:
                    if used_key > 0:
                        encrypted +=  chr(90 - used_key)
                    else:
                        encrypted +=  chr(90 - 64 + as_ascii + used_key)
                else:
                    encrypted +=  chr(as_ascii + used_key)
            else:
                encrypted +=  chr(as_ascii + used_key)
        else:
            encrypted += text[i]
    return encrypted

