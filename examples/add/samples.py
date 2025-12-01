import random

from gage_inspect.dataset import dataset


@dataset(task="add")
def add_tests(n=100):
    """Test cases for add task."""

    def sample():
        x = random.randint(-100_000, 100_000)
        y = random.randint(-100_000, 100_000)
        z = x + y
        return {"x": x, "y": y, "target": str(z)}

    return [sample() for _ in range(n)]
