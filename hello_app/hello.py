def hello(name: str | None = None) -> str:
    target = name or "World"
    return f"Hello, {target}!"
