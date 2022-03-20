from pyser.core.either import Either, Left, Right
from pyser.core.parser import Parser


def parse_any_char(s: str) -> Either[str]:
    if len(s) == 0:
        return Left(Exception(""))
    return Right(s[0], s[1:])


any_char = Parser(parse_any_char)


def parse_eof(s: str) -> Either[None]:
    if len(s) > 0:
        return Left(Exception(""))
    return Right(None, "")


eof = Parser(parse_eof)
