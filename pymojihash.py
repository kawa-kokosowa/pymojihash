import hashlib
import math
import json


with open('emojis.json') as f:
    EMOJIS = json.loads(f.read())
NUMBER_OF_EMOJIS = len(EMOJIS)


def hash_to_emoji(string_to_hash: str, hash_length=1):
    string_to_hash = string_to_hash.encode('utf8')
    m = hashlib.sha256()
    m.update(string_to_hash)
    hex_hashed = m.hexdigest()
    decimal_hash = int(hex_hashed, 16)
    emoji_index = decimal_hash % math.pow(NUMBER_OF_EMOJIS, hash_length)

    emoji_string = ''
    for n in range(hash_length):
        emoji_string = EMOJIS[int(emoji_index % NUMBER_OF_EMOJIS)] + emoji_string
        emoji_index = emoji_index // NUMBER_OF_EMOJIS

    return emoji_string

print(hash_to_emoji('friend'))
