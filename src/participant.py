'''A data repoure for a single participant of the event.'''


class Participant:
    '''A data structure for a single participant. 
    Attributes: 
        name: the full name of the person
        first name: the first name
        wishes: namea of the people who the person wishes for company. It's assured elsewhere that
                these names exist in the list of participants.
        placed: whether the person has a place or not
        place_on_the_left: who sits on the person's left hand side
        place_on_the_right: the same but on the right
        place_opposite: the same but opposite
        seat_coords: the coordinates of the person's assigned seat as a tuple (row, seat)'''

    def __init__(self, name):
        '''Args: "name" is a list with i=0 is the full name str, i=1 is a list containing
        strings of the wishes'''
        self.name = name
        self._first_name = name.split(" ")[0]
        self.wishes = []
        self._placed = False
        self._place_on_the_left = None
        self._place_on_the_right = None
        self._place_opposite = None
        self.seat_coords = None

    def get_wishes(self):
        '''Method to access attribute'''
        return self.wishes

    def on_the_left(self):
        '''Method to access attribute'''
        return self._place_on_the_left

    def set_on_the_left(self, name):
        '''Method to set the attribute'''
        self._place_on_the_left = name

    def on_the_right(self):
        '''Method to access attribute'''
        return self._place_on_the_right

    def set_on_the_right(self, name):
        '''Method to set the attribute'''
        self._place_on_the_right = name

    def opposite(self):
        '''Method to access attribute'''
        return self._place_opposite

    def set_opposite(self, name):
        '''Method to set the attribute'''
        self._place_opposite = name

    def get_firstname(self):
        '''Method to access attribute'''
        return self._first_name

    def is_placed(self):
        '''Check if participant has been placed'''
        if self._placed:
            return True
        return False

    def place(self):
        '''Put a participant in a placed state'''
        self._placed = True

    def update_friendgroup(self, friend):
        '''Adds a friend to a place next to or opposite of the person. The opposite place is
        filled the last.'''

        if (not self._place_on_the_left) and (not friend.on_the_right()):
            self._place_on_the_left = friend.name
            friend.set_on_the_right(self.name)
        elif (not self._place_on_the_right) and (not friend.on_the_left()):
            self._place_on_the_right = friend.name
            friend.set_on_the_left(self.name)
        elif (not self._place_opposite) and (not friend.opposite()):
            self._place_opposite = friend.name
            friend.set_opposite(self.name)
#            self.surrounded = True
        else:
            return
        self.place()
