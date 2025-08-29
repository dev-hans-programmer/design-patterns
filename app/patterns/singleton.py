from typing import Self

"""
Singleton ensures that only one instance of a class is created in the entire 
application, and that same instance is used everywhere.

Use cases:
1. Db connection
2. Logger
3. Config settings etc
"""


class Singleton:
    _instance: Self | None = None

    # gets called before __init__
    def __new__(cls) -> Self:
        if not cls._instance:
            print(f'Creating singleton instance of {cls.__name__}')
            cls._instance = super().__new__(cls)
        return cls._instance


class Logger(Singleton):
    def __init__(self) -> None:
        print('Creating Logger')


def test_singleton():
    logger1 = Logger()
    logger2 = Logger()
    print(logger1 is logger2)
