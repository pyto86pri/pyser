from pyser.core.char import char, satisfy
from pyser.core.either import Left, Right


class TestChar:
    def test_empty(self) -> None:
        assert isinstance(char("a")(""), Left)

    def test_chars(self) -> None:
        assert char("a")("a") == Right("a", "")
        assert isinstance(char("a")("A"), Left)
        assert isinstance(char("a")("hoge"), Left)


class TestSatisfy:
    def test_empty(self) -> None:
        assert isinstance(satisfy(lambda c: c == "b")(""), Left)

    def test_chars(self) -> None:
        assert satisfy(lambda c: c == "a")("abc") == Right("a", "bc")
        assert isinstance(satisfy(lambda c: c == "b")("abc"), Left)
