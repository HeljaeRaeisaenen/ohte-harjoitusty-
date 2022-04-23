'''ÄÄÄÄÄÄÄÄh'''


class Friendgroup:
    '''helps with optimizing the seating arrangement'''

    def __init__(self, cluster: list):
        self.potentially_on_left = []
        self.potentially_on_right = []
        self.people = set(cluster[1], cluster[2], cluster[3])
        self.cluster = cluster
        self.neighbors = []
        self.pos_3_wishes = cluster[0]
        self.key = cluster[0]
