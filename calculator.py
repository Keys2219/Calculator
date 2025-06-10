import math

class Calculator:
    def __init__(self):
        self.reset()

    def reset(self):
        """Clear all calculator state (AC button)."""
        self.current = "0"
        self.previous = None
        self.operation = None
        self.memory = 0
        self.new_input = True

    def clear(self):
        """Clear current entry (C button)."""
        self.current = "0"
        self.new_input = True

    def input_digit(self, digit):
        """Handle digit input (0-9)."""
        if self.new_input:
            self.current = digit
            self.new_input = False
        else:
            self.current = self.current + digit if self.current != "0" else digit
        return self.current

    def input_decimal(self):
        """Handle decimal point (.)."""
        if self.new_input:
            self.current = "0."
            self.new_input = False
        elif "." not in self.current:
            self.current += "."
        return self.current

    def toggle_sign(self):
        """Toggle positive/negative (± button)."""
        if self.current.startswith("-"):
            self.current = self.current[1:]
        elif self.current != "0":
            self.current = "-" + self.current
        return self.current

    def percent(self):
        """Calculate percentage (% button)."""
        try:
            self.current = str(float(self.current) / 100)
            self.new_input = True
            return self.current
        except ValueError:
            return "Error"

    def square_root(self):
        """Calculate square root (√ button)."""
        try:
            value = float(self.current)
            if value < 0:
                return "Error"
            self.current = str(math.sqrt(value))
            self.new_input = True
            return self.current
        except ValueError:
            return "Error"

    def reciprocal(self):
        """Calculate reciprocal (1/x button)."""
        try:
            value = float(self.current)
            if value == 0:
                return "Error"
            self.current = str(1 / value)
            self.new_input = True
            return self.current
        except ValueError:
            return "Error"

    def memory_clear(self):
        """Clear memory (MC button)."""
        self.memory = 0

    def memory_recall(self):
        """Recall memory (MR button)."""
        self.current = str(self.memory)
        self.new_input = True
        return self.current

    def memory_add(self):
        """Add to memory (M+ button)."""
        try:
            self.memory += float(self.current)
            self.new_input = True
            return self.current
        except ValueError:
            return "Error"

    def memory_subtract(self):
        """Subtract from memory (M- button)."""
        try:
            self.memory -= float(self.current)
            self.new_input = True
            return self.current
        except ValueError:
            return "Error"

    def set_operation(self, op):
        """Set arithmetic operation (+, -, ×, ÷)."""
        try:
            if self.previous is None:
                self.previous = float(self.current)
            elif self.operation:
                self.compute()
            self.operation = op
            self.new_input = True
            return self.current
        except ValueError:
            return "Error"

    def compute(self):
        """Perform calculation (= button)."""
        try:
            if self.previous is not None and self.operation:
                current = float(self.current)
                if self.operation == "+":
                    self.previous += current
                elif self.operation == "-":
                    self.previous -= current
                elif self.operation == "×":
                    self.previous *= current
                elif self.operation == "÷":
                    if current == 0:
                        return "Error"
                    self.previous /= current
                self.current = str(self.previous)
                self.previous = None
                self.operation = None
                self.new_input = True
            return self.current
        except ValueError:
            return "Error"

    def handle_input(self, key):
        """Process keyboard or GUI button input."""
        key_map = {
            "0": lambda: self.input_digit("0"),
            "1": lambda: self.input_digit("1"),
            "2": lambda: self.input_digit("2"),
            "3": lambda: self.input_digit("3"),
            "4": lambda: self.input_digit("4"),
            "5": lambda: self.input_digit("5"),
            "6": lambda: self.input_digit("6"),
            "7": lambda: self.input_digit("7"),
            "8": lambda: self.input_digit("8"),
            "9": lambda: self.input_digit("9"),
            ".": self.input_decimal,
            "+": lambda: self.set_operation("+"),
            "-": lambda: self.set_operation("-"),
            "*": lambda: self.set_operation("×"),
            "/": lambda: self.set_operation("÷"),
            "=": self.compute,
            "Enter": self.compute,
            "c": self.clear,
            "C": self.clear,
            "Escape": self.reset,
            "%": self.percent,
            "±": self.toggle_sign,
            "√": self.square_root,
            "1/x": self.reciprocal,
            "mc": self.memory_clear,
            "mr": self.memory_recall,
            "m+": self.memory_add,
            "m-": self.memory_subtract
        }
        if key in key_map:
            return key_map[key]()
        return self.current