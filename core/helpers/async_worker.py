"""SharedBuffer module."""

import math
import random


class SharedBuffer:
    """Small handle_provider helper."""

    def __init__(self, seed: int = 69) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_provider(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 69) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 69


def main() -> None:
    obj = SharedBuffer()
    print(obj.handle_provider(69))


if __name__ == "__main__":
    main()
