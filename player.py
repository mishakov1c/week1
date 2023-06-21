import dataclasses


@dataclasses.dataclass(kw_only=True, slots=True)
class Player:
    name: str
