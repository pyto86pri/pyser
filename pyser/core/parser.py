from typing import Callable, Generic, TypeVar

from pyser.core.either import Either, Left, Right

T = TypeVar("T")
U = TypeVar("U")

ParseFunc = Callable[[str], Either[T]]


class Parser(Generic[T]):
    def __init__(self, parse: ParseFunc[T]) -> None:
        self._parse = parse

    def __call__(self, s: str) -> Either[T]:
        return self._parse(s)

    def __invert__(self) -> "Parser[None]":
        def parse(s: str) -> Either[None]:
            match self(s):
                case Right():
                    return Left(Exception(""))
                case _:
                    return Right(None, s)

        return Parser(parse)

    def __or__(self, other: "Parser[U]") -> "Parser[T | U]":
        def parse(s: str) -> Either[T | U]:
            match self(s):
                case Right(value=value, rest=rest):
                    return Right(value, rest)
            match other(s):
                case Right(value=value, rest=rest):
                    return Right(value, rest)
            return Left(Exception(""))

        return Parser(parse)

    def __sub__(self, other: "Parser[U]") -> "Parser[T]":
        def parse(s: str) -> Either[T]:
            match (self(s), other(s)):
                case (Right(value=value, rest=rest), Left()):
                    return Right(value, rest)
                case (Right(), Right()):
                    return Left(Exception(""))
                case (Left(error=error), _):
                    return Left(error)
                case _:
                    raise Exception("unreachable")

        return Parser(parse)

    def map(self, f: Callable[[T], U]) -> "Parser[U]":
        def parse(s: str) -> Either[U]:
            match self(s):
                case Right(value=value, rest=rest):
                    return Right(f(value), rest)
                case Left(error=error):
                    return Left(error)
                case _:
                    raise Exception("unreachable")

        return Parser(parse)
