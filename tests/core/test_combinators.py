from re import match

from pyser.core.char import char, satisfy
from pyser.core.combinators import sequence
from pyser.core.either import Left, Right


class TestNot:
    def test_empty(self) -> None:
        assert (~char("a"))("") == Right(None, "")

    def test_chars(self) -> None:
        assert isinstance((~char("a"))("a"), Left)
        assert (~char("a"))("A") == Right(None, "A")
        assert (~char("a"))("hoge") == Right(None, "hoge")


class TestOr:
    def test_empty(self) -> None:
        assert isinstance((char("a") | char("b"))(""), Left)

    def test_chars(self) -> None:
        assert (char("a") | char("b") | char("c"))("a") == Right("a", "")
        assert (char("a") | char("b") | char("c"))("b") == Right("b", "")
        assert (char("a") | char("b") | char("c"))("c") == Right("c", "")
        assert isinstance((char("a") | char("c") | char("b"))("A"), Left)
        assert isinstance((char("a") | char("c") | char("b"))("hoge"), Left)


class TestSub:
    def test_empty(self) -> None:
        assert isinstance(
            (satisfy(lambda c: bool(match(r"^[0-9]$", c))) - char("0"))(""), Left
        )

    def test_chars(self) -> None:
        assert (satisfy(lambda c: bool(match(r"^[0-9]$", c))) - char("0"))(
            "2"
        ) == Right("2", "")
        assert isinstance(
            (satisfy(lambda c: bool(match(r"^[0-9]$", c))) - char("0"))("0"), Left
        )
        assert isinstance(
            (satisfy(lambda c: bool(match(r"^[0-9]$", c))) - char("0"))("a"), Left
        )


class TestSequence:
    def test_empty(self) -> None:
        assert isinstance(sequence(char("a"), char("b"))(""), Left)

    def test_chars(self) -> None:
        assert sequence(char("a"), char("b"), char("c"))("abc") == Right(
            ["a", "b", "c"], ""
        )
        assert isinstance(sequence(char("a"), char("b"), char("c"))("ABC"), Left)
        assert isinstance(sequence(char("a"), char("b"), char("c"))("hoge"), Left)
