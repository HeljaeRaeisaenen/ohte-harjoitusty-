'''class for storing the participants of the event, i.e. the names which should be placed,
and info relating to them'''

from readwrite import fileread

class Participants:
    '''a Participants-object contains four lists:
    - full names of the participants
    - first names of the participants
    - wishes
    - and whether they have been placed in a seat in a friendgroup/table.
    All these lists are in the same order, meaning that if Mikko's name is in index place 3 in the
    'names'-list, then Mikko's wishes are in index 3 on the 'wishes'-list etc. '''

    def __init__(self, filepath=None):
        self.names = []
        self.firstnames = []
        self.wishes = []
        if filepath:
            self.read_the_file(filepath)
        else:
            pass  # todo raise something
        self.placed = [False] * len(self.names)

    def read_the_file(self, filename: str):
        '''putting the read file contents in the Participants object'''
        output = fileread(filename)
        for i in output:
            self.names.append(i[0])
            self.firstnames.append(i[0].split(" ")[0])
            if len(i[1][0]) != 0:
                # remove empty wishes.
                # consequence: wish list is shorter than names list, and this will cause surprises
                self.wishes.append(i[1])


if __name__ == "__main__":
    P = Participants("/home/raisaneh/k/ohte/ohte_harjtyo/src/data/testi.csv")
    print(P.wishes)
    # print(x.firstnames)
