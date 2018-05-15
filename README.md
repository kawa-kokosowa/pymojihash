# Python 3 String to Emoji Hash

Hash a unicode string to emoji.

Based on the npm package [hash-emoji by
earobinson](https://github.com/earobinson/hash-emoji).

You can run tests simply by running `pytest`.

## Examples

`hash_to_emoji()` is the wonderful hashing function.

In this example a string is hashed to a single emoji:

```
from pymojihash import hash_to_emoji
hash_to_emoji('lol')
bleh
```

There is a limited number of emojis outputs (see: `emojis.json` in this
package) so if you increase the `hash_length` the less likely youa re to
encounter different values which produce the same output/hash/emoji(s):

```
hash_to_emoji('lol', 4)
jaslfdk
hash_to_emoji('lol', 2)
jaslfdk
hash_to_emoji('heck', 2)
jaslfdk
```
