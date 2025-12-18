class Figure:
    def __init__(self, fig_type, length) -> None:
        assert length > 0, "Length must be greater than 0!"
        assert fig_type in ["square", "rectangle", "triangle"], \
            "Allowed figures: square, rectangle, triangle"
        self.fig_type = fig_type
        self.length = length


# Test cases
print("1) Create square with length 1")
c = Figure("square", 1)
print("Object created successfully\n")

print("2) Try to create trapezoid")
a = Figure("trapezoid", 12)

print("3) Try to create square with length 0")
b = Figure("square", 0)
