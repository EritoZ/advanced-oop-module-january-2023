from project.band_members.musician import Musician


class Guitarist(Musician):

    def learnable_skills(self):
        return ["play metal", "play rock", "play jazz"]
