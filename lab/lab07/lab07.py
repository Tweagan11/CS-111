class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

    def __str__(self):
        return f"Key: \'{self.key}\', Pos: {self.pos}"

    def __repr__(self):
        return f"Button({self.pos}, \'{self.key}\')"


class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    >>> k.add_button(Button(2, "!"))
    >>> k.add_button(Button(2, "?"))
    >>> str(k)
    """
    def __init__(self, *args):
        self.buttons = {}
        for arg in args:
            self.add_button(arg)

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if info in self.buttons:
            self.buttons[info].times_pressed += 1
            return self.buttons[info].key
        else:
            return ''


    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        output = ""
        for pos in typing_input:
            if pos in self.buttons:
                self.buttons[pos].times_pressed += 1
                output += self.buttons[pos].key
        return output


    def add_button(self, button):
        """Adds a button to the keyboard if the position is not taken"""
        for position in self.buttons:
            if button.pos == self.buttons[position].pos:
                return
        self.buttons[button.pos] = button


    def __str__(self):
        output = ""
        for button in self.buttons:
            output += str(self.buttons[button])
            if button < len(self.buttons) - 1:
                output += " | "
        return output

    def __repr__(self):
        output = "Keyboard("
        for button in self.buttons:
            output += repr(self.buttons[button])
            if button < len(self.buttons) - 1:
                output += ", "
        output += ")"
        return output