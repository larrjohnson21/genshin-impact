"""BatchGateway module."""

import math
import random


class BatchGateway:
    """Small render_resolver helper."""

    def __init__(self, seed: int = 85) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_resolver(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 85) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 85


def main() -> None:
    obj = BatchGateway()
    print(obj.render_resolver(85))


if __name__ == "__main__":
    main()
