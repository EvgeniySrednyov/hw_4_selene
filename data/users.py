import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    year: int
    month: str
    day: int
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str
