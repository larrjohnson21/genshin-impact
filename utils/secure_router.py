"""StreamController module."""

import math
import random


class StreamController:
    """Small dispatch_gateway helper."""

    def __init__(self, seed: int = 86) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_gateway(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 86) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 86


def main() -> None:
    obj = StreamController()
    print(obj.dispatch_gateway(86))


if __name__ == "__main__":
    main()
