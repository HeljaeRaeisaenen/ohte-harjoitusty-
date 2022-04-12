'''class for creating the actual placement'''
from participants import Participants


class Placement:
    '''Turns the lists of names and wishes into a full seating arrangement.'''

    def __init__(self, tables: int,
                 filepath="/home/raisaneh/k/ohte/ohte_harjo/src/data/testi.csv"):  # todo
        self.file = Participants(filepath)  # test material
        self.friendgroups = []
        self.tables = tables
        self.finished_placement = []

    def create_friendgroup(self, personindex: int):
        '''idea is to iterate through the names by index number elsewhere, and here create
        a cluster of 4 people.
        The cluster is saved as a list named 'cluster' and can be visualized like this:
           [3]
        [1][0][2]
        where each pair of brackets is a seat in a real-world table. The numbers inside are the
        list indices. The finished seating layout is composed
        mostly of these clusters, arranged into a 2 x n dimensional rectanlge/array. The person,
         whos is used as a key to form the friendgroup, sits in place 0 and is surrounded
        (hopefully) by cluster.
        '''
        cluster = [None]*4
        cluster[0] = self.file.names[personindex]

        if len(self.file.wishes[personindex]) > 1:
            for i in range(2):
                self.place_friend_immediate(
                    personindex, cluster, i, len(self.file.wishes[personindex]))
            self.place_friend_secondary(personindex, cluster, 3)
        else:
            self.place_friend_immediate(personindex, cluster, 0, 1)
            for i in range(2, 4):
                self.place_friend_secondary(personindex, cluster, i)

        if (cluster[1] is None) and (cluster[2] is None) and (cluster[3] is None):
            return "Bad luck"
        self.friendgroups.append(cluster)
        self.file.placed[personindex] = True
        return "ok"

    def place_friend_immediate(self, personindex: int, cluster: list, i: int, maximum: int):
        '''place a person that person x wished for in x's friendgroup'''
        # should be made possible to split the wished names and search y only first name, or:
        # someone could modify the input file by hand and make sure the'res no weird misspellings
        indx = i
        while indx < maximum:
            if self.file.wishes[personindex][indx] in self.file.names:
                friendindex = self.file.names.index(
                    self.file.wishes[personindex][indx])
                if not self.file.placed[friendindex]:
                    cluster[i+1] = self.file.wishes[personindex][indx]
                    self.file.placed[friendindex] = True
                    break
            elif self.file.wishes[personindex][indx].lower() in self.file.names:
                friendindex = self.file.names.index(
                    self.file.wishes[personindex][indx].lower())
                if not self.file.placed[friendindex]:
                    cluster[i+1] = self.file.wishes[personindex][indx]
                    self.file.placed[friendindex] = True
                    break
            elif self.file.wishes[personindex][indx] in self.file.firstnames:
                friendindex = self.file.firstnames.index(
                    self.file.wishes[personindex][indx])
                if not self.file.placed[friendindex]:
                    cluster[i+1] = self.file.names[friendindex]
                    self.file.placed[friendindex] = True
                    break
            indx += 1

    def place_friend_secondary(self, personindex: int, cluster: list, indx: int):
        '''place a person who wished for person x in x's friendgroup
        iterate through the wishes and check if our person appears in any of them'''
        for i in range(len(self.file.wishes)):
            if self.file.placed[i] is False:
                if cluster[0] in self.file.wishes[i]:
                    #print(True,"sec 1")
                    cluster[indx] = self.file.names[i]
                    self.file.placed[i] = True
                elif cluster[0].lower() in self.file.wishes[i]:
                    #print(True, "sec 2")
                    cluster[indx] = self.file.names[i]
                    self.file.placed[i] = True
                elif self.file.firstnames[personindex] in self.file.wishes[i]:
                    #print(True, "sec 3")
                    cluster[indx] = self.file.names[i]
                    self.file.placed[i] = True




class Combine:
    '''create a priority list: the more limbs know othre limbs of other clusters, the higher the
    priority.'''
    def __init__(self) -> None:
        self.__best = {}

    def combine_friendgroups(self):
        '''combine created friendgroups into a finished seating'''
        
        first = self.friendgroups.pop(0)