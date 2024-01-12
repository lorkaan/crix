

class HashParts:

    hash_separator = '$'

    _type_index = 0
    _rounds_index = 1
    _salt_index = 2
    _cipher_text_index = 3

    @classmethod
    def create_object(cls, hash_text):
        if hash_text.startswith(cls.hash_separator):
            hash_text = hash_text[1:]
        cipher_parts = hash_text.split(cls.hash_separator)
        hash_type = cipher_parts[cls._type_index]
        rounds = cipher_parts[cls._rounds_index]
        salt = cipher_parts[cls._salt_index]
        cipher_text = cipher_parts[cls._cipher_text_index]
        return cls(hash_type, cipher_text, rounds, salt)

    def __init__(self, hash_type, cipher_text, rounds, salt):
        self.type = hash_type
        self.cipher_text = cipher_text
        self.rounds = rounds
        self.salt = salt

class Hasher:
    
    hash_parts = HashParts

    @classmethod
    def create_hash(cls, plain_text, random, salt):
        return plain_text

    """
    Finds a plain text that produces the same hash as given.


    """
    @classmethod
    def find_hash(cls, filepath, hash_text, hash_parts_flag=False):
        hash_part_obj = cls.hash_parts.create_object(hash_text)
        with open(filepath, 'r') as file:
            line = file.readline()
            while line:
                if line.endswith('\n'):
                    line = line[0:-1]
                cur_hashed = cls.create_hash(line, hash_part_obj.rounds, hash_part_obj.salt)
                if hash_parts_flag:
                    hashed = cls.hash_parts.create_object(cur_hashed)
                    cur_hashed = hashed.cipher_text
                if cur_hashed == hash_part_obj.cipher_text:
                    return line
                else:
                    line = file.readline()
        return None

