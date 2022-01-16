# python-mnemonic
🐍 Mnemonic code for generating deterministic keys, BIP39


Installation
To install this library and its dependencies use:

pip install mnemonic
Usage examples
Import library into python project via:

from mnemonic import Mnemonic
Initialize class instance, picking from available dictionaries:

english
chinese_simplified
chinese_traditional
french
italian
japanese
korean
spanish
mnemo = Mnemonic(language)
mnemo = Mnemonic("english")
Generate word list given the strength (128 - 256):

words = mnemo.generate(strength=256)
Given the word list and custom passphrase (empty in example), generate seed:

seed = mnemo.to_seed(words, passphrase="")
Given the word list, calculate original entropy:

entropy = mnemo.to_entropy(words)
