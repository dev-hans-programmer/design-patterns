from app.patterns.factory import test_factory
from app.patterns.singleton import test_singleton
from app.patterns.strategy import (
    test_strategy,
)

if __name__ == '__main__':
    test_singleton()
    test_factory()
    test_strategy()
