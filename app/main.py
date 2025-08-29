from app.patterns.singleton import Logger


def test_singleton():
    logger1 = Logger()
    logger2 = Logger()
    print(logger1 is logger2)


if __name__ == '__main__':
    test_singleton()
