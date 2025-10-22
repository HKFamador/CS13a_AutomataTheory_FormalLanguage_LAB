class MooreMachine:
    def __init__(self):
        self.state = 'A'  # initial state
        # Output associated with each state
        self.output_map = {
            'A': '0',
            'B': '0',
            'C': '1'
        }

    def transition(self, input_symbol):
        if self.state == 'A':
            if input_symbol == '0':
                self.state = 'C'
            elif input_symbol == '1':
                self.state = 'B'

        elif self.state == 'B':
            if input_symbol == '0':
                self.state = 'C'
            elif input_symbol == '1':
                self.state = 'B'

        elif self.state == 'C':
            if input_symbol == '0':
                self.state = 'C'
            elif input_symbol == '1':
                self.state = 'B'

    def process(self, input_string):
        # Moore machines output before any input (based on current state)
        result = self.output_map[self.state]
        for ch in input_string:
            self.transition(ch)
            result += self.output_map[self.state]
        return result


# Example usage
if __name__ == "__main__":
    moore = MooreMachine()
    input_str = "010110"
    output_str = moore.process(input_str)
    print("Input:  ", input_str)
    print("Output: ", output_str)
