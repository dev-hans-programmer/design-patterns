from typing import Self


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
