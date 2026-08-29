"""SimpleController module."""

import math
import random


class SimpleController:
    """Small encode_manager helper."""

    def __init__(self, seed: int = 16) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_manager(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 16) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 16


def main() -> None:
    obj = SimpleController()
    print(obj.encode_manager(16))


if __name__ == "__main__":
    main()
