class PlotBuilder:
    """A fluent interface for creating plots"""

    def __init__(self):
        self._data = []
        self._labels = []
        self._title = None
        self._xlabel = None
        self._ylabel = None
        self._figsize = (8, 6)
        self._style = "default"
        self._gird: bool = False

    def add_line(self, x, y, label=None):
        """Add a line to the plot"""
        self._data.append((x, y))
        self._labels.append(label)
        return self  # Return self for chaining!

    def add_scatter(self, x, y, label=None):
        self._data.append((x, y))
        self._labels.append(label)
        return self

    def title(self, title):
        """Set plot title"""
        self._title = title
        return self

    def xlabel(self, label):
        """Set x-axis label"""
        self._xlabel = label
        return self

    def ylabel(self, label):
        """Set y-axis label"""
        self._ylabel = label
        return self

    def figsize(self, width, height):
        """Set figure size"""
        self._figsize = (width, height)
        return self

    def grid(self, grid=True):
        self._gird = grid
        return self

    def style(self, style):
        self._style = style
        return self

    def build(self):
        """Actually create the plot"""
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=self._figsize)

        for (x, y), label in zip(self._data, self._labels):
            ax.plot(x, y, label=label)

        if self._title:
            ax.set_title(self._title)
        if self._xlabel:
            ax.set_xlabel(self._xlabel)
        if self._ylabel:
            ax.set_ylabel(self._ylabel)
        if any(self._labels):
            ax.legend()

        return fig, ax

    def show(self):
        """Build and display the plot"""
        self.build()
        import matplotlib.pyplot as plt

        plt.show()

    def save(self, filename: str):
        self.build()
        import matplotlib.pyplot as plt

        plt.savefig(filename)


# Usage - clean and readable
plot = (
    PlotBuilder()
    .title("Quadratic and Cubic Functions")
    .xlabel("x")
    .ylabel("f(x)")
    .figsize(10, 6)
    .add_line([1, 2, 3, 4], [1, 4, 9, 16], label="x²")
    .add_line([1, 2, 3, 4], [1, 8, 27, 64], label="x³")
)

print("Plot configured successfully!")
# plot.show()  # Uncomment to display

if __name__ == "__main__":
    (
        PlotBuilder()
        .title("Data Visualization")
        .grid(True)
        .style("ggplot")
        .add_scatter([1, 2, 3], [2, 4, 6], label="Data A")
        .add_line([1, 2, 3], [3, 3, 3], label="Average")
        .save("plot.png")
    )
