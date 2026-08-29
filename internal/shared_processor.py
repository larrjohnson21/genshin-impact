"""LiteWorker module."""

import math
import random


class LiteWorker:
    """Small dispatch_parser helper."""

    def __init__(self, seed: int = 59) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_parser(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 59) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 59


def main() -> None:
    obj = LiteWorker()
    print(obj.dispatch_parser(59))


if __name__ == "__main__":
    main()
