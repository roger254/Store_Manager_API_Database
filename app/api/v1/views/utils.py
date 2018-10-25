import re


class Validate:
    def is_input_valid(self, name):
        error = []
        if not re.match("^[a-zA-Z0-9-._@ `]+$", name):
            error += "Name must be a string"
