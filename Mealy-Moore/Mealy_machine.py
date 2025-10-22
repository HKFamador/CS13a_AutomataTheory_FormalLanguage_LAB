class MealyMachine:
    def __init__(self):
        self.state = 'A'  # Start state

    def transition(self, input_symbol):
        output = None

        if self.state == 'A':
            if input_symbol == '0':
                self.state = 'A'
                output = '0'
            elif input_symbol == '1':
                self.state = 'B'
                output = '1'

        elif self.state == 'B':
            if input_symbol == '0':
                self.state = 'C'
                output = '0'
            elif input_symbol == '1':
                self.state = 'B'
                output = '1'

        elif self.state == 'C':
            if input_symbol == '0':
                self.state = 'B'
                output = '1'
            elif input_symbol == '1':
                self.state = 'C'
                output = '0'

        return output

    def process(self, input_string):
        result = ""
        for symbol in input_string:
            output = self.transition(symbol)
            result += output
        return result


# Example usage
if __name__ == "__main__":
    mealy = MealyMachine()
    input_str = "011001"
    output_str = mealy.process(input_str)
    print("Input:  ", input_str)
    print("Output: ", output_str)
