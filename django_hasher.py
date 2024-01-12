import base64
import hashlib
from hasher import Hasher

class DjangoHasher(Hasher):

    _hmac_type = 'sha256'
    _decode_format = "utf-8"


    @classmethod
    def create_hash(cls, plain_text, rounds, salt):
        if type(rounds) != int:
            rounds = int(rounds)
        encoded_text = plain_text.encode()
        encoded_salt = salt.encode()
        return base64.b64encode(hashlib.pbkdf2_hmac('sha256', encoded_text, salt.encode(), rounds, None)).decode('utf-8').strip()