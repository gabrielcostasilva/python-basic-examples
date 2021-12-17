from dataclasses import dataclass, field

@dataclass
class User:
    # id: int = field(init=False, repr=False)
    id: int = field(init=False)
    name: str
    salary: float

    def __post_init__(self):
        self.id = 3

@dataclass(frozen=True)
class Role:
    description: str


if __name__ == "__main__":
    a_user = User("John Doe", 34422.33)
    print(a_user)
    
    a_role = Role("Admin")
    print(a_role)

    try:
        a_role.description = "A new description"
    except Exception as e:
        print(e)
