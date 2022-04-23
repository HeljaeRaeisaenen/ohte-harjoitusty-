from placement import Placement
from readwrite import filewrite
from participants_repo import ParticipantsRepo


def main():
    '''for testing purposes'''
    plac = Placement(2, ParticipantsRepo(
        "/home/raisaneh/Documents/oikeatestimateriaali.csv"))
    c = 0
    for t in plac.fin_placement:
        c += len(t)
        print(t)
    print(c)

    plac.create_placement()
    filewrite(plac.fin_placement, "/home/raisaneh/Documents/testisave.csv")


if __name__ == "__main__":
    main()
