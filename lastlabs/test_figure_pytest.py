from app import Figure

def test_get_angles():
    triangle = Figure("triangle", 1)
    assert triangle.get_angles == 3, "Triangle should have 3 angles"

    square = Figure("square", 2)
    assert square.get_angles == 4, "Square should have 4 angles"

    rectangle = Figure("rectangle", 3)
    assert rectangle.get_angles == 4, "Rectangle should have 4 angles"
