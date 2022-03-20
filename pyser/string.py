from re import match

from pyser.char import char, satisfy
from pyser.core.combinators import sequence
from pyser.core.parser import Parser

upper_alpha = satisfy(lambda c: bool(match(r"^[A-Z]$", c)))
lower_alpha = satisfy(lambda c: bool(match(r"^[a-z]$", c)))
alpha = upper_alpha | lower_alpha


def string(s: str) -> Parser[str]:
    return sequence(*[char(c) for c in str.split("")]).map(lambda cs: "".join(cs))
