from typing import TypeVar

from pyser.core.either import Either, Left, Right
from pyser.core.parser import Parser

T = TypeVar("T")


def sequence(*parsers: Parser[T]) -> Parser[list[T]]:
    def parse(s: str) -> Either[list[T]]:
        values: list[T] = []
        rest = s
        for parser in parsers:
            match parser(rest):
                case Right(value=value, rest=_rest):
                    values.append(value)
                    rest = _rest
                case Left(error=error):
                    return Left(error)
        return Right(values, rest)

    return Parser(parse)


def many(parser: Parser[T]) -> Parser[list[T]]:
    def parse(s: str) -> Either[list[T]]:
        values = []
        rest = s
        while True:
            match parser(rest):
                case Right(value=value, rest=_rest):
                    values.append(value)
                    rest = _rest
                case _:
                    break
        return Right(values, rest)

    return Parser(parse)
