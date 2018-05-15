"""Hash (unicode) strings to emoji(s). You can set the length.

Importing is as easy as `from pymojihash import hash_to_emoji`!
`hash_to_emoji()` is the wonderful hashing function.

In this example a string is hashed to a single emoji:
    >>> hash_to_emoji('lol')
    '🇫🇲'

There is a limited number of emojis outputs (see: `emojis.json` in this package) so if you increase the `hash_length` the less likely youa re to encounter different values which produce the same output/hash/emoji(s):
    >>> hash_to_emoji('lol', 4)
    '◼️🍕🍐🇫🇲'
    >>> hash_to_emoji('lol', 2)
    '🍐🇫🇲'
    >>> hash_to_emoji('heck', 2)
    '♠️🇨🇦'

"""

import hashlib
import math
import json
import pkgutil


EMOJIS = json.loads(pkgutil.get_data('pymojihash', 'emojis.json'))
NUMBER_OF_EMOJIS = len(EMOJIS)


def hash_to_emoji(string_to_hash: str, hash_length: int = 1):
    """Hash a string to emoji(s).

    Arguments:
        string_to_hash: What you want to make the hash/emojis from!

    Returns:
        str: Unicode/emoji(s)

    """

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
