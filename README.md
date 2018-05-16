# Python 3 String to Emoji Hash

[![Build
Status](https://travis-ci.org/lily-fyi/pymojihash.svg?branch=master)](https://travis-ci.org/lily-fyi/pymojihash)

Hash a unicode string to emoji.

Based on the npm package [hash-emoji by
earobinson](https://github.com/earobinson/hash-emoji).

[View a live demo on my website bubblebbs.cafe!](http://bubblebbs.cafe)

![pymojihash in action on bubblebbs.cafe!](https://i.imgur.com/7FlSOop.png)

You can run tests simply by running `pytest`.

## Examples

`hash_to_emoji()` is the wonderful hashing function.

In this example a string is hashed to a single emoji:

```python
from pymojihash import hash_to_emoji
hash_to_emoji('lol')
'🇫🇲'
```

There is a limited number of emojis outputs (see: `emojis.json` in this
package) so if you increase the `hash_length` the less likely you are to
encounter different values which produce the same output/hash/emoji(s):

```python
hash_to_emoji('lol', 4)
'◼️🍕🍐🇫🇲'
hash_to_emoji('lol', 2)
'🍐🇫🇲'
hash_to_emoji('heck', 2)
'♠️🇨🇦'
```
