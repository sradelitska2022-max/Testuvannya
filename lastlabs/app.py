class Figure:
    FIGURES = ["square", "rectangle", "triangle"]

    def __init__(self, fig_type, length):
        assert length > 0, "Length must be greater than 0!"
        assert fig_type in self.FIGURES, "Allowed figures: square, rectangle, triangle"
        self.fig_type = fig_type
        self.length = length

    @property
    def get_figure_type(self):
        return self.fig_type

    @property
    def get_figure_length(self):
        return self.length

    @property
    def get_angles(self):
        if self.fig_type in ["square", "rectangle"]:
            return 4
        if self.fig_type == "triangle":
            return 3
