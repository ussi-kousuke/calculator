class Calculator:
    def __init__(self, number1, number2):
        self.first = number1
        self.second = number2
        self.total_count = 0

    def add(self):
        add_answer = self.first + self.second
        self.total_count += add_answer
        return self.total_count

    def subtract(self):
        subtract_answer = self.first - self.second
        self.total_count += subtract_answer
        return self.total_count

    def multiply(self):
        multiply_answer = self.first * self.second
        self.total_count += multiply_answer
        return self.total_count

    def divide(self):
        divide_answer = self.first / self.second
        self.total_count += divide_answer
        return self.total_count

    def is_calculate(self):
        self.first = self.total_count

    def reset(self):
        self.total_count = 0