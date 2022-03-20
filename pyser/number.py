from re import match

from iteration_utilities import deepflatten

from pyser.core.char import char, satisfy
from pyser.core.combinators import many, sequence

digit = satisfy(lambda c: bool(match(r"^[0-9]$", c)))
non_zero_digit = satisfy(lambda c: bool(match(r"^[1-9]$", c)))

zero_number = char("0").map(lambda _: 0)
non_zero_number = sequence(non_zero_digit, many(digit)).map(
    lambda ss: int("".join(deepflatten(ss)))
)
number = zero_number | non_zero_number

sign = char("+").map(lambda _: 1) | char("-").map(lambda _: -1)
integer = number | sequence(sign, number).map(lambda ns: ns[0] * ns[1])
