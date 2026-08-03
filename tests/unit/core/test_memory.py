import inspect

from ai_commerce_os.core.memory import Memory


class ExampleMemory(Memory):
    def __init__(self) -> None:
        self.values: dict[str, object] = {}

    def store(self, key: str, value: object) -> None:
        self.values[key] = value

    def retrieve(self, key: str) -> object | None:
        return self.values.get(key)


def test_memory_is_abstract() -> None:
    assert inspect.isabstract(Memory)


def test_memory_contract_stores_and_retrieves_values() -> None:
    memory = ExampleMemory()
    memory.store("key", "value")

    assert memory.retrieve("key") == "value"
    assert memory.retrieve("unknown") is None
