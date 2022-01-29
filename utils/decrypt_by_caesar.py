from common.variables import key
from utils.encrypt_by_caesar import encrypt_by_caesar


def decrypt_by_caesar(text:str, used_key: int = key):
    used_key = used_key * -1
    decrypted = encrypt_by_caesar(text, used_key)
    return decrypted

