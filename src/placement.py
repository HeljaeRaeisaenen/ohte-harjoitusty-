'''class for creating the actual placement'''
from readwrite import filewrite
from participants import Participants

class Placement:
    def __init__(self, tables: int, filepath="/home/raisaneh/k/ohte/ohte_harjtyo/src/data/testi.csv"):
        self.file = Participants(filepath)  # test material
        self.friendgroups = []
        self.tables = tables
        self.finished = []

    def create_friendgroup(self, personindex: int):
        '''idea is to iterate through the names by index number elsewhere, and here create
        a cluster of 4 people.
        The cluster is saved as a list named 'friends' and can be visualized like this:
           [3]
        [1][0][2]
        where each pair of brackets is a seat in a real-world table. The numbers inside are the
        list indices. The finished seating layout is composed
        mostly of these clusters, arranged into a 2 x n dimensional rectanlge/array. The person,
         whos is used as a key to form the friendgroup, sits in place 0 and is surrounded
        (hopefully) by friends.
        '''
        friends = [None]*4
        friends[0] = self.file.names[personindex]

        if len(self.file.wishes[personindex]) > 1:
            for i in range(2):
                self.place_friend_immediate(
                    personindex, friends, i, len(self.file.wishes[personindex]))
            self.place_friend_secondary(personindex, friends, 3)
        else:
            self.place_friend_immediate(personindex, friends, 0, 1)
            for i in range(2, 4):
                self.place_friend_secondary(personindex, friends, i)

        if (friends[1] is None) and (friends[2] is None) and (friends[3] is None):
            return "Bad luck"
        self.friendgroups.append(friends)
        self.file.placed[personindex] = True

    def place_friend_immediate(self, personindex: int, friends: list, i: int, maximum: int):
        '''place a person that person x wished for in x's friendgroup'''
        # should be made possible to split the wished names and search y only first name, or:
        # someone could modify the input file by hand and make sure the'res no weird misspellings
        indx = i
        while indx < maximum:
            if self.file.wishes[personindex][indx] in self.file.names:
                friendindex = self.file.names.index(
                    self.file.wishes[personindex][indx])
                if not self.file.placed[friendindex]:
                    friends[i+1] = self.file.wishes[personindex][indx]
                    self.file.placed[friendindex] = True
                    break
            elif self.file.wishes[personindex][indx].lower() in self.file.names:
                friendindex = self.file.names.index(
                    self.file.wishes[personindex][indx].lower())
                if not self.file.placed[friendindex]:
                    friends[i+1] = self.file.wishes[personindex][indx]
                    self.file.placed[friendindex] = True
                    break
            elif self.file.wishes[personindex][indx] in self.file.firstnames:
                friendindex = self.file.firstnames.index(
                    self.file.wishes[personindex][indx])
                if not self.file.placed[friendindex]:
                    friends[i+1] = self.file.names[friendindex]
                    self.file.placed[friendindex] = True
                    break
            indx += 1

    def place_friend_secondary(self, personindex: int, friends: list, indx: int):
        '''place a person who wished for person x in x's friendgroup'''
        '''iterate through the wishes and check if our person appears in any of them'''
        for i in range(len(self.file.wishes)):
            if (friends[0] in self.file.wishes[i]) and (self.file.placed[i] is False):
                #print(True,"sec 1")
                friends[indx] = self.file.names[i]
                self.file.placed[i] = True
            elif (friends[0].lower() in self.file.wishes[i]) and (self.file.placed[i] is False):
                #print(True, "sec 2")
                friends[indx] = self.file.names[i]
                self.file.placed[i] = True
            elif (self.file.firstnames[personindex] in self.file.wishes[i]) and (self.file.placed[i] is False):
                #print(True, "sec 3")
                friends[indx] = self.file.names[i]
                self.file.placed[i] = True

    def combine_friendgroups(self):
        '''combine created friendgroups into a finished seating'''


def main():
    p = Placement(3, "/home/raisaneh/k/ohte/ohte_harjtyo/src/data/testi.csv")
    # using the len of wishes, because that's how many people had wishes. for the rest,
    # creating a friendgroup won't work
    for i in range(len(p.file.wishes)):
        if not p.file.placed[i]:
            p.create_friendgroup(i)
    # for i in p.friendgroups:
    # print(p.friendgroups)
    filewrite(p.friendgroups)


if __name__ == "__main__":
    #x = Placement(3)
    # print(x.file.wishes)
    main()
