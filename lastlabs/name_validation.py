class Name:
    def __init__(self, name) -> None:
        if name not in ["Sofia", "Anonymous"]:
            raise ValueError("Allowed names: Sofia, Anonymous")
        self.name = name


# Test cases
print("1) Correct name")
a = Name("Sofia")
print("Object created successfully\n")

print("2) Incorrect name")
b = Name("Sofa")
