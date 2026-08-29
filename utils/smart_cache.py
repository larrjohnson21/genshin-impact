"""LocalWorker module."""

import math
import random


class LocalWorker:
    """Small flush_provider helper."""

    def __init__(self, seed: int = 70) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_provider(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 70) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 70


def main() -> None:
    obj = LocalWorker()
    print(obj.flush_provider(70))


if __name__ == "__main__":
    main()
