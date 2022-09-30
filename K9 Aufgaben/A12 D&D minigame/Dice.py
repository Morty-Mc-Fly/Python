from random import randint


class Die():
    def throwD3() -> int:
        return randint(1, 3)

    def throwD4() -> int:
        return randint(1, 4)

    def throwD6() -> int:
        return randint(1, 6)

    def throwD7() -> int:
        return randint(1, 7)

    def throwD8() -> int:
        return randint(1, 8)

    def throwD10() -> int:
        return randint(1, 10)
