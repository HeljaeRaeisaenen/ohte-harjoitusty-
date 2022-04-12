'''Glues everything together?'''
from placement import Placement
from readwrite import filewrite


def main():
    '''for testing purposes'''
    plac = Placement(3, "/home/raisaneh/k/ohte/ohte_harjo/src/data/testi.csv")
    # using the len of wishes, because that's how many people had wishes. for the rest,
    # creating a friendgroup won't work
    for i in range(len(plac.file.wishes)):
        if not plac.file.placed[i]:
            plac.create_friendgroup(i)
    # for i in p.friendgroups:
    # print(p.friendgroups)
    filewrite(plac.friendgroups,
              "/home/raisaneh/k/ohte/ohte_harjo/src/data/testsave.csv")


if __name__ == "__main__":
    #x = Placement(3)
    # print(x.file.wishes)
    main()
