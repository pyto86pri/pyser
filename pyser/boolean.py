from pyser.string import string

boolean = string("true").map(lambda _: True) | string("false").map(lambda _: False)
