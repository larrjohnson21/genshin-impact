"""LocalContext module."""

import math
import random


class LocalContext:
    """Small parse_manager helper."""

    def __init__(self, seed: int = 48) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_manager(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 48) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 48


def main() -> None:
    obj = LocalContext()
    print(obj.parse_manager(48))


if __name__ == "__main__":
    main()
