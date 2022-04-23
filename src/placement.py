'''class for creating the actual placement'''
from participants_repo import ParticipantsRepo


class Placement:
    '''Turns the lists of names and wishes into a full seating arrangement.
    Attributes:
        repo = a Participants object already set up
        tables_n = number of tables set by the user
        fin_placement = the finished placement as a 2D matrix
        total_wishes = the number of individuals wished as company by total of participants
        wishes_placed = number of the aforementioned, that have been filled in fin_placement
        '''

    def __init__(self, tables: int, participants: ParticipantsRepo):
        '''I've speficied ParticipantsRepo as the correct type so that the methods of the class
        will autocomplete as I write.
        '''
        self.repo = participants
        self.tables_n = tables
        self.fin_placement = []
        self.total_wishes = 0
        self.wishes_placed = 0
        self._check_everything_ok()
        self._count_wishes()
        self._create_tables()
        self.create_placement()

    def _check_everything_ok(self):
        if self.tables_n > len(self.repo.get_participants()):
            raise Exception("There are more tables than people")

    def _count_wishes(self):
        ''' Count how many wishes the people have in total. This will be used to get a feel of
        how well the placement was done.'''

        for participant in self.repo.participants.values():
            self.total_wishes += len(participant.wishes)

    def _create_tables(self):
        '''This causes fin_placement to have the correct number of seats and tables.
        This could be improved to make the difference in row length similar to a real-world table
        ,  like 3 places (a table that seats 6 people).

        fin_placement is a list, containing tables_n * 2 sublists, which all contain "seats".
        Two sublists make a table, i.e. index 0 and 1 are table number 1, 2 and 3 are table 2 etc.
        The number of seats in fin placement will be equal or greater to the numer of participants.
        '''

        seats_n = len(self.repo.get_participants())
        row_len = seats_n // (self.tables_n * 2)
        difference = seats_n - ((self.tables_n * 2)*row_len)

        for row in range(self.tables_n * 2):
            self.fin_placement.append([None]*row_len)

        for row in range(difference):
            self.fin_placement[row].append(None)

    def create_placement(self):
        '''The big method that glues it all together'''
        has_wishes = self.repo.return_has_wishes()
        for person in has_wishes:
            self.create_friendgroup(person)
        self._combine_friendgroups()
        self._do_fin_placement()
        self._ensure_everyone_placed()

###################################################################################################

    def create_friendgroup(self, name):
        '''This makes the initial building blocks of the placement: clusters of friends.
        The cluster can be visualized like this:
           [3]
        [1][0][2]
        where each pair of brackets is a seat in a real-world table. The numbers inside are
        list indices. The finished seating layout is composed
        mostly of these clusters, placed into self.fin_placement. The person,
        whos is used as a key to form the friendgroup, sits in place 0 and is surrounded
        (hopefully) by friends on all sides. These are saved in the corresponding Participant
        object's attributes.
        '''
        participants = self.repo.get_participants()
        name_obj = participants[name]
        if name_obj.is_placed() or len(name_obj.wishes) == 0:
            return
        cluster = []

        while len(cluster) < 4:
            for wish in name_obj.wishes:
                success = self._add_friend_ok(wish)
                if success:
                    cluster.append(participants[wish])
            break

        if len(cluster) < 3:
            while True:
                friendname = self._place_friend_secondary(name)
                if friendname != "fail":
                    cluster.append(participants[friendname])
                else:
                    break
        if len(cluster) > 0:
            name_obj.place()
            self._cluster_into_neighbors(name, cluster)

    def _place_friend_rows(self, friend_rows):
        table_row = self.tables_n * 2

        while len(friend_rows) > 0:
            while table_row > 0:
                table_row -= 1
                self._place_friend_row(table_row, friend_rows.pop(0))
                self._placement_place_opposite(table_row)
                if table_row % 2 == 0:
                    self._placement_place_opposite(table_row+1)
                else:
                    self._placement_place_opposite(table_row-1)
                if len(friend_rows) == 0:
                    break
            table_row = self.tables_n * 2

###################################################################################################

    def _add_friend_ok(self, name: str):
        '''Check if it's possible to add a friend to a cluster.
            Args: name, string. It should be sure that this name is in the participants.
            Returns: name of the friend, if the name isn't placed yet, otherwise False.
        Called from create_friendgroup
        '''
        participants = self.repo.get_participants()
        if not participants[name].is_placed():
            participants[name].place()
            return True
        return False

    def _place_friend_secondary(self, name):
        '''Check iif it's ok to place a person who wished for person x in x's friendgroup.
        Iterate through the wishes and check if our person appears in any of them'''
        participants = self.repo.get_participants()
        for random_name, random_obj in participants.items():
            if not random_obj.is_placed():
                if name in random_obj.get_wishes():
                    random_obj.place()
                    return random_name
        return "fail"

    def _cluster_into_neighbors(self, name, cluster):
        '''Place the finished friend cluster of x into  x's Participant object. The result: x's
        Participant-object has attributes for who sits in whihc direction from him.
            Args: name of x, cluster of friends (list)
            Returns: None'''
        participants = self.repo.get_participants()
        for friend in cluster:
            participants[name].update_friendgroup(friend)
            friend.place()
            self.repo.add_has_friendgroup(friend.name)
        self.repo.add_has_friendgroup(name)

    def _combine_friendgroups(self):
        '''Iterate throupgh the names who have a friendgroup, and see if you can add more friends
        in them.
        '''
        participants = self.repo.get_participants()
        has_friendgroup = self.repo.get_has_friendgroup()

        for person in has_friendgroup:
            for wish in participants[person].wishes:
                # both are never true at the same time
                if wish in has_friendgroup and not self.repo.check_if_placed(wish):
                    participants[person].update_friendgroup(
                        participants[wish])
                    participants[wish].place()
        for person in self.repo.return_not_placed():
            for wish in participants[person].wishes:
                if wish and (wish in has_friendgroup):
                    participants[person].update_friendgroup(
                        participants[wish])
                    participants[wish].place()

    def _friend_row(self, name):
        '''Make a list from the seating info in the Particpant objects. The list is like a
        row in the finished seating.
            Args: the name of the leftmost people in the row
            Returns: the row (a list)'''
        output = []
        while True:
            if not name:
                break
            output.append(name)
            name = self.repo.participants[name].on_the_right()

        return output


###############################################################################################


    def _do_fin_placement(self):
        '''Start putting people in friendgroups in the fin_placement.'''

        people_no_left = []  # people who don't have anyone sitting on their left
        friend_rows = []
        for person in self.repo.get_has_friendgroup():
            if not self.repo.participants[person].on_the_left():
                people_no_left.append(person)

        for person in people_no_left:
            friend_rows.append(self._friend_row(person))

        friend_rows.sort(key=len, reverse=True)

        self._place_friend_rows(friend_rows)
        self._place_missing_friends()
        self._place_missing_friends()

        for person in self.repo.return_has_wishes():
            for wish in self.repo.participants[person].wishes:
                if wish not in self.repo.placed_fin:
                    self._place_next_to_name(person, wish)
        for person in self.repo.return_not_placed_fin():
            self._place_random(person)

    def _place_friend_row(self, row, friends: list):
        '''Place a friend row in a table in fin_placement.
        Args:
            row = number of the row in fin_placement in which the friends will be placed
            friends = list of the names to be placed in the order to be placed
        '''
        for name in friends:
            if name in self.repo.placed_fin:
                return
        for i in range(len(self.fin_placement[row])):
            if not self.fin_placement[row][i]:
                if i+len(friends) > len(self.fin_placement[row]):
                    break
                for index, person in enumerate(friends, start=i):
                    self._place_fin(person, (row, index))
                self.wishes_placed += (len(friends) * 2) - 2
                break

    def _placement_place_opposite(self, row):
        success = False

        if row % 2 == 1:
            opposite_row = row - 1
        else:
            opposite_row = row + 1
        for place in self.fin_placement[row]:
            # print(place)
            if place:
                indx = self.fin_placement[row].index(place)
                new = self.repo.participants[place].opposite()
                if new and (new not in self.repo.placed_fin):
                    success = self._place_fin(new, (opposite_row, indx))
        if success:
            self.wishes_placed += 1

    def _place_next_to_name(self, placed, friend):
        #friend = self.repo.return_full_name(friend)
        if placed not in self.repo.placed_fin:
            return

        coords = self.repo.participants[placed].seat_coords
        friend_coords = None
        opposite = 0
        if not coords:  # idk why there's sometimes None coords, coords are always added when person
            # is added to fin placement
            return
        if coords[0] % 2 == 1:
            opposite = coords[0] - 1
        else:
            opposite = coords[0] + 1

        if coords[1]-1 != -1:
            if not self.fin_placement[coords[0]][coords[1]-1]:
                friend_coords = (coords[0], coords[1]-1)
        if coords[1]+1 != len(self.fin_placement[coords[0]]):
            if not self.fin_placement[coords[0]][coords[1]+1]:
                friend_coords = (coords[0], coords[1]+1)
        elif not self.fin_placement[opposite][coords[1]]:
            friend_coords = (opposite, coords[1])

        if not friend_coords:
            return

        success = self._place_fin(friend, friend_coords)
        if success:
            self.wishes_placed += 1

    def _place_missing_friends(self):
        particpants = self.repo.get_participants()
        for r_ind, row in enumerate(self.fin_placement):
            for p_ind, place in enumerate(row):
                if place:
                    friend = particpants[place].on_the_left()
                    if friend and not self.repo.check_if_placed_fin(friend):
                        self._place_fin(friend, (r_ind, p_ind-1))
                        self.wishes_placed += 1
                    friend = particpants[place].on_the_right()
                    if friend and not self.repo.check_if_placed_fin(friend):
                        self._place_fin(friend, (r_ind, p_ind+1))
                        self.wishes_placed += 1

    def _place_random(self, name):
        for row in self.fin_placement:
            for place in row:
                if not place:
                    row_i = self.fin_placement.index(row)
                    place_i = self.fin_placement[row_i].index(
                        place)
                    self._place_fin(name, (row_i, place_i))
                    return

    def _place_fin(self, name: str, coordinates: tuple):
        '''Actually place a single person in a single seat in fin_placemnt.'''
        if self.fin_placement[coordinates[0]][coordinates[1]]:
            return False

        self.fin_placement[coordinates[0]
                           ][coordinates[1]] = name
        self.repo.placed_fin.add(name)
        self.repo.participants[name].seat_coords = coordinates

        return True


###############################################################################################


    def _ensure_everyone_placed(self):
        '''Check if everyone is placed in the fin_placement.'''
        failstr = ""
        for person in self.repo.participants:
            if person not in self.repo.placed_fin:
                failstr += person + " "
        if len(failstr) > 0:
            raise Exception(failstr)
