from pyser.core.either import Left, Right
from pyser.core.primitives import any_char, eof


class TestAnyChar:
    def test_empty(self) -> None:
        assert isinstance(any_char(""), Left)

    def test_one_char(self) -> None:
        assert any_char("a") == Right("a", "")

    def test_chars(self) -> None:
        assert any_char("abc") == Right("a", "bc")


class TestEof:
    def test_empty(self) -> None:
        assert eof("") == Right(None, "")

    def test_one_char(self) -> None:
        assert isinstance(eof("a"), Left)
