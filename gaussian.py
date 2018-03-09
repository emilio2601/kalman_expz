class Gaussian:
    def __init__(self, mean, variance):
        self.mean     = mean
        self.variance = variance

    def __repr__(self):
        return f"N({self.mean}, {self.variance})"

    def __add__(self, other):
        return Gaussian(self.mean + other.mean, self.variance + other.variance)

    def __mul__(self, other):
        mean = (self.variance * other.mean + other.variance * self.mean) / (self.variance + other.variance)
        variance = (self.variance * other.variance) / (self.variance + other.variance)
        return Gaussian(mean, variance)