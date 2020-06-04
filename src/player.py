# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f'{self.name}'

    def print_location(self):
        return f'{self.location}'

    def move(self, direction, current_loc):
        attribute = direction + '_to'

        if hasattr(current_loc, attribute):
            return getattr(current_loc, attribute)

        print('you cnt go that way')
        return current_loc
