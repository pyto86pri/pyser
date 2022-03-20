from typing import Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class Either(Generic[T]):
    ...


class Right(Generic[T], Either[T]):
    value: T
    rest: str

    def __init__(self, value: T, rest: str) -> None:
        self.value = value
        self.rest = rest

    def __eq__(self, o: object) -> bool:
        return (
            self.__class__ == o.__class__
            and self.value == o.value
            and self.rest == o.rest
        )

    def __str__(self) -> str:
        return f"Right({self.value}, {self.rest})"


class Left(Either[T]):
    error: Exception

    def __init__(self, error: Exception) -> None:
        self.error = error

    def __eq__(self, o: object) -> bool:
        return self.__class__ == o.__class__ and self.error == o.error

    def __str__(self) -> str:
        return f"Left({self.error})"
