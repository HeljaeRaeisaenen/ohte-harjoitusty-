'''A repository (maybe?) for handling the participants of the event'''
from file_and_database_functions.readwrite import fileread
from application_logic.participant import Participant


class ParticipantsRepo:
    '''The repository.
    Attributes:
        participants: a dictionary of the people, key = name, value = a Participant object
        has_friendgroup: people who have people sitting next to them
        placed_fin: people who have been placed in the final '''

    def __init__(self, filepath: str):
        self.participants = {}
        self._odd_wishes = {}
        self._has_friendgroup = set()
        self.placed_fin = set()
        # the existence of filepath is ensured elsewhere, in the ui
        self.initialize(filepath)

    def initialize(self, filename: str):
        '''putting the read file contents in the Participants object'''
        output = fileread(filename)
        for i in output:
            # give the name to the init.
            self.participants[i[0]] = Participant(i[0])
            self._odd_wishes[i[0]] = []
        for i in output:
            for name in i[1]:
                friend = self.is_in_participants(name)
                if friend:
                    self.participants[i[0]].wishes.append(friend)
                else:
                    self._odd_wishes[i[0]].append(name)
        self._handle_odd_names()

    def get_participants(self):
        '''Returns a dictionary of the participants. Key: name, value: Participant-object.'''
        return self.participants

    def get_has_friendgroup(self):
        '''Returns the attribute'''
        return self._has_friendgroup

    def add_has_friendgroup(self, name):
        '''If a person gets a friendgroup, add them to the set'''
        self._has_friendgroup.add(name)

    def is_in_participants(self, name: str):
        '''Check if a name is in participants (full name or first name)'''
        if name in self.participants:
            return name
        if name.capitalize() in self.participants:
            return name.capitalize()
        fullname = self.return_full_name(name)
        if fullname:
            return fullname
        return False

    def _handle_odd_names(self):
        for name, wishes in self._odd_wishes.items():
            for wish in wishes:
                if wish == "":
                    continue
                for name2, wishes2 in self._odd_wishes.items():
                    for wish2 in wishes2:
                        if wish2 == "":
                            continue
                        if wish == wish2 and (not name in self.participants[name2].wishes):
                            if name != name2:
                                self.participants[name].wishes.append(name2)
                                self.participants[name2].wishes.append(name)

    def return_full_name(self, name: str):
        '''If only first name is known, return full name. If full name is put in as an argument,
        the full name is returned. Will not be reliable, if there are many participants with the
        same first name, but that's a risk taken.'''
        if name in self.participants:
            return name
        for person, obj in self.participants.items():
            if obj.get_firstname() == name:
                return person
            if obj.get_firstname() == name.capitalize():
                return person
        return None

    def return_has_wishes(self):
        '''Returns a list containing all names (keys to self.participants) that have 1 or more
        wishes'''
        output = []
        for person, obj in self.participants.items():
            if len(obj.wishes) > 0:
                output.append(person)
        return output

    def return_not_placed(self):
        '''Returns a list containing all names (keys to self.participants) that don't have a
        friendgroup.
        '''
        output = []
        for person, obj in self.participants.items():
            if not obj.is_placed():
                output.append(person)
        return output

    def return_not_placed_fin(self):
        '''Returns a list containing all names (keys to self.participants) that haven't been
        placed in the final seating'''
        output = []
        for person in self.participants:
            if not person in self.placed_fin:
                output.append(person)
        return output

    def check_if_placed(self, name):
        '''Like the name says.
            Args: name to be checked
            Returns: bool'''
        if self.participants[name].is_placed():
            return True
        return False

    def check_if_placed_fin(self, name):
        '''Like the name says.
            Args: name to be checked
            Returns: bool'''
        if name in self.placed_fin:
            return True
        return False
