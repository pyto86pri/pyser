from typing import Callable, TypeVar

from pyser.core.either import Either, Left, Right
from pyser.core.parser import Parser
from pyser.core.primitives import any_char

T = TypeVar("T")
U = TypeVar("U")


def parse_char(char: str, s: str) -> Either[str]:
    match any_char(s):
        case Right(value=value, rest=rest):
            if value != char:
                return Left(Exception(""))
            return Right(value, rest)
        case left:
            return left


def char(char: str) -> Parser[str]:
    return Parser(lambda s: parse_char(char, s))


def parse_satisfy(f: Callable[[str], bool], s: str) -> Either[str]:
    match any_char(s):
        case Right(value=value, rest=rest):
            if not f(value):
                return Left(Exception(""))
            return Right(value, rest)
        case left:
            return left


def satisfy(f: Callable[[str], bool]) -> Parser[str]:
    return Parser(lambda s: parse_satisfy(f, s))
